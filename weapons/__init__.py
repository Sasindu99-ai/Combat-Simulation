from .Weapon import Weapon

AirRifle = Weapon('Air Rifle', 7, 300)
SniperRifle = Weapon('Sniper Rifle', 16, 700)
Shotgun = Weapon('Shotgun', 21, 200)
Bomb = Weapon('Bomb', 33, 500)
Grenade = Weapon('Grenade', 25, 300)
Pistol = Weapon('Pistol', 12, 100)
Rifle = Weapon('Rifle', 15, 400)
MachineGun = Weapon('Machine Gun', 30, 500)
RocketLauncher = Weapon('Rocket Launcher', 50, 1000)
Flamethrower = Weapon('Flamethrower', 40, 200)

__all__ = [
    'Weapon', 'AirRifle', 'SniperRifle', 'Shotgun', 'Bomb', 'Grenade', 'Pistol', 'Rifle', 'MachineGun',
    'RocketLauncher', 'Flamethrower'
]
