import netmiko
from netmiko import ConnectHandler
sshCli = ConnectHandler(
        device_type='cisco_ios',
        host='10.10.20.70',
        port=2231,
        username='admin',
        password='admin'
        )

config_commands = [
    'int loopback 1'
    'ip add 192.168.1.1 255.255.255.0'
    'no shutdown'
    'Prueba loboratorio 2'
    ]

sshCli.send_command('Configure terminal', expect_string =r"", read_timeout=150)
sshCli.send_config_set("config_commands")
result = sshCli.send_command('show ip int brief')
print(result)

