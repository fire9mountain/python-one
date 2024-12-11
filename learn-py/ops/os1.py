import os
import subprocess

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
