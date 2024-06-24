import bullets_module
import pygame

class EnemyBullet(bullets_module.Bullet):
    def __init__(self, screen, x, y, width, height, color, angle):
        super().__init__(screen, x, y, width, height, color, angle)

    def hitPlayer(self, player):
        bulletRect = pygame.Rect(self.x,
                                 self.y,
                                 4,
                                 4)
        return pygame.Rect.colliderect(bulletRect, player.hitbox)