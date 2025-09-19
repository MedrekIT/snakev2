# Classic "Snake" game clone

Snake - clone of classic game written in Python with Pygame. Game is about a snake that moves in four directions, looks for an apple and extends its length after consumption.

---

## Table of Contents

- [Demo](#demo)
- [Motivation](#motivation)
- [Information](#information)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

---

## Demo

![Gameplay](./demo/gameplay.gif)

---

## Motivation

My development of this project was driven by the desire to:
- Make it fast - I wanted this game to not be laggy, what I accomplished with a few well designed functions and classes.
- Make it clean - The game as well as its code are well organized and self-explanatory.
- Make it fun - You can literally play this game, try to reach high scores, get addicted, and even invite your friends to compete.

---

## Information

> [!NOTE]
> **Requirements:**
> - `python>=3.12`
> - `pygame==2.6.1`
> - `uv==0.7.21`

> [!IMPORTANT]
> This game is probably not optimized for huge scores, apple randomly chooses coordinates and checks if they are not occupied by snake, which may affect performance, snake starts to move much faster during gameplay.

- Saved scores are automatically added to `./leaderboard/leaderboard.log` file.

## Installation

```bash
git clone https://github.com/MedrekIT/snakev2.git
cd snakev2
uv venv
source .venv/bin/activate
uv add -r requirements.txt
```

---

## Usage

### Run
```bash
source .venv/bin/activate
uv run main.py
```

### Gameplay
**Instructions on the screen guide you through everything, but in case you needed:**

There are 4 levels of difficulty:
> - `EASY`
> - `NORMAL`
> - `HARD`
> - `INSANE`

Each of them alters acceleration of the snake after every apple consumption.

In-game movement:
> - `W` - Move up
> - `S` - Move down
> - `A` - Move left
> - `D` - Move right
> - `SPACE` - Pause

After you lose, you might save your score with `S`.

In main menu you can see leaderboard with `TAB`.

---

## Contributing

### Clone the repo

```bash
git clone https://github.com/MedrekIT/snakev2.git
cd snakev2
```

### Install requirements

```bash
uv venv
source .venv/bin/activate
uv add -r requirements.txt
```

### Test if it works

```bash
source .venv/bin/activate
uv run main.py
```

### Submit a pull request

If you'd like to contribute, please fork the repository and open a pull request to the `main` branch.
