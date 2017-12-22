#!/usr/bin/python 
import os,sys,time

def ping_once(ip):
    backinfo =  os.system('ping -c 1 -w 1 %s'%ip)
    print 'backinfo:' ,backinfo

    if backinfo == 0:
        return 'ping_ok'
    else:
        return "ping_fails"


def ping_minutes(ip,sec):
    ping_result = ping_once(ip)
    time = 0

    while ping_result == 'ping_fails':
        if time < sec:
            ping_result = ping_once(ip)
            if ping_result == 'ping_fails':
                time = time + 1
            elif ping_result == 'ping_ok':
                break
        else:
            return 'fail:timeout!'

    return ping_result

###########################################################################
if __name__ == '__main__':
    ip = '10.245.36.66'
    sec = 600

    ping_result = ping_minutes(ip,sec)
    print ('ping ' + ip + ':' ,ping_result)
