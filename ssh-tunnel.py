import subprocess
import time
import socket
ip = socket.gethostbyname(socket.gethostname())
cloudport =  3000
localport = 80

p = subprocess.Popen("ssh -N -f -R 5000:+ip+:80 ubuntu@13.234.76.83 -i rsa_key", shell=True, stdin=None, stdout=None, stderr=None, close_fds=False)
return_code = None
while True:
    return_code = p.poll()
    if return_code != None:
        break
    time.sleep(1)
