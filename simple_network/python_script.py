
from netmiko import ConnectHandler


# read device and login details from a file required to login to the device.
def read_device_credentials(filename):
    commands = {}
    with open(filename) as fh:
        for line in fh:
            command, description = line.strip().split(' ', 1)
            commands[command] = description.strip()

    return commands


# read commands to be executed from a file
def read_user_commands(filename):

    # read the user commands to be executed
    with open(filename) as f:
        commands = f.read().splitlines()
    return commands


read_devices = read_device_credentials("device_credential")
all_devices = [read_devices]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    commands_to_send = read_user_commands('command_file')
    output = net_connect.send_config_set(commands_to_send)
    with open("Output_{}.txt".format(devices['host']), "w") as text_file:
        text_file.write(output)
    print(output)
    print("Done! Output saved on Output_{}.txt".format(devices['host']))
