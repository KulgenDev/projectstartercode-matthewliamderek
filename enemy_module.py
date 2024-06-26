import pygame
import random
import math
import player_module
import sys
import time
import enemy_manager
import bullets_module


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
        pygame.draw.circle(self.screen,pygame.Color("Purple"), (self.x + 12,self.y + 12),15)
        basic_enemy_image = pygame.image.load("images/basic_enemy_face.bmp")
        basic_enemy_image = pygame.transform.scale(basic_enemy_image, (24, 24))
        self.width = 20
        self.height = 20
        self.screen.blit(basic_enemy_image, (self.x, self.y))

class Kamikaze(Enemy):
    def __init__(self,screen,player,manager):
        super().__init__(screen,player,manager)
        self.scream = pygame.mixer.Sound("sfx/Attack.wav")
        self.scream.set_volume(0.2)
        self.speed = 5

    def move(self):
        pygame.mixer.Sound.play(self.scream)
        angle = 90
        location_of_player = (self.player.x, self.player.y)
        if location_of_player[0] != self.x:
            angle = math.atan((location_of_player[1] - self.y)/(location_of_player[0] - self.x))
        if self.x > location_of_player[0]:
            angle += math.pi
        #print(math.cos(angle), math.sin(angle))
        self.x += self.speed*math.cos(angle)
        self.y += self.speed*math.sin(angle)

    def stopSound(self):
        pygame.mixer.Sound.stop(self.scream)

    def draw(self):
        pygame.draw.circle(self.screen, pygame.Color("Red"), (self.x + 13, self.y + 13), 15)
        kamikaze_enemy_image = pygame.image.load("images/kamikaze_enemy_face.bmp")
        kamikaze_enemy_image = pygame.transform.scale(kamikaze_enemy_image, (26, 26))
        self.width = 20
        self.height = 20
        self.screen.blit(kamikaze_enemy_image, (self.x, self.y))



class Shooter(Enemy):
    def __init__(self, screen, player, manager):
        super().__init__(screen, player, manager)
        self.lastShot = time.time()

    def draw(self):
        pygame.draw.circle(self.screen,(0,0,255), (self.x + 12,self.y + 12),15)
        pistol_enemy_image = pygame.image.load("images/pistol_enemy_face.bmp")
        pistol_enemy_image = pygame.transform.scale(pistol_enemy_image, (24, 24))
        self.width = 20
        self.height = 20
        self.screen.blit(pistol_enemy_image, (self.x, self.y))

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
            self.manager.shoot(self.screen, self.x, self.y, 4, 4, pygame.Color("Cyan"), angle)
            bullet_sound = pygame.mixer.Sound("sfx/jasbro_laser.wav")
            bullet_sound.set_volume(.5)
            # sound created by jobro on fressound
            bullet_sound.play(0)
            self.lastShot = time.time()

class Elite(Shooter):
    def __init__(self, screen, player, manager):
        super().__init__(screen, player, manager)
        self.lastShot = time.time()

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

        if time.time() - self.lastShot >= 0.9:
            self.manager.shoot(self.screen, self.x, self.y, 4, 4, pygame.Color("Cyan"), angle)
            self.manager.shoot(self.screen, self.x, self.y, 4, 4, pygame.Color("Cyan"), angle + math.pi/6)
            self.manager.shoot(self.screen, self.x, self.y, 4, 4, pygame.Color("Cyan"), angle - math.pi/6)
            bullet_sound = pygame.mixer.Sound("sfx/laser_shot_big.wav")
            bullet_sound.set_volume(.5)
            # sound created by bulbaproducer on fressound
            bullet_sound.play(0)
            self.lastShot = time.time()

    def draw(self):
        pygame.draw.circle(self.screen,(255,255,0), (self.x + 12,self.y + 12),15)
        elite_enemy_image = pygame.image.load("images/elite_enemy_face.bmp")
        elite_enemy_image = pygame.transform.scale(elite_enemy_image, (24, 24))
        self.width = 20
        self.height = 20
        self.screen.blit(elite_enemy_image, (self.x, self.y))

class Titan(Enemy):

    def __init__(self, screen, player, manager):
        super().__init__(screen, player, manager)
        self.titan_health = 0
        self.speed = 2

    def move(self):
        angle = 90
        location_of_player = (self.player.x, self.player.y)
        if location_of_player[0] != self.x:
            angle = math.atan((location_of_player[1] - self.y)/(location_of_player[0] - self.x))
        if self.x > location_of_player[0]:
            angle += math.pi
        self.x += self.speed*math.cos(angle)
        self.y += self.speed*math.sin(angle)

    def draw(self):
        pygame.draw.circle(self.screen,pygame.Color(37, 145, 37), (self.x + 12,self.y + 12),15)
        titan_enemy_image = pygame.image.load("images/titan_enemy_face.bmp")
        titan_enemy_image = pygame.transform.scale(titan_enemy_image, (24, 24))
        self.width = 20
        self.height = 20
        self.screen.blit(titan_enemy_image, (self.x, self.y))



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





