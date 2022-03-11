class Settings:
  def __init__(self):
    #screen settings
    self.screen_width = 1920
    self.screen_height = 1026
    self.bg_color = (0, 0, 0)

    #ship settings
    self.ship_speed = 1.5
    self.ship_limit = 3

    #bullet settings
    self.bullet_speed = 1.5
    self.bullet_width = 3
    self.bullet_height = 15
    self.bullet_color = (212, 104, 242)
    self.bullets_allowed = 20

    #alien settings
    self.alien_speed = 1.0
    self.fleet_drop_speed = 10
    self.fleet_direction = 1  #1 represents right | -1 represents left

    #speed up
    self.speedup_scale = 1.2
    self.initialize_dynamic_settings()

    #alien point values increase
    self.score_scale = 1.5

  def initialize_dynamic_settings(self):
    self.ship_speed = 1.5
    self.bullet_speed = 3.0
    self.alien_speed = 1.0

    self.fleet_direction = 1  #going right(1)

    #scoring
    self.alien_points = 5
  
  def increase_speed(self):
    self.ship_speed *= self.speedup_scale
    self.bullet_speed *= self.speedup_scale
    self.alien_speed *= self.speedup_scale

    self.alien_points = int(self.alien_points * self.score_scale)