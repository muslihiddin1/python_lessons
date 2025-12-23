# from uuid import uuid4
# class Avto:
#     def __init__(self, make, model, rang, yil, narh, km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()
#     def get_km(self):
#         return self.__km
    
#     def get_id(self):
#         return self.__id
        
#     def add_km(self, km):
#         if km >= 0:
#             self.__km += km
#         else:
#             print("Km soni manfiy bo'lishi mumkin emas")
        
        
        
        
        



from uuid import uuid4
class Avto:
    num_avto = 0
    def __init__(self, make, model, rang, yil, narh, km=0,):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.num_avto += 1
        
    @classmethod
    def get_num_avto(cls):
        return cls.num_avto
    
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id
    
    def add_km(self, km):
        if km >= 0:
            self.__km += km
        else:
            print("Km soni manfiy bo'lishi mumkin emas")
            
            
avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000)
avto2 = Avto("GM", "Malibu", "Qora", 2020, 40000)
avto3 = Avto("GM", "Malibu", "Qora", 2020, 40000)
print(Avto.get_num_avto())