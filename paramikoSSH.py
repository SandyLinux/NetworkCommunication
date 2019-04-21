import paramiko
from getpass import getpass
import time,socket
from multiprocessing import Process, Pipe

def f1(conn):
    msglist = ['show run', 'show ip int br', 'show clock', 'show int trunk', 'exit']
    for msg in  msglist:
        
        conn.send([msg])
        time.sleep(5)
    conn.close()

def main():
    parent_conn, child_conn = Pipe()
    ip = '172.18.200.10'
    username =  'cmlab'
    password = 'cisco123'
    remote_conn_pre=paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        
        remote_conn_pre.connect(ip, port=22, username=username,  
                            password=password,
                            look_for_keys=False, allow_agent=False,
                            timeout=10,
                            auth_timeout=10)
        
        
        remote_conn = remote_conn_pre.invoke_shell()
        output = remote_conn.recv(65535)
        print ('----1',output)

        remote_conn.send("terminal length 0\n")
        time.sleep(1)
        output = remote_conn.recv(65535)
        print ('----2',output)
        p = Process(target=f1, args=(child_conn,))
        p.start()
        
        for _ in range(5):
            print('-----------execution result')

            tst2=  (parent_conn.recv()[0])  # prints "[42, None, 'hello']"
            if tst2=='exit':
                break
            else:
                tst2 = tst2 +"\n" 
            print('---!!!!!sending......', tst2)
            remote_conn.send(tst2)
            time.sleep(2)
            output = remote_conn.recv(655350).decode('utf-8')
            #for i in output.splitlines():
            print (output)
        remote_conn.close()    
    except socket.timeout as err:
        print(err)
    except paramiko.ssh_exception.AuthenticationException as err:
        print(err)
    except Exception as err:
        print(err)
    
    """
    remote_conn.send("show ip int br\n")
    time.sleep(1)
    output = remote_conn.recv(655350)
    for i in output.splitlines():
        print (i)
    """


if __name__=='__main__':
    main()