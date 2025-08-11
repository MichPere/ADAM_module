import os
import json
import yaml
from pymodbus.client import ModbusTcpClient as tcp


with open('configadm.yaml','r') as file:
    cfg=yaml.safe_load(file)

client=tcp(cfg['HOST'],port=cfg['PORT'])
client.connect()

rr=client.read_coils(0,count=8)
if rr.isErrors():
    print('Błąd odczytu',rr)
else:
    print('DI states',rr.bits)

client.close()
