import pygame
import sys
import random
import time
import player_module
import enemy_module
import enemy_manager
import time


def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("Gopher Shooter")
    # TODO: Change the size of the screen as you see fit!

    #REMOVE THE PYGAME.FULLSCREEN AT THE END TO MAKE IT NOT FORCE FULLSCREEN, IT WILL INSTEAD BE A SQUARE 800 by 800 window.
    screen = pygame.display.set_mode((800,800))
    player = player_module.Player(screen,400,400,6)
    enemies = enemy_manager.enemy_manager(screen,player)
    enemies.add_enemy()
    # let's set the framerate
    clock = pygame.time.Clock()
    init_clock = time.time()

    spawn_time = 3
    while True:
        final_clock = time.time()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()

            # TODO: Add you events code

        # TODO: Fill the screen with whatever background color you like!
        screen.fill((110, 79, 33))


        ##DRAW BACKGROUND:::


        ## BLACK LINES AROUND RECKTANGLES

        #left side
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 0, 120, 250),10)
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 550, 120, 250),10)

        #top side
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 0, 250, 120),10)
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(500, 0, 250, 120),10)

        #right side
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(screen.get_width()-120, 0, 120, 250),10)
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(screen.get_width()-120, 550, 120, 250),10)

        #bottom side
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, screen.get_height()-120, 250, 120),10)
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(500, screen.get_height()-120, 250, 120),10)



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
        player.draw()
        player.move()
        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()


main()
