import pygame
import sys
import weapon_module
import math
import numpy


class Player:
    def __init__(self, screen, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.screen = screen

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

    def get_pos(self):
        return (self.x, self.y)


    def draw(self):
        pygame.draw.rect(self.screen, pygame.Color("White"), (self.x, self.y, 20, 20))

def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("Testing the Player")
    screen = pygame.display.set_mode((640, 650))
    player = Player(screen, 300, 300, 3)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                angle = numpy.arctan((pos[1] - player.y)/(pos[0] - player.x))





        screen.fill((0, 0, 0))

        player.move()
        player.draw()

        pygame.display.update()

if __name__ == "__main__":
    main()