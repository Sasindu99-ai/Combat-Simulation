from enum import Enum

__all__ = ['Action']


class Action(Enum):
    """
	Enum class for actions

	Action.CHANGE_WEAPON	- Change weapon
	Action.ATTACK			- Attack
	Action.EAT				- Eat
	"""

    CHANGE_WEAPON = [1, 'Change Weapon']
    ATTACK = [2, 'Attack']
    EAT = [3, 'Eat']

    def __str__(self):
        return self.value[1]

    def __repr__(self):
        return f'Action.{self.name}'
