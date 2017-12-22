#!/usr/bin/python

import paramiko,os,sys,time
sys.path.append('/home/ubuntu17/Documents/shared/github/dj/django-nic/mysite/mysite/tool/')
import ssh_cmd
import scp_sendrecv
#import ping_timeout

#################################################################################
####  tc0: Install driver of OmniPath
#################################################################################
def opa_tc0(ip,port,usr,passwd,oss_number):
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'mkdir /opa/')
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'mkdir /opa/tc0/')

    testcase_path_local = '/home/ubuntu17/Documents/shared/github/dj/django-nic/mysite/mysite/testcase/tc0/'
    testcase_path_remote= '/opa/tc0/'
    for file_name in os.listdir(testcase_path_local):
        file_path_local  = os.path.join(testcase_path_local,file_name)
        file_path_remote = os.path.join(testcase_path_remote,file_name)
        print(file_path_local)
        print(file_path_remote)
        #scp_sendrecv.ssh_scp_put(ip,port,usr,passwd,file_path_local,file_path_remote)

    cmd = 'mkdir -p /opa/oss/' + oss_number
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'mkdir -p /opa/oss/88905')
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,cmd)
    oss_path_local  = '/home/ubuntu17/Documents/shared/github/dj/django-nic/mysite/mysite/oss/' + oss_number
    oss_path_remote = '/opa/oss/' + oss_number
    for file_name in os.listdir(oss_path_local):
        file_path_local = os.path.join(oss_path_local,file_name)
        file_path_remote = os.path.join(oss_path_remote,file_name)
        print(file_path_local)
        #scp_sendrecv.ssh_scp_put(ip,port,usr,passwd,file_path_local,file_path_remote)


    ###ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'source /opa/tc0/local_yum.sh')



    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'tar zxvf /opa/oss/88905/IntelOPA-IFS.RHEL74-x86_64.10.6.0.0.134.tgz -C /opa/oss/88905/')
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'cp /opa/tc0/install.sh /opa/oss/88905/IntelOPA-IFS.RHEL74-x86_64.10.6.0.0.134/install.sh')
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'cp /opa/tc0/driver.sh /opa/oss/88905/IntelOPA-IFS.RHEL74-x86_64.10.6.0.0.134/driver.sh')
    print("install RPMs")
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'source /opa/oss/88905/IntelOPA-IFS.RHEL74-x86_64.10.6.0.0.134/install.sh')
    print("./INSTALL -a")
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'source /opa/oss/88905/IntelOPA-IFS.RHEL74-x86_64.10.6.0.0.134/driver.sh')
    print("INSTALL.sh -a ok")


    return ("opa_tc0 driver installation: finished")

#################################################################################
####  tc0: Install firmware of OmniPath
#################################################################################
def opa_tc1(ip,port,usr,passwd):
    print ("cd /usr/share/opa/bios_images/")
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'cd /usr/share/opa/bios_images/')
    print ("hfi1_eprom -w -o -c")
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'hfi1_eprom -w -o HfiPcieGen3Loader_1.6.0.0.0.rom -b HfiPcieGen3_1.6.0.0.0.efi -c /lib/firmware/updates/hfi1_platform.dat')
    print ("hfi1_eprom -V -o")
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'hfi1_eprom -V -o')
    print ("hfi1_eprom -V -b")
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'hfi1_eprom -V -b')
    print ("hfi1_eprom -V -c")
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'hfi1_eprom -V -c')


    print ("cd /lib/firmware/updates/")
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'cd /lib/firmware/updates/')
    print ("opatmmtool -f hfi1_smbus.fw fileversion")
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'opatmmtool -f hfi1_smbus.fw fileversion')
    print ("opatmmtool -f hfi1_smbus.fw update")
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'opatmmtool -f hfi1_smbus.fw update')
    print ("opahfirev")
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'opahfirev')
    print ("opainfo")
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'opainfo')

    return ("opa_tc1 firmware installation: finished")


###########################################################################
if __name__ == '__main__':
#    length = len(sys.argv)
#    if len(sys.argv) < 5:
        print "Error: wrong parameters"
        print("Notes:%s,host_ip root password command" %sys.argv[0])
#    else:
#	print "this is test entry"
#        ip = sys.argv[1]
#        account = sys.argv[2]
#        password = sys.argv[3]
#        cmd = sys.argv[4]
#        port = 22
#        ssh_cmd_send(ip, port, account, password, cmd)
