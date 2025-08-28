from pymodbus.client import ModbusTcpClient
import time

client = ModbusTcpClient("10.0.0.1", port=502)

if client.connect():
    while True:
        # czytamy 8 rejestrów wejściowych (Input Registers, funkcja 0x04)
        result = client.read_input_registers(address=0, count=8, device_id=1)
        resu=[]
        if not result.isError():
            for i in range(len(result.registers)):
                resu.append(((result.registers[i]/65535*110)-50))
                #resu.append(result.registers[i])

            print("Odczytane AI:", resu)
        else:
            print("Błąd odczytu:", result)

        time.sleep(1)
client.close()
