import pygame


class Ship():
    def __init__(self, screen, step=1):
        """Initialize , and set starting position"""
        self.screen = screen
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

        self.step = step

    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)

    def recenter(self):
        self.moving_left = False
        self.moving_right = False
        self.rect.centerx = self.screen_rect.centerx

    def update_motion(self):
        if self.moving_right:
            self.move_right()
        elif self.moving_left:
            self.move_left()

    def move_right(self):
        self.rect.x += self.step
        if self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right

    def move_left(self):
        self.rect.x -= self.step
        if self.rect.x < 0:
            self.rect.x = 0
