import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
  """A class to represent a single alien in the fleet."""

  def __init__(self, ai_game):
    """Initialize alien and starting position"""
    super().__init__()
    self.screen = ai_game.screen

    #load alien image (add randomnes later)
    self.image = pygame.image.load('../images/alien_2.bmp').convert()
    self.rect = self.image.get_rect()

    #start each new alien near the top left
    self.rect.x = self.rect.width
    self.rect.y = self.rect.height
    
    #store alien's x position
    self.x = float(self.rect.x)
