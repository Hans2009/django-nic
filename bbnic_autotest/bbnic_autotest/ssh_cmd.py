#!/usr/bin/python

import paramiko,os,sys,time
#this function is to issue the command to the remote server and the command will be excuted like local server.
#ip: the remote ip address.
#port: port = 22
#user: root
#password: password of root
#the actual command of command  such as "mkdir /jason && touch /jason/jason.txt"

def ssh_cmd_send(ip,port,user,password,cmd):
    import paramiko,os,sys,time

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, user, password)
    a = ssh.exec_command(cmd)
    stdin, stdout, stderr = a
    print stdout.read()
    ssh.close()
    return 'ssh_cmd_send successfully'

if __name__ == '__main__':
    length = len(sys.argv)
    if len(sys.argv) < 5:
        print "Error: wrong parameters"
        print("Notes:%s,host_ip root password command" %sys.argv[0])
    else:
	print "this is test entry"
        ip = sys.argv[1]
        account = sys.argv[2]
        password = sys.argv[3]
        cmd = sys.argv[4]
        port = 22
        ssh_cmd_send(ip, port, account, password, cmd)




