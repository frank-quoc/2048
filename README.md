# 2048

<p align="center">
  <img src="https://i1.wp.com/itsfoss.com/wp-content/uploads/2018/07/play-2048-game-linux.jpeg?fit=800%2C450&ssl=1" alt="2048 Banner"/>
</p>

## Table of Contents

1. [About The Project](README.md#about-the-project)
2. [Getting Started](README.md#getting-started)
    * [Prerequisites](README.md#prerequisites)
    * [Installation](README.md#installation)
3. [Game Rules](README.md#game-rules)
4. [File Descriptions](README.md#file-descriptions)
5. [Contact](README.md#contact)
6. [Acknowledgements](README.md#contact)

## About the Project

A command line 2048 game to practice programming skills, specificaly newly learned skills in the NumPy library and using Test Driven Development techniques with PyTest.

![2048: Testing Code](/images/2048_testing_code)

## Getting Started

In order to run the application, install and do the following.

### Prerequisites
Update System

```sudo apt-get update```

Install Python and Pip3
  * Python 3.8
  
  ```sudo apt install python3.8 ```

  * pip3
  
  ``` sudo apt-get update```

### Installation

Clone the repo
  
  ```git clone https://github.com/frank-quoc/2048.git```

Install required libraries from ```requirement.txt```
  * Numpy 1.19.4
  * PyTest 6.2.1
  
  ```pip3 install -r requirements.txt```
  
Check what modules are installed
  
  ```pip freeze > requirements.txt```
  

### Game Rules
```
This is a 4 x 4 grid game with the ultimate goal of achieving the elusive 2048 tile.
Every turn, either a 2 (90% chance) or a 4 (10% chance) will appear. 
Tiles will slide to the farthest possible position in a certain direction chosen by the player.
If two tiles of the same value collide, they will merge into their respective sums.
Three consecutive tiles will only have the two of the farthest direction merge.
Your score goes up by the value of the tiles that merge. Enjoy!!!
```

![2048: Start](/images/2048_start_game)

![2048: Lose](/images/2048_lose_cond)

## File Descriptions
- **images**: Gameplay Images
- **2048_version_1**: Unfinished version (no NumPy implementation).
    - ***2048_v1.py***: First version of the game.
    - ***board.py***: Board for first version.
- **2048_version_2**: Final version.
    - ***src***: Source Folder
        - *board.py*: Board for final version.
        - *game.py*: Final version of the game (Run game here).
    - ***tests***: Testing folder.
        - *test_board.py*: Testing file.
    - ***requirements.txt***: Required libraries to download.
    - ***venv_2048***: Virtual Environment to run tests.

## Contacts

Frank Ho - [@cuLyTech](https://twitter.com/culyTech)

Project Link: [https://github.com/frank-quoc/2048](https://github.com/frank-quoc/2048)

## Acknowledgements
[2048 python numpy](https://medium.com/byte-tales/the-classic-tic-tac-toe-game-in-python-3-1427c68b8874) by @github.com/wbars
