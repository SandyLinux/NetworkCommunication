from subprocess import Popen,PIPE,STDOUT
NULL = open("/dev/null", 'w')                       # Null file

def checkInterfaceHasInternetConnectionHelper(name, dest_port, protocol):
    """
    check the interface to see if it has network access with :w, i.e., if it can ping google DNS
    Args:
        name: the name of the interface to check
    Returns:
        True if it has internet connection, False otherwise
    """
    try:
        ping_cmd = ['nping', '--interface', name, '--dest-port', dest_port, '--%s'%protocol, '-c', '4', "188.8.8.8"]
        #Create a subprocess to ping google's DNS and get the return code
        retcode = Popen(ping_cmd, stdout=PIPE, stderr=PIPE, bufsize=0)
        retcode.wait()
        (stdout,stderr) = retcode.communicate()

        print(retcode)
        #print(stdout)
        for i in stdout.splitlines():
            if i.decode('utf-8').startswith('Max rtt'):
                print(i.decode('utf-8').split())
                print(i.decode('utf-8').split()[-1])
                
        print(stderr)
        print(retcode.returncode)
        print(retcode.pid)
        #Ping returns 0 on success, 1 or 2 on failure
    except ValueError as verr:
        print(verr)
        print(stderr)
    except Exception as err:
        print(err)
        print(stderr)

    if(retcode == 0):
        return True
    else:
        return False

if __name__=='__main__':
    checkInterfaceHasInternetConnectionHelper('eth0', '443', 'tcp')
