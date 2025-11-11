import random
class Jatek:
    def __init__(self,harcos, varazslo):
        self.harcos=harcos
        self.varazslo=varazslo
        
    
    def tulajdonsag_lap(self, obj):
        print("*"*15)
        print(f"név: {obj.nev}")
        print(f"hely: {obj.hely}")
        print(f"pont: {obj.eletpont}")
        print("*"*15)
    

    def kor(self):  
        self.harcos.set_hely()
        self.varazslo.set_hely()
        vhely=self.varazslo.hely
        hhely=self.harcos.hely
        if vhely==hhely:
            print("harc")
            ve=random.randint(0,1)
            self.varazslo.set_eletpont(ve)
            he=random.randint(0,1)
            self.harcos.set_eletpont(he)
        else:
            print("nincs harc")
            
    def jatek_menet(self):
        while (self.harcos.eletpont>0 and self.varazslo.eletpont>0):
            self.kor()  
            self.tulajdonsag_lap(self.varazslo)
            self.tulajdonsag_lap(self.harcos)
            print("_________________________________________")
            input()
            
            
    """ játék. 
    1. minden körben lépnek a játékosok (meghívjuk a lepes() metódust)
    2. meg kell tudni, hoyg hova léptek le kell kérni a hely adattagot
    3. Ha a hely adattagjuk megegyezik, akkor harcolnak
        1. generálunk életerőt mindkét járékosnak 
        2. és ezzel csökkentjük az életerő pontjukat    
    """ 