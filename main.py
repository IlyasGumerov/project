import pygame
import os, sys

size = width, height = 550, 550
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color("white"))


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
    image = load_image("platform.png")
    image = pygame.transform.scale(image, (200, 120))
    def __init__(self, group):
        super().__init__(group)
        self.image = Box.image
        self.rect = self.image.get_rect()

    def update(self):
        self.rect = self.image.get_rect().move(x, y)


player = None

# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

pygame.init()
x = 0
y = 450
pygame.key.set_repeat(200, 70)
STEP = 50
FPS = 50

clock = pygame.time.Clock()
running = True
start_screen()
while running:

    screen.fill(pygame.Color("white"))

    all_sprites.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > -45:
            x -= 15
        if keys[pygame.K_RIGHT] and x < 550 - 175:
            x += 15
    box = Box(all_sprites)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(FPS)

terminate()
