import pygame
import sys
from random import randint
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLOR = (30, 120, 90)
BUTTERSCOTCH = (193, 106, 2)
SOFTBLUE = (160, 180, 255)
PURPLE = (104, 48, 80)
DARKBLUE  = (60,46,66)
OFFWHITE = (239,233,232)

topladder = 'topladder.png'
botladder = 'botladder.png'
dirt = 'dirt.png'
bolder = 'bolder.png'
support = 'support.png'
miner = 'miner.png'
tunnel = 'tunnel.png'
backgroundimg = 'background.png'
new_level = True
level = 1
bolder_list = []
mpos = [0,0]
mposcheck = [0,0]
mposcheck2 = [0,0]
end_game = False
win = False

SZ = 41
X = [None, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440]
Y = [None, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560,] 

r1c1 = [pygame.Rect(X[1], Y[1], SZ, SZ), None]
r1c2 = [pygame.Rect(X[2], Y[1], SZ, SZ), None]
r1c3 = [pygame.Rect(X[3], Y[1], SZ, SZ), None]
r1c4 = [pygame.Rect(X[4], Y[1], SZ, SZ), None]
r1c5 = [pygame.Rect(X[5], Y[1], SZ, SZ), None]
r1c6 = [pygame.Rect(X[6], Y[1], SZ, SZ), None]
r1c7 = [pygame.Rect(X[7], Y[1], SZ, SZ), None]
r1c8 = [pygame.Rect(X[8], Y[1], SZ, SZ), None]
r1c9 = [pygame.Rect(X[9], Y[1], SZ, SZ), None]
r1c10 = [pygame.Rect(X[10], Y[1], SZ, SZ), None]
r1c11 = [pygame.Rect(X[11], Y[1], SZ, SZ), None]
r2c1 = [pygame.Rect(X[1], Y[2], SZ, SZ), None]
r2c2 = [pygame.Rect(X[2], Y[2], SZ, SZ), None]
r2c3 = [pygame.Rect(X[3], Y[2], SZ, SZ), None]
r2c4 = [pygame.Rect(X[4], Y[2], SZ, SZ), None]
r2c5 = [pygame.Rect(X[5], Y[2], SZ, SZ), None]
r2c6 = [pygame.Rect(X[6], Y[2], SZ, SZ), None]
r2c7 = [pygame.Rect(X[7], Y[2], SZ, SZ), None]
r2c8 = [pygame.Rect(X[8], Y[2], SZ, SZ), None]
r2c9 = [pygame.Rect(X[9], Y[2], SZ, SZ), None]
r2c10 = [pygame.Rect(X[10], Y[2], SZ, SZ), None]
r2c11 = [pygame.Rect(X[11], Y[2], SZ, SZ), None]
r3c1 = [pygame.Rect(X[1], Y[3], SZ, SZ), None]
r3c2 = [pygame.Rect(X[2], Y[3], SZ, SZ), None]
r3c3 = [pygame.Rect(X[3], Y[3], SZ, SZ), None]
r3c4 = [pygame.Rect(X[4], Y[3], SZ, SZ), None]
r3c5 = [pygame.Rect(X[5], Y[3], SZ, SZ), None]
r3c6 = [pygame.Rect(X[6], Y[3], SZ, SZ), None]
r3c7 = [pygame.Rect(X[7], Y[3], SZ, SZ), None]
r3c8 = [pygame.Rect(X[8], Y[3], SZ, SZ), None]
r3c9 = [pygame.Rect(X[9], Y[3], SZ, SZ), None]
r3c10 = [pygame.Rect(X[10], Y[3], SZ, SZ), None]
r3c11 = [pygame.Rect(X[11], Y[3], SZ, SZ), None]
r4c1 = [pygame.Rect(X[1], Y[4], SZ, SZ), None]
r4c2 = [pygame.Rect(X[2], Y[4], SZ, SZ), None]
r4c3 = [pygame.Rect(X[3], Y[4], SZ, SZ), None]
r4c4 = [pygame.Rect(X[4], Y[4], SZ, SZ), None]
r4c5 = [pygame.Rect(X[5], Y[4], SZ, SZ), None]
r4c6 = [pygame.Rect(X[6], Y[4], SZ, SZ), None]
r4c7 = [pygame.Rect(X[7], Y[4], SZ, SZ), None]
r4c8 = [pygame.Rect(X[8], Y[4], SZ, SZ), None]
r4c9 = [pygame.Rect(X[9], Y[4], SZ, SZ), None]
r4c10 = [pygame.Rect(X[10], Y[4], SZ, SZ), None]
r4c11 = [pygame.Rect(X[11], Y[4], SZ, SZ), None]
r5c1 = [pygame.Rect(X[1], Y[5], SZ, SZ), None]
r5c2 = [pygame.Rect(X[2], Y[5], SZ, SZ), None]
r5c3 = [pygame.Rect(X[3], Y[5], SZ, SZ), None]
r5c4 = [pygame.Rect(X[4], Y[5], SZ, SZ), None]
r5c5 = [pygame.Rect(X[5], Y[5], SZ, SZ), None]
r5c6 = [pygame.Rect(X[6], Y[5], SZ, SZ), None]
r5c7 = [pygame.Rect(X[7], Y[5], SZ, SZ), None]
r5c8 = [pygame.Rect(X[8], Y[5], SZ, SZ), None]
r5c9 = [pygame.Rect(X[9], Y[5], SZ, SZ), None]
r5c10 = [pygame.Rect(X[10], Y[5], SZ, SZ), None]
r5c11 = [pygame.Rect(X[11], Y[5], SZ, SZ), None]
r6c1 = [pygame.Rect(X[1], Y[6], SZ, SZ), None]
r6c2 = [pygame.Rect(X[2], Y[6], SZ, SZ), None]
r6c3 = [pygame.Rect(X[3], Y[6], SZ, SZ), None]
r6c4 = [pygame.Rect(X[4], Y[6], SZ, SZ), None]
r6c5 = [pygame.Rect(X[5], Y[6], SZ, SZ), None]
r6c6 = [pygame.Rect(X[6], Y[6], SZ, SZ), None]
r6c7 = [pygame.Rect(X[7], Y[6], SZ, SZ), None]
r6c8 = [pygame.Rect(X[8], Y[6], SZ, SZ), None]
r6c9 = [pygame.Rect(X[9], Y[6], SZ, SZ), None]
r6c10 = [pygame.Rect(X[10], Y[6], SZ, SZ), None]
r6c11 = [pygame.Rect(X[11], Y[6], SZ, SZ), None]
r7c1 = [pygame.Rect(X[1], Y[7], SZ, SZ), None]
r7c2 = [pygame.Rect(X[2], Y[7], SZ, SZ), None]
r7c3 = [pygame.Rect(X[3], Y[7], SZ, SZ), None]
r7c4 = [pygame.Rect(X[4], Y[7], SZ, SZ), None]
r7c5 = [pygame.Rect(X[5], Y[7], SZ, SZ), None]
r7c6 = [pygame.Rect(X[6], Y[7], SZ, SZ), None]
r7c7 = [pygame.Rect(X[7], Y[7], SZ, SZ), None]
r7c8 = [pygame.Rect(X[8], Y[7], SZ, SZ), None]
r7c9 = [pygame.Rect(X[9], Y[7], SZ, SZ), None]
r7c10 = [pygame.Rect(X[10], Y[7], SZ, SZ), None]
r7c11 = [pygame.Rect(X[11], Y[7], SZ, SZ), None]
r8c1 = [pygame.Rect(X[1], Y[8], SZ, SZ), None]
r8c2 = [pygame.Rect(X[2], Y[8], SZ, SZ), None]
r8c3 = [pygame.Rect(X[3], Y[8], SZ, SZ), None]
r8c4 = [pygame.Rect(X[4], Y[8], SZ, SZ), None]
r8c5 = [pygame.Rect(X[5], Y[8], SZ, SZ), None]
r8c6 = [pygame.Rect(X[6], Y[8], SZ, SZ), None]
r8c7 = [pygame.Rect(X[7], Y[8], SZ, SZ), None]
r8c8 = [pygame.Rect(X[8], Y[8], SZ, SZ), None]
r8c9 = [pygame.Rect(X[9], Y[8], SZ, SZ), None]
r8c10 = [pygame.Rect(X[10], Y[8], SZ, SZ), None]
r8c11 = [pygame.Rect(X[11], Y[8], SZ, SZ), None]
r9c1 = [pygame.Rect(X[1], Y[9], SZ, SZ), None]
r9c2 = [pygame.Rect(X[2], Y[9], SZ, SZ), None]
r9c3 = [pygame.Rect(X[3], Y[9], SZ, SZ), None]
r9c4 = [pygame.Rect(X[4], Y[9], SZ, SZ), None]
r9c5 = [pygame.Rect(X[5], Y[9], SZ, SZ), None]
r9c6 = [pygame.Rect(X[6], Y[9], SZ, SZ), None]
r9c7 = [pygame.Rect(X[7], Y[9], SZ, SZ), None]
r9c8 = [pygame.Rect(X[8], Y[9], SZ, SZ), None]
r9c9 = [pygame.Rect(X[9], Y[9], SZ, SZ), None]
r9c10 = [pygame.Rect(X[10], Y[9], SZ, SZ), None]
r9c11 = [pygame.Rect(X[11], Y[9], SZ, SZ), None]
r10c1 = [pygame.Rect(X[1], Y[10], SZ, SZ), None]
r10c2 = [pygame.Rect(X[2], Y[10], SZ, SZ), None]
r10c3 = [pygame.Rect(X[3], Y[10], SZ, SZ), None]
r10c4 = [pygame.Rect(X[4], Y[10], SZ, SZ), None]
r10c5 = [pygame.Rect(X[5], Y[10], SZ, SZ), None]
r10c6 = [pygame.Rect(X[6], Y[10], SZ, SZ), None]
r10c7 = [pygame.Rect(X[7], Y[10], SZ, SZ), None]
r10c8 = [pygame.Rect(X[8], Y[10], SZ, SZ), None]
r10c9 = [pygame.Rect(X[9], Y[10], SZ, SZ), None]
r10c10 = [pygame.Rect(X[10], Y[10], SZ, SZ), None]
r10c11 = [pygame.Rect(X[11], Y[10], SZ, SZ), None]
r11c1 = [pygame.Rect(X[1], Y[11], SZ, SZ), None]
r11c2 = [pygame.Rect(X[2], Y[11], SZ, SZ), None]
r11c3 = [pygame.Rect(X[3], Y[11], SZ, SZ), None]
r11c4 = [pygame.Rect(X[4], Y[11], SZ, SZ), None]
r11c5 = [pygame.Rect(X[5], Y[11], SZ, SZ), None]
r11c6 = [pygame.Rect(X[6], Y[11], SZ, SZ), None]
r11c7 = [pygame.Rect(X[7], Y[11], SZ, SZ), None]
r11c8 = [pygame.Rect(X[8], Y[11], SZ, SZ), None]
r11c9 = [pygame.Rect(X[9], Y[11], SZ, SZ), None]
r11c10 = [pygame.Rect(X[10], Y[11], SZ, SZ), None]
r11c11 = [pygame.Rect(X[11], Y[11], SZ, SZ), None]
r12c1 = [pygame.Rect(X[1], Y[12], SZ, SZ), None]
r12c2 = [pygame.Rect(X[2], Y[12], SZ, SZ), None]
r12c3 = [pygame.Rect(X[3], Y[12], SZ, SZ), None]
r12c4 = [pygame.Rect(X[4], Y[12], SZ, SZ), None]
r12c5 = [pygame.Rect(X[5], Y[12], SZ, SZ), None]
r12c6 = [pygame.Rect(X[6], Y[12], SZ, SZ), None]
r12c7 = [pygame.Rect(X[7], Y[12], SZ, SZ), None]
r12c8 = [pygame.Rect(X[8], Y[12], SZ, SZ), None]
r12c9 = [pygame.Rect(X[9], Y[12], SZ, SZ), None]
r12c10 = [pygame.Rect(X[10], Y[12], SZ, SZ), None]
r12c11 = [pygame.Rect(X[11], Y[12], SZ, SZ), None]
r13c1 = [pygame.Rect(X[1], Y[13], SZ, SZ), None]
r13c2 = [pygame.Rect(X[2], Y[13], SZ, SZ), None]
r13c3 = [pygame.Rect(X[3], Y[13], SZ, SZ), None]
r13c4 = [pygame.Rect(X[4], Y[13], SZ, SZ), None]
r13c5 = [pygame.Rect(X[5], Y[13], SZ, SZ), None]
r13c6 = [pygame.Rect(X[6], Y[13], SZ, SZ), None]
r13c7 = [pygame.Rect(X[7], Y[13], SZ, SZ), None]
r13c8 = [pygame.Rect(X[8], Y[13], SZ, SZ), None]
r13c9 = [pygame.Rect(X[9], Y[13], SZ, SZ), None]
r13c10 = [pygame.Rect(X[10], Y[13], SZ, SZ), None]
r13c11 = [pygame.Rect(X[11], Y[13], SZ, SZ), None]
r14c1 = [pygame.Rect(X[1], Y[14], SZ, SZ), None]
r14c2 = [pygame.Rect(X[2], Y[14], SZ, SZ), None]
r14c3 = [pygame.Rect(X[3], Y[14], SZ, SZ), None]
r14c4 = [pygame.Rect(X[4], Y[14], SZ, SZ), None]
r14c5 = [pygame.Rect(X[5], Y[14], SZ, SZ), None]
r14c6 = [pygame.Rect(X[6], Y[14], SZ, SZ), None]
r14c7 = [pygame.Rect(X[7], Y[14], SZ, SZ), None]
r14c8 = [pygame.Rect(X[8], Y[14], SZ, SZ), None]
r14c9 = [pygame.Rect(X[9], Y[14], SZ, SZ), None]
r14c10 = [pygame.Rect(X[10], Y[14], SZ, SZ), None]
r14c11 = [pygame.Rect(X[11], Y[14], SZ, SZ), None]



