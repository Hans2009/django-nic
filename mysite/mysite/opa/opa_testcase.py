#!/usr/bin/python

import paramiko,os,sys,time
#sys.path.insert(0,'./tool/')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../tool')
import ssh_cmd
import scp_sendrecv
import ping_timeout

#################################################################################
####  tc0: Install driver of OmniPath
#################################################################################
def opa_tc0(ip,port,usr,passwd,oss_number):
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'mkdir /opa/')
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'mkdir /opa/tc0/')

    print("--------------------directory----------------")
    print("os.path.dirname__file__:%s" %os.path.dirname(os.path.abspath(__file__)))
    print("os.path.dirname__file__:%s" %os.path.dirname(os.path.abspath('./')))
    print("--------------------directory----------------")

    #transfer testcase bash scripts to target server
    testcase_path_local = os.path.dirname(os.path.abspath(__file__)) + "/testcase/tc0/"
    print("os.path.dirname:%s" %testcase_path_local)
    testcase_path_remote= '/opa/tc0/'
    for file_name in os.listdir(testcase_path_local):
        file_path_local  = os.path.join(testcase_path_local,file_name)
        file_path_remote = os.path.join(testcase_path_remote,file_name)
        print(file_path_local)
        print(file_path_remote)
        scp_sendrecv.ssh_scp_put(ip,port,usr,passwd,file_path_local,file_path_remote)

    #transfer testcase pkgs scripts to target server
    cmd = 'mkdir -p /opa/pkgs/' + oss_number
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,cmd)
    oss_path_local = os.path.dirname(os.path.abspath(__file__)) + "/pkgs/" + oss_number
    oss_path_remote = '/opa/pkgs/' + oss_number
    for file_name in os.listdir(oss_path_local):
        file_path_local = os.path.join(oss_path_local,file_name)
        file_path_remote = os.path.join(oss_path_remote,file_name)
        print(file_path_local)
        scp_sendrecv.ssh_scp_put(ip,port,usr,passwd,file_path_local,file_path_remote)

    cmd = 'source /opa/tc0/local_yum.sh'
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'source /opa/tc0/local_yum.sh')

    print("======================================================================")
    for file_name in os.listdir(oss_path_local):
        #print("file_name:%s"%file_name)
        file_name_local  = os.path.join(oss_path_local,file_name)
        print("file_name_local:%s"%(file_name_local))
        file_name_remote = os.path.join(oss_path_remote,file_name)
        print("file_name_remote:%s"%file_name_remote)

        if file_name_local.find(".tgz") > 0 and file_name_local.find("RHEL74") > 0:
            print("file_name_remote:%s"%file_name_remote)
            cmd = ("cd %s && tar zxvf %s -C %s"%(oss_path_remote,file_name_remote,oss_path_remote))
            print("ssh_cmd.ssh_cmd_send(ip,port,usr,passwd, cmd):%s"%cmd)
            ssh_cmd.ssh_cmd_send(ip,port,usr,passwd, cmd)

            (file_shotname,file_extension) = os.path.splitext(file_name_remote);
            print("file_shotname:%s"%file_shotname)

            cmd = 'cp /opa/tc0/install.sh ' + file_shotname + '/install.sh'
            ssh_cmd.ssh_cmd_send(ip,port,usr,passwd, cmd)
            print("ssh_cmd.ssh_cmd_send(%s,%s,%s,%s,%s):"%(ip,port,usr,passwd,cmd))

            cmd = 'cp /opa/tc0/driver.sh ' + file_shotname + '/driver.sh'
            ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,cmd)
            print("ssh_cmd.ssh_cmd_send(%s,%s,%s,%s,%s):"%(ip,port,usr,passwd,cmd))
    print("======================================================================")

    cmd = 'source ' + file_shotname + '/install.sh'
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,cmd)
    print("ssh_cmd.ssh_cmd_send(%s,%s,%s,%s,%s):"%(ip,port,usr,passwd,cmd))

    cmd = 'source ' + file_shotname + '/driver.sh'
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd, cmd)
    print("ssh_cmd.ssh_cmd_send(%s,%s,%s,%s,%s):"%(ip,port,usr,passwd,cmd))

    return ("opa_tc0 driver installation: finished")

#################################################################################
####  tc0: Install firmware of OmniPath
#################################################################################
def opa_tc1(ip,port,usr,passwd):
    print ("cd /usr/share/opa/bios_images/")
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'cd /usr/share/opa/bios_images/')
    print ("hfi1_eprom -w -o -c")
    cmd = 'hfi1_eprom -w -o HfiPcieGen3Loader' + '*' + '.rom -b HfiPcieGen3_' + '*' + '.efi -c /lib/firmware/updates/hfi1_platform.dat'
    ssh_cmd.ssh_cmd_send(ip,port,usr,passwd, cmd)
    #ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'hfi1_eprom -w -o HfiPcieGen3Loader_1.6.0.0.0.rom -b HfiPcieGen3_1.6.0.0.0.efi -c /lib/firmware/updates/hfi1_platform.dat')
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

#################################################################################
####  tc2: Install firmware and driver of OmniPath
#################################################################################
def opa_tc2(ip,port,usr,passwd,oss_number):
    print ("run opa_tc0")
    opa_tc0(ip,port,usr,passwd,oss_number)
    print ("run reboot")
    #ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'reboot')

    print "Start : %s" % time.ctime()
    time.sleep( 10 )
    print "End : %s" % time.ctime()

    ping_result = ping_timeout.ping_minutes(ip,600)
    print(ping_result)

    if ping_result == 'ping_ok':
        print('ifconfig')
        ssh_cmd.ssh_cmd_send(ip,port,usr,passwd,'ip a s')
        opa_tc1(ip,port,usr,passwd)
    else:
        print ("reboot then cant connect to target test server")

    return ("opa_tc2 driver & firmware installation: finished")



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
