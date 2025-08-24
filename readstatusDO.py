from pymodbus.client import ModbusTcpClient

# Połączenie z ADAM
client = ModbusTcpClient('10.0.0.2', port=502)
client.connect()

# 0x0033 = 51 decimal
address = 33

result = client.read_coils(address=address, count=1, device_id=1)
if result.isError():
    print("Błąd odczytu")
else:
    print("DO status:", result.bits[0])

client.close()