"""
Some lines are commented out.
You may or may not want to use the ipaddress library
but you will still need to check for a valid IPv4 adddress.

The 'with open('JSONdata') as f:' line will read the data file
AS LONG AS IT IS IN THE SAME DIRECTORY :)

The next line should get you started with a method you will need
from the json library to change the JSON text into something 
you can call from Python
"""
import json

import validate_ip  # Using from challenge 1 solution

if __name__ == '__main__':

    with open('JSONdata') as f:
        devices_data = json.loads(f.read())

    for device in devices_data:

        ip = device['lanIp']
        serial_num = '#' + device['serial']

        if validate_ip.is_valid_address(ip):
            print(f'{ip:<15} is a Valid IP Address for Serial {serial_num:>20}')
        else:
            print(f'{ip:<15} is an Invalid IP Address for Serial {serial_num:>17}')


