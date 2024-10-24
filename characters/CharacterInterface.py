from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

from actions import Action, Movement
from foods import Food
from weapons import Weapon

__all__ = ['CharacterInterface']

T = TypeVar('T', bound='CharacterInterface')


class CharacterInterface(ABC, Generic[T]):
    """
	Class Character:
	Attributes:
		name: str
		weapon: Weapon
		energy: int
		life: int
		color: str
		boundary: int
		x: int
		y: int
		alive: bool
	Methods:
		getPrompt(self) -> str
		change_name(self, new_name)
		change_weapon(self, new_weapon)
		increase_energy(self, food_type)
		decrease_energy(self, shots)
	Description:
		This class represents a character in a game. The character has a name, weapon, energy, and life. The character
		can change its name, weapon, increase energy by consuming foods, decrease energy by taking shots, and move left,
		right, forward, or backward by 10 units within the game space limited to a 1000 x 1000 square unit area.
	"""

    name: str
    weapon: Weapon | None
    energy: int
    life: int
    color: str
    boundary: int
    x: int
    y: int
    alive: bool

    @abstractmethod
    def getPrompt(self) -> str:
        """
		This method returns the prompt of the character.
		:return:  The prompt of the character.
		"""
        pass

    @abstractmethod
    def tabIndent(self) -> str:
        """
		This method returns the tab indent of the character.
		:return: The tab indent of the character.
		"""

    @abstractmethod
    def change_name(self, new_name: str) -> None:
        """
		This method changes the name of the character.
		:param new_name: New name of the character.
		:type new_name: str
		"""
        pass

    @abstractmethod
    def change_weapon(self, new_weapon: Weapon) -> None:
        """
		This method changes the weapon of the character.
		:param new_weapon: New weapon of the character.
		:type new_weapon: Weapon
		"""
        pass

    @abstractmethod
    def increase_energy(self, food_type: Food) -> None:
        """
		This method increases the energy of the character by consuming foods.
		:param food_type: Type of foods consumed.
		:type food_type: Food
		"""
        pass

    @abstractmethod
    def decrease_energy(self, shots: int) -> None:
        """
		This method decreases the energy of the character by taking shots.
		:param shots: Number of shots taken.
		:type shots: int
		"""
        pass

    @abstractmethod
    def move_left(self) -> None:
        """
		This method moves the character to the left by 10 units.
		"""
        pass

    @abstractmethod
    def move_right(self) -> None:
        """
		This method moves the character to the right by 10 units.
		"""
        pass

    @abstractmethod
    def move_forward(self) -> None:
        """
		This method moves the character forward by 10 units.
		"""
        pass

    @abstractmethod
    def move_backward(self) -> None:
        """
		This method moves the character backward by 10 units.
		"""
        pass

    @abstractmethod
    def intro(self) -> str:
        """
		This method returns the introduction of the character.
		:return: Introduction of the character.
		"""
        pass

    @abstractmethod
    def setPosition(self, x: int, y: int) -> None:
        """
		This method sets the position of the character.
		:param x: X-coordinate of the character.
		:type x: int
		:param y: Y-coordinate of the character.
		:type y: int
		"""
        pass

    @abstractmethod
    def getDistance(self, opponent: T) -> int:
        """
		This method calculates the distance between the character and the opponent.
		:param opponent: Opponent character.
		:return: Distance between the character and the opponent.
		"""
        pass

    @abstractmethod
    def getAvailableActions(self, playground, opponent: T) -> List[Movement | Action]:
        """
		This method returns the available actions of the character.
		:param playground:
		:param opponent:
		:return:
		"""
        pass

    @abstractmethod
    def launchAction(self, action: Action | Movement, playground, opponent: T) -> bool:
        """
		This method launches an action of the character.
		:param action:
		:param playground:
		:param opponent:
		:return:
		"""
        pass
