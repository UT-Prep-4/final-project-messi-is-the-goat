#Name(s):
#Final Project - Build Something Worth Showing Off
'''
This is the big one. At the end of camp you will demo this project at the
SHOWCASE, and it should be good enough to put on a resume or mention in a
college application. That means it is not just "code that works." It is a
project you designed, built, polished, and can explain.

WHAT MAKES IT SHOWCASE-WORTHY (the autograder checks for these):
  1. ORGANIZED: your code is split into clear, purposeful segments (functions optional), not one
     giant blob. (Aim for at least 3-4 functions with real jobs.)
  2. SUBSTANTIAL: this is a multi-day build, bigger than the mini-project.
  3. REAL LOGIC: decisions (if/elif/else) and repetition (loops) working together.
  4. DOCUMENTED: fill out PROJECT.md so a stranger (or a college admissions
     reader!) can understand what you built and how to run it.

Whether it is impressive, creative, and demo-ready is judged by humans at
showcase, not by the autograder.

============================= PICK YOUR TRACK =================================

TRACK A: IMAGE PROCESSING PROGRAM
  Build a program that opens an image and transforms it with a special
  function you write yourself: brightness adjustment, a color filter overlay,
  grayscale, mirror, pixelate, or invent your own effect.
  The Pillow library is preinstalled. The core moves:

      from PIL import Image
      img = Image.open("photo.png")
      width, height = img.size
      pixel = img.getpixel((x, y))          # (red, green, blue), each 0-255
      img.putpixel((x, y), (r, g, b))       # set a pixel
      img.save("output.png")                # then click it in VS Code to view!

  Brightness is a for loop over every pixel that multiplies r, g, b by a
  factor the user chooses (careful: values must stay between 0 and 255).
  A filter overlay nudges every pixel toward a color (add red, drop blue...).
  Level up: ask the user which effect to apply with input(), show a menu,
  process any image file they name, draw the result with turtle or pygame.

TRACK B: ADVENTURE GAME
  Build a text adventure where the player explores, makes choices, and wins
  or loses based on decisions and luck. Use random for surprises: treasure,
  traps, enemy encounters, dice rolls, critical hits.
  The shape of it: one function per location or scene, input() for choices,
  an inventory list, health or gold as numbers, and random.randint() for
  the unexpected. Level up: turn-based combat, a map, multiple endings,
  ASCII art title screens, a save-your-score high score.

TRACK C: YOUR OWN IDEA
  A bigger game (pygame or turtle), a quiz app, a tool that solves a real
  problem you have, a simulation, generative turtle art... Pitch it to your
  instructor FIRST, then build it. The four requirements above still apply.

=============================== PLAN FIRST ====================================
Before you write code, fill this in (it will keep you honest all week):

  MY PROJECT: A Factory Game
  THE PIECES I NEED TO BUILD:
    The different factory parts:
      Resource attainment,
      Resource Processing,
      Output
    Ways to do research and upgrades
    Maybe add defenses and attackers
    Exploration and world generation
  WHAT I WILL DEMO AT SHOWCASE: (the 60-second version)

==============================================================================
Build your project below (and split it into more .py files if it gets big;
the grader reads all of them). Delete this line and start!
'''
import pygame
import random
import sys
from pygame.locals import *
from PIL import Image 
pygame.init()

vec = pygame.math.Vector2

font = pygame.font.Font(None, 48)
text_surface = font.render("Hello, Pygame!", True, (255, 255, 255))

