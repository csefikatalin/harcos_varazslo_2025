import random
class Jatekos:
    def __init__(self,nev:str,hely:int):
        self.nev=nev
        self.hely=hely
        self.eletpont=3+random.randint(1,6)
    
    def set_hely(self):
        """setter - amivel az adattagok értékét beálíltjuk"""
        self.hely=random.randint(0,2)
        
    def set_eletpont(self,ertek):
        """setter"""
        self.eletpont=self.eletpont-ertek
        """ ellenőrzötten módosítjuk az adatot """
        if self.eletpont<0:
            self.eletpont=0
    