row1 = [r1c1[0],r1c2[0],r1c3[0],r1c4[0],r1c5[0],r1c6[0],r1c7[0],r1c8[0],r1c9[0],r1c10[0],r1c11[0]]
row2 = [r2c1[0],r2c2[0],r2c3[0],r2c4[0],r2c5[0],r2c6[0],r2c7[0],r2c8[0],r2c9[0],r2c10[0],r2c11[0]]
row3 = [r3c1[0],r3c2[0],r3c3[0],r3c4[0],r3c5[0],r3c6[0],r3c7[0],r3c8[0],r3c9[0],r3c10[0],r3c11[0]]
row4 = [r4c1[0],r4c2[0],r4c3[0],r4c4[0],r4c5[0],r4c6[0],r4c7[0],r4c8[0],r4c9[0],r4c10[0],r4c11[0]]
row5 = [r5c1[0],r5c2[0],r5c3[0],r5c4[0],r5c5[0],r5c6[0],r5c7[0],r5c8[0],r5c9[0],r5c10[0],r5c11[0]]
row6 = [r6c1[0],r6c2[0],r6c3[0],r6c4[0],r6c5[0],r6c6[0],r6c7[0],r6c8[0],r6c9[0],r6c10[0],r6c11[0]]
row7 = [r7c1[0],r7c2[0],r7c3[0],r7c4[0],r7c5[0],r7c6[0],r7c7[0],r7c8[0],r7c9[0],r7c10[0],r7c11[0]]
row8 = [r8c1[0],r8c2[0],r8c3[0],r8c4[0],r8c5[0],r8c6[0],r8c7[0],r8c8[0],r8c9[0],r8c10[0],r8c11[0]]
row9 = [r9c1[0],r9c2[0],r9c3[0],r9c4[0],r9c5[0],r9c6[0],r9c7[0],r9c8[0],r9c9[0],r9c10[0],r9c11[0]]
row10 = [r10c1[0],r10c2[0],r10c3[0],r10c4[0],r10c5[0],r10c6[0],r10c7[0],r10c8[0],r10c9[0],r10c10[0],r10c11[0]]
row11 = [r11c1[0],r11c2[0],r11c3[0],r11c4[0],r11c5[0],r11c6[0],r11c7[0],r11c8[0],r11c9[0],r11c10[0],r11c11[0]]
row12 = [r12c1[0],r12c2[0],r12c3[0],r12c4[0],r12c5[0],r12c6[0],r12c7[0],r12c8[0],r12c9[0],r12c10[0],r12c11[0]]
row13 = [r13c1[0],r13c2[0],r13c3[0],r13c4[0],r13c5[0],r13c6[0],r13c7[0],r13c8[0],r13c9[0],r13c10[0],r13c11[0]]
row14 = [r14c1[0],r14c2[0],r14c3[0],r14c4[0],r14c5[0],r14c6[0],r14c7[0],r14c8[0],r14c9[0],r14c10[0],r14c11[0]]

