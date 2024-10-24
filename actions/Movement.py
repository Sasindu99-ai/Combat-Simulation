from enum import Enum

__all__ = ['Movement']


class Movement(Enum):
    """
	Enum class for movement actions.

	Movement.FORWARD	- Move forward
	Movement.BACKWARD	- Move backward
	Movement.LEFT		- Move left
	Movement.RIGHT 		- Move right
	"""

    FORWARD = [1, 'Move Forward']
    BACKWARD = [2, 'Move Backward']
    LEFT = [3, 'Move Left']
    RIGHT = [4, 'Move Right']

    def __str__(self):
        return self.value[1]

    def __repr__(self):
        return f'Action.{self.name}'
