#Sprite Classes
from Constants import *
import pygame as pg

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
    def __init__(self, xy_pos):
        pg.sprite.Sprite.__init__(self)
        self.xy_pos = xy_pos
        self.image = pg.Surface((2,10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
