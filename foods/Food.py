from dataclasses import dataclass

__all__ = ['Food']


@dataclass
class Food:
    """
	Class Food:
	Attributes:
		name: str
		energy: int
	Methods:
		None
	Description:
		This class represents a food item in a game. The food item has a name and energy level. The energy level of the
		food item is used to increase the energy level of the character in the game.
	"""
    name: str
    energy: int
