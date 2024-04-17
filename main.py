from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum
from typing import Union

"""
Задача: 
Реализовать базовый класс Человек (в данном примере абстрактный), со свойством пол (sex), и методом приветствия (greet) 
Классы наследники Мужчина и Женщина.
Мужчина должен жать руку другому мужчине при приветсвии (реализует интерфейс Handshaker). + _свойство счётчик рукопожатий
Женщина должна обнимать другую женщину при приветсвии (реализует интерфейс Hugger). + _свойство счётчик обнимашек
"""


class Human(ABC):

    @property
    @abstractmethod
    def sex(self) -> Sex:
        pass

    @abstractmethod
    def greet(self, human: Union[Hugger, Handshaker]) -> None:
        pass


class Sex(Enum):
    MALE = "Male"
    FEMALE = "Female"


class Hugger:

    def _give_a_hug(self, other: Hugger):
        raise NotImplementedError


class Handshaker:

    def _handshake(self, other: Handshaker):
        raise NotImplementedError


class Man(Human, Handshaker):
    _sex = Sex.MALE
    _handshakes_cntr: int = 0

    @property
    def sex(self):
        return self._sex

    @property
    def handshakes(self) -> int:
        return self._handshakes_cntr

    @handshakes.setter
    def handshakes(self, val: int):
        self._handshakes_cntr = val

    def greet(self, human: Union[Woman, Man]):
        if human.sex == Sex.MALE:
            self._handshake(human)
        else:
            Man.give_a_hug(human)

    def _handshake(self, other: Man):
        self.handshakes = self.handshakes + 1
        other.handshakes = other.handshakes + 1

    @staticmethod
    def give_a_hug(other: Woman):
        other.hugs = other.hugs + 1


class Woman(Human, Hugger):
    _sex = Sex.FEMALE
    _hugs_cntr: int = 0

    @property
    def sex(self):
        return self._sex

    @property
    def hugs(self) -> int:
        return self._hugs_cntr

    @hugs.setter
    def hugs(self, val: int):
        self._hugs_cntr = val

    def greet(self, human: Union[Man, Woman]):
        if human.sex == Sex.FEMALE:
            self._give_a_hug(human)
        else:
            Woman.handshake(human)

    def _give_a_hug(self, other: Woman):
        self.hugs = self.hugs + 1
        other.hugs = other.hugs + 1

    @staticmethod
    def handshake(other: Man):
        other.handshakes = other.handshakes + 1


if __name__ == "__main__":
    man = Man()
    man2 = Man()
    woman = Woman()

    man.greet(woman)
    man2.greet(man)