globalSpeed= 500
screen = pygame.display.set_mode((1200,675))
FPS = pygame.time.Clock()
quit_event = pygame.event.Event(pygame.QUIT)
current_zombies = 0
sun = 20
placeing = False

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
class sunflower(pygame.sprite.Sprite):
  def __init__(self, y_offset,x_offset):
    super().__init__()
    self.pos = vec((x_offset, y_offset))
    self.image = pygame.image.load("sunflower.png")
    self.rect = self.image.get_rect(topleft=(self.pos.x, self.pos.y))
    self.surf = pygame.transform.scale(self.image, (78.75,78.75)) 
    self.spacing = 0
    self.health = 20
    self.cooldown = 30
    all_sprites.add(self)
    plants.add(self)

  def clicked(self):
    pass

  def attacked(self):
    if self.cooldown < 0:
      self.health -= 5
      self.cooldown = 30
    else:
      self.cooldown -= 1
    
    if self.health <= 0:
        self.kill()

  def update(self):
    if self.spacing > 0:
      sunflower_sun(self.pos.y + random.randint(-20, 20), self.pos.x + random.randint(-20, 20))
      self.spacing = random.randint(-500, -400)
    self.spacing += 1
    
  
class peashooter(pygame.sprite.Sprite):
  def __init__(self, y_offset,x_offset):
    super().__init__()
    self.pos = vec((x_offset, y_offset))
    self.inc = 0
    self.image = pygame.image.load("peashooter.png")
    self.rect = self.image.get_rect(topleft=(self.pos.x, self.pos.y))
    self.surf = pygame.transform.scale(self.image, (78.75,78.75)) 
    self.health = 20
    self.cooldown = 30
    all_sprites.add(self)
    plants.add(self)
  
  def clicked(self):
    pass

  def update(self):
    if [sprite.pos.y for sprite in zombies if sprite.pos.y == self.pos.y] != []:
      if self.inc % 1000 == 0:
        peashooter_pea(self.pos.y, self.pos.x + 20)
      self.inc += 1

  def attacked(self):
    if self.cooldown < 0:
      self.health -= 5
      self.cooldown = 30
    else:
      self.cooldown -= 1
    
    if self.health <= 0:
        self.kill()



class wall_nut(pygame.sprite.Sprite):
  def __init__(self, y_offset,x_offset):
    super().__init__()
    self.pos = vec((x_offset, y_offset))
    self.image = pygame.image.load("wallnut.png")
    self.rect = self.image.get_rect(topleft=(self.pos.x, self.pos.y))
    self.surf = pygame.transform.scale(self.image, (78.75,78.75)) 
    self.health = 50
    self.cooldown = 30
    all_sprites.add(self)
    walls.add(self)
    plants.add(self)

  def clicked(self):
    pass

  def update(self):
    pass
  
  def attacked(self):
    if self.cooldown < 0:
      self.health -= 5
      self.cooldown = 30
    else:
      self.cooldown -= 1
    
    if self.health <= 0:
        self.kill()


class potatomine(pygame.sprite.Sprite):
  def __init__(self, y_offset,x_offset):
    super().__init__()
    self.pos = vec((x_offset, y_offset))
    self.image = pygame.image.load("Potato_Mine.png")
    self.rect = pygame.Rect(self.pos.x, self.pos.y,79,79)
    self.surf = pygame.transform.scale(self.image, (78.75,78.75)) 
    all_sprites.add(self)
    plant_attack.add(self)
    #plants.add(self)

  def update(self):
     pass
  
  def clicked(self):
    pass
  
  def end(self):
    self.kill()

class sunflower_sun(pygame.sprite.Sprite):
  def __init__(self, y_offset,x_offset):
    super().__init__()
    self.pos = vec((x_offset, y_offset))
    self.image = pygame.image.load("sun.png")
    self.rect = self.image.get_rect(topleft=(self.pos.x, self.pos.y))
    self.surf = pygame.transform.scale(self.image, (78.75,78.75)) 
    all_sprites.add(self)

  def clicked(self):
    global sun 
    sun += 10
    self.end()

  def end(self):
    self.kill()

  def update(self):
     pass

class peashooter_pea(pygame.sprite.Sprite):
  def __init__(self, y_offset,x_offset):
    super().__init__()
    self.pos = vec((x_offset, y_offset))
    self.image = pygame.image.load("pea.png")
    self.rect = pygame.Rect(self.pos.x, self.pos.y, 42,42)
    self.surf = pygame.transform.scale(self.image, (42,42)) 
    all_sprites.add(self)
    plant_attack.add(self)

  def clicked(self):
    pass

  def update(self):
    self.pos.x += 4
    self.rect = pygame.Rect(self.pos.x, self.pos.y, 42,42)
  
  def end(self):
    self.kill()
  

