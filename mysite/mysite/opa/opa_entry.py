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
    if len(sys.argv) > 6:
        print "Error: wrong parameters"
        print("Notes:%s,ip,usr,passwd,oss_number,tc_number" %sys.argv[0])
    else:
        print "this is opa test entry"
        #ip         = sys.argv[1]
        ip         = '10.245.36.98'
        #port       = sys.argv[2]
        usr        = 'root'
        passwd     = '111111'
        oss_number = '88905'
        tc_number  = 'tc0'

        port = 22
        #ssh_cmd_send(ip, port, account, password, cmd)
        opa_entry_cli(ip,port,usr,passwd,oss_number,tc_number)
