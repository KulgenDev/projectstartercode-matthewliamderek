import enemy_module
import pygame
import math
import gc
import sys
import enemy_bullets_module
import random
import inspect
global titan_health



class enemy_manager:
    def __init__(self, screen, player):
        self.enemies = []
        self.screen = screen
        self.player = player
        self.kills = 0
        self.spawned = 0
        self.hit_player = False
        self.bullets = []
        self.pickups = []
        self.Types = {"Enemy" : enemy_module.Enemy, "Shooter" : enemy_module.Shooter, "Elite" : enemy_module.Elite, "Kamikaze" : enemy_module.Kamikaze, "Titan" : enemy_module.Titan}

    def add_enemy(self):
        if self.kills % 50 == 0 and self.kills != 0:
            type = self.Types["Titan"]
        else:
            chance = random.randint(1, 100)
            type = self.Types["Enemy"]
            match chance:
                case chance if 1 < chance < 40:
                    type = self.Types["Enemy"]
                case chance if 41 < chance < 64:
                    type = self.Types["Kamikaze"]
                case chance if 65 < chance < 85:
                    type = self.Types["Shooter"]
                case chance if 86 < chance < 100:
                    type = self.Types["Elite"]

        self.enemies.append(type(self.screen, self.player, self))
        self.spawned += 1

        return
    def shoot(self, screen, x, y, width, height, color, angle):
        self.bullets.append(enemy_bullets_module.EnemyBullet(screen, x, y, width, height, color, angle))

    def checkBulletOffScreenAndMove(self):
        for bullet in self.bullets:
            bullet.move()
            bullet.draw()
            if bullet.off_screen():
                self.bullets.remove(bullet)

    def check_for_dead(self):
        for enemy in self.enemies:

            for bullet in self.player.weapon.bullets:
                if (bullet.x < enemy.x+15 and bullet.y > enemy.y-15 and bullet.y < enemy.y+15 and bullet.x > enemy.x -15) or (bullet.y+4 < enemy.y + 15 and bullet.y+4 > enemy.y-15 and bullet.x <enemy.x+15 and bullet.x>enemy.x-15) or (bullet.x+4 > enemy.x-15 and bullet.x+4 < enemy.x+15 and bullet.y > enemy.y-15 and bullet.y < enemy.y+15) or (bullet.x+4 > enemy.x-15 and bullet.x+4 < enemy.x+15 and bullet.y+4 > enemy.y-15 and bullet.y-4 < enemy.y+15):
                    if isinstance(enemy, enemy_module.Kamikaze):
                        enemy.stopSound()
                        explosion_sound = pygame.mixer.Sound("sfx/explosion.wav")
                        explosion_sound.set_volume(1)
                        explosion_sound.play()
                    if isinstance(enemy, enemy_module.Titan):
                        self.player.weapon.bullets.remove(bullet)
                        enemy.titan_health += 1
                        if enemy.titan_health == 10:
                            try:
                                enemy.titan_health = 0
                                self.enemies.remove(enemy)
                                self.kills += 1
                                gc.collect()
                            except:
                                pass
                    else:
                        chance = random.randint(1, 100)
                        if (isinstance(enemy, enemy_module.Shooter) or isinstance(enemy, enemy_module.Kamikaze)) and not type(enemy) == enemy_module.Elite:
                            if chance >= 95:
                                self.player.weapon.addPickup(enemy.x, enemy.y, "Fast Bullet")
                        elif isinstance(enemy, enemy_module.Elite):
                            if chance >= 85:
                                self.player.weapon.addPickup(enemy.x, enemy.y, "Shotgun")
                        try:
                            self.enemies.remove(enemy)
                        except:
                            pass
                        self.player.weapon.bullets.remove(bullet)
                        self.kills += 1
                        gc.collect()

                   # print(len(self.enemies))
                   # print(len(self.player.weapon.bullets))

    def spawn_enemies(self):
        for enemy in self.enemies:
            enemy.draw()


    def check_hit_player(self):
        for bullet in self.bullets:
            if bullet.hitPlayer(self.player):
                self.hit_player = True
                pygame.mixer.music.unload()
                pygame.mixer.music.load("sfx/total_distortion_you_are_dead.mp3")
                pygame.mixer.music.play()
        for enemy in self.enemies:
            if (self.player.x < enemy.x+15 and self.player.y > enemy.y-15 and self.player.y < enemy.y+15 and self.player.x > enemy.x -15) or (self.player.y+20 < enemy.y + 15 and self.player.y+20 > enemy.y-15 and self.player.x <enemy.x+15 and self.player.x>enemy.x-15) or (self.player.x+20 > enemy.x-15 and self.player.x+20 < enemy.x+15 and self.player.y > enemy.y-15 and self.player.y < enemy.y+15) or (self.player.x+20 > enemy.x-15 and self.player.x+20 < enemy.x+15 and self.player.y+20 > enemy.y-15 and self.player.y-20 < enemy.y+15):
                self.hit_player = True
                if isinstance(enemy, enemy_module.Kamikaze):
                    enemy.stopSound()
                    explosion_sound = pygame.mixer.Sound("sfx/explosion.wav")
                    explosion_sound.set_volume(1)
                    explosion_sound.play()
                pygame.mixer.music.unload()
                pygame.mixer.music.load("sfx/total_distortion_you_are_dead.mp3")
                pygame.mixer.music.play()


                #sys.exit()  ## COMMENT THIS LINE OUT IF YOU DONT WANT TO DIE
        return self.hit_player
                #print(hit_player)
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



