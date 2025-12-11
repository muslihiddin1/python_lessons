class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        
    def get_name(self):
        return self.ism
    
    def get_age(self, yil = 2025):
        return yil - self.tyil
        
    def tanishtir(self):
        return f"Ismim {self.ism}. Familiyam {self.familiya}. Tug'ilgan yilim {self.tyil}"
        
talaba1 = Talaba("Ne'matulloh", "Nurmamatov", "2006")
talaba2 = Talaba("Muslihiddin", "Nurmamatov", "2008")
talaba3 = Talaba("Mujohiddin", "Nurmamatov", "2011")
# print(talaba1.ism, talaba1.familiya, talaba1.tyil)
# print(talaba2.ism, talaba2.familiya, talaba2.tyil)
# print(talaba3.ism, talaba3.familiya, talaba3.tyil)