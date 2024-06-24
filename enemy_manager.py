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
    def check_for_dead(self):
        for enemy in self.enemies:

            for bullet in self.player.weapon.bullets:
                if bullet.x < enemy.x+15 and bullet.y > enemy.y-15 and bullet.y < enemy.y+15 and bullet.x > enemy.x -15:
                    self.enemies.remove(enemy)
                    self.player.weapon.bullets.remove(bullet)

    def spawn_enemies(self):
        for enemy in self.enemies:
            enemy.draw()
    def move_enemies(self):

        for enemy in self.enemies:
            first_pos = (enemy.x, enemy.y)
            enemy.move()
            #move every enemy that is spawned in

            for enemy2 in self.enemies:
                #for every enemy, go through every other enemy and grab its distnace, if the distance is too small, undo the move.
                if enemy2 is not enemy:
                    distance = math.sqrt((enemy.x - enemy2.x)**2 + (enemy.y - enemy2.y)**2)
                    if distance < 35:
                        enemy.x, enemy.y = first_pos
                        break

        # for enemy in self.enemies:
        #     enemy.move()

    # add a method to check to see if an enemy has been hit, or anything else that would kill a enemy, then remove it from the enemies list . do this once a method has been made in the enemies module to check to see if the enemy should be removed.



