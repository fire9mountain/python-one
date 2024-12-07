import subprocess
import time
import os


def get_process_pids(pattern):
    """ 获取符合模式的进程 PID 列表 """
    process = subprocess.Popen(['ps', '-ef'], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    output_str = output.decode()
    lines = output_str.split('\n')

    pids = []
    for line in lines:
        if pattern in line and 'grep' not in line and 'awk' not in line:
            parts = line.split()
            if len(parts) >= 2:
                pid = parts[1]
                pids.append(pid)
    return pids


def send_signal(pids, signal):
    """ 发送信号给指定的进程 ID 列表 """
    for pid in pids:
        try:
            os.kill(int(pid), signal)
        except OSError as e:
            print(f"无法向进程 {pid} 发送信号 {signal}: {e}")


def check_processes_alive(pids):
    """ 检查进程是否仍在运行 """
    alive_pids = []
    for pid in pids:
        try:
            os.kill(int(pid), 0)  # 如果进程存在，则不会抛出异常
            alive_pids.append(pid)
        except OSError:
            pass
    return alive_pids


def restart_service():
    """ 重启服务 """
    directory = '/usr/local/serverweb/backend/'
    command = ['nohup', 'java', '-jar', 'filter-center-service.jar', '>', 'catalina.out', '2>&1', '&']

    try:
        os.chdir(directory)
        subprocess.Popen(command)
        print("服务已重启。")
    except Exception as e:
        print(f"重启服务时发生错误: {e}")


# 主程序
if __name__ == '__main__':
    pattern = 'filter-center-service.jar'
    wait_time = 5

    # 获取进程 PID 列表
    pids = get_process_pids(pattern)

    if pids:
        print(f"找到进程 PID: {pids}")

        # 发送 SIGTERM 信号
        send_signal(pids, 15)

        # 等待一段时间让进程自行关闭
        for i in range(wait_time):
            alive_pids = check_processes_alive(pids)
            if not alive_pids:
                print(f"所有进程在 {i + 1} 秒内优雅地关闭。")
                break
            time.sleep(1)

        # 如果仍有进程存活，则发送 SIGKILL
        if alive_pids:
            print(f"仍有进程存活，正在发送 SIGKILL: {alive_pids}")
            send_signal(alive_pids, 9)

    # 重启服务
    restart_service()