column1 = [r1c1,r2c1,r3c1,r4c1,r5c1,r6c1,r7c1,r8c1,r9c1,r10c1,r11c1,r12c1,r13c1,r14c1]
column2 = [r1c2,r2c2,r3c2,r4c2,r5c2,r6c2,r7c2,r8c2,r9c2,r10c2,r11c2,r12c2,r13c2,r14c2]
column3 = [r1c3,r2c3,r3c3,r4c3,r5c3,r6c3,r7c3,r8c3,r9c3,r10c3,r11c3,r12c3,r13c3,r14c3]
column4 = [r1c4,r2c4,r3c4,r4c4,r5c4,r6c4,r7c4,r8c4,r9c4,r10c4,r11c4,r12c4,r13c4,r14c4]
column5 = [r1c5,r2c5,r3c5,r4c5,r5c5,r6c5,r7c5,r8c5,r9c5,r10c5,r11c5,r12c5,r13c5,r14c5]
column6 = [r1c6,r2c6,r3c6,r4c6,r5c6,r6c6,r7c6,r8c6,r9c6,r10c6,r11c6,r12c6,r13c6,r14c6]
column7 = [r1c7,r2c7,r3c7,r4c7,r5c7,r6c7,r7c7,r8c7,r9c7,r10c7,r11c7,r12c7,r13c7,r14c7]
column8 = [r1c8,r2c8,r3c8,r4c8,r5c8,r6c8,r7c8,r8c8,r9c8,r10c8,r11c8,r12c8,r13c8,r14c8]
column9 = [r1c9,r2c9,r3c9,r4c9,r5c9,r6c9,r7c9,r8c9,r9c9,r10c9,r11c9,r12c9,r13c9,r14c9]
column10 = [r1c10,r2c10,r3c10,r4c10,r5c10,r6c10,r7c10,r8c10,r9c10,r10c10,r11c10,r12c10,r13c10,r14c10]
column11 = [r1c11,r2c11,r3c11,r4c11,r5c11,r6c11,r7c11,r8c11,r9c11,r10c11,r11c11,r12c11,r13c11,r14c11]

