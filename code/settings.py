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
    self.bullets_allowed = 10

    #alien settings
    self.alien_speed = 1.0
    self.fleet_drop_speed = 10
    self.fleet_direction = 1  #1 represents right | -1 represents left