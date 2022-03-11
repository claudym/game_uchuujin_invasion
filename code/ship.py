import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
  def __init__(self, ai_game):
    """Initialize the ship and starting position"""
    super().__init__()
    self.screen = ai_game.screen
    self.settings = ai_game.settings
    self.screen_rect = ai_game.screen.get_rect()

    #load ship image
    self.image = pygame.image.load('../images/cat.bmp').convert()
    self.rect = self.image.get_rect()

    #start each new ship at the bottom of the screen
    self.rect.midbottom = self.screen_rect.midbottom

    #store decimal float for ship's x position
    self.x = float(self.rect.x)

    #movement flag 
    self.moving_right = False
    self.moving_left = False
  
  def center_ship(self):
    self.rect.midbottom = self.screen_rect.midbottom
    self.x = float(self.rect.x)

  def update(self):
    if self.moving_right and self.rect.right < self.screen_rect.right:
      self.x += self.settings.ship_speed
    if self.moving_left and self.rect.left > 0:
      self.x -= self.settings.ship_speed
    
    self.rect.x = self.x
 
  def blitme(self):
    """Draw the ship at the current location"""
    self.screen.blit(self.image, self.rect)