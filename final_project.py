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

screen = pygame.display.set_mode((1200,675))
FPS = pygame.time.Clock()
FPS.tick(60)

current_zombies = 0
sun = 20

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
class sunflower(pygame.sprite.Sprite):
  def __init__(self, y_offset,x_offset):
    super().__init__()
    self.pos = vec((x_offset, y_offset))
    self.image = pygame.image.load("sunflower.png")
    self.rect = self.image.get_rect(topleft=(self.pos.x, self.pos.y))
    self.surf = pygame.transform.scale(self.image, (78.75,78.75)) 
    all_sprites.add(self)

  def update(self):
     pass
  
class peashooter(pygame.sprite.Sprite):
  def __init__(self, y_offset,x_offset):
    super().__init__()
    self.pos = vec((x_offset, y_offset))
    self.inc = 0
    self.image = pygame.image.load("peashooter.png")
    self.rect = self.image.get_rect(topleft=(self.pos.x, self.pos.y))
    self.surf = pygame.transform.scale(self.image, (78.75,78.75)) 
    all_sprites.add(self)

  def update(self):
    if [sprite.pos.y for sprite in zombies if sprite.pos.y == self.pos.y] != []:
      if self.inc % 1000 == 0:
        peashooter_pea(self.pos.y, self.pos.x + 20)
      self.inc += 1



class wall_nut(pygame.sprite.Sprite):
  def __init__(self, y_offset,x_offset):
    super().__init__()
    self.pos = vec((x_offset, y_offset))
    self.image = pygame.image.load("wallnut.png")
    self.rect = self.image.get_rect(topleft=(self.pos.x, self.pos.y))
    self.surf = pygame.transform.scale(self.image, (78.75,78.75)) 
    all_sprites.add(self)

  def update(self):
     pass

class potatomine(pygame.sprite.Sprite):
  def __init__(self, y_offset,x_offset):
    super().__init__()
    self.pos = vec((x_offset, y_offset))
    self.image = pygame.image.load("Potato_Mine.png")
    self.rect = pygame.Rect(self.pos.x, self.pos.y,79,79)
    self.surf = pygame.transform.scale(self.image, (78.75,78.75)) 
    all_sprites.add(self)
    plant_attack.add(self)

  def update(self):
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

  
  def update(self):
    self.pos.x -= 0.5
    self.rect = pygame.Rect(self.pos.x, self.pos.y,60,96.1)
    if self.pos.x < 300:
       self.kill()
    collided_enemies = pygame.sprite.spritecollideany(self, plant_attack)
    #print(collided_enemies)
    #print(self.rect)
    if collided_enemies != None:  
      print("hit")
      print(plant_attack)
      collided_enemies.end()
      self.health -= 5
      if self.health <= 0:
        self.kill()

max_zombies = 0



def Zombie_gen(speed = 100):
  global current_zombies
  if random.randint(1,speed) == 25:
    if max_zombies > current_zombies:
      current_zombies += 1
      new_zombie = zombie(random.choice([125, 225, 325, 420, 520]))
      
      

all_sprites = pygame.sprite.Group()
zombies = pygame.sprite.Group()
plant_attack = pygame.sprite.Group()

test_wall_nut = wall_nut(225,325)
test_potatomine = potatomine(325,325)
test_sunflower = sunflower(420,325)
test_sunflower_sun = sunflower_sun(420,400)
test_peashooter = peashooter(125, 325)
#test_peashooter_pea = peashooter_pea(125,400)
test_zombie = zombie(125)

bg_image = pygame.image.load("lawn.jpg").convert()
bg_image = pygame.transform.scale(bg_image, (1600, 675))

while True:
    screen.blit(bg_image, (-250, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    for entry in all_sprites:
        entry.update()
        screen.blit(entry.surf, entry.pos)
    max_zombies = 20
    #hits = pygame.sprite.groupcollide(zombies, plant_attack, True, True)
    Zombie_gen(500)
    keys = pygame.key.get_pressed()
    pygame.display.update()



