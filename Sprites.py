#Sprite Classes

from Constants import *
import pygame as pg
import math

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game, objectWidth, objectHeight):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.object_height = objectHeight
        self.object_width = objectWidth
        self.image = pg.Surface((objectWidth,objectHeight))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        #jump only if standing on platform
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x += 1
        if hits:
            self.vel.y = -20
    def update(self):
        self.acc = vec(0, PLAYER_GRAVITY)
        keys = pg.key.get_pressed()
        if keys [pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_d]:
            self.acc.x = PLAYER_ACC
        if keys[pg.K_w]:
            self.acc.y = -PLAYER_ACC
        if keys[pg.K_s]:
            self.acc.y = PLAYER_ACC


        #applying friction to prevent running forever
        self.acc.x += self.vel.x * PLAYER_FRICTION
        #calculating motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        #setting boundaries
        if self.pos.x > WIDTH-(self.object_width/2):
            self.pos.x = WIDTH-(self.object_width/2)
        if self.pos.x <0+self.object_width/2:
            self.pos.x = 0+self.object_width/2
        if self.pos.y > HEIGHT:
            self.pos.y = HEIGHT
        if self.pos.y < 0 + self.object_height :
            self.pos.y = 0 + self.object_height
            self.vel.y = 0

        self.rect.midbottom = self.pos

class Platform(pg.sprite.Sprite):
    def __init__(self,x ,y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Bullet(pg.sprite.Sprite):
    def __init__(self, xy_pos, player_x, player_y,object_height):
        pg.sprite.Sprite.__init__(self)
        self.starting_x = player_x
        self.starting_y = player_y
        self.xy_pos = xy_pos
        self.image = pg.Surface((10,10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = self.starting_x
        self.rect.y = self.starting_y-object_height

        #self.rect.x = player_x
        #self.rect.y = player_y-object_height
        self.orig = self.rect.y
        self.x_increment = 0
        self.change_x = 0
        self.change_y = 0
        #finding out the distance



    def update(self):
        self.slope = (self.xy_pos[1]-self.starting_y)/(self.xy_pos[0]-self.starting_x)
        if self.xy_pos[0] > self.starting_x:
            self.rect.x += self.x_increment
            self.rect.y += self.slope * self.x_increment
        else:
            self.rect.x -= self.x_increment
            self.rect.y += self.slope * -self.x_increment
        self.x_increment += 1
        if self.rect.x > WIDTH or self.rect.y < 0:
            self.rect.x,self.rect.y = 0,0



        """
            bullet_vec = vec(self.xy_pos[0]-self.starting_x, self.xy_pos[1] - self.starting_y)
            self.distance = math.sqrt(((bullet_vec[0]) ** 2 + (bullet_vec[1]) ** 2))
            bullet_vec_x = (bullet_vec[0]/ self.distance)
            bullet_vec_y = (bullet_vec[1]/self.distance)
            self.change_x += bullet_vec_x
            self.change_y += bullet_vec_y
            #print(bullet_vec_x, bullet_vec_y)

            self.starting_x += self.change_x
            self.starting_y += self.change_y
            self.rect.x = self.starting_x
            self.rect.y = self.starting_y
        """


