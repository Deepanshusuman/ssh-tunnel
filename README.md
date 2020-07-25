# ssh-tunnel
SSH tunnel via python using serveo

install net-tools
`sudo apt-get install net-tools`
check ip address
`ip a`
eth0 or wlan0

check gateway 
`sudo route -n`

edit conf file
`sudo nano /etc/dhcpcd.conf`

write 
`
static ip_address= 192.168.0.200
static routers= 192.168.0.1
static domain_name_servers= 8.8.8.8 8.8.8.4
`
