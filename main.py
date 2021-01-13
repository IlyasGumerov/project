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


class Menu():
    bg_image = load_image('fon1.png')
    bg = load_image('gameover.png')

    def __init__(self):
        self.image = Menu.bg_image
        self.image_end = Menu.bg
        self.image = pygame.transform.scale(self.image, size)
        self.image_end = pygame.transform.scale(self.bg, size)
        self.buttons_sp = []

    # Метод для создания кнопок и отрисовка этих кнопок
    def buttons(self, sc, rect):
        rect_dr = pygame.draw.rect(sc, pygame.Color('red'),
                               rect)
        return rect_dr

    # Метод для паузы
    def pause(self, sc):
        flag = True
        intro_text = ["Меню", "", "",
                      "Продолжить",
                      "",
                      'Главное меню',
                      "",
                      "Выход из игры"]

        sc.blit(self.image, (0, 0))
        font = pygame.font.Font(None, 40)
        text_coord = 50
        # Отрисовка кнопок
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.centerx = 550 // 2
            text_coord += intro_rect.height
            # Если текст кнопки не пустой, то с ней можно будет взаимодействовать
            if line:
                a = self.buttons(screen, intro_rect)
                self.buttons_sp.append(a)
            sc.blit(string_rendered, intro_rect)

        while flag:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
                elif i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    flag = self.click_on_btn_pause(i.pos)
                elif i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_ESCAPE:
                        flag = False
            pygame.display.flip()
            clock.tick(FPS)
        return False

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
x = 550 // 2
y = 470
pygame.key.set_repeat(200, 70)
STEP = 50
FPS = 50
speed = 30
c = 0
bg = load_image('fon.jpg')
bg = pygame.transform.scale(bg, size)
bg_rect = bg.get_rect()
clock = pygame.time.Clock()
running = True
menu = Menu()

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
