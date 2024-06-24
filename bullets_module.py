import pygame
import sys
import math

#https://www.youtube.com/watch?v=_VWQWIWQuOg&list=PLpUXyegQw-SFWpeg9q6XgarxtQVdnaoMM&index=4

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

    def move(self):
        self.x += 7 * math.cos(self.angle)
        self.y += 7 * math.sin(self.angle)
        points = []
        center_x = self.x + (self.width / 2)
        center_y = self.y + (self.height / 2)
        radius = math.sqrt((self.height / 2) ** 2 + (self.width / 2) ** 2)
        specific_angle = math.atan2(self.height / 2, self.width / 2)
        specific_angles = [specific_angle, -specific_angle + math.pi, specific_angle + math.pi, -specific_angle]
        specific_radians = (math.pi / 180) * self.angle
        for part in specific_angles:
            y_offset = -1 * radius * math.sin(part + specific_radians)
            x_offset = radius * math.cos(part + specific_radians)
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
        if self.x > self.screen.get_width():
            return True
        else:
            return False

    def play_bullet_sound(self):
        bullet_sound = pygame.mixer.Sound("sfx/jasbro_laser.wav")
        # sound created by jobro on fressound
        bullet_sound.play(0)


bullet_list = []

def main():
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(pygame.Color("Black"))
        for bullet in bullet_list:
            bullet.draw()
            bullet.move()
            if bullet.x < 0:
                bullet_list.remove(bullet)
            if bullet.x > screen.get_width():
                bullet_list.remove(bullet)
            if bullet.y < 0:
                bullet_list.remove(bullet)
            if bullet.y > screen.get_height():
                bullet_list.remove(bullet)
        pygame.display.update()


if __name__ == "__main__":
    main()
