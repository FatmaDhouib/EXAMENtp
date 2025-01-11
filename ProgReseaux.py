from netmiko import ConnectHandler

cisco_router = {
  'device_type': 'cisco_ios',
  'host': 'sandbox-iosxe-latest-1.cisco.com',
  'username': 'admin',
  'password': 'C1sco12345',
  'port': 22,
}
connection = ConnectHandler(**cisco_router)
clock = connection.send_command ('sh clock')

result =connection.send_command('sh ip int br')

with open("interfaces.txt", "w") as f:
        f.write(result)
print("Interfaces in 'interfaces.txt'.")
commands = ['conf t','int loopback 0', 'ip address 10.8.8.8 255.255.255.240']
result = connection.send_config_set(commands)

print (result)