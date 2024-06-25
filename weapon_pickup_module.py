import pygame
import weapon_module
import time

class Pickup:

    def __init__(self, screen, x, y, width, height, color, type, ammo):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.type = type
        self.ammo = ammo
        self.removed = False
        self.time = 4
        self.spawnTime = time.time()

    def process(self, player):
        if self.isPickedUp(player):
            self.changeWeapon(player.weapon)
            self.removed = True
        if time.time() >= self.spawnTime + self.time:
            self.removed = True
        self.draw()

    def draw(self):
        match self.type:
            case "Shotgun":
                the_shotgun_image = pygame.image.load("images/shotgun_image.bmp")
                the_shotgun_image = pygame.transform.scale(the_shotgun_image, (82.5, 20))
                self.width = 82.5
                self.height = 20
                self.screen.blit(the_shotgun_image, (self.x, self.y))
            case "Fast Bullet":
                the_rifle_image = pygame.image.load("images/sniper_rifle_image.bmp")
                the_rifle_image = pygame.transform.scale(the_rifle_image, (80, 40))
                self.width = 80
                self.height = 40
                self.screen.blit(the_rifle_image, (self.x, self.y))
            case _:
                pygame.draw.rect(self.screen, pygame.Color("Pink"), (self.x, self.y, 20, 20))

    def isPickedUp(self, player):
        if self.type == "Shotgun":
            hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
            return pygame.Rect.colliderect(hitbox, pygame.Rect(player.x, player.y, 20, 20))
        else:
            hitbox_2 = pygame.Rect(self.x, self.y, self.width, self.height)
            return pygame.Rect.colliderect(hitbox_2, pygame.Rect(player.x, player.y, 20, 20))

    def changeWeapon(self, weapon):
        weapon.changeWeapon(self.type, self.ammo)