pygame.init()


screen = pygame.display.set_mode((720, 640)) # creates screen to be used
pygame.display.set_caption('Dig Deeper') 
font = pygame.font.Font(None, 24)
background = pygame.Surface(screen.get_size())
#background = background.convert()
#background.fill(SOFTBLUE)
screen.blit(background, (0,0))
#dirt_layer = pygame.Surface(450, 410)
#dirt_layer =  dirt_layer.convert()
#dirt_rect = pygame.Rect(0, 200, 400, 440)
bolder_img = pygame.image.load(bolder)
dirtimg = pygame.image.load(dirt)
top_ladder_img = pygame.image.load(topladder)
bot_ladder_img = pygame.image.load(botladder)
support_img = pygame.image.load(support)
tunnel_img = pygame.image.load(tunnel)
miner_img = pygame.image.load(miner)
rminer_img = pygame.image.load('rminer.png')
background_img = pygame.image.load(backgroundimg)
screen.blit(background_img, (0,0))
dead_img = pygame.image.load('dead.png')
lost_img = pygame.image.load('lost.png')
win_img = pygame.image.load('win.png')

def DrawDirtInitial(): #called each level once

    for rect in row1:
        screen.blit(dirtimg, rect)
    for rect in row2:
        screen.blit(dirtimg, rect)
    for rect in row3:
        screen.blit(dirtimg, rect)
    for rect in row4:
        screen.blit(dirtimg, rect)
    for rect in row5:
        screen.blit(dirtimg, rect)
    for rect in row6:
        screen.blit(dirtimg, rect)
    for rect in row7:
        screen.blit(dirtimg, rect)
    for rect in row8:
        screen.blit(dirtimg, rect)
    for rect in row9:
        screen.blit(dirtimg, rect)
    for rect in row10:
        screen.blit(dirtimg, rect)
    for rect in row11:
        screen.blit(dirtimg, rect)
    for rect in row12:
        screen.blit(dirtimg, rect)
    for rect in row13:
        screen.blit(dirtimg, rect)
    for rect in row14:
        screen.blit(dirtimg, rect)
    
    #dirtimg = pygame.image.load(dirt)
    #imagerect = rect
    #dirt_image = pygame.transform.scale(dirt_image, (450,410))
    #dirt_layer.blit(dirt_image, dirt_rect)
