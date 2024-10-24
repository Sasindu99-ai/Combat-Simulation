from foods import Food
from weapons import Weapon

__all__ = ['InventoryItem']


class InventoryItem:
    """
	Class InventoryItem:
	Attributes:
		item: Food | Weapon
		stock: int
	Methods:
		None
	"""
    item: Food | Weapon
    stock: int

    def __init__(self, item: Food | Weapon, stock: int):
        self.item = item
        self.stock = stock
