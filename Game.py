import asyncio
from random import choice
from typing import List

from characters import NPC, Player
from foods import EnergyDrink, Food, MagicPotion, Mushroom, PowerBar
from inventory import InventoryItem

__all__ = ['Game']

from utils import LOG
from weapons import (
    AirRifle, Bomb, Flamethrower, Grenade, MachineGun, Pistol, Rifle, RocketLauncher, Shotgun, SniperRifle, Weapon
)


class Game:
    """
	Class Game:
	Attributes:
		characters: List
		weapons: List[InventoryItem]
		foods: List[InventoryItem]
		boundary: int
		opponent_1: NPC | Player
		opponent_2: NPC | Player
	Methods:
		__init__(): None
		add_character(character: NPC | Player): None
		view_characters(): None
		select_character(index: int) -> NPC
		start(): None
		simulate(): None
		combat(attacker: NPC, defender: NPC): None
		convertNPCtoPlayer(npc: NPC) -> Player
		multiplayer(): None
		getAvailableWeapons() -> List[Weapon]
		getAvailableFoods() -> List[Food]
	Description:
		This class represents a game. The game has a list of characters, weapons, and food items. The game can simulate a
		combat between two characters or start a multiplayer game between a player and an opponent.
	"""

    characters: List
    weapons: List[InventoryItem]
    foods: List[InventoryItem]
    boundary: int = 1000

    opponent_1: NPC | Player
    opponent_2: NPC | Player

    def __init__(self):
        """
		This method initializes the attributes of the class.
		"""
        print(f'{LOG.BOLD}{LOG.ENERGY}Welcome to the Combat Simulator!{LOG.RESET}')

        # Initializing characters
        print(f'{LOG.BOLD}Initializing Characters{LOG.RESET}')
        self.characters = [
            NPC('Warrior', None, 100, 1, LOG.PURPLE, self.boundary),
            NPC('Mage', None, 100, 1, LOG.ORANGE, self.boundary),
            NPC('Archer', None, 100, 1, LOG.CYAN, self.boundary),
        ]

        # Initializing weapons
        print(f'{LOG.BOLD}Initializing Weapons{LOG.RESET}')
        self.weapons = [
            InventoryItem(AirRifle, 1),
            InventoryItem(SniperRifle, 1),
            InventoryItem(Shotgun, 1),
            InventoryItem(Bomb, 10),
            InventoryItem(Grenade, 10),
            InventoryItem(Pistol, 10),
            InventoryItem(Rifle, 10),
            InventoryItem(MachineGun, 10),
            InventoryItem(RocketLauncher, 10),
            InventoryItem(Flamethrower, 10),
        ]

        # Initializing foods
        print(f'{LOG.BOLD}Initializing Foods{LOG.RESET}')
        self.foods = [
            InventoryItem(EnergyDrink, 5),
            InventoryItem(Mushroom, 5),
            InventoryItem(MagicPotion, 5),
            InventoryItem(PowerBar, 5),
        ]

        # Displaying characters
        print(f'{LOG.BOLD}Characters: {LOG.RESET}')
        for index, character in enumerate(self.characters):
            print(f'\t{index + 1}. {character.intro()}')

        # Displaying weapons
        print(f'{LOG.BOLD}Weapons: {LOG.RESET}')
        for index, weapon in enumerate(self.weapons):
            print(
                f'\t{index + 1}. {weapon.item.name} - Damage: {weapon.item.damage}, Range: {weapon.item.rangeRadius}'
            )

        # Displaying foods
        print(f'{LOG.BOLD}Foods: {LOG.RESET}')
        for index, food in enumerate(self.foods):
            print(f'\t{index + 1}. {food.item.name} - Energy: {food.item.energy}')

        self.start()

    def add_character(self, character: NPC | Player):
        """
		This method adds a character to the game.
		:param character: The character to be added.
		:return: None
		"""
        self.characters.append(character)
        print(f'{LOG.BOLD}Character added to the game{LOG.RESET}')
        print(f'{self.characters.index(character) + 1}. {character.intro()}')

    def view_characters(self):
        """
		This method displays all the characters in the game.
		:return: None
		"""
        print(f'{LOG.BOLD}Characters: {LOG.RESET}')
        for index, character in enumerate(self.characters):
            print(f'\t{index + 1}. {character.intro()}')

    def select_character(self, index) -> NPC:
        """
		This method selects a character from the list based on its index.
		:param index: The index of the character in the list.
		:type index: int
		:return: Character
		"""
        return self.characters[index]

    def start(self) -> None:
        """
		This method starts the game.
		:return: None
		"""

        while True:
            print('\n\nChoose an action: \n\t1. Simulate\n\t2. Multiplayer\n\t-1. Exit')
            action = input('Enter the action: ')
            if action == '1':
                asyncio.run(self.simulate())
            elif action == '2':
                asyncio.run(self.multiplayer())
            elif action == '-1':
                break
            else:
                print(f'{LOG.DAMAGE}Error: Invalid action{LOG.RESET}')

    async def simulate(self):
        """
		This method simulates a combat between two characters.
		:return: None
		"""
        print(f'{LOG.BOLD}Simulation Started{LOG.RESET}')
        print(f'{LOG.BOLD}Choose two characters{LOG.RESET}')
        self.view_characters()
        self.opponent_1 = self.select_character(int(input('Select the first character: ')) - 1)
        self.opponent_2 = self.select_character(int(input('Select the second character: ')) - 1)
        print(f'{LOG.BOLD}Characters selected{LOG.RESET}')
        print(f'{self.opponent_1.intro()}')
        print(f'{self.opponent_2.intro()}')

        self.opponent_1.setPosition(0, 0)
        self.opponent_2.setPosition(1000, 1000)

        task = [
            self.combat(self.opponent_1, self.opponent_2),
            self.combat(self.opponent_2, self.opponent_1),
        ]
        await asyncio.gather(*task)

    async def combat(self, attacker: NPC, defender: NPC):
        """
		This method simulates a combat between two characters.
		:param attacker: The attacking character.
		:param defender: The defending character.
		:return: None
		"""
        while attacker.alive and defender.alive:
            await attacker.takeAction(self, defender)
            await asyncio.sleep(0)
        if attacker.alive:
            print(f'{LOG.BOLD}{LOG.DAMAGE}Game Over!{LOG.RESET}')
            print(f'{attacker.getPrompt()} {LOG.DAMAGE}{defender.name} is dead!{LOG.RESET}')
            print(f'{attacker.getPrompt()} {LOG.HEALING}I Won!{LOG.RESET}')

    def convertNPCtoPlayer(self, npc: NPC) -> Player:
        """
		This method converts an NPC to a Player.
		:param npc: The NPC to be converted.
		:return: Player
		"""
        return Player(npc.name, npc.weapon, npc.energy, npc.life, npc.color, self.boundary)

    async def multiplayer(self):
        """
		This method starts a multiplayer game.
		:return: None
		"""
        # Let user choose his character
        print(f'{LOG.BOLD}Choose a character{LOG.RESET}')
        self.view_characters()
        player = self.convertNPCtoPlayer(self.select_character(int(input('Select a character: ')) - 1))
        self.characters.remove(player)
        print(f'{LOG.BOLD}Character selected{LOG.RESET}')
        print(f'{player.intro()}')
        print(f'{LOG.BOLD}Waiting for the opponent to join{LOG.RESET}')
        print(f'{LOG.BOLD}Choose an opponent{LOG.RESET}')
        self.view_characters()
        print(f'\t{len(self.characters) + 1}. Random')
        selectedChoice = int(input('Select the opponent: '))
        if selectedChoice == len(self.characters) + 1:
            opponent = choice(self.characters)
        else:
            opponent = self.select_character(selectedChoice - 1)
        print(f'{LOG.BOLD}Opponent selected{LOG.RESET}')
        print(f'{opponent.intro()}')
        print(f'{LOG.BOLD}Game Started{LOG.RESET}')

        player.setPosition(0, 0)
        opponent.setPosition(1000, 1000)

        while player.alive and opponent.alive:
            player.chooseAction(self, opponent)
            if not player.alive:
                print(f'{LOG.BOLD}{LOG.DAMAGE}Game Over!{LOG.RESET}')
                break
            await opponent.takeAction(self, player)
            await asyncio.sleep(0)
            if not opponent.alive:
                print(f'{LOG.BOLD}{LOG.DAMAGE}Game Over!{LOG.RESET}')
                break
        print(f'{LOG.BOLD}Game Ended{LOG.RESET}')
        if player.alive:
            print(f'{LOG.BOLD}{LOG.HEALING}You Won!{LOG.RESET}')
        else:
            print(f'{LOG.BOLD}{LOG.DAMAGE}You Lost!{LOG.RESET}')
        playerCharacter: NPC = NPC(player.name, None, 100, 1, player.color, self.boundary)
        self.add_character(playerCharacter)

    def getAvailableWeapons(self) -> List[Weapon]:
        """
		This method returns the list of available weapons.
		:return: List[Weapon]
		"""
        weapons: List[Weapon] = []
        for item in self.weapons:
            if item.stock > 0 and isinstance(item.item, Weapon):
                weapons.append(item.item)
        return weapons

    def getAvailableFoods(self) -> List[Food]:
        """
		This method returns the list of available food items.
		:return: List[Food]
		"""
        foods: List[Food] = []
        for item in self.foods:
            print()
            if item.stock > 0 and isinstance(item.item, Food):
                foods.append(item.item)
        return foods
