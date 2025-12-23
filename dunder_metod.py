class Avto:
    __num_avto = 0
    def __init__(self, make, model, rang, yil, narh,):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1
        
    def __repr__(self):                                         # __repr__ - obyekt haqida ma'lumot
        return f"Avto: {self.make} {self.model}"
    
    def __eq__(self, y):                                        # __eq__ - teng (yoki tengmas)  ==, !=
        return self.narh == y.narh
    
    def __lt__(self, y):                                        # __lt__ - kichik (yoki katta)  <, >
        return self.narh < y.narh
    
    def __le__(self, y):                                        # __le__ - kichik yoki teng  (yoki katta yoki teng) <=, >=
        return self.narh <= y.narh
    
class AvtoSalon:
    def __init__(self, name):
            self.name = name
            self.avtolar = []
            
    def __repr__(self): 
             return f"{self.name} avtosaloni" 
         
    def __getitem__(self, index):                               # __getitem__ - obyektdan qiymat olish
         return self.avtolar[index]
     
    def __setitem__(self, index, qiymat):                       # __setitem__ - obyektga qiymat qo'shish
         self.avtolar[index]=qiymat
         
    def add_avto(self, *qiymat):
         for avto in qiymat:
             if isinstance(avto, Avto):
                 self.avtolar.append(avto)
             else:
                 print("Avto kiriting")
             
             
         
salon1 = AvtoSalon("MaxAvto") 
# print(salon1)
        
avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000)
avto2 = Avto("GM", "Lacetti", "Qizil", 2020, 20000)
avto3 = Avto("GM", "Cobalt", "Oq", 2019, 25000)
salon1.add_avto(avto1, avto2, avto3)