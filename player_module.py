import pygame
import sys
import weapon_module
import math


class Player:
    def __init__(self, screen, x, y, speed, weapon):
        self.x = x
        self.y = y
        self.speed = speed
        self.screen = screen
        self.weapon = weapon

    def process(self):
        # all functions that run every frame are held here in one place
        self.move()
        self.draw()
        #Derek needs to change line 59 of bullets_module from "if self.x < self.screen.get_width():" to "if self.x > self.screen.get_width():"
        self.removeBullets()
        print(len(self.weapon.bullets))

    def move(self):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_UP] or keys[pygame.K_w]):
            self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed


    def get_pos(self):
        return (self.x, self.y)


    def draw(self):
        pygame.draw.rect(self.screen, pygame.Color("White"), (self.x, self.y, 20, 20))

    def removeBullets(self):
        self.weapon.removeOffScreen()

class testBullet:
    def __init__(self, screen, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.screen = screen

    def move(self):
        self.x += 10 * math.cos(self.angle)
        self.y += 10 * math.sin(self.angle)

    def draw(self):
        pygame.draw.rect(self.screen, pygame.Color("Blue"), (self.x, self.y, 5, 5))

def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Testing the Player")
    screen = pygame.display.set_mode((640, 650))
    weapon = weapon_module.Weapon(screen)
    player = Player(screen, 300, 300, 3, weapon)
#    bullets = []

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if not (pos[0] - player.x == 0):
                    angle = math.atan((pos[1] - player.y)/(pos[0] - player.x))
                    if pos[0] - player.x < 0:
                        angle += math.pi
#                   bullets.append(testBullet(screen, player.x, player.y, angle))
                    player.weapon.fire(player.x, player.y , angle)

        screen.fill((0, 0, 0))

        for b in weapon.bullets:
            b.move()
            b.draw()





        player.process()

        pygame.display.update()

if __name__ == "__main__":
    main()