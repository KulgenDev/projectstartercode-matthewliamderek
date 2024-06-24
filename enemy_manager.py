import enemy_module
import pygame
import math

class enemy_manager:
    def __init__(self, screen, player):
        self.enemies = []
        self.screen = screen
        self.player = player
    def add_enemy(self):
        self.enemies.append(enemy_module.Enemy(self.screen, self.player))
        return
    def spawn_enemies(self):
        for enemy in self.enemies:
            enemy.draw()
    def move_enemies(self):
        # if len(self.enemies) == 1:
        #     self.enemies[0].move()
        # else:
        #     for enemy in self.enemies:
        #         for enemy2 in self.enemies:
        #             if enemy2.x == enemy.x and enemy2.y == enemy.y:
        #                 continue
        #             distance = math.sqrt((enemy.x - enemy2.x)**2 + (enemy.y - enemy2.y)**2)
        #             if distance > 35:
        for enemy in self.enemies:
            enemy.move()

    # add a method to check to see if an enemy has been hit, or anything else that would kill a enemy, then remove it from the enemies list . do this once a method has been made in the enemies module to check to see if the enemy should be removed.



