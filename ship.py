import pygame

class Ship:
    '''Classe que controla a nave'''
    def __init__(self, ai_game):
        '''inicializa a nave e define sua posiçao inicial'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #carrega a img da nave e configura como retangulo
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #inicia a nave no centro inferior da tela
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        #Movimento continuo - nave começa parada
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #atualiza a posiçao da nave baseado no movimento contínuo e define um limite
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speedy
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speedy

        #Atualiza a posiçao
        self.rect.x =self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