font = pygame.font.Font(None, 36)
textrect = pygame.Rect(500,360,110,35)
def DrawLevelNumber():
    text = font.render('Level: ' + str(level), 1, OFFWHITE)
    text_loc = (textrect[0]+5,textrect[1]+5)
    pygame.draw.rect(screen, DARKBLUE, textrect)
    screen.blit(text, text_loc)
    
    
def DrawRects():
    for rect in row1:
        pygame.draw.rect(screen, PURPLE, rect, 1)
    for rect in row2:
        pygame.draw.rect(screen, PURPLE, rect, 1)
    for rect in row3:
        pygame.draw.rect(screen, PURPLE, rect, 1)
    for rect in row4:
        pygame.draw.rect(screen, PURPLE, rect, 1)
    for rect in row5:
        pygame.draw.rect(screen, PURPLE, rect, 1)
    for rect in row6:
        pygame.draw.rect(screen, PURPLE, rect, 1)
    for rect in row7:
        pygame.draw.rect(screen, PURPLE, rect, 1)
    for rect in row8:
        pygame.draw.rect(screen, PURPLE, rect, 1)
    for rect in row9:
        pygame.draw.rect(screen, PURPLE, rect, 1)
    for rect in row10:
        pygame.draw.rect(screen, PURPLE, rect, 1)
    for rect in row11:
        pygame.draw.rect(screen, PURPLE, rect, 1)
    for rect in row12:
        pygame.draw.rect(screen, PURPLE, rect, 1)
    for rect in row13:
        pygame.draw.rect(screen, PURPLE, rect, 1)
    for rect in row14:
        pygame.draw.rect(screen, PURPLE, rect, 1)

