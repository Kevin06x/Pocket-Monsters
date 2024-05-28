from settings import *

class MonsterIndex:
    def __init__(self, monsters, fonts):
        self.display_surface = pygame.display.get_surface()
        self.fonts = fonts