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


    ## Green text variable used for flashing restart screen opun death.

    green = True
    score_font = pygame.font.Font('font/scorefont.ttf', 70)
    restartGreen = score_font.render("PLAY AGAIN", True, (75,204,31))
    restartYellow = score_font.render("PLAY AGAIN", True, (238,234,37))


    ##START SCREEN INITIALIZATION STUFF
    startBG = pygame.image.load("images/startBG.png")
    title_font = pygame.font.Font('font/scorefont.ttf', 150)
    start_font = pygame.font.Font('font/scorefont.ttf', 90)
    startTitle = title_font.render("Gopher Shooter", True, (255, 0, 0))
    startGreen = start_font.render("START", True, (75,204,31))




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


            if (event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE)) and not enemies.hit_player and player.playing:
                pos = pygame.mouse.get_pos()
                if not (pos[0] - player.x == 0):
                    angle = math.atan((pos[1] - player.y) / (pos[0] - player.x))
                    if pos[0] - player.x < 0:
                        angle += math.pi
                        #bullets.append(testBullet(screen, player.x, player.y, angle))
                    player.weapon.fire(player.x+10, player.y+10, angle)
            elif event.type == pygame.MOUSEBUTTONDOWN and enemies.hit_player:
                pos = pygame.mouse.get_pos()
                if (pos[0] < screen.get_width()/2 - (restartGreen.get_width()/2)+ restartGreen.get_width()) and (pos[0] > screen.get_width()/2 - (restartGreen.get_width()/2)) and pos[1] > screen.get_height()/2 + 100 and pos[1] < screen.get_height()/2 + 100+restartGreen.get_height():
                    enemies.hit_player = False
                    enemies.enemies = []
                    pygame.mixer.music.load("sfx/19th Floor - Bobby Richards.mp3")
                    player.weapon.bullets = []
                    enemies.kills = 0
                    pygame.mixer.music.play()
                    player.x = player.OriginalX
                    player.y = player.OriginalY
            elif event.type == pygame.MOUSEBUTTONDOWN and not player.playing:
                pos = pygame.mouse.get_pos()
                if (pos[0] < screen.get_width()/2 - (startGreen.get_width()/2)+ startGreen.get_width()) and (pos[0] > screen.get_width()/2 - (startGreen.get_width()/2)) and pos[1] > screen.get_height()/2 + 100 and pos[1] < screen.get_height()/2 + 100+startGreen.get_height():
                    player.playing = True



            # TODO: Add you events code

        ## START GAME SCREEN
        if not player.playing:
            screen.blit(startBG, (0, 0))
            screen.blit(startTitle, (screen.get_width()/2-(startTitle.get_width()/2),screen.get_height()/2-200))
            screen.blit(startGreen, (screen.get_width()/2-(startGreen.get_width()/2),screen.get_height()/2+100))





        ##END GAME SCREEN
        if enemies.hit_player and player.playing:
            screen.fill((0, 0, 0))
            enemies.bullets = []
            enemies.enemies = []
            try:
                high_score = high_score
            except:
                high_score = 0
            if enemies.kills > high_score:
                high_score = enemies.kills
            game_over_text = title_font.render("GAME OVER", True, (255, 0, 0))
            high_score_text = score_font.render(f'HIGH SCORE: {high_score}', True, (255, 0, 0))
            screen.blit(game_over_text, (screen.get_width() / 2 - (game_over_text.get_width() / 2), screen.get_height() / 2 - game_over_text.get_height() / 2 - 100))
            screen.blit(high_score_text,
                        (screen.get_width() / 2 - (high_score_text.get_width() / 2), screen.get_height() / 2))
            screen.blit(score_label, (screen.get_width()/2 - (score_label.get_width()/2), screen.get_height()/2 + (game_over_text.get_height()+10)-180))





            if final_clock - init_clock > .3:
                init_clock = final_clock
                green = not green
            if green:
                screen.blit(restartGreen, (screen.get_width()/2 - (restartGreen.get_width()/2), screen.get_height()/2 + 100))
            elif not green:
                screen.blit(restartYellow, (screen.get_width()/2 - (restartGreen.get_width()/2), screen.get_height()/2 + 100))

        ## GAME SCREEN
        if not enemies.hit_player and player.playing:
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
            enemies.checkBulletOffScreenAndMove()
            player.process()


            ## SCORE COUNTER

            score_label = score_font.render(f"SCORE: {enemies.kills}", True, (255, 0, 0))
            screen.blit(score_label, (5, 0))


            # TODO: Add your project code

            # don't forget the update, otherwise nothing will show up!
        pygame.display.update()

main()
