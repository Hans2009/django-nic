#!/usr/bin/python

import paramiko,os,sys,time
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../tool')
import ssh_cmd
import scp_sendrecv
import ping_timeout
import opa_testcase

#################################################################################
####                   Test Entry of OmniPath
#################################################################################
def opa_entry_cli(ip,port,usr,passwd,oss_number,tc_number):
    if tc_number == 'tc0':
        print("opa_testcase.opa_tc0")
        result  = opa_testcase.opa_tc0(ip,port,usr,passwd,oss_number)
    elif tc_number == 'tc1':
        print("opa_testcase.opa_tc1")
        result  = opa_testcase.opa_tc1(ip,port,usr,passwd)
    elif tc_number == 'tc2':
        print("opa_testcase.opa_tc2")
        result  = opa_testcase.opa_tc2(ip,port,usr,passwd,oss_number)

    return result



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
