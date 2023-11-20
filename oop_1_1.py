class GameCharacter:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, enemy):
        print(f"{self.name} {self.attack_power} ta zarb bilan {enemy.name} ga hujm qildi!")
        enemy.health -= self.attack_power
        print(f"{enemy.name} ning jami hayoti {enemy.health}")

class Warrior(GameCharacter):
    def __init__(self, name, health, attack_power, weapon_type):
        super().__init__(name, health, attack_power)
        self.weapon_type = weapon_type

    def special_attack(self, enemy):
        print(f"{self.name} {self.weapon_type} bilan maxsus hujm qiladi!")
        enemy.health -= self.attack_power * 2
        print(f"{enemy.name} ning jami hayoti {enemy.health}")

class Mage(GameCharacter):
    def __init__(self, name, health, attack_power, magic_type):
        super().__init__(name, health, attack_power)
        self.magic_type = magic_type

    def cast_spell(self, enemy):
        print(f"{self.name} {self.magic_type} janrligi asosida sihrlashadi!")
        enemy.health -= self.attack_power * 1.5
        print(f"{enemy.name} ning jami hayoti {enemy.health}")

# Test qismi
warrior = Warrior("G'aznaviy", 100, 20, "Miyonga")
mage = Mage("Merlin", 80, 25, "No'luv")
enemy = GameCharacter("Dushman", 120, 15)

warrior.attack(enemy)
warrior.special_attack(enemy)

mage.attack(enemy)
mage.cast_spell(enemy)

if __name__ == '__mian__':
    print(warrior)
    print(mage)