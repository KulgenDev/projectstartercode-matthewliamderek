import pygame
import sys
import weapon_module
import math
import player_module
import enemy_module


class Wall:
    def __init__(self, screen, color, rect, width):
        self.screen = screen
        self.color = color
        self.rect = rect
        self.width = width

    def process(self):
        self.draw()

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect, self.width)

    def isCollided(self, object):
        if pygame.Rect.colliderect(pygame.Rect(self.rect), object.hitbox):
            return True
        return False


