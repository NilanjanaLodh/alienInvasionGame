import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from pygame.sprite import Group
from gameStats import GameStats
from time import sleep

class AlienGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self.screen, self.settings.ship_speed)
        pygame.display.set_caption("Alien invasion")
        self.bullets = Group()
        self.aliens = Group()
        self.stats = GameStats(self.settings)

    def run_game(self):
        self.create_fleet()

        while True:
            self.check_events()
            self.ship.update_motion()
            self.update_bullets()
            self.update_aliens()
            self.update_screen()

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.draw_bullets()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def update_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.reachedTop:
                self.bullets.remove(bullet)
        self.bullets.update()
        self.check_bullet_alien_collisions()

    def check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if len(self.aliens) == 0:
            print("fleet empty")
            self.create_fleet()

    def draw_bullets(self):
        for bullet in self.bullets.sprites():
            bullet.draw()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def check_keyup_events(self, event):
        if self.ship.moving_right:
            self.ship.moving_right = False
        elif self.ship.moving_left:
            self.ship.moving_left = False

    def fire_bullet(self):
        new_bullet = Bullet(
            settings=self.settings,
            screen=self.screen,
            ship=self.ship)

        self.bullets.add(new_bullet)

    def create_fleet(self):

        for row_number in range(self.settings.num_alien_rows):
            for alien_number in range(self.settings.num_aliens_x):
                self.create_alien(alien_number, row_number)

    def create_alien(self, alien_number, row_number):
        new_alien = Alien(
            screen=self.screen,
            settings=self.settings,
            xpos=self.settings.alien_border
                 + (self.settings.alien_width + self.settings.alien_xspacing) * alien_number,
            ypos=self.settings.alien_height +
                 (self.settings.alien_height + self.settings.alien_yspacing) * row_number)
        self.aliens.add(new_alien)

    def update_aliens(self):
        for alien in self.aliens.sprites():
            if alien.check_edge_hit():
                self.change_alien_fleet_direction()
                break
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            print("ship hit")
            self.ship_hit()

    def change_alien_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.shift_down()
        self.settings.alien_direction *= -1

    def ship_hit(self):
        """respond to shit hit and reset game"""
        self.stats.lives_left -= 1
        self.aliens.empty()
        self.bullets.empty()

        self.create_fleet()
        self.ship.recenter()

        if self.stats.lives_left == 0:
            self.game_over()

        sleep(0.5)

    def game_over(self):
        WHITE = (255, 255, 255)
        print("game over")
        font = pygame.font.Font(None,100)
        text = font.render("GAME OVER", True, WHITE)
        text_rect = text.get_rect()
        text_x = self.screen.get_width() // 2 - text_rect.width / 2
        text_y = self.screen.get_height() // 2 - text_rect.height / 2
        self.screen.blit(text, [text_x, text_y])
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                    elif event.key == pygame.K_p:
                        self.restart_game()

    def restart_game(self):
        self.stats.reset()
        self.run_game()


g = AlienGame()
g.run_game()
