import pygame
import weapon_module

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

    def process(self, player):
        if self.isPickedUp(player):
            self.changeWeapon(player.weapon)
            self.removed = True
        self.draw()

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def isPickedUp(self, player):
        hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        return pygame.Rect.colliderect(hitbox, pygame.Rect(player.x, player.y, 20, 20))

    def changeWeapon(self, weapon):
        weapon.changeWeapon(self.type, self.ammo)
