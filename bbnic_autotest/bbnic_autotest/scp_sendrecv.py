#!/usr/bin/python


import paramiko,os,sys,time

#this function is to put the file to the remote server via the scp command.
#ip: the ip address.
#port: port =22.
#user: user: root
#password: password of the root account.
#local_file: please use the absolute file path.  such as "/meils/123.txt"
#remote_file: please use the remote file_path. need define the name of the file. such as "/meils1/123.txt"
#note: local_file/remote_file can't be the directory.


def ssh_scp_put(ip,port,user,password,local_file,remote_file):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, user, password)
#  a = ssh.exec_command('date')
#  stdin, stdout, stderr = a
#  print stdout.read()
    
    sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
    sftp = ssh.open_sftp()
    sftp.put(local_file, remote_file)
    ssh.close()
    
#this function is to get the file from remote server  via the scp command.
#ip: the ip address.
#port: port =22.
#user: user: root
#password: password of the root account.
#local_file: please use the absolute file path.  such as "/meils/123.txt"
#remote_file: please use the remote file_path. need define the name of the file. such as "/meils1/123.txt"
#note: local_file/remote_file can't be the directory.

def ssh_scp_get(ip, port, user, password, remote_file, local_file):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, 22, 'root', password)
   # a = ssh.exec_command('date')
   # stdin, stdout, stderr = a
   # print stdout.read()
    sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
    sftp = ssh.open_sftp()
   # print("remote_file:%s" %remote_file)
   # print("local_file:%s" %local_file)
 
    sftp.get(remote_file, local_file)
    ssh.close()


if __name__ == '__main__':
	length = len(sys.argv)
	if len(sys.argv) < 7:
	    print "Error: wrong parameters"
	    print("Notes:%s,host_ip send/recv root rootpassword local_file remote_file " %sys.argv[0])
	else:
	    ip = sys.argv[1]
	    account = sys.argv[3]
	    password = sys.argv[4]
	    localfile = sys.argv[5]
	    remotefile = sys.argv[6]
	   # print("Debug Sending with: para0:%s ip:%s account:%s password:%s localfile:%s remotefile:%s "%(sys.argv[0], ip, account, password, localfile,remotefile))
	    if sys.argv[2] == "send":	
		ssh_scp_put(ip,22, account,password,localfile,remotefile)
	    elif sys.argv[2] == "recv":
		ssh_scp_get(ip,22, account,password,remotefile,localfile)

	    else:
		print "Error: wrong parameters, only send/recv"	





