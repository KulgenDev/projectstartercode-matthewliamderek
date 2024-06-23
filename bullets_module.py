import pygame
import time
import sys
import player_module
import math

class Bullet:

    def __init__(self, screen, x, y, width, height, color, angle):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.angle = angle

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        # take an angle and create a move direction
        self.x += 1 * math.cos(self.angle)
        self.y += 1 * math.sin(self.angle)
        points = []
        center_x = self.x + (self.width / 2)
        center_y = self.y + (self.height / 2)
        radius = math.sqrt((self.height / 2) ** 2 + (self.width / 2) ** 2)
        specific_angle = math.atan2(self.height / 2, self.width / 2)
        specific_angles = [specific_angle, -specific_angle + math.pi, specific_angle + math.pi, -specific_angle]
        specific_radians = (math.pi / 180) * self.angle
        for angle in specific_angles:
            y_offset = -1 * radius * math.sin(angle + specific_radians)
            x_offset = radius * math.cos(angle + specific_radians)
            points.append((center_x + x_offset, center_y + y_offset))
        pygame.draw.polygon(self.screen, self.color, points)

        # credit to Tim Swast on stackoverflow.com


    def hit_enemy(self):
        # when hit by enemy, cause the enemy to be removed and remove the bullet
        pass

    def off_screen(self):
        return (int(self.y) > int(self.screen.get_height())) or (int(self.y) < 0) or (int(self.x) > int(self.screen.get_width())) or (int(self.x) < int(0))

test_list = []
def main():
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    clock = pygame.time.Clock()

    test_bullet = Bullet(screen, 400, 400, 2, 4, pygame.Color("Green"), math.radians(60))
    test_list.append(test_bullet)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        key_press = pygame.key.get_pressed()
        if key_press[pygame.K_UP]:
            test_bullet.y -= 10
        if key_press[pygame.K_DOWN]:
            test_bullet.y += 10
        screen.fill(pygame.Color("Black"))
        test_bullet.draw()
        test_bullet.move()
        pygame.display.update()

if __name__ == "__main__":
    main()