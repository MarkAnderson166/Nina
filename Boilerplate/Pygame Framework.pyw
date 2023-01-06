
import pygame as pg
from random import *
from Block import *
from Bomb import *
from Fire import *
from Player import *
from constants import *

class Game:

  def draw_text(surf, text, size, x, y):
    font = pg.font.Font(pg.font.match_font('arial'), size)
    text_surface = font.render(text, True, (150,150,250))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
  
  pg.init()
  pg.mixer.init()
  screen = pg.display.set_mode((WIDTH,HEIGHT))

  pg.joystick.init()
  joystick_count = pg.joystick.get_count()
  joybuttons = pg.joystick.Joystick(0).get_numbuttons()

  pg.display.set_caption("Pygame Framework")
  clock = pg.time.Clock()

  all_objects = pg.sprite.Group()
  all_bombs = pg.sprite.Group()
  all_blocks = pg.sprite.Group()
  all_fires = pg.sprite.Group()

  all_objects.add(all_bombs,all_blocks,all_fires)
  player = Player((WIDTH/2,HEIGHT/2),(200,200,200))
  all_objects.add(player)

  score = 0

    # list of things to spawn next frame
    # objects making other objects in pygame is a bitch
    # this work-around uses a return value the update() method on every sprite
  spawn = []
  start_ticks=pg.time.get_ticks()

  # main loop

  running = True
  while running:

  # --------  controls -------------------

    keys = pg.key.get_pressed()
    for event in pg.event.get():
      if event.type == pg.QUIT:
        running = False

      if event.type == pg.MOUSEBUTTONDOWN:
        print('clicked '+ str(pg.mouse.get_pos()))

      for j in range( 0, joystick_count, 1 ):
        for i in range( 0, joybuttons, 1 ):
          if pg.joystick.Joystick(j).get_button(i) :
            score -= 1
            player.button(i)
      if keys[pg.K_LALT] or keys[pg.K_RALT]:
        score -= 1
        player.button(0)
      if keys[pg.K_LCTRL] or keys[pg.K_RCTRL]:
        score -= 1
        player.button(1)
      if keys[pg.K_SPACE]:
        score -= 1
        player.button(2)
      if keys[pg.K_RETURN]:
        score -= 1
        player.button(3)

    player.moveX(pg.joystick.Joystick(0).get_axis(0)*-1+keys[pg.K_LEFT]+keys[pg.K_a]+keys[pg.K_RIGHT]*-1+keys[pg.K_d]*-1)
    player.moveY(pg.joystick.Joystick(0).get_axis(1)*-1+keys[pg.K_UP  ]+keys[pg.K_w]+keys[pg.K_DOWN ]*-1+keys[pg.K_s]*-1)

    for i in range(joystick_count):
      joystick = pg.joystick.Joystick(i)
      joystick.init()
        
  # --------  end controls -------------------


    # spawn blocks above player randomly
    timer=(pg.time.get_ticks()-start_ticks)
    if timer > 100 and timer % 20 == 0 and len(all_blocks) < 10+int(score/10):
      spawn.append(['Block',randint(0,WIDTH),-30,randint(-30,30)*0.1,1])


    # collisions
    for block in all_blocks:
      hitFire = pg.sprite.spritecollideany(block, all_fires)
      hitBomb = pg.sprite.spritecollideany(block, all_bombs)
      if hitFire:
        score += 3
        block.die()
      if hitBomb:
        score += 10
        block.die()
        hitBomb.die()

    hitBlock = pg.sprite.spritecollideany(player, all_blocks)
    if hitBlock:
      hitBlock.die()
      player.takeHit()
      pass


    # using return value of all_objects.update() to spawn everything
    if spawn:
      for arr in spawn:
        if arr[0] == 'Block':
          block = Block(arr[1],arr[2],arr[3],arr[4])
          all_blocks.add(block)
          all_objects.add(block)
        if arr[0] == 'Bomb':
          bomb = Bomb(arr[1],arr[2],arr[3],arr[4])
          all_bombs.add(bomb)
          all_objects.add(bomb)
        if arr[0] == 'Fire':
          fire = Fire(arr[1],arr[2],arr[3],arr[4])
          all_fires.add(fire)
          all_objects.add(fire)
      spawn = []

    #Update
    for obj in all_objects:
      spawn.append(obj.update())


    # Render
    screen.fill((0,0,0))
    all_objects.draw(screen)
    draw_text(screen, str(score), 40, 30, 20 )

    pg.display.flip()
    clock.tick(FPS)

Game()
pg.quit()
