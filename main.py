#NOME DOS PARTICIPANTES --> LUIS THAYLOR/EMANOEL ROSA

import pygame
from tkinter import simpledialog, messagebox
import math

pygame.init()

tamanho = (800,600)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("SpaceMaker")
fundo = pygame.image.load("assets/fundo.jpg")
icone = pygame.image.load("assets/space.png")
fonte = pygame.font.SysFont("Arial", 18)
som = pygame.mixer.Sound("assets/somgame.mp3")
som.play(-1)
estrelas = {}
raio = 5
branco = (225,225,225)
preto = (0,0,0)


def salvarMarcacoes():
     with open("Estralas Marcadas.txt", "w") as arquivo:
          for nome, posicao in estrelas.items():
               arquivo.write(f"{posicao[0]},{posicao[1]},{nome}\n")

def carregarMarcacoes():
     estrelas.clear()
     try:
          with open("Estrelas Marcadas.txt", "r") as arquivo:
               for linha in arquivo:
                    try:
                         x, y, nome = linha.strip().split(",")
                         posicao = (int(x), int(y))
                         estrelas[nome] = posicao
                    except ValueError:
                         continue
     except FileNotFoundError:
          messagebox.showinfo("Erro", "Arquivo não encontrado.")          


def excluirMarcacoes():
     estrelas.clear()


while True:
     for evento in pygame.event.get():
          if evento.type == pygame.QUIT:
               quit()
               salvarMarcacoes()
          elif evento.type == pygame.KEYDOWN:
               if evento.key ==pygame.K_ESCAPE:
                    pygame.quit()
                    salvarMarcacoes()
               elif evento.key == pygame.K_F10:
                    salvarMarcacoes()
               elif evento.key == pygame.K_F11:
                    carregarMarcacoes()
               elif evento.key == pygame.K_F12:
                    excluirMarcacoes()
          elif evento.type == pygame.MOUSEBUTTONUP:
               pos = pygame.mouse.get_pos()
               item = simpledialog.askstring("Space", "Nome da Estrela: ")
               print(item)
               if item == None:
                    item = "desconhecido"+str(pos)
               estrelas[item] = pos

     tela.fill(branco)
     tela.blit(fundo,(0,0))

     for item, posicoes in estrelas.items():
        pygame.draw.circle(tela, branco, posicoes, raio)
        fonte = pygame.font.Font(None, 20)
        texto = fonte.render(item, True, (255, 255, 255))
        tela.blit(texto, (posicoes[0] + 10, posicoes[1] + 10))

#EMANOEL





     textoOpcoes = fonte.render("Opções:", True, branco)
     textoSalvar = fonte.render("F10 - Salvar marcações", True, branco)
     textoCarregar = fonte.render("F11 - Carregar ultimas marcações", True, branco)
     textoExcluir = fonte.render("F12 - Excluir todas as marcações", True, branco)
     tela.blit(textoOpcoes, (10, 10))
     tela.blit(textoSalvar, (10, 40))
     tela.blit(textoCarregar, (10, 70))
     tela.blit(textoExcluir, (10, 100))

     pygame.display.update()
     clock.tick(60)

pygame.quit()