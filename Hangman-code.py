from pygame import *
import pygame 
import math
import random as rand

#display settings
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
font_dasar = pygame.font.SysFont("comicsans",32)
clock = pygame.time.Clock()
pygame.display.set_caption("Hangman")

#tombol
radius = 20
gap = 15
alfabet = []
startx = 550
starty = 50
for i in range(26):
    if i<24:
        x = startx + gap * 2 + ((radius * 2 + gap) * (i % 4))#590, 592,2, 594,4, 596,6, 598,8, 601
        y = starty + ((i // 4) * (gap + radius * 2))# 50, 50, 50, 50, 120, 120, 120, 120, 190, 190, 190, 190
    else:
        x = startx + gap * 2 + ((radius * 2 + gap) * ((i+1) % 4))
        y = starty + (((i+1) // 4) * (gap + radius * 2))
    alfabet.append([x, y, chr(65 + i), True])

#gambar
images=[]
for i in range(7):
    image = pygame.image.load(f"assets/hangman{str(i)}.png")
    images.append(image)

#assets
list_text=(['AYAM','KUCING','BERUANG','BADAK','HARIMAU','KELINCI','KEPITING'],['APEL','PISANG','KENTANG','DAGING','JERUK','COKELAT','KUE'],['YOUTUBER','PROGRAMMER','POLISI','DOKTER','PILOT','CHEF','DRIVER'])
stats = 0
terjawab=[]

class Hangman:
    global quest
    quest = rand.choice(list_text[rand.randint(0,2)])
    def __init__(self,nama):
        self.nama = nama

    def close():
        pygame.quit()

    def tampilan_out(self,word):
        self.word = word
        pygame.time.delay(1000)
        display.fill(background)
        text = font_dasar.render(word, 1, (0,0,0))
        display.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
        pygame.display.update()
        pygame.time.delay(3000)
        Hangman.close()

    def show():
        display.fill(background)

        #draw title
        text = font_dasar.render("Hangman Game", 1, (0,0,0))
        display.blit(text, (width/2 - text.get_width()/2, 20))
        
        #draw words
        show_alfabet = ""
        for teks in quest:
            if teks in terjawab:
                show_alfabet += teks + " "
            else:
                show_alfabet += "_ "
        text = font_dasar.render(show_alfabet, 1, (0,0,0))
        display.blit(text, (200, 400))

        #draw buttons
        for teks in alfabet:
            x, y, txt, status = teks
            if status:
                pygame.draw.circle(display, (0,0,0), (x, y), radius,3)
                text = font_dasar.render(txt, 1, (0,0,0))
                display.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
        
        #draw images    
        display.blit(images[stats], (150,100))
        pygame.display.update()

    def utama(self):
        global stats
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Hangman.close()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos_x, pos_y = pygame.mouse.get_pos()
                    click.play()
                    for teks in alfabet:
                        x, y, txt, status = teks
                        if status:
                            cek = math.sqrt((x - pos_x)**2 + (y - pos_y)**2)
                            if cek <= radius:
                                teks[3] = False
                                terjawab.append(txt)
                                print(terjawab)
                                if txt not in quest:
                                    stats += 1
            Hangman.show()

            game = True
            for teks in alfabet:
                if teks not in terjawab:
                    game = False
                    break
            
            if game:
                Hangman.tampilan_out(self,"You Won")
                break
            if stats == 6:
                Hangman.tampilan_out(self,"You Lost")
                break

class Animal(Hangman):
    quest = rand.choice(list_text[1])
    def __init__(self,nama):
        super().__init__(nama)

    def tampilan_out(self,word):
        super().tampilan_out(word)
    
    def show():
        super().show()

    def utama(self):
        super().utama()

class Food(Hangman):
    quest = rand.choice(list_text[2])
    def __init__(self,nama):
        super().__init__(nama)

    def tampilan_out(self,word):
        super().tampilan_out(word)
    
    def show():
        super().show()

    def utama(self):
        super().utama()

class Jobs(Hangman):
    quest = rand.choice(list_text[0])
    def __init__(self,nama):
        super().__init__(nama)

    def tampilan_out(self,word):
        super().tampilan_out(word)
    
    def show():
        super().show()

    def utama(self):
        super().utama()
        
display.fill(background)
pygame.display.update()
play = "Player 1 "
player=Hangman(play)
player.utama()

pygame.quit()
