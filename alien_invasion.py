import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    '''Classe geral para controlar recursos do jogo'''
    def __init__(self):
        '''Inicializa o jogo e cria os recursos do jogo'''
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()


    def run_game(self):
        '''Main loop do jogo'''
        while True:
            self._check_events()
            self.ship.update()  # Atualiza a posição da nave
            self.bullets.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        # Eventos do mouse e teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #move a nave para direita
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        # Redesenha a tela durante cada passo do jogo
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Mostrar a última tela visível
        pygame.display.flip()

if __name__ == '__main__':
    # Cria uma instância do jogo e roda o jogo
    ai = AlienInvasion()
    ai.run_game()