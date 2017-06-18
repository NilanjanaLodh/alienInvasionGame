import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, settings, screen, ship):
        super().__init__()
        self.size = settings.bullet_size
        self.color = settings.bullet_color
        self.step = settings.bullet_speed
        self.screen = screen

        self.rect = pygame.Rect(0, 0, self.size , self.size) ###testing
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.reachedTop = False

    def update(self):
        self.y -= self.step
        self.rect.y = self.y
        if self.rect.bottom <= 0:
            self.reachedTop = True

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
