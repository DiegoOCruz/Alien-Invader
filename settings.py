class Settings:
    def __init__(self):
        '''Inicializa as configurações do jogo'''
        # Configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # configuraçoes da nave
        self.ship_speedy = 2

        # configuraçoes das balas
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)