column_list = [column1, column2, column3, column4, column5, column6, column7, column8, column9, column10, column11]

def GenerateBolders():
    bolder_count = (level * 2) + 4
    iii = 0
    while iii < bolder_count:
        col = randint(0, 10)
        row = randint(2, 11)
        test = CheckProximity(col, row)
        #print(test)
        if test == 'pass':
            screen.blit(bolder_img, column_list[col][row][0])
            column_list[col][row][1] = 'bolder'
            iii += 1
            bold = (col, row)
            bolder_list.append(bold)
            #print (column_list[col][row][0])
            #print (bolder_list)

def ResetBolders():
    for bolder in bolder_list:
        #print (column_list[bolder[0]][bolder[1]][1])
        column_list[bolder[0]][bolder[1]][1] = None

mtype = column_list[mpos[0]][mpos[1]][1]
facing = 'r'
def MoveMiner(action, pos):
    global mpos, mposcheck, mposcheck2, facing
    if action == 'left':
        if pos[0] == 0:
            return None
        elif column_list[pos[0]-1][pos[1]][1] == 'support' or column_list[pos[0]-1][pos[1]][1] == 'bolder':
            return None
        else:
            DrawType(pos)
            mpos = [pos[0]-1,pos[1]]
            mposcheck = [pos[0]-1,pos[1]]
            mposcheck2 = [pos[0]-1,pos[1]]
            if column_list[mpos[0]][mpos[1]][1] == None:
                column_list[mpos[0]][mpos[1]][1] = 'tunnel'
            DrawType(mpos)
            CheckBolderFall(mposcheck2)
            facing = 'l'
            #print(mpos)
    if action == 'right':
        if pos[0] == 10:
            return None
        elif column_list[pos[0]+1][pos[1]][1] == 'support' or column_list[pos[0]+1][pos[1]][1] == 'bolder':
            return None
        else:
            DrawType(pos)
            mpos = [pos[0]+1,pos[1]]
            mposcheck = [pos[0]+1,pos[1]]
            mposcheck2 = [pos[0]+1,pos[1]]
            if column_list[mpos[0]][mpos[1]][1] == None:
                column_list[mpos[0]][mpos[1]][1] = 'tunnel'
            DrawType(mpos)
            CheckBolderFall(mposcheck2)
            facing = 'r'
            #print (mpos)
    if action == 'up':
        if column_list[pos[0]][pos[1]][1] == 'botladder':
            DrawType(pos)
            mpos = [pos[0], pos[1]-1]
            mposcheck = [pos[0], pos[1]-1]
            mposcheck2 = [pos[0],pos[1]-1]
            DrawType(mpos)
            CheckBolderFall(mposcheck2)
        else:
            pass
    if action == 'down':
        if column_list[pos[0]][pos[1]][1] == 'topladder':
            DrawType(pos)
            mpos = [pos[0], pos[1]+1]
            mposcheck = [pos[0], pos[1]+1]
            mposcheck2 = [pos[0],pos[1]+1]
            DrawType(mpos)
            CheckBolderFall(mposcheck2)
        else:
            pass
    if action == 'left support':
        if column_list[pos[0]-1][pos[1]][1] == None:
            column_list[pos[0]-1][pos[1]][1] = 'support'
            DrawType((pos[0]-1,pos[1]))
            #print(column_list[pos[0]-1][pos[1]][1])
        else:
            pass
    if action == 'right support':
        if column_list[pos[0]+1][pos[1]][1] == None:
            column_list[pos[0]+1][pos[1]][1] = 'support'
            DrawType((pos[0]+1,pos[1]))
        else:
            pass
    if action == 'ladder':
        if column_list[pos[0]][pos[1]][1] == 'tunnel' and column_list[pos[0]][pos[1]+1][1] != 'bolder' and column_list[pos[0]][pos[1]+1][1] != 'support':
                column_list[pos[0]][pos[1]][1] = 'topladder'
                DrawType(mpos)
                DrawMiner()
                column_list[pos[0]][pos[1]+1][1] = 'botladder'
                x = pos[0]
                y = pos[1]+1
                pas = (x,y)
                DrawType(pas)
                CheckLadder(mposcheck)
        else:
            return None

