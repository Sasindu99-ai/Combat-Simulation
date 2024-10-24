from dataclasses import dataclass

__all__ = ['Weapon']


@dataclass
class Weapon:
    """
	Class Weapon:
	Attributes:
		name: str
		damage: int
		rangeRadius: int
	Methods:
		None
	Description:
		This class represents a weapon in a game. The weapon has a name, damage level, and range. The weapon is used by
		the character to attack other characters in the game.
	"""
    name: str
    damage: int
    rangeRadius: int
