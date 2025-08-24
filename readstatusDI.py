from pymodbus.client import ModbusTcpClient

# Połączenie z ADAM
client = ModbusTcpClient('10.0.0.2', port=502)
client.connect()
count=11

# Odczyt 11 wejść dyskretnych (DI) od adresu 0
result = client.read_discrete_inputs(address=0, count=count, device_id=1)

if result.isError():
    print("Błąd:", result)
else:
    di_states = result.bits  # lista bitów [0/1]
    # Tworzymy słownik DI1..DI11
    di_dict = {f"DI{i+1}": di_states[i] for i in range(count)}
    print(di_dict)

client.close()