def DrawType(pos):
    type = column_list[pos[0]][pos[1]][1]
    if type == 'topladder':
        screen.blit(top_ladder_img,  column_list[pos[0]][pos[1]][0])
    if type == 'botladder':
        screen.blit(bot_ladder_img, column_list[pos[0]][pos[1]][0])
    if type == 'support':
        screen.blit(support_img,  column_list[pos[0]][pos[1]][0])
    if type == 'tunnel':
        screen.blit(tunnel_img, column_list[pos[0]][pos[1]][0])
    
def ScreenDead():
    for rect in row1:
        screen.blit(dead_img, rect)
        pygame.display.flip()
    for rect in row2:
        screen.blit(dead_img, rect)
        pygame.display.flip()
    for rect in row3:
        screen.blit(dead_img, rect)
        pygame.display.flip()
    for rect in row4:
        screen.blit(dead_img, rect)
        pygame.display.flip()
    for rect in row5:
        screen.blit(dead_img, rect)
        pygame.display.flip()
    for rect in row6:
        screen.blit(dead_img, rect)
        pygame.display.flip()
    for rect in row7:
        screen.blit(dead_img, rect)
        pygame.display.flip()
    for rect in row8:
        screen.blit(dead_img, rect)
        pygame.display.flip()
    for rect in row9:
        screen.blit(dead_img, rect)
        pygame.display.flip()
    for rect in row10:
        screen.blit(dead_img, rect)
        pygame.display.flip()
    for rect in row11:
        screen.blit(dead_img, rect)
        pygame.display.flip()
    for rect in row12:
        screen.blit(dead_img, rect)
        pygame.display.flip()
    for rect in row13:
        screen.blit(dead_img, rect)
        pygame.display.flip()
    for rect in row14:
        screen.blit(dead_img, rect)
        pygame.display.flip()
    
    
def EndGame():
    global end_game, win
    end_game = True
    if win == True:
        WinScreen()
    if win == False:
        ScreenDead()
##    pygame.display.flip()

def WinScreen():
    screen.blit(win_img, (0,0))
    pygame.display.flip()

def CheckLadder(pos):
    
    global mposcheck
    iii = 0
    z = pos
    x = pos
    while iii < 3:
        if x[1]-1 < 0:
            iii = 3
            return None
        else:
            check = column_list[x[0]][x[1]-1][1]
        if check == 'support':
            #print ('support')
            iii = 3
            return None
        elif check == 'tunnel' or check == None:
            #print ('tunnel')            
            iii += 1
            x[1] -= 1
        elif check == 'bolder' or 'topladder' or 'botladder':
            #print ('bolder')
            iii = 3           
            EndGame()
    iii = 0
    '''while iii < 3:
        if y[1]+1 > 13 or y[1]+2 > 13:
            iii = 3
            return None
        else:
            check = column_list[y[0]][y[1]+2][1]
        if check == 'support':
            print('support')
            iii = 3
            return None
        elif check == 'tunnel' or check == None:
            print('tunnel')
            iii += 1
            y[1] += 1
        elif check == 'topladder':
            print('ladder')
            print(iii)
            EndGame()'''
    '''rcmin1 = rc[col][row-1][1]
        rcmin2 = rc[col][row-2][1]
        rcpls1 = rc[col][row+1][1]
        rcpls2 = rc[col][row+2][1]'''
        

def DrawMiner():
    global facing
    if facing == 'r':
        screen.blit(rminer_img, column_list[mpos[0]][mpos[1]][0])
    elif facing == 'l':
        screen.blit(miner_img, column_list[mpos[0]][mpos[1]][0])

def DrawBotLadder():
    screen.blit(bot_ladder_img, r1c1[0])
    r1c1[1] = 'ladder'

