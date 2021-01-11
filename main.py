import os
import random
import sys

import pygame

size = width, height = 550, 550
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color("white"))
HIT = 3
SCKORE = 0

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)

    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["       Лови фрукты",
                  "       Правила игры",
                  "Нужно ловить падающие фрукты",
                  "Падение ускоряется",
                  "3 ошибки - проигрыш"]

    fon = pygame.transform.scale(load_image('fon1.png'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 45)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 2, pygame.Color('red'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


class Box(pygame.sprite.Sprite):
    image = load_image("kor.png")
    image = pygame.transform.scale(image, (135, 100))

    def __init__(self, group):
        super().__init__(group)
        self.image = Box.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect = self.image.get_rect().move(x, y)


class Fruit(pygame.sprite.Sprite):
    image = load_image("fruit.png")
    image = pygame.transform.scale(image, (25, 25))

    def __init__(self, group):
        super().__init__(group)

        self.image = Fruit.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1, 500)
        self.rect.y = 0
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        global HIT
        global SCKORE
        global speed
        self.rect.y += 7
        if pygame.sprite.spritecollideany(self, all_sprites):
            self.kill()
            SCKORE += 10


        if self.rect.y >= 550:
            HIT -= 1
            self.kill()
        # if HIT <= 0:
        #     terminate()


all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()

pygame.init()
x = 0
y = 470
pygame.key.set_repeat(200, 70)
STEP = 50
FPS = 50
speed = 45
c = 0

clock = pygame.time.Clock()
running = True
start_screen()
while running:

    screen.fill(pygame.Color("white"))
    c += 1
    all_sprites.draw(screen)
    tiles_group.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 0:
            x -= 30
        if keys[pygame.K_RIGHT] and x < 550 - 135:
            x += 30

    box = Box(all_sprites)
    if c % speed == 0:
        fruit = Fruit(tiles_group)

    f1 = pygame.font.Font(None, 48)
    text1 = f1.render('Жизней - ' + str(HIT), True,
                      (200, 0, 90))
    screen.blit(text1, (350, 0))
    f2 = pygame.font.Font(None, 48)
    text2 = f2.render('Счет - ' + str(SCKORE), True,
                      (0, 150, 30))
    screen.blit(text2, (350, 50))
    print(speed)

    tiles_group.update()
    all_sprites.update()

    pygame.display.flip()
    clock.tick(FPS)

terminate()
