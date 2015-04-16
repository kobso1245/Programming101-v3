from soldier import Soldier


class Enemy(Soldier):

    def __init__(self, health, mana, damage):
        super().__init__(health, mana)
        self.damage = damage

    def __str__(self):
        return "Enemy(hp:{}, mana:{}, damage:{}".format(
            self.health, self.mana, self.damage)

    def __hash__(self):
        return hash(self.__str__())

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def take_mana(self, mana):
        if not isinstance(mana, int):
            raise TypeError("Enter valid mana_points.")
        if self.mana + mana > self.__max_mana:
            self.mana = self.__max_mana
        else:
            self.mana += mana
