import pygame
import math
import random

SCREEN_WIDTH = 2000
SCREEN_HEIGHT = 1200

class Planet:
  def __init__(self, name, r, d, a, c):
    self.name = name
    self.radius = r
    self.distance = d 
    self.angle = a
    self.color = c

  def paint(self, screen):
    center_x = int(SCREEN_WIDTH/2)
    center_y = int(SCREEN_HEIGHT/2)
    x = round(self.distance*math.cos(self.angle)+center_x)
    y = round(self.distance*math.sin(self.angle)+center_y)
    pygame.draw.circle(screen, self.color, (x, y), self.radius)
    font = pygame.font.Font(None, 20)
    text = font.render(self.name, 1, (255,255,255))
    text2 = font.render(str(self.distance) + " M. de KM", 1, (255,255,255))
    screen.blit(text2, (x-20, y-17))
    screen.blit(text, (x-30, y-30))

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done = False

clock = pygame.time.Clock()

# 2439
mercury = Planet("Mercurio", 2, 257, random.randint(0,360), (200,200,200))
# 6051
venus = Planet("Venus", 6, 308, random.randint(0,360), (127,127,127))
#6371
earth = Planet("Tierra", 6, 349, random.randint(0,360), (0,255,255))
#3389
mars = Planet("Marte", 3, 527, random.randint(0,360), (255,0,0))
# 69911
jupiter = Planet("Jupiter", 69, 978, random.randint(0,360), (100,40,0))
# 58232
saturn = Planet("Saturno", 58, 1684, 0, (115,0,0))
#25362
uranus = Planet("Urano", 25, 3071, 0, (200,200,200))
# 24622
neptune = Planet("Neptuno", 24, 4695, 0, (0,0,255))

planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
  
  screen.fill((0, 0, 0))
  
  pygame.draw.circle(screen, (random.randint(240,255), random.randint(240,255), 0), (int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2)),  200)

  for p in planets:
    p.angle = p.angle + 0.01
    p.paint(screen)

  pygame.display.flip()
  clock.tick(40)