import pygame
import random

pygame.init()
tela = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

rect = pygame.Rect(0, 0, 15, 15)
rect.center = tela.get_rect().center
vel = 1

class Jogador:
   def __init__(self, x, y):
       self.x = x
       self.y = y
       self.raio = 6
       self.cor = (255, 255, 255)

class Bola:
   def __init__(self, x, y):
       self.x = x
       self.y = y
       self.raio = 5
       self.cor = (255, 255, 255)
def main():
    bolas = []
    jogadores = []
    conta = 0
    jogadores.append(Jogador(random.randint(7, tela.get_width()-7), random.randint(7, tela.get_height()-7)))
    for i in range(0, random.randint(30, 150)):
        bolas.append(Bola(random.randint(6, tela.get_width()-6), random.randint(6, tela.get_height()-6)))
        bolas[i].cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    populacao = len(bolas)
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                print(pygame.key.name(event.key))

        x = pygame.mouse.get_pos()[0]
        y = pygame.mouse.get_pos()[1]

        if rect.x > x:
            rect.x -= vel
        if rect.x < x:
            rect.x += vel
        if rect.y > y:
            rect.y -= vel
        if rect.y < y:
            rect.y += vel

        if rect.x > tela.get_width() - rect.width:
            rect.x = tela.get_width() - rect.width
        if rect.x < 0:
            rect.x = 0
        if rect.y > tela.get_height() - rect.width:
            rect.y = tela.get_height() - rect.width
        if rect.y < 0:
            rect.y = 0


        #rect.h += 1
        #rect.w += 1



#        pygame.draw.circle(tela, jogadores[0].cor, (jogadores[0].x, jogadores[0].y), jogadores[0].raio)
        bolas_remove = []

        for i, bola in enumerate(bolas):
            if rect.w <= tela.get_width() / 2:
                if bola.x - bola.raio >= rect.x and bola.x + bola.raio <= rect.x + rect.width  \
                   and bola.y - bola.raio >= rect.y and bola.y + bola.raio <= rect.y + rect.height:
                    rect.h +=1
                    rect.w +=1
                    bolas_remove.append(i)
                    conta +=1

        for n in bolas_remove:
            print(n, len(bolas))
            if n < len(bolas):
                bolas.pop(n)



        if conta > 10:
            conta = 0
            for i in range(0, populacao - len(bolas)):
                bolas.append(Bola(random.randint(6, tela.get_width() - 6), random.randint(6, tela.get_height() - 6)))
                bolas[i].cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        tela.fill(0)
        for bola in bolas:
            pygame.draw.circle(tela, bola.cor, (bola.x, bola.y), bola.raio)

        pygame.draw.rect(tela, (0, 255, 0), rect)
        pygame.mouse.set_visible(False)
        pygame.display.flip()

    pygame.quit()
    exit()

if __name__ == '__main__':
    main()