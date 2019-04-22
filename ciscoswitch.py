#!/usr/bin/env python
#This Script expects you are providing a level 15 user priveledge
#Uses FTP & Telnet and is insecure
#Will work if run through a linux terminal, not windows
#needs ftp server setup and username password added in the cisco device
#and is only a sample reference to get started.
import pexpect
import sys
import time
import datetime
 
class CiscoSwitch():
     
    def __init__(self, host, username, password):
        self.username = username
        self.host = host
        self.password = password
 
    def Login(self):
        str1 = 'ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -c 3des-cbc %s@%s'%(self.username, self.host)

        self.child = pexpect.spawn('ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -c 3des-cbc %s@%s'%(self.username, self.host), echo=False, timeout=30)
        self.child.expect('Password:')
        self.child.sendline(self.password)
        self.child.expect('#')
        self.child.sendline('terminal length 0')
        self.child.expect('#')
         
        return (self.child, self.child.before)
 
    def RunShowCmd(self,cmd):
        self.child.sendline(cmd)
        self.child.expect('#')
        #self.child.logfile=sys.stdout.buffer

        return (self.child, self.child.before)
     
    def FtpBackupCmd(self,ftpip):
        self.child.sendline('copy running-config ftp:')
        self.child.expect(']?')
        self.child.sendline(ftpip)
        self.child.expect(']?')
        DATE = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        self.child.sendline(DATE+'-'+self.host)
        self.child.expect('#')
        return (self.child, self.child.before)
 
if __name__ == '__main__':
        print ('This program is being run by itself')
        Switch = CiscoSwitch('172.18.200.10','cmlab','cisco123')
        (obj,stdout) = Switch.Login()
        print (stdout.decode('utf-8'))
        (obj,stdout) = Switch.RunShowCmd('show ip int brief')

        print(stdout.decode('utf-8')) 
        for i in (stdout.decode('utf-8')).splitlines():
            print(i)

        """
        (obj,stdout) = Switch.FtpBackupCmd('1.1.1.1')
        print stdout
        """