class zombie(pygame.sprite.Sprite):
  def __init__(self, y_offset):
    
    super().__init__()
    self.health = 10
    self.pos = vec((1200, y_offset))
    self.image = pygame.image.load("zombie.png")
    self.rect = pygame.Rect(self.pos.x, self.pos.y,60,96.1)
    self.surf = pygame.transform.scale(self.image, (60,96.1))
    all_sprites.add(self)
    zombies.add(self)

  def clicked(self):
    pass

  def update(self):
    global current_zombies
    collided_walls = False
    for sprite in plants.sprites():
      if sprite.pos.y == self.pos.y:
        if abs((sprite.pos.x+60) - self.pos.x) < 10:
          collided_walls = True
          sprite.attacked()

    if collided_walls == False:
      self.pos.x -= 0.30

    self.rect = pygame.Rect(self.pos.x, self.pos.y,60,96.1)
    if self.pos.x < 300:
       self.kill()
       pygame.event.post(quit_event)
    collided_enemies = pygame.sprite.spritecollideany(self, plant_attack)
    #print(collided_enemies)
    #print(self.rect)
    if collided_enemies != None:  
      print("hit")
      print(plant_attack)
      
      collided_enemies.end()
      if isinstance(collided_enemies, peashooter_pea):
        self.health -= 5
      else:
        self.health -= 1000
      if self.health <= 0:
        current_zombies -= 1
        self.kill()

max_zombies = 0



def Zombie_gen(speed = 100):
  global current_zombies
  global globalSpeed
  if random.randint(1,speed) == 1:
    print(f"{max_zombies}, {current_zombies}")
    #if max_zombies > current_zombies:
    if True:
      current_zombies += 1
      new_zombie = zombie(random.choice([125, 225, 325, 420, 520]))
      if globalSpeed > 15:
        globalSpeed -= 10
      
def placment(targetX, targetY, key):
  global sun
  roundedX = min([325, 425, 525, 625, 725, 820, 920, 1020, 1120], key=lambda x: abs(x - targetX))
  roundedY = min([125, 225, 325, 420, 520], key=lambda y: abs(y - targetY))
  if sun >= 20:
   try:
    {pygame.K_1:sunflower, pygame.K_2:peashooter, pygame.K_3:wall_nut, pygame.K_4:potatomine}[key](roundedY,roundedX)
    sun -= 20
   except:
    pass
  return
      

all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()
zombies = pygame.sprite.Group()
plant_attack = pygame.sprite.Group()
plants = pygame.sprite.Group()

test_wall_nut = wall_nut(225,1020)
test_potatomine = potatomine(325,325)
test_sunflower = sunflower(420,325)
# test_sunflower_sun = sunflower_sun(420,400)
test_peashooter = peashooter(125, 325)
# test_peashooter_pea = peashooter_pea(125,400)
#test_zombie = zombie(125)

bg_image = pygame.image.load("lawn.jpg").convert()
bg_image = pygame.transform.scale(bg_image, (1600, 675))

while True:
    screen.blit(bg_image, (-250, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            print("ending")
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            if placeing == False:
              mouse_pos = event.pos  

              clicked_sprites = [s for s in all_sprites if s.rect.collidepoint(mouse_pos)]
              for sprite in clicked_sprites:
                sprite.clicked()
            else:
              placment(event.pos[0], event.pos[1], placeing)
              placeing = False
        elif event.type == pygame.KEYDOWN:
          placeing = event.key
          

    for entry in all_sprites:
        entry.update()
        screen.blit(entry.surf, entry.pos)

    text_surface = font.render(f"Sun: {sun}", True, (255, 255, 255))
    screen.blit(text_surface, (20, 20))
    max_zombies = 20
    #hits = pygame.sprite.groupcollide(zombies, plant_attack, True, True)
    Zombie_gen(globalSpeed)
    # keys = pygame.key.get_pressed()
    pygame.display.update()
    FPS.tick(60)



