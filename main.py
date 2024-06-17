#NOME DOS PARTICIPANTES --> LUIS THAYLOR/EMANOEL ROSA



import pygame
import random
import os
from tkinter import simpledialog

tamanho = (800, 600)
clock = pygame.time.Clock()
tela=pygame.display.set_mode(tamanho)
pygame.display.set_caption('Game Titulo')


branco = (255,255,255)
preto = (0,0,0)
vermelho=(255,0,0)



posiçãoXBolinha= 0
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()





    tela.fill(branco)

    pygame.draw.line(tela,preto,(80,95), (200,400) , 3)
    pygame.draw.circle(tela,preto,(70,70),30,3)
    pygame.draw.circle(tela,preto,(205,430),30,3)

    #pygame.draw.rect(tela,preto,(20,50,50,100),2)



    
    pygame.display.update()
    clock.tick(60)



