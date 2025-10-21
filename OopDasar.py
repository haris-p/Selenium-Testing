class Hero:

    __jumlah = 0
    def __init__(self, name, healt, attPower, armor):
        self.__name = name
        self.__healt = healt
        self.__attPower = attPower
        self.__armor = armor

        self.__level = 1
        self.__exp = 0
        self.__healtMax = self.__healt * self.__level
        self.__attPowerMax = self.__attPower * self.__level
        self.__armorMax = self.__armor * self.__level
        self.__healt = self.__healtMax
        Hero.__jumlah += 1

    @property
    def showInfo(self):
        return "{}level{}: \n\thealt: {}/{} \n\tattack = {} \n\tarmor = {}".format(self.__name, self.__level, self.__healt, self.__healtMax,self.__attPowerMax, self.__armorMax, self.__armorMax)

    @property
    def gainExp(self, exp):
        pass
    
    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(self.__name, "level up")
            self.__level += 1
            self.__exp -= 100
            self.__healtMax = self.__healt * self.__level
            self.__attPowerMax = self.__attPower * self.__level
            self.__armorMax = self.__armor * self.__level
            self.__healt = self.__healtMax
           
    def attack(self, musuh):
        self.gainExp = 50

hero1 = Hero("sniper", 100, 10, 5)
hero2 = Hero("sven", 150, 15, 10)

hero1.attack(hero2)
hero1.attack(hero2)
print(hero1.showInfo)