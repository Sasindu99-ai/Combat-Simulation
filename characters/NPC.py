from random import choice

from characters.Character import Character

__all__ = ['NPC']


class NPC(Character):
    """
	Class NPC:
	Attributes:
		See Character class.
	Methods:
		takeAction(self, playground, opponent)
	Description:
		This class represents a non-player character in a game. The NPC has the same attributes and methods as the
		Character class. The NPC takes actions randomly from the available actions until it takes an action successfully.
	"""

    async def takeAction(self, playground, opponent: Character) -> None:
        """
		This method takes an action randomly from the available actions until it takes an action successfully.
		:param playground: Playground of the game.
		:param opponent: Opponent character.
		:return: None
		"""
        tookAction = False
        rounds = 0
        while not tookAction and rounds < 20:
            availableActions = self.getAvailableActions(playground, opponent)
            action = choice(availableActions)
            print(f'{self.getPrompt()} took action: {action}')
            tookAction = self.launchAction(action, playground, opponent)
            rounds += 1
