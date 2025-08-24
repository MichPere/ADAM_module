from pymodbus.client import ModbusTcpClient
import yaml

# Połączenie z ADAM
client = ModbusTcpClient('10.0.0.2', port=502)
client.connect()

# 0x0033 = 51 decimal

address = 0x0020  

result = client.write_coil(address, 0, device_id=1)
if result.isError():
    print("Błąd odczytu")
else:
    print(f"DO status:{result.bits[0]}")

client.close()