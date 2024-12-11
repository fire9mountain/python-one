import paramiko


def ssh_command(ip, port, user, password, command):
    # 创建 SSH 客户端
    client = paramiko.SSHClient()

    # 自动添加主机名和密钥到本地 HostKeys 对象，如果缺少对应的密钥，则自动添加
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # 连接到服务器
        client.connect(ip, port=port, username=user, password=password)

        # 执行命令
        stdin, stdout, stderr = client.exec_command(command)

        # 获取命令输出
        print("Command output:")
        print(stdout.read().decode())

        # 获取命令错误信息
        print("Error output:")
        print(stderr.read().decode())

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # 关闭连接
        client.close()


if __name__ == "__main__":
    # 这里填写你的服务器 IP 地址、端口号、用户名和密码
    ip = '192.168.110.205'
    port = 22
    user = 'root'
    password = '67890,qwert'

    # 要执行的命令
    command = ''

    # 调用函数
    ssh_command(ip, port, user, password, command)