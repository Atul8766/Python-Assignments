class Laptop:
    def __init__(self,brand,ram,cpu,ssd):
        self.brand = brand
        self.ram = ram
        self.cpu = cpu
        self.ssd = ssd
    
    def config(self):
        print(self.brand,self.ram,"GB",self.cpu,self.ssd,"GB")


lapi1 = Laptop("DELL",8,"i3",256)
lapi1.config()

