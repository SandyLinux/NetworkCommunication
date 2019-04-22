from subprocess import Popen, PIPE, STDOUT
from time import sleep

def get_fping_time(cmd):
    try:
        #execute the fping command, get the output, and convert to ascii format
        #get the 3 latency time
        ret = Popen(cmd, stdout=PIPE, stderr=STDOUT).communicate()[0].decode('ascii')
        str_line = ret.splitlines()
        latency_time = 0
        for i in str_line:
            output = i.strip().split(':')[-1].split()
            #get the 3 latency time list 
            res = [float(x) for x in output if x != '-']
            if len(res) > 0:
                latency_time = round(sum(res) / len(res),2)
            else:
                latency_time= 0

        return latency_time
    except Exception as err:
        return 0

if __name__ == "__main__":
    for i in range(10):
        sleep(2)
        ret = get_fping_time(['fping', '-A','172.16.50.131', '-C', '1', '-q'])

    print("Import me into main.py to use my functions")

