# 🐍💧🔫 Snake Water Gun Game

A simple **Snake Water Gun game built with Python**, where the player competes against the computer.

The player chooses **Snake, Water, or Gun**, while the computer randomly selects one of the three choices. The program then compares both choices and determines the winner.

## ✨ Features

* 🐍 Snake
* 💧 Water
* 🔫 Gun
* 🤖 Computer makes a random choice
* 🏆 Automatically determines the winner
* 🤝 Handles draw situations
* ⚠️ Validates incorrect input
* 🔤 Accepts user input without being case-sensitive

## 🛠️ Technologies Used

* **Python**
* Random selection
* Lists
* User input
* Conditional statements
* String methods
* `if-elif-else`

## ⚙️ How It Works

The game contains three possible choices:

```text
Snake
Water
Gun
```

The player enters one choice, while the computer randomly selects one from the available choices.

The program converts both choices to lowercase so that inputs such as `SNAKE`, `snake`, or `Snake` can be handled consistently.

The winner is then determined using conditional statements:

* 🐍 **Snake beats Water**
* 🔫 **Gun beats Snake**
* 💧 **Water beats Gun**
* 🤝 Same choices result in a draw

If the player enters something other than the three valid choices, the program displays an invalid-input message.

## 🎮 Example

```text
choose any one---> SNAKE / WATER / GUN : SNAKE

Player selected snake
Computer selected water

Snake won
```

## 🎯 Learning Concepts

This project demonstrates:

* Random choice selection
* Lists
* User input
* String manipulation
* `.lower()` method
* Conditional statements
* Comparison operators
* Basic game logic
* Input validation

## 👨‍💻 Author

**Abhinav**

A simple Python project created for practicing **Python programming fundamentals, conditional logic, and basic game development**.
