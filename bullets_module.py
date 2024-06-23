import pygame
import time
import sys
import player_module
import math

screen = pygame.display.set_mode((700, 700))

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


    def spawn_sound(self):
        bullet_sound = pygame.mixer.Sound("jasbro_laser.wav")
        bullet_sound.play(0)

    def move(self):
        # take an angle and create a move direction
        self.x += 7 * math.cos(self.angle)
        self.y += 7 * math.sin(self.angle)
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
        if self.y < 0:
            return True
        if self.y > self.screen.get_height():
            return True
        if self.x < 0:
            return True
        if self.x < self.screen.get_width():
            return True
        else:
            return False

bullet_list = []

def bullet_spawn():
    # from player_module import angle
    # ask matthew to make angle a global variable and then change math.radians(60) to angle
    bullet = Bullet(screen, 350, 350, 2, 4, pygame.Color("Green"), math.radians(60))
    bullet_list.append(bullet)
    bullet_sound = pygame.mixer.Sound("jasbro_laser.wav")
    bullet_sound.play(0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    clock = pygame.time.Clock()

    #bullet = Bullet(screen, 1000, 1000, 2, 4, pygame.Color("Green"), math.radians(60))
    #bullet_list.append(bullet)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                bullet_spawn()
                print(bullet_list)
        key_press = pygame.key.get_pressed()
        if key_press[pygame.K_UP]:
            bullet.y -= 10
        if key_press[pygame.K_DOWN]:
            bullet.y += 10
        screen.fill(pygame.Color("Black"))
        for bullet in bullet_list:
            bullet.draw()
            bullet.move()
            if bullet.x < 0:
                bullet_list.remove(bullet)
                print(bullet_list)
            if bullet.x > screen.get_width():
                bullet_list.remove(bullet)
                print(bullet_list)
            if bullet.y < 0:
                bullet_list.remove(bullet)
                print(bullet_list)
            if bullet.y > screen.get_height():
                bullet_list.remove(bullet)
                print(bullet_list)
        pygame.display.update()

if __name__ == "__main__":
    main()