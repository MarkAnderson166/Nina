
import pygame as pg
from random import *

from data.toon import *
from data.player import *
from data.globals import *

class Game:

  def __init__(self):
    pg.init()
    pg.mixer.init()
    pg.joystick.init()
    pg.display.set_caption("Ninjasuit Nina in the Neighbourhood of the N... N...") # necro? nasty?

    self.screen = pg.display.set_mode((WIDTH,HEIGHT))
    self.clock = pg.time.Clock()
    self.start_ticks=pg.time.get_ticks()
    self.running = False
    self.score = 0
    self.topScore = 0
    self.backgroundimageRandomiser = 0
    self.all_objects = pg.sprite.Group()
    #self.all_bombs = pg.sprite.Group()
    self.joystick_count = pg.joystick.get_count()
    self.joybuttons = pg.joystick.Joystick(0).get_numbuttons()


  def draw_text(self, surf, text, size, x, y):
    font = pg.font.Font(pg.font.match_font('arial'), size)
    text_surface = font.render(text, True, (150,150,250))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


  def get_input(self,player):

    for j in range( 0, self.joystick_count, 1 ):
      for i in range( 0, self.joybuttons, 1 ):
        if pg.joystick.Joystick(j).get_button(i) :
          player.button(i%4+5)
    keys = pg.key.get_pressed()
    player.moveX(pg.joystick.Joystick(0).get_axis(0)*-1+keys[pg.K_LEFT]+keys[pg.K_a]+keys[pg.K_RIGHT]*-1+keys[pg.K_d]*-1)
    player.moveY(pg.joystick.Joystick(0).get_axis(1)*-1+keys[pg.K_UP  ]+keys[pg.K_w]+keys[pg.K_DOWN ]*-1+keys[pg.K_s]*-1)
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        running = False
      if event.type == pg.MOUSEBUTTONDOWN:
        print('clicked '+ str(pg.mouse.get_pos()))
        self.new_game()
        return 1 
    if keys[pg.K_LALT] or keys[pg.K_RALT]:
      player.button(5)
    if keys[pg.K_LCTRL] or keys[pg.K_RCTRL]:
      player.button(6)
    if keys[pg.K_SPACE]:
      player.button(7)
    if keys[pg.K_x]:
      player.button(8)
    if keys[pg.K_RETURN]:
      pass # open menu


  def get_input_menu(self):

    for j in range( 0, self.joystick_count, 1 ):
      for i in range( 0, self.joybuttons, 1 ):
        if pg.joystick.Joystick(j).get_button(i) :
          if i >=4:
            return 1
    keys = pg.key.get_pressed()
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        running = False
      if event.type == pg.MOUSEBUTTONDOWN:
        print('clicked '+ str(pg.mouse.get_pos()))
        return 1
    if keys[pg.K_RETURN]:
      return 1


  def show_start_screen(self):

    self.draw_text(self.screen, 'Press enter for new game', 40, WIDTH/2, HEIGHT/2-100)
    self.draw_text(self.screen, 'Previous score: '+str(self.score), 30, WIDTH/2, HEIGHT/2)
    self.draw_text(self.screen, 'Top score: '+str(self.topScore), 30, WIDTH/2, HEIGHT/2+40)

    for i in range(self.joystick_count):
      joystick = pg.joystick.Joystick(i)
      joystick.init()
    waiting = True
    while waiting:
      pg.display.flip()
      if self.get_input_menu():
        self.new_game()

       
  def spawn_blocks(self):
    self.timer=(pg.time.get_ticks()-self.start_ticks)
    if self.timer > 100 and self.timer % 20 == 0 and len(self.all_blocks) < 10+abs(self.score/10):
      self.spawn.append(['Block',randint(0,WIDTH),-30,randint(-30,30)*0.1,1])


  #def look_for_collisions(self,player):
  #  for block in self.all_blocks:
  #    hitFire = pg.sprite.spritecollideany(block, self.all_fires)
  #    hitBomb = pg.sprite.spritecollideany(block, self.all_bombs)
  #    if hitFire:
  #      self.score += 3
  #      block.die()
  #    if hitBomb:
  #      self.score += 10
  #      block.die()
  #      hitBomb.die()
  #  hitBlock = pg.sprite.spritecollideany(player, self.all_blocks)
  #  if hitBlock:
  #    hitBlock.die()
  #    self.playerHealth -= 10
  #    player.takeHit()
  #    pass


  def spawner_func(self):
    if self.spawn:
      for arr in self.spawn:
      #  if arr[0] == 'Block':
      #    block = Block(arr[1],arr[2],arr[3],arr[4])
      #    self.all_blocks.add(block)
      #    self.all_objects.add(block)
      #  if arr[0] == 'Bomb':
      #    bomb = Bomb(arr[1],arr[2],arr[3],arr[4])
      #    self.all_bombs.add(bomb)
      #    self.all_objects.add(bomb)
      #  if arr[0] == 'Fire':
      #    fire = Fire(arr[1],arr[2],arr[3],arr[4])
      #    self.all_fires.add(fire)
      #    self.all_objects.add(fire)
        if arr[0] == 'GAMEOVER':
          self.show_start_screen()
      self.spawn = []


  def update_all(self):
    # Update
    for obj in self.all_objects:
      self.spawn.append(obj.update())    
    # Add new objects
    self.spawner_func()
    # Render
    self.screen.fill((0,0,0))
    self.screen.blit(backgroundimage,(0,0))


    self.all_objects.draw(self.screen)
    for obj in self.all_objects: pg.draw.rect(self.screen, (200,200,200), obj.getRect(),  2)
    self.draw_text(self.screen, 'Score: '+str(self.score), 40, 90, 10 )
    self.draw_text(self.screen, 'Health: '+str(self.playerHealth), 40, 90, 60 )

    pg.display.flip()
    self.clock.tick(FPS)


  def new_game(self):
    self.running = True
    self.all_objects.empty()
    #self.all_bombs.empty()
    choices = ['zombieboy' , 'zombiegirl' , 'ninjagirl']
    player = Player((WIDTH/2,HEIGHT/2),choice(choices)) 
    self.all_objects.add(player)
    self.score = 0
    self.playerHealth = 100
    self.spawn = []
    self.backgroundimageRandomiser = randint(0,3)

    for i in range(self.joystick_count):
      joystick = pg.joystick.Joystick(i)
      joystick.init()

    while self.running:
      self.get_input(player)
      self.spawner_func()
      #self.spawn_blocks()
      #self.look_for_collisions(player)
      self.update_all()
      if self.playerHealth <= 0:
        self.running = False
        if self.score > self.topScore:
           self.topScore = self.score
        g.show_start_screen()



g = Game()
g.show_start_screen()

pg.quit()