def CheckProximity(col, row):
        rc = column_list
        cc = column_list
        rcmin1 = rc[col][row-1][1]
        rcmin2 = rc[col][row-2][1]
        rcpls1 = rc[col][row+1][1]
        rcpls2 = rc[col][row+2][1]
        if col == 10:
            ccpls1 = None
            ccdiag2 = None
            ccdiag4 = None
        else:
            ccpls1 = cc[col+1][row][1]
            ccdiag2 = cc[col+1][row+1][1]
            ccdiag4 = cc[col+1][row-1][1]
        if col == 9 or 10:
            ccpls2 = None
        else:
            ccpls2 = cc[col+2][row][1]
        if col == 0:
            ccmin1 = None
            ccdiag1 = None
            ccdiag3 = None
        else:
            ccmin1 = cc[col-1][row][1]
            ccdiag1 = cc[col-1][row+1][1]
            ccdiag3 = cc[col-1][row-1][1]
        if col == 0 or col == 1:
            ccmin2 = None
        else:
            ccmin2 = cc[col-2][row][1]
        
        if rc[col][row][1] == 'bolder':
            return 'fail'
        if rcmin1 == 'bolder':
            return 'fail'
        if rcmin2 == 'bolder':
            return 'fail'
        if rcpls1 == 'bolder':
            return 'fail'
        if rcpls2 == 'bolder':
            return 'fail'
        if ccmin1 == 'bolder':
            return 'fail'
        if ccmin2 == 'bolder':
            return 'fail'
        if ccpls1 == 'bolder':
            return 'fail'
        if ccpls2 == 'bolder':
            return 'fail'
        if ccdiag1 == 'bolder':
            return 'fail'
        if ccdiag2 == 'bolder':
            return 'fail'
        if ccdiag3 == 'bolder':
            return 'fail'
        if ccdiag4 == 'bolder':
            return 'fail'
        else:
            return 'pass'
        
def NextLevel(res = False):
    global level, new_level, mpos, end_game, win
    screen.blit(background_img, (0,0))
    if res == 'reset':
        level = 1
        win = False
    else:
        level += 1
    new_level = True
    ResetAll()
    mpos = (0,0)
    end_game = False
    
def CheckBolderFall(pos):
    pass
    global mpos, mposcheck2
    iii = 0
    x = pos
    while iii < 3:
        if x[1]-1 < 0:
            iii = 3
            return None
        else:
            check = column_list[x[0]][x[1]-1][1]

        if check == 'support':
            print ('support')
            iii = 3
            return None
        elif check == 'bolder':
            print ('bolder')
            iii = 3           
            EndGame()
        else:
            print ('none')            
            iii += 1
            x[1] -= 1
    
    
def ResetAll():
    for rect in column1:
        rect[1] = None
    for rect in column2:
        rect[1] = None
    for rect in column3:
        rect[1] = None
    for rect in column4:
        rect[1] = None
    for rect in column5:
        rect[1] = None
    for rect in column6:
        rect[1] = None
    for rect in column7:
        rect[1] = None
    for rect in column8:
        rect[1] = None
    for rect in column9:
        rect[1] = None
    for rect in column10:
        rect[1] = None
    for rect in column11:
        rect[1] = None
    r1c1[1] = 'botladder'

while True:
    #print('running loop')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if end_game == True:
                NextLevel('reset')
            else:
                NextLevel()
        if event.type == pygame.KEYDOWN:
            if end_game != True:
                if event.key == K_LEFT:
                    MoveMiner('left', mpos)
                if event.key == K_RIGHT:
                    MoveMiner('right', mpos)
                if event.key == K_UP:
                    MoveMiner('up', mpos)
                if event.key == K_DOWN:
                    MoveMiner('down', mpos)
                if event.key == K_z:
                    MoveMiner('left support', mpos)
                if event.key == K_x:
                    MoveMiner('ladder', mpos)
                if event.key == K_c:
                    MoveMiner('right support', mpos)
    if new_level == True:
        bolder_list = []
        DrawDirtInitial()
        pygame.display.flip()
        new_level = False
        GenerateBolders()
        DrawBotLadder()
        #print (str(new_level))
        #print (mpos)
    if end_game != True:
        DrawBotLadder()
        DrawMiner()    
        DrawRects()
        DrawMiner()
        DrawLevelNumber()
        pygame.display.flip()
    if mpos[1] == 13:
        if level == 6:
            win = True
            EndGame()
        else:
            NextLevel()
    if level == 7:
        win = True
        EndGame()
            