from random import choice
from typing import List

from actions import Action, Movement
from foods import Food
from utils import LOG
from weapons import Weapon

from .CharacterInterface import CharacterInterface

__all__ = ['Character']


class Character(CharacterInterface):
    x: int = 0
    y: int = 0
    alive: bool = True

    def __init__(self, name: str, weapon: Weapon | None, energy: int, life: int, color: str, boundary: int = 1000):
        """
		This method initializes the attributes of the class.
		:param name: Name of the character.
		:param weapon: Weapon of the character.
		:param energy: Energy of the character.
		:param life: Life of the character.
		:param boundary: Boundary of the game space.
		:type name: str
		:type weapon: Weapon
		:type energy: int
		:type life: int
		:type boundary: int
		"""
        self.name = name
        self.weapon = weapon
        self.energy = energy
        self.life = life
        self.boundary = boundary

        self.color = color

    def getPrompt(self) -> str:
        return f'{self.color}# {self.name}: {LOG.RESET}'

    def tabIndent(self) -> str:
        return ' ' * len('# ' + self.name + ':')

    def change_name(self, new_name: str):
        print(f'{self.getPrompt()} changed their name to {self.color}{new_name}{LOG.RESET}')
        self.name = new_name

    def change_weapon(self, new_weapon: Weapon):
        print(f'{self.getPrompt()} changed their weapon to {self.color}{new_weapon.name}{LOG.RESET}')
        self.weapon = new_weapon

    def increase_energy(self, food: Food):
        self.energy += food.energy
        if self.energy >= 100:
            if self.life < 2:
                self.life += 1
                self.energy -= 100
                print(
                    f'{self.getPrompt()} consumed {food.name} and increased their energy by {LOG.ENERGY}{food.energy}'
                    f'{LOG.RESET}\n{self.tabIndent()} {LOG.ENERGY}Energy: {self.energy}{LOG.RESET}'
                    f'\n{self.tabIndent()} {LOG.LIFE}Life: {self.life}{LOG.RESET}'
                )
            else:
                print(
                    f'{self.getPrompt()} consumed {food.name} and increased their energy by '
                    f'{LOG.ENERGY}{100 - self.energy}{LOG.RESET}\n{self.tabIndent()} {LOG.ENERGY}Energy: {self.energy}'
                    f'{LOG.RESET}\n{self.tabIndent()} {LOG.LIFE}Life: {self.life}{LOG.RESET}'
                )
                self.energy = 100

    def decrease_energy(self, shots: int):
        self.energy -= shots
        if self.energy <= 0 < self.life:
            self.life -= 1
            self.energy += 100
        elif self.energy <= 0 and self.life == 0:
            self.alive = False
        print(
            f'{self.getPrompt()} took {LOG.DAMAGE}{shots}{LOG.RESET} shots and decreased their energy by '
            f'{LOG.ENERGY}{shots}{LOG.RESET}\n{self.tabIndent()} {LOG.ENERGY}Energy: {self.energy}{LOG.RESET}\n'
            f'{self.tabIndent()} {LOG.LIFE}Life: {self.life}{LOG.RESET}'
        )

    def move_left(self):
        if self.x - 10 >= 0:
            self.x -= 10
            print(
                f'{self.getPrompt()} moved 10 units to the left\n{self.tabIndent()} '
                f'Position: ({self.x}, {self.y})'
            )

    def move_right(self):
        if self.x + 10 <= self.boundary:
            self.x += 10
            print(
                f'{self.getPrompt()} moved 10 units to the right\n{self.tabIndent()} '
                f'Position: ({self.x}, {self.y})'
            )

    def move_forward(self):
        if self.y + 10 <= self.boundary:
            self.y += 10
            print(f'{self.getPrompt()} moved 10 units forward\n{self.tabIndent()} '
                  f'Position: ({self.x}, {self.y})')

    def move_backward(self):
        if self.y - 10 >= 0:
            self.y -= 10
            print(
                f'{self.getPrompt()} moved 10 units backward\n{self.tabIndent()} '
                f'Position: ({self.x}, {self.y})'
            )

    def intro(self) -> str:
        return f'{self.getPrompt()} {self.color}Name: {self.name}, Energy: {self.energy}, Life: {self.life}{LOG.RESET}'

    def setPosition(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def getDistance(self, opponent) -> int:
        return ((self.x - opponent.x)**2 + (self.y - opponent.y)**2)**0.5

    def getAvailableActions(self, playground, opponent) -> List[Movement | Action]:
        actions: List[Movement | Action] = []
        if len(playground.getAvailableWeapons()) > 0:
            actions += [Action.CHANGE_WEAPON] * 2
        if self.energy >= 20 and self.weapon is not None and self.getDistance(opponent) <= self.weapon.rangeRadius:
            actions += [Action.ATTACK] * 10
        if self.energy < 100 and len(playground.getAvailableFoods()) > 0:
            actions += [Action.EAT] * 5
        if self.x - 10 >= 0:
            actions.append(Movement.LEFT)
        if self.x + 10 <= self.boundary:
            actions.append(Movement.RIGHT)
        if self.y + 10 <= self.boundary:
            actions.append(Movement.FORWARD)
        if self.y - 10 >= 0:
            actions.append(Movement.BACKWARD)
        return actions

    def launchAction(self, action: Action | Movement, playground, opponent) -> bool:
        if action == Action.CHANGE_WEAPON:
            self.change_weapon(choice(playground.getAvailableWeapons()))
            return False
        elif action == Action.ATTACK and isinstance(self.weapon, Weapon):
            opponent.decrease_energy(self.weapon.damage)
            return True
        elif action == Action.EAT:
            self.increase_energy(choice(playground.getAvailableFoods()))
            return True
        elif action == Movement.LEFT:
            self.move_left()
            return False
        elif action == Movement.RIGHT:
            self.move_right()
            return False
        elif action == Movement.FORWARD:
            self.move_forward()
            return False
        elif action == Movement.BACKWARD:
            self.move_backward()
            return False
        return False
