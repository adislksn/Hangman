# Hangman 
[![PyPI version](https://badge.fury.io/py/pygame.svg)](https://badge.fury.io/py/pygame)

## Youtube Video
[![Click to open youtube video](https://img.youtube.com/vi/9u2yUmBjJmc/0.jpg)](https://youtu.be/9u2yUmBjJmc)

## Description
Program that allows the user to play the classic game of Hangman. The user is prompted to enter a word, and the program will display a partially completed word, as well as the number of incorrect guesses remaining. The user is prompted to guess a letter, and the program will respond appropriately. If the user guesses a letter that is not in the word, the program will display the incorrect guess count, and the user will be prompted to guess another letter. If the user guesses a letter that is in the word, the program will display the partially completed word, and the user will be prompted to guess another letter. If the user guesses all the letters in the word, the program will display the completed word, and the user will be prompted to play again.

## Installation
To install the program with docker, run the following command in the terminal:
```bash
docker build -t hangman-py .
```
or
```bash
make build-hangman
```
Then run the following command in the terminal:
```bash
docker run hangman-py
```
or
```bash
make run-windows
```
But we still encountered a problem with the videodriver.
```bash
Traceback (most recent call last):
  File "/app/Hangman-code.py", line 13, in <module>
    display = pygame.display.set_mode((width, height))
pygame.error: No available video device
```
## Anggota Kelompok RD-07

|  [<img src="https://avatars.githubusercontent.com/u/94353897?s=64&v=4" width="100px;"/><br /><sub><b>Pandu F</b></sub>](https://github.com/PanduF)<br />[🖥️](https://github.com/adislksn/FE-PPLK-2022/commits?author=PanduF "Code") 120140020  | [<img src="https://avatars.githubusercontent.com/u/104607855?s=64&v=4" width="100px;"/><br /><sub><b>Nashirotul</b></sub>](https://github.com/nashirotul)<br />[🖥️](https://github.com/adislksn/FE-PPLK-2022/commits?author=nashirotul "Code") 120140031  |  [<img src="https://avatars.githubusercontent.com/u/98870264?s=64&v=4" width="100px;"/><br /><sub><b>Adi S</b></sub>](https://github.com/adislksn)<br />[🖥️](https://github.com/adislksn/FE-PPLK-2022/commits?author=adislksn "Code") 120140038 | [<img src="https://avatars.githubusercontent.com/u/104456433?s=64&v=4" width="100px;"/><br /><sub><b>Lidya A</b></sub>](https://github.com/lalvionisya)<br />[🖥️](https://github.com/adislksn/FE-PPLK-2022/commits?author=lalvionisya "Code") 120140042  | [<img src="https://avatars.githubusercontent.com/u/104608536?s=64&v=4" width="100px;"/><br /><sub><b>Devi Kurnia</b></sub>](https://github.com/devikrn)<br />[🖥️](https://github.com/adislksn/FE-PPLK-2022/commits?author=devikrn "Code") 120140060  | [<img src="https://avatars.githubusercontent.com/u/75107950?s=64&v=4" width="100px;"/><br /><sub><b>Adi S</b></sub>](https://github.com/hanif354-bayte)<br />[🖥️](https://github.com/adislksn/FE-PPLK-2022/commits?author=hanif354-bayte "Code") 120140120  |
|--|--|--|--|--|--|

- Beta Ver. 0.1.2