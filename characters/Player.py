from characters.Character import Character

__all__ = ['Player']


class Player(Character):
    """
	Class Player:
	Attributes:
		See Character class.
	Methods:
		chooseAction(self, playground, opponent)
	Description:
		This class represents a player in a game. The player can choose an action from a list of available actions.
	"""

    def chooseAction(self, playground, opponent: Character) -> None:
        """
		This method allows the player to choose an action.
		:param playground: Playground of the game.
		:param opponent: Opponent character.
		:return: None
		"""
        tookAction = False
        rounds = 0
        while not tookAction and rounds < 20:
            try:
                availableActions = list(set(self.getAvailableActions(playground, opponent)))
                print(f'{self.getPrompt()} Choose an action: ')
                for index, action in enumerate(availableActions):
                    print(f'\t{index + 1}. {action}')
                action = availableActions[int(input('Enter the index of the action: ')) - 1]
                print(f'{self.getPrompt()} took action: {action}')
                tookAction = self.launchAction(action, playground, opponent)
                rounds += 1
            except ValueError:
                print('Invalid input. Please enter a valid index.')
