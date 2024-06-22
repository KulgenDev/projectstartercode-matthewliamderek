import pygame
import random
import player_module


class Enemy():
    def __init__(self,screen,player):
        self.screen = screen
        self.player = player
        self.speed = 3

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
        location_of_player = (self.player.x, self.player.y)

    def is_hitting_wall(self):
        return (self.x <= 120 and self.y <= 250) or (self.x >= 680  and self.y <= 250) or (self.x <= 250 and self.y <= 120) or (self.x >= 550 and self.y <= 250) or (self.x <= 250 and self.y >= 680) or (self.x <=120 and self.y >= 430) or (self.x >= 550 and self.y >= 550)

    def draw(self):
        pygame.draw.circle(self.screen, pygame.color("Red"), (self.x,self.y))




