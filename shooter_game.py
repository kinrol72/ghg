from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 595:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > height: 
            self.rect.x = randint(80, width - 80)
            self.rect.y = 0
            lost += 1
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()
font.init()
font1 = font.SysFont('Arial', 80)
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
font2 = font.SysFont('Arial', 36)
score = 0
lost = 0
width = 700
height = 500
clock = time.Clock()
window = display.set_mode((700, 500))
FPS = 60
mixer.init()
ship = Player('rocket.png', 5, height - 100, 80, 100, 10)
monsters = sprite.Group()
bullets = sprite.Group()
abobusi = sprite.Group()
for i in range(1,6):
    monster = Enemy('ufo.png', randint(80, width - 80), -40, 80, 50, randint(1,5))
    monsters.add(monster)
for i in range(1,3):
    abobus = Enemy('asteroid.png', randint(80, width - 80), -40, 80, 50, randint(1,5))
    abobusi.add(abobus)
background = transform.scale(image.load('galaxy.jpg'), (700, 500))
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')
fin = False
run = True
while run:
    window.blit(background, (0,0))
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                ship.fire()
    if not fin:
        window.blit(background, (0,0))
        text = font2.render("Счёт" + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))
        text_lose = font2.render("Пропущено" + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))
        ship.update()
        abobusi.update()
        monsters.update()
        bullets.update()
        ship.reset()
        abobusi.draw(window)
        monsters.draw(window)
        bullets.draw(window)
        listik = sprite.groupcollide(monsters, bullets, True, True)
        for c in listik:
            score += 1
            monster = Enemy('ufo.png', randint(80, 620), -40, 80, 50, randint(1,5))
            monsters.add(monster)
        if sprite.spritecollide(ship, monsters, False) or lost >= 7:
            fin = True
            window.blit(lose, (200, 200))
        if sprite.spritecollide(ship, abobusi, False):
            fin = True
            window.blit(lose, (200, 200))
        if score >= 10:
            fin = True
            window.blit(win, (200, 200))
    else:
        fin = False
        score = 0
        lost = 0
        for b in bullets:
            b.kill()
        for j in abobusi:
            j.kill()
        for m in monsters:
            m.kill()
        time.delay(3000)
        for i in range(1,6):
            monster = Enemy('ufo.png', randint(80, width - 80), -40, 80, 50, randint(1,5))
            monsters.add(monster)
        for i in range(1,3):
            abobus = Enemy('asteroid.png', randint(80, width - 80), -40, 80, 50, randint(1,5))
            abobusi.add(abobus)
    display.update()
    clock.tick(FPS)
# class Enemy(GameSprite):
#     def update(self):
#         if self.rect.x <= 470:
#             self.direction = 'right'
#         if self.rect.x >= 615:
#             self.direction = 'left'
        
#         if self.direction == 'left':
#             self.rect.x -= self.speed
#         else:
#             self.rect.x += self.speed
# class Wall(sprite.Sprite):
#     def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width):
#         super().__init__()
#         self.color_1 = color_1
#         self.width = wall_width
#         self.image = Surface((self.width, self.height))
#         self.image.fill((color_1, color_2, color_3))
#         self.rect = self.image.get_rect()
#         self.rect.x = wall_x
#         self.rect.y = wall_y
#     def draw_wall(self):
#         window.blit(self.image, (self.rect.x, self.rect.y))
# wall_height = 700
# wall_width = 500
# window = display.set_mode((700, 500))
# background = transform.scale(image.load('background.jpg'), (700, 500))
# clock = time.Clock()
# FPS = 60
# font.init()
# font = font.Font(None, 70)
# win = font.render('YOU WIN!', True, (255, 215, 0))
# lose = font.render('YOU LOSE!', True,(180, 0, 0))
# mixer.init()
# mixer.music.load('jungles.ogg')
# jungles = mixer.music.play()
# money = mixer.Sound('money.ogg')
# kick = mixer.Sound('kick.ogg')
# wall_1 = Wall(238, 123, 123, 39, 123, 234)
# hero = Player('hero.png', 5, 80, 4)
# cyborg = GameSprite('cyborg.png', 620, 280, 2)
# treasure = GameSprite('treasure.png', 120, 80, 0)
# run = True
# fin = False
# while run:
#     window.blit(background, (0,0))

#     for e in event.get():
#         if e.type == QUIT:
#             run = False

#     if finish != True:
#         if sprite.collide.rect(player, monster) or sprite.collide.rect(player, wall_1):
#             fin = True
#             kick.play()
#     hero.update()
#     hero.reset()
#     cyborg.update()
#     cyborg.reset()
#     treasure.reset()
#     display.update()
#     clock.tick(FPS)
