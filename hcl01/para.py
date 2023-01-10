import paramiko
import pandas as pd
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="10.0.2.15",username="sindhu",password="1234")
stdin,stdout,stderr,=ssh.exec_command("netstat --listening|less")
df=pd.DataFrame(stdout)
print(df)

