import subprocess
import time

p = subprocess.Popen("ssh -R pivpn:8194:localhost:8194 serveo.net", shell=True, stdin=None, stdout=None, stderr=None, close_fds=False)
return_code = None
while True:
    return_code = p.poll()
    if return_code != None:
        break
    time.sleep(1)
