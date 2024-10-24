from random import choice
from typing import List

__all__ = ['LOG']


class LOG:
    """
	Class Colors:
	Attributes:
		DAMAGE: str
		HEALING: str
		ENERGY: str
		LIFE: str
		RESET: str
		characterColors: dict
	Methods:
		randomCharacterColor(self)
	Description:
		This class represents the colors used in the game. The class has color codes for damage, healing, energy, and
		life. The class also has color codes for characters in the game.
	"""
    DAMAGE = '\033[91m'  # Color code for damage
    HEALING = '\033[92m'  # Color code for healing
    ENERGY = '\033[94m'  # Color code for energy
    LIFE = '\033[93m'  # Color code for life
    RESET = '\033[0m'  # Reset color code
    BOLD = '\033[1m'  # Bold text
    UNDERLINE = '\033[4m'  # Underline text
    # Character colors
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    PINK = '\033[95m'
    ORANGE = '\033[33m'
    PURPLE = '\033[35m'
    BROWN = '\033[33m'
    characterColors: List

    @classmethod
    def randomCharacterColor(cls):
        """
		This method returns a random color code for a character.
		:return: str
		"""
        if not hasattr(cls, 'characterColors'):
            cls.characterColors = [
                cls.CYAN,
                cls.MAGENTA,
                cls.PINK,
                cls.ORANGE,
                cls.PURPLE,
                cls.BROWN,
            ]
        return choice(list(cls.characterColors))
