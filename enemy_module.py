import pygame
import random
import math
import player_module
import sys
import time
import enemy_manager



class Enemy():
    def __init__(self,screen,player,manager):
        self.screen = screen
        self.player = player
        self.speed = 3
        self.manager = manager

        # spawn 1 is left, spawn 2 is top, spawn 3 is right, spawn 4 is bottom

        spawn = random.randint(1,4)

        if spawn == 1:
            self.x = 0
            self.y = 400
        if spawn == 2:
            self.x = 400
            self.y = 0
        if spawn == 3:
            self.x = 800
            self.y = 400
        if spawn == 4:
            self.x = 400
            self.y = 800
    def move(self):
        angle = 90
        location_of_player = (self.player.x, self.player.y)
        if location_of_player[0] != self.x:
            angle = math.atan((location_of_player[1] - self.y)/(location_of_player[0] - self.x))
        if self.x > location_of_player[0]:
            angle += math.pi
        #print(math.cos(angle), math.sin(angle))
        self.x += self.speed*math.cos(angle)
        self.y += self.speed*math.sin(angle)





    def is_hitting_wall(self):
        return (self.x <= 120 and self.y <= 250) or (self.x >= 680  and self.y <= 250) or (self.x <= 250 and self.y <= 120) or (self.x >= 550 and self.y <= 250) or (self.x <= 250 and self.y >= 680) or (self.x <=120 and self.y >= 430) or (self.x >= 550 and self.y >= 550)

    def draw(self):
        pygame.draw.circle(self.screen,(255,0,0), (self.x,self.y),15)

class Shooter(Enemy):
    def __init__(self, screen, player, manager):
        super().__init__(screen, player, manager)
        self.lastShot = time.time()

    def draw(self):
        pygame.draw.circle(self.screen,(0,0,255), (self.x,self.y),15)

    def move(self):
        angle = 90
        location_of_player = (self.player.x, self.player.y)
        if location_of_player[0] != self.x:
            angle = math.atan((location_of_player[1] - self.y) / (location_of_player[0] - self.x))
        if self.x > location_of_player[0]:
            angle += math.pi
        # print(math.cos(angle), math.sin(angle))
        self.x += self.speed * math.cos(angle)
        self.y += self.speed * math.sin(angle)

        if time.time() - self.lastShot >= 1:
            self.manager.shoot(self.screen, self.x, self.y, 4, 4, pygame.Color("Black"), angle)
            self.lastShot = time.time()

def main():
    pygame.init()
    pygame.display.set_caption("TESTING ENEMY")

    screen = pygame.display.set_mode((800,600))

    clock = pygame.time.Clock()
    player = player_module.Player(screen, 400,400,10)
    enemys = [Enemy(screen,player)]

    enemy1 = Enemy(screen,player)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 0))

        player.draw()
        player.move()
        enemy1.draw()
        enemy1.move()


        pygame.display.update()




if __name__ == '__main__':
    main()





