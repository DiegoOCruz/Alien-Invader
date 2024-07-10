import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''classe que controla a balas'''
    def __init__(self, ai_game):
        '''cria um obj bala'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #cria uma bala no ponto (0,0) e define a posiçao correta
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        '''move a bala na tela'''
        #atualiza aposiçao da bala
        self.y -= self.settings.bullet_speed
        #atualiza posiçao correta
        self.rect.y = self.y

    def draw_bullet(self):
        #cria a bala no screen
        pygame.draw.rect(self.screen, self.color, self.rect)

