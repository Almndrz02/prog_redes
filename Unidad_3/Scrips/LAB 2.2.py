import netmiko
from netmiko import ConnectHandler
sshCli = ConnectHandler(
        device_type='cisco_ios',
        host='10.10.20.70',
        port=2231,
        username='admin',
        password='admin'
        )

output = sshCli.send_command("show ip int brief", read_timeout = 10, expect_string = r"#")
print ("show ip int brief:\n{}\n".format(output))
#print(output)

