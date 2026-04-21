# Durak Game (Python)

A simple console implementation of the classic Russian card game Durak, written in Python.
Includes basic game mechanics and a simple AI opponent.

## 🎮 Features

* 36-card deck
* Trump suit system
* Turn-based gameplay
* Player vs Computer
* Automatic card drawing
* Win/lose detection

## 🧠 AI Logic

The computer uses a simple strategy:
* Attacks with the weakest available card
* Defends using the lowest possible card (taking trump into account)

## 🚀 How to Run

Make sure you have Python 3 installed, then run:
```
python3 main.py
```

## 📁 Project Structure

```
src/
├── main.py        # Entry point, starts the game loop
├── game.py        # Core game mechanics (rules, turns, flow)
├── ai.py          # AI logic (bot behavior)
├── cards.py       # Deck system and card utilities

```

## 📌 Future Improvements

* Add table mechanics (cards on the table)
* Implement card throwing (“podkidnoy” rules)
* Improve AI decision-making
* Add a graphical interface

## 🛠 Tech Stack

* Python 3

## 👤 Author

DrPenic