from pygame import *
import pygame 
import math
import random as rand

#display & music settings
pygame.init()
logo = pygame.image.load("assets/hangman6.png")
pygame.display.set_icon(logo)
music = pygame.mixer.music.load("assets/AWM.mp3")
pygame.mixer.music.play(-1)
click = pygame.mixer.Sound("assets/click.wav")
width = 800
height = 500
display = pygame.display.set_mode((width, height))
background = (255,255,255)
base_font = pygame.font.SysFont("comicsans",32)
clock = pygame.time.Clock()
pygame.display.set_caption("Hangman")

#button
radius = 20
gap = 15
alphabet = []
startx = 550
starty = 50
for i in range(26):
    if i<24:
        x = startx + gap * 2 + ((radius * 2 + gap) * (i % 4))#590, 592,2, 594,4, 596,6, 598,8, 601
        y = starty + ((i // 4) * (gap + radius * 2))# 50, 50, 50, 50, 120, 120, 120, 120, 190, 190, 190, 190
    else:
        x = startx + gap * 2 + ((radius * 2 + gap) * ((i+1) % 4))
        y = starty + (((i+1) // 4) * (gap + radius * 2))
    alphabet.append([x, y, chr(65 + i), True])

#images
images=[]
DEFAULT_IMAGE_SIZE = (250,253)
for i in range(7):
    image = pygame.image.load(f"assets/hangman{str(i)}.png")
    image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
    images.append(image)

#assets
list_text=(['CHICKEN','CAT','BEAR','BIRD','TIGER','RABBIT','ZEBRA'],['APPLE','BANANA','POTATO','MEAT','ORANGE','CHOCOLATE','CAKE'],['YOUTUBER','PROGRAMMER','POLICE','DOCTOR','PILOT','CHEF','DRIVER'])
stats = 0
answered=[]

#parent class
class Hangman:
    global quest #variabel quest bermasalah, blm fix
    quest = rand.choice(list_text[rand.randint(0,2)])
    def __init__(self,name):
        self.name = name

    def close():
        pygame.quit()

    def out_display(self,word):
        self.word = word
        pygame.time.delay(1000)
        display.fill(background)
        text = base_font.render(word, 1, (0,0,0))
        display.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000)
        Hangman.close()

    def show():
        display.fill(background)

        #draw title
        text = base_font.render("Hangman Game", 1, (0,0,0))
        display.blit(text, (width/2 - text.get_width()/2, 20))
        
        #draw words
        show_alphabet = ""
        for check in quest:
            if check in answered:
                show_alphabet += check + " "
            else:
                show_alphabet += "_ "
        text = base_font.render(show_alphabet, 1, (0,0,0))
        display.blit(text, (200, 400))

        #draw buttons
        for check in alphabet:
            x, y, txt, status = check
            if status:
                pygame.draw.circle(display, (0,0,0), (x, y), radius,3)
                text = base_font.render(txt, 1, (0,0,0))
                display.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
        
        #draw images    
        display.blit(images[stats], (150,100))
        pygame.display.update()

    #main program
    def main_p(self):
        global stats
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Hangman.close()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos_x, pos_y = pygame.mouse.get_pos()
                    click.play()
                    for check in alphabet:
                        x, y, txt, status = check
                        if status:
                            cek = math.sqrt((x - pos_x)**2 + (y - pos_y)**2)
                            if cek <= radius:
                                check[3] = False
                                answered.append(txt)
                                print(answered)
                                if txt not in quest:
                                    stats += 1
            Hangman.show()

            game = True
            for check in alphabet:
                if check not in answered:
                    game = False
                    break
            
            if game:
                Hangman.out_display(self,"You Won")
                break
            if stats == 6:
                Hangman.out_display(self,"You Lost")
                break

class Animal(Hangman):
    quest = rand.choice(list_text[0])
    def __init__(self,name):
        super().__init__(name)
    
    def out_display(self,word):
        super().out_display(word)
    
    def show():
        super().show()

    def main_p(self):
        super().main_p()

class Food(Hangman):
    quest = rand.choice(list_text[1])
    def __init__(self,name):
        super().__init__(name)

    def out_display(self,word):
        super().out_display(word)
    
    def show():
        super().show()

    def main_p(self):
        super().main_p()

class Jobs(Hangman):
    quest = rand.choice(list_text[2])
    def __init__(self,name):
        super().__init__(name)

    def out_display(self,word):
        super().out_display(word)
    
    def show():
        super().show()

    def main_p(self):
        super().main_p()
        
display.fill(background)
pygame.display.update()
play = "Player 1 "
player=Food(play)
player.main_p()

pygame.quit()
