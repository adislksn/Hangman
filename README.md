# Hangman 
[![PyPI version](https://badge.fury.io/py/pygame.svg)](https://badge.fury.io/py/pygame)

[![Click to open youtube video](Thumbnail.gif)](https://youtu.be/9u2yUmBjJmc)

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
|        NAMA         |     NIM    |
| ------------------- | ---------- |
| Pandu Firmanto      | 120140020  |
| Nashirotul Maftuha  | 120140031  |
| Adi Sulaksono       | 120140038  |
| Lidia Alvionisya    | 120140042  |
| Devi Kurnia         | 120140060  |
| Hanif Putra Agusta  | 120140120  |

- Beta Ver. 0.1.2