# ⚔️ Dice Battle 🎲

A simple **two-player Dice Battle game built with Python** using **Object-Oriented Programming (OOP)** concepts.

Each player starts with **120 health points**. Players roll a six-sided die each round, and the player with the higher roll deals damage to the opponent based on the difference between their dice rolls.

## ✨ Features

* 🎲 Two-player dice battle
* ⚔️ Round-based gameplay
* ❤️ Each player starts with 120 health
* 🎯 Random dice rolls from 1 to 6
* 💥 Higher dice roll deals damage
* 🔥 Damage is calculated based on the difference between the rolls
* 🤝 Draws are possible when both players roll the same number
* 🏆 Battle ends when a player's health reaches zero
* 🎉 Displays the final winner
* ⚔️ Uses emojis for a more interactive experience

## 🛠️ Technologies Used

* **Python**
* **Object-Oriented Programming (OOP)**
* `random` module
* `emoji` module
* Classes and objects
* Loops
* Conditional statements
* User input

## ⚙️ How It Works

The game creates a `Game` class for each player. Each player has a **name** and **120 health points**. The `roll()` method generates a random number between **1 and 6**.

Two players are created at the beginning of the game and added to a player list.

During each round:

1. Player 1 rolls the dice.
2. Player 2 rolls the dice.
3. The dice values are compared.
4. The player with the higher roll wins the round.
5. The difference between the rolls is multiplied by **10** and deducted from the loser's health.
6. If both players roll the same number, the round ends in a draw.

### 💥 Damage Example

If Player 1 rolls **6** and Player 2 rolls **3**:

```text
6 - 3 = 3
3 × 10 = 30 damage
```

Player 2's health will be reduced by **30 points**.

## 🎮 Example

```text
----- Welcome to Dice Battle -----

Enter player 1 name : Abhinav
Enter player 2 name : Player 2

------------------
⚔️ Dice Battle ⚔️
------------------

Abhinav's turn!! Type(R) : R
You got 6

Player 2's turn!! Type(R) : R
You got 3

Abhinav won this round 🔥

Player 2's health has been cut down by 30

Player 2 Health : 90/120
Abhinav Health : 120/120
```

## 🎯 Learning Concepts

This project demonstrates:

* Classes and objects
* Constructors
* Instance attributes
* Instance methods
* Random number generation
* Lists
* `while` loops
* `for` loops
* Conditional statements
* User input
* Mathematical calculations
* Game-state management
* Basic Object-Oriented Programming

## 👨‍💻 Author

**Abhinav**

A Python project created for practicing **Object-Oriented Programming, random number generation, and game development logic**.
