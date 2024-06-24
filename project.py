import pygame
import sys
import random
import time
import player_module
import enemy_module
import enemy_manager
import time
import math
import wall_module


def main():
    # turn on pygame
    pygame.init()
    pygame.mixer.music.load("sfx/19th Floor - Bobby Richards.mp3")
    pygame.mixer.music.set_volume(10)
    # sound created by Bobby Richards on youtube music
    pygame.mixer.music.play()

    # create a screen
    pygame.display.set_caption("Gopher Shooter")
    # TODO: Change the size of the screen as you see fit!


    #REMOVE THE PYGAME.FULLSCREEN AT THE END TO MAKE IT NOT FORCE FULLSCREEN, IT WILL INSTEAD BE A SQUARE 800 by 800 window.
    screen = pygame.display.set_mode((800,800))
    player = player_module.Player(screen,400,400,3)
    enemies = enemy_manager.enemy_manager(screen,player)
    enemies.add_enemy()
    # let's set the framerate
    clock = pygame.time.Clock()
    init_clock = time.time()
    walls = []

    walls.append(wall_module.Wall(screen, (0, 0, 0), (0, 0, 120, 250), 10))
    walls.append(wall_module.Wall(screen, (0, 0, 0), pygame.Rect(0, 550, 120, 250), 10))

    # top side
    walls.append(wall_module.Wall(screen, (0, 0, 0), pygame.Rect(0, 0, 250, 120), 10))
    walls.append(wall_module.Wall(screen, (0, 0, 0), pygame.Rect(500, 0, 250, 120), 10))

    # right side
    walls.append(wall_module.Wall(screen, (0, 0, 0), pygame.Rect(screen.get_width() - 120, 0, 120, 250), 10))
    walls.append(wall_module.Wall(screen, (0, 0, 0), pygame.Rect(screen.get_width() - 120, 550, 120, 250), 10))

    # bottom side
    walls.append(wall_module.Wall(screen, (0, 0, 0), pygame.Rect(0, screen.get_height() - 120, 250, 120), 10))
    walls.append(wall_module.Wall(screen, (0, 0, 0), pygame.Rect(500, screen.get_height() - 120, 250, 120), 10))


    score_font = pygame.font.Font('font/scorefont.ttf', 70)

    spawn_time = 1
    while True:
        final_clock = time.time()
        clock.tick(60)
        if spawn_time - .00002 > 0:
            spawn_time -= .00009
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not enemies.hit_player:
                pos = pygame.mouse.get_pos()
                if not (pos[0] - player.x == 0):
                    angle = math.atan((pos[1] - player.y) / (pos[0] - player.x))
                    if pos[0] - player.x < 0:
                        angle += math.pi
                        #bullets.append(testBullet(screen, player.x, player.y, angle))
                    player.weapon.fire(player.x+10, player.y+10, angle)

            # TODO: Add you events code



        ##END GAME SCREEN
        if enemies.check_hit_player():
            screen.fill((0, 0, 0))
            game_over_text = score_font.render("GAME OVER", True, (255, 0, 0))
            screen.blit(game_over_text, (screen.get_width()/2 - (game_over_text.get_width()/2), screen.get_height()/2 - game_over_text.get_height()/2))
            screen.blit(score_label, (screen.get_width()/2 - (score_label.get_width()/2), screen.get_height()/2 + (game_over_text.get_height()+10)))
            pygame.mixer.music.stop()
        ## GAME SCREEN
        if not enemies.hit_player:
            # TODO: Fill the screen with whatever background color you like!
            screen.fill((110, 79, 33))


            ##DRAW BACKGROUND:::


            ## BLACK LINES AROUND RECKTANGLES

            #left side

            for wall in walls:
                wall.process()
                if wall.isCollided(player):
                    player.colliding(pygame.Rect(wall.rect))


            ##BROWN EDGE RECTANGLES
            #left side
            pygame.draw.rect(screen, (56, 40, 16), pygame.Rect(0, 0, 110, 240))
            pygame.draw.rect(screen, (56, 40, 16), pygame.Rect(0, 560, 110, 240))

            #top side
            pygame.draw.rect(screen, (56, 40, 16), pygame.Rect(0, 0, 240, 110))
            pygame.draw.rect(screen, (56, 40, 16), pygame.Rect(510, 0, 250, 110))

            #right side
            pygame.draw.rect(screen, (56, 40, 16), pygame.Rect(screen.get_width()-110, 0, 120, 240))
            pygame.draw.rect(screen, (56, 40, 16), pygame.Rect(screen.get_width()-110, 560, 120, 250))

            #bottom side
            pygame.draw.rect(screen, (56, 40, 16), pygame.Rect(0, screen.get_height()-110, 240, 120))
            pygame.draw.rect(screen, (56, 40, 16), pygame.Rect(510, screen.get_height()-110, 250, 120))




            ## START GAME CODE HERE::
            if final_clock - init_clock > spawn_time:
                enemies.add_enemy()
                init_clock = final_clock

            enemies.spawn_enemies()
            enemies.move_enemies()
            enemies.check_for_dead()
            enemies.check_hit_player()
            player.process()


            ## SCORE COUNTER
            score_font = pygame.font.Font('font/scorefont.ttf', 70)
            score_label = score_font.render(f"SCORE: {enemies.kills}", True, (255, 0, 0))
            screen.blit(score_label, (5, 0))


            # TODO: Add your project code

            # don't forget the update, otherwise nothing will show up!
        pygame.display.update()

main()
