from netmiko import ConnectHandler

with open('device1.txt') as routers:
    for IP in routers:
        router = {
        "device_type": "cisco_ios",
        "ip": "sandbox-iosxe-latest-1.cisco.com",
        "username": "developer",
        "password": "C1sco12345"
        }
        net_connect = ConnectHandler(**router)
        print ("Connecting to " + IP)
        print('-'*80)
        output = net_connect.send_command('sh ip int brief')
        print(output)
        print()
        print('-'*80)
# Finally close the connection
net_connect.disconnect()