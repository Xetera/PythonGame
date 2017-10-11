import pygame as pg
from Constants import *
from Sprites import *

class Movement:
    lead_x = 300
    lead_y = 300


class Game:
    def __init__(self):
        self.running = True
        pg.init()
        pg.mixer.init()
        self.gameDisplay = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.pressed = pg.key.get_pressed()

    def new(self):
        #start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.all_bullets = pg.sprite.Group()
        self.player = Player(self, 15,40)
        self.all_sprites.add(self.player)

        #adding platforms
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            #print("1")
            self.events()
            #print("2")
            self.update()
            #print("3")
            self.draw()
            #print("41")

    def update(self):
        self.all_sprites.update()
        #check if palyer hits a latform only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                #if self.player.pos + (0, self.player.object_height/2 +1)  == hits[0].rect.top:
                self.player.vel.y = 0

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
            if event.type == pg.MOUSEBUTTONDOWN:
                xy_pos = event.pos
                self.bullet = Bullet(xy_pos)
                self.all_sprites.add(self.bullet)
                self.all_bullets.add(self.bullet)



    def draw(self):
        self.gameDisplay.fill(BLACK)
        pg.draw.rect(self.gameDisplay, BLACK, [Movement.lead_x, Movement.lead_y, 10, 10])
        self.all_sprites.draw(self.gameDisplay)
        pg.display.update()

    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()