import pygame
import sys
import math
import bullets_module
import gc
import weapon_pickup_module

class Weapon:
    def __init__(self, screen):
        self.screen = screen
        self.bullets = []
        self.types = {"Bullet" : bullets_module.Bullet, "Fast Bullet" : bullets_module.fastBullet, "Shotgun" : bullets_module.Shotgun}
        self.type = self.types["Bullet"]
        self.pickups = []
        self.ammo = 0

    def fire(self, x, y, angle):
        if self.type == self.types["Bullet"] or self.type == self.types["Fast Bullet"]:
            self.bullets.append(self.type(self.screen, x, y, 4, 4, pygame.Color("Green"), angle))
            self.bullets[len(self.bullets) - 1].play_bullet_sound()
        elif self.type == self.types["Shotgun"]:
            self.bullets.append(self.type(self.screen, x, y, 4, 4, pygame.Color("Green"), angle))
            self.bullets.append(self.type(self.screen, x, y, 4, 4, pygame.Color("Green"), angle + math.pi/6))
            self.bullets.append(self.type(self.screen, x, y, 4, 4, pygame.Color("Green"), angle - math.pi/6))
            self.bullets[len(self.bullets) - 1].play_shotgun_sound()
        self.ammo -= 1
        if self.ammo <= 0:
            self.changeWeapon("Bullet", 0)

    def process(self, player):
        for pickup in self.pickups:
            pickup.process(player)
            if pickup.removed:
                self.pickups.remove(pickup)

    def changeWeapon(self, type, ammo):
        self.type = self.types[type]
        self.ammo = ammo

    def addPickup(self, x, y, type):
        if type == "Fast Bullet":
            self.pickups.append(weapon_pickup_module.Pickup(self.screen, x, y, 15, 15, pygame.Color("Pink"), "Fast Bullet", 40))
        elif type == "Shotgun":
            self.pickups.append(weapon_pickup_module.Pickup(self.screen, x, y, 15, 15, pygame.Color("Orange"), "Shotgun", 30))

    def removeOffScreen(self):
        for bullet in self.bullets:
            if bullet.off_screen():
                self.bullets.remove(bullet)
                gc.collect()

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
