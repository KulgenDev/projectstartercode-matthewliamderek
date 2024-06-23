import pygame
import sys
import math
import bullets_module

class Weapon:
    def __init__(self, screen):
        self.screen = screen
        self.bullets = []
        self.types = {"Bullet" : bullets_module.Bullet}
        self.type = self.types["Bullet"]

    def fire(self, x, y, angle):
        self.bullets.append(self.type(self.screen, x, y, 4, 4, pygame.Color("Blue"), angle))
        self.bullets[len(self.bullets) - 1].spawn_sound()

    def changeWeapon(self, type):
        self.type = self.types[type]

    def removeOffScreen(self):
        for bullet in self.bullets:
            if bullet.off_screen():
                self.bullets.remove(bullet)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Testing the Player")
    screen = pygame.display.set_mode((640, 650))

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0, 0, 0))

        pygame.display.update()

if __name__ == "__main__":
    main()
