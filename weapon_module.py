import pygame
import sys
import math
import bullets_module

class Weapon:
    def __init__(self, screen, bulletType):
        self.screen = screen
        self.bulletType = bulletType
        self.bullets = []

    def fire(self):
        pass

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
