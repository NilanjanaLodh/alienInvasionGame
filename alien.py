import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, settings, screen, xpos, ypos):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ugly_alien.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.settings = settings
        self.x = float(self.rect.x)

    def update(self):
        self.x += (self.settings.alien_direction * self.settings.alien_speed)
        self.rect.x = self.x

    def check_edge_hit(self):
        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= self.screen_rect.left:
            return True
        else:
            return False

    def shift_down(self):
        self.rect.y += self.settings.alien_drop_speed

    def blitme(self):
        self.screen.blit(self.image, self.rect)
