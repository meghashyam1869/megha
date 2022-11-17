from netmiko import ConnectHandler

CSR = {

			"device_type": "cisco_ios",
			"ip": "sandbox-iosxe-latest-1.cisco.com",
			"username": "developer",
			"password": "C1sco12345"
        }

net_connect = ConnectHandler(**CSR)

#discover the hostname from the prompt

hostname = net_connect.send_command('show run | i host')
hostname.split(" ")

hostname, device, *rest= hostname.split(" ")

print ("Backing up " + device)

filename = "device3.txt"

showrun = net_connect.send_command('show run')
showvlan = net_connect.send_command('show vlan')
showver = net_connect.send_command('show ver')
log_file = open(filename, "a")
log_file.write(showrun)
log_file.write("\n")
log_file.write(showrun)
log_file.write("\n")
log_file.write(showver)
log_file.write("\n")

# Finally close the connection
net_connect.disconnect()