from pymodbus.client import ModbusTcpClient
import yaml

class Adam6317:
    def __init__(self):
        
        self.resultDI=None
        self.resultDO=None
        self.settingDO=None
        self.dictBits=[]

        self.getConfFromYaml()
        self.ADDRESS=self.config['IP_ADDRESS']
        self.PORT=self.config['PORT']
        self.connectADAM()


    def __del__(self):
        self.client.close()

    def getConfFromYaml(self):
        try:
            with open('confAddresses.yaml','r',encoding='utf-8') as foo:
                self.config=yaml.safe_load(foo) 
        except Exception as e:
            print(f'Read file Error or do not found file: {e}')
        

    def connectADAM(self):
        try:
            self.client=ModbusTcpClient(self.ADDRESS, port=self.PORT)
            self.client.connect()
        except Exception as e:
            print(f'Error connection: {e}')

    def getStatusDI(self):
        try:
            lenListDI=len(self.config['DI'])
            self.resultDI=self.client.read_discrete_inputs(address=self.config['DI']['DI0'], count=lenListDI, device_id=self.config['ID'])
            return self.resultDI.bits[:lenListDI]
        except Exception as e:
            print(f'Unexcept error:{e}')

    def getStatusDO(self):
        try:
            lenListDO=len(self.config['DO'])
            self.resultDO=self.client.read_coils(address=self.config['DO']['DO0'],count=lenListDO,device_id=self.config['ID'])
            return self.resultDO.bits[:lenListDO]       
        except Exception as e:
            print(f'Unexcept error:{e}')

    def setDO(self,DO):
        try:
            lenListDO=len(self.config['DO'])
            self.settingDO=self.client.write_coil(address=self.config['DO'][''])


        except Exception as e:
            print(f'Unexcept error:{e}') 

            

def main():
    ster1=Adam6317()
    print(f'StatusDI:{ster1.getStatusDI()}')
    print(f'StatusDO: {ster1.getStatusDO()}')
    
    
    
if __name__=='__main__':
    main()