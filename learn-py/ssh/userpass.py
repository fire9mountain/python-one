import paramiko

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect("192.168.103.24",22,"root","12345,abcde ")

stdin,stdout,stderr = client.exec_command("cat /etc/passwd")
print((stdout.read().decode('utf-8')))