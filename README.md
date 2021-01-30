# 2048

[2048 Tweet](https://twitter.com/culyTech/status/1351367472583041026?s=20)

<p align="center">
  <img src="/images/2048_start_game.png" alt="2048 Banner"/>
</p>

## Table of Contents

1. [About The Project](README.md#about-the-project)
2. [Getting Started](README.md#getting-started)
    * [Prerequisites](README.md#prerequisites)
    * [Installation](README.md#installation)
3. [Game Rules](README.md#game-rules)
4. [Testing Examples](README.md#testing-examples)
4. [File Descriptions](README.md#file-descriptions)
5. [Contact](README.md#contact)
6. [Acknowledgements](README.md#contact)

## About the Project

A command line 2048 game to practice programming skills, specificaly newly learned skills in the NumPy library and using Test Driven Development techniques with PyTest.

## Getting Started

In order to run the application, install and do the following in an Ubuntu Linux Environment.

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

Run the game in the Ubuntu Command Line from the  ```~/final/src/``` directory.

```python3 game.py```

### Game Rules

* This is a 4 x 4 grid game with the ultimate goal of achieving the elusive 2048 tile.
* Every turn, either a 2 (90% chance) or a 4 (10% chance) will appear. 
* Tiles will slide to the farthest possible position in a certain direction chosen by the player.
* If two tiles of the same value collide, they will merge into their respective sums.
* Three consecutive tiles will only have the two of the farthest direction merge.
* Your score goes up by the value of the tiles that merge. Enjoy!!!

**UP**

To go up, press 'w" and then enter.

![2048: Up](/images/2048_up.png)

'a' to go left and then enter.

![2048: Left](/images/2048_left.png)

Press 's'  and then enter to go down.

![2048: Down](/images/2048_down.png)

'd' and then enter for right.

![2048: Right](/images/2048_right.png)

## Testing Examples

To run tests, simply use the coding editor of your choice. The following directions are done on VS Code.
1. Press in **Ctrl-\`** to open up your command terminal.
2. Activate the virtual env: ```source venv_2048```
3. Navigate (```cd```) to ```~/final/tests/``` folder
4. Run every test: ```pytest test_board.py```

![2048: Testing 1](/images/2048_pytest_1.png)

5. Or, run individual test by typing in the specific test module or test class in "" after -k. Example: ```pytest test_board.py -k "test_shift_matrix_left"```

![2048: Testing 2](/images/2048_pytest_2.png)

## File Descriptions
- **images**: Gameplay Images
- **2048_version_1**: Unfinished version (no NumPy implementation).
    - ***2048_v1.py***: First version of the game.
    - ***board.py***: Board for first version.
- **Final**: Final version.
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
[2048 python numpy](https://gist.github.com/wbars/88df9704306629c40c7929e691b48b98) by @github.com/wbars
