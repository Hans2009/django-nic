#!/usr/bin/python
import ssh_cmd

if __name__ == '__main__':
    ip = '192.168.182.129'
    port  = '22'
    account = 'root'
    password = '1111111'
    cmd = 'ifconfig'
    
    print "this is test entry"
    #ssh_cmd.ssh_cmd_send(ip, port, account, password, cmd)
    ssh_cmd.ssh_cmd_send('192.168.182.129','22','root','1111111','ifconfig')




