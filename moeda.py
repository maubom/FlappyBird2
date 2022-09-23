import pygame
import os
import random

TELA_LARGURA = 800
TELA_ALTURA = 600
VEL_MAX = 60
VEL_MIN = 5
VEL_NORMAL = 5

IMAGEMS_MOEDA = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png')))
]
IMAGEM_ARVORE = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
IMAGEM_FUNDO = pygame.transform.scale(pygame.image.load(os.path.join('imgs', 'bg.png')),(TELA_LARGURA, TELA_ALTURA))
IMAGEM_TESOURO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png')))

pygame.font.init()
FONTE = pygame.font.SysFont('arial', 36)

class Jogador:
    IMGS = IMAGEMS_MOEDA
    VELOCIDADE = VEL_MIN

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.altura = self.x
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = self.IMGS[0]

    def move_up(self):
        self.y -= self.VELOCIDADE
        if self.y < 0:
            self.y = 0
    def move_down(self):
        self.y += self.VELOCIDADE
        if self.y > TELA_ALTURA - self.imagem.get_height():
            self.y = TELA_ALTURA - self.imagem.get_height()
    def move_left(self):
        self.x -= self.VELOCIDADE
        if self.x < 0:
            self.x = 0
    def move_right(self):
        self.x += self.VELOCIDADE
        if self.x > TELA_LARGURA - self.imagem.get_width():
            self.x = TELA_LARGURA - self.imagem.get_width()
    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)
    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, self.y))

class Arvore:
    VELOCIDADE = VEL_NORMAL
    LARGURA = IMAGEM_ARVORE.get_width()
    IMAGEM = IMAGEM_ARVORE

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.LARGURA

    def mover(self):
        self.x1 -= self.VELOCIDADE
        self.x2 -= self.VELOCIDADE

        if self.x1 + self.LARGURA < 0:
            self.x1 = self.x2 + self.LARGURA
        if self.x2 + self.LARGURA < 0:
            self.x2 = self.x1 + self.LARGURA

    def desenhar(self, tela):
        tela.blit(self.IMAGEM, (self.x1, self.y))
        tela.blit(self.IMAGEM, (self.x2, self.y))

def desenhar_tela(tela, arvore, jogadores,pontos):
    tela.blit(IMAGEM_FUNDO, (0, 0))
    arvore.desenhar(tela)
    for jogador in jogadores:
        jogador.desenhar(tela)
    texto = FONTE.render(f"Pontuação: {pontos}", 1, (255,255,255) )
    tela.blit(texto, (TELA_LARGURA - 10 - texto.get_width(), 10))

    pygame.display.update()

def main():
    jogadores = [Jogador(200, 200), Jogador(300, 300)]
    arvore = Arvore(500)
    tela = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
    pontos = 0
    relogio = pygame.time.Clock()

    rodando = True
    while rodando:
        relogio.tick(30)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()


        # Jogador 1
        if pygame.key.get_pressed()[pygame.K_w]:
            jogadores[0].move_up()
        if pygame.key.get_pressed()[pygame.K_s]:
            jogadores[0].move_down()
        if pygame.key.get_pressed()[pygame.K_a]:
            jogadores[0].move_left()
        if pygame.key.get_pressed()[pygame.K_d]:
            jogadores[0].move_right()
        if pygame.key.get_pressed()[pygame.K_e]:
            if jogadores[0].VELOCIDADE < VEL_MAX:
                jogadores[0].VELOCIDADE += 1
        if pygame.key.get_pressed()[pygame.K_q]:
            if jogadores[0].VELOCIDADE > VEL_MIN:
                jogadores[0].VELOCIDADE -= 1

        # Jogador 2
        if pygame.key.get_pressed()[pygame.K_UP]:
            jogadores[1].move_up()
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            jogadores[1].move_down()
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            jogadores[1].move_left()
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            jogadores[1].move_right()
        if pygame.key.get_pressed()[pygame.K_KP_PLUS]:
            if jogadores[1].VELOCIDADE < VEL_MAX:
                jogadores[1].VELOCIDADE += 1
        if pygame.key.get_pressed()[pygame.K_KP_MINUS]:
            if jogadores[1].VELOCIDADE > VEL_MIN:
                jogadores[1].VELOCIDADE -= 1

        arvore.mover()
        desenhar_tela(tela, arvore, jogadores, pontos)


if __name__ == '__main__':
    main()