import os
import random
import sys

import pygame

pygame.init()
size = width, height = 550, 550
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color("white"))
HIT = 3
SCKORE = 0
pygame.mixer.music.load('data/muzlo.wav')
pygame.mixer.music.play(-1)


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
    fon_image = load_image('fon1.png')
    game_over_image = load_image('gameover.png')

    def __init__(self):
        self.image = Menu.fon_image
        self.game_over_image = Menu.game_over_image
        self.knopka_sp = []
        self.image = pygame.transform.scale(self.image, size)
        self.game_over_image = pygame.transform.scale(self.game_over_image, size)

    # Метод для создания кнопок и отрисовка этих кнопок
    def knopka(self, sc, rect):
        rect_dr = pygame.draw.rect(sc, pygame.Color('red'),
                                   rect)
        return rect_dr

    # Метод для паузы
    def pause_game(self, screen):
        cheking = True
        intro_text = ["Меню", "", "",
                      "Продолжить",
                      "",
                      'Главное меню',
                      "",
                      "Выход из игры"]

        screen.blit(self.image, (0, 0))
        font = pygame.font.Font(None, 40)
        coordin_text = 50
        # Отрисовка кнопок
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            coordin_text += 10
            intro_rect.top = coordin_text
            intro_rect.centerx = 550 // 2
            coordin_text += intro_rect.height
            # Если текст кнопки не пустой, то с ней можно будет взаимодействовать
            if line:
                a = self.knopka(screen, intro_rect)
                self.knopka_sp.append(a)
            screen.blit(string_rendered, intro_rect)

        while cheking:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
                elif i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    cheking = self.click_pause(i.pos)
                elif i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_ESCAPE:
                        cheking = False
            pygame.display.flip()
            clock.tick(FPS)
        return False

    def game_over_screen(self, screen):
        pygame.mouse.set_visible(True)
        cheking = True
        intro_text = ['', 'Главное Меню', '', '', f'Счет - {SCKORE}', '', '', '', 'Выход из игры']
        screen.blit(self.game_over_image, (0, 0))
        font = pygame.font.Font(None, 40)
        coordin_text = 50

        # Отрисовка кнопок
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            coordin_text += 10
            intro_rect.top = coordin_text
            intro_rect.centerx = 550 // 2
            coordin_text += intro_rect.height
            # Если текст кнопки не пустой, то с ней можно будет взаимодействовать
            if line:
                a = self.knopka(screen, intro_rect)
                self.knopka_sp.append(a)
            screen.blit(string_rendered, intro_rect)

        while cheking:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    cheking = self.click_on_btn_end(event.pos)
            pygame.display.flip()
            clock.tick(FPS)
        return False

    def main_menu(self, screen):
        # Player().new_game()

        cheking = True
        intro_text = ["Правила игры", "", "", "",
                      "Начать игру",
                      "", '', '',
                      "Выход из игры"]

        screen.blit(self.image, (0, 0))
        font = pygame.font.Font(None, 40)
        coordin_text = 50
        # Отрисовка кнопок
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            coordin_text += 10
            intro_rect.top = coordin_text
            intro_rect.centerx = 550 // 2
            coordin_text += intro_rect.height
            # Если текст кнопки не пустой, то с ней можно будет взаимодействовать
            if line:
                new_btn = self.knopka(screen, intro_rect)
                self.knopka_sp.append(new_btn)
            screen.blit(string_rendered, intro_rect)

        while cheking:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
                elif i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    cheking = self.click_btn_menu(i.pos)
                elif i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_ESCAPE:
                        cheking = False
            pygame.display.flip()
            clock.tick(FPS)
        return False

    def reaction_but(self, pos):
        for btn in self.knopka_sp:
            if btn.collidepoint(pos):
                return self.knopka_sp.index(btn) + 1
        return 0

    def click_pause(self, pos):
        click_cheking = self.reaction_but(pos)
        if not click_cheking or click_cheking == 4:
            return True
        else:
            if click_cheking == 5:
                return False
            elif click_cheking == 6:
                self.main_menu(screen)

                return
            elif click_cheking == 7:
                sys.exit()

    # Метод для рекции на нажатие кнопок в режиме меню
    def click_btn_menu(self, pos):
        click_cheking = self.reaction_but(pos)
        if not click_cheking:
            return True
        else:
            if click_cheking == 1:
                self.show_rules(screen)
                return
            elif click_cheking == 2:
                pygame.mouse.set_visible(False)
                return False
            elif click_cheking == 3:
                sys.exit()

    # Отрисовываем правила игры
    def show_rules(self, screen):
        cheking = True
        intro_text = ["Вы отправились на ферму фруктов.",
                      "",
                      "Фрукты очень хрупкие",
                      "и очень дорогие.",
                      "Вам надо их собрать.",
                      "",
                      "Нельзя допустить попадания их на землю.",
                      '',
                      "Желаем вам удачи и хорошей игры!",
                      '',
                      'Управление корзиной - стрелки.']

        screen.blit(self.image, (0, 0))
        font = pygame.font.Font(None, 30)
        coordin_text = 50
        # Отрисовка кнопок
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            coordin_text += 10
            intro_rect.top = coordin_text
            intro_rect.centerx = 550 // 2
            coordin_text += intro_rect.height
            # Если текст кнопки не пустой, то с ней можно будет взаимодействовать
            if line:
                a = self.knopka(screen, intro_rect)
                self.knopka_sp.append(a)
            screen.blit(string_rendered, intro_rect)

        while cheking:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
                elif i.type == pygame.MOUSEBUTTONDOWN:
                    self.main_menu(screen)
                    return
            pygame.display.flip()
            clock.tick(FPS)
        return False

    def click_on_btn_end(self, pos):
        click_cheking = self.reaction_but(pos)
        if not click_cheking:
            return True
        else:
            if click_cheking == 4:
                self.main_menu(screen)
                return False
            elif click_cheking == 3:
                sys.exit()


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
            if SCKORE % 100 == 0:
                if speed != 5:
                    speed -= 5
                else:
                    speed = 1

        if self.rect.y >= 550:
            HIT -= 1
            self.kill()


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
fon_game = load_image('fon.jpg')
fon_game = pygame.transform.scale(fon_game, size)
fon_game_rect = fon_game.get_rect()
clock = pygame.time.Clock()
running = True
menu = Menu()
menu.main_menu(screen)
pause_game = False
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if pause_game:
                    pause_game = False
                else:
                    pause_game = True
                    pygame.mouse.set_visible(True)

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
    if HIT <= 0:
        menu.game_over_screen(screen)
    if pause_game:
        pause_game = menu.pause_game(screen)
        pygame.mouse.set_visible(False)

    tiles_group.update()
    all_sprites.update()

    pygame.display.flip()
    clock.tick(FPS)

terminate()
