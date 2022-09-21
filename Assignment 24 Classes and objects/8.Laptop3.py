class Laptop:
    def __init__(self,brand,ram,cpu,ssd):
        self.brand = brand
        self.ram = ram
        self.cpu = cpu
        self.ssd = ssd
    
    def config(self):
        print(self.brand,self.ram,"GB",self.cpu,self.ssd,"GB")

    def sort(self,l1):
        print(sorted(l1))

lap1 = Laptop("HP",16,"i9",500)
lap2 = Laptop("DELL",8,"i5",256)
lap3 = Laptop("Lenovo",4,"i3",126)

l1 = [lap1,lap2,lap3]
lap1.sort(l1)
