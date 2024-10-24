# Combat Simulator Game

## Overview

The **Combat Simulator Game** is a Python-based combat simulation game that demonstrates the use of **SOLID design principles** and **Object-Oriented Programming (OOP)**. The game involves turn-based combat between characters with customizable weapons, actions, and movement. It supports both single-player and multiplayer modes, with asynchronous functionality for smoother gameplay.

## Key Features

- **OOP Design**: The game is structured around classes and objects, representing characters, weapons, food items, and the game logic itself. This design approach ensures modularity, making it easier to extend or modify the game's functionality.
  
- **SOLID Principles**:
  - **Single Responsibility Principle (SRP)**: Each class in the game has a specific responsibility. For instance, the character class handles character attributes and actions, while the weapon class deals only with weapon properties. This separation of concerns ensures that changes in one part of the code do not affect unrelated functionality.
  
  - **Open/Closed Principle (OCP)**: The system is open for extension but closed for modification. New weapons, food items, or actions can be added by creating new subclasses or objects without modifying existing code. This makes it easy to introduce new features with minimal risk of breaking existing functionality.

  - **Liskov Substitution Principle (LSP)**: Subclasses of the main objects (e.g., character types or weapon types) can be used interchangeably without affecting the correctness of the program. This ensures that derived classes extend base classes without altering the expected behavior.
  
  - **Interface Segregation Principle (ISP)**: The game interfaces are designed to be client-specific, preventing characters from being forced to implement unnecessary actions. Each character class has access to only the actions relevant to them, keeping interfaces lean and focused.

  - **Dependency Inversion Principle (DIP)**: High-level modules like the game logic do not depend on low-level modules (e.g., specific weapons or foods). Instead, abstractions are used to decouple components, making the game easier to scale and maintain.

- **Asynchronous Gameplay**: The game uses Python's `asyncio` library for handling combat and player actions in an asynchronous manner, improving performance and responsiveness, particularly in multiplayer mode.

## Gameplay

The game revolves around two main combat modes:

- **Single-Player Simulation**: Players can simulate battles between two characters by selecting them and allowing the game to automatically execute actions until one character wins.
  
- **Multiplayer Mode**: Players can choose their character, select actions in real-time, and battle against either a random opponent or a specific one.

## Object-Oriented Structure

The core of the game revolves around object-oriented concepts:

- **Encapsulation**: Each game entity (character, weapon, food) is encapsulated within its own class, with clearly defined attributes and methods that manage the entity's state and behavior.

- **Inheritance**: Characters can inherit common behaviors and attributes from a base character class, and specific types of weapons or actions can be created by extending base classes. This promotes code reuse and allows for easy customization of new features.

- **Polymorphism**: Methods in the game (such as attack or movement actions) are implemented polymorphically, meaning that different characters can have unique implementations of these actions while sharing the same interface.

## Extending the Game

The design is highly modular, allowing you to extend the game with new characters, weapons, or features easily. By following SOLID principles, adding new functionality, such as new game mechanics or additional items, becomes a straightforward process that maintains the integrity of the existing codebase.

## Getting Started

1. Clone the repository to your local machine.
2. Install Python 3.x if it's not already installed.
3. Run the game,
```shell
make run
```