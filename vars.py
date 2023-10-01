import pygame
from pygame import mixer

pygame.init()
mixer.init()

WIDTH = 1500
HEIGHT = 800
FPS = pygame.time.Clock()
COLOR_GREEN = (38, 46, 36)
COLOR_ORANGE = (84, 63, 40)
mixer.music.load("Assets/Sounds/song.mp3")
mixer.music.set_volume(0.2)
mixer.music.play(-1)
FONT = pygame.font.Font("Assets/Font/smallburg_Italic.ttf", 45)
FONT_MENU = pygame.font.Font("Assets/Font/smallburg_Italic.ttf", 35)
bg = pygame.transform.scale(
    pygame.image.load("Assets/Background/bg.jpg"), (WIDTH, HEIGHT)
)
bg_lose = pygame.transform.scale(
    pygame.image.load("Assets/Background/bg_lose.jpg"), (WIDTH, HEIGHT)
)
icon = pygame.image.load("Assets/Icon/icon.jpg")
caption = "Heroes"
main_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(caption)
pygame.display.set_icon(icon)
player = pygame.image.load("Assets/Enemies/assassin/PNG/Mage/mage_stay.png")
label = FONT_MENU.render("YOU LOSE!", False, COLOR_ORANGE)
label_restart = FONT_MENU.render("RESTART", False, COLOR_ORANGE)

fire_pic = pygame.image.load("Assets/Enemies/fire1.png")
fire_pic_list = []
max_fire_pic = 3
image_index = 0
score = 0
health = 5
player_anim_count = 0
bg_x = 0
player_speed = 5
player_x = WIDTH // 2
player_y = 680
is_jump = False
jump_count = 10
gameplay = True
ghost = pygame.transform.scale(pygame.image.load("Assets/Enemies/ghost.png"), (30, 30))
ghost_list_in_game = []
bonus = pygame.transform.scale(
    pygame.image.load("Assets/Enemies/Coins_00.png"), (30, 30)
)
bonus_list_in_game = []
health_pic = pygame.transform.scale(
    pygame.image.load("Assets/Enemies/Red_Potion.png"), (30, 30)
)
health_pic_list_in_game = []
fire_pic_bonus = pygame.transform.scale(
    pygame.image.load("Assets/Enemies/Blue_Potion.png"), (30, 30)
)
fire_pic_bonus_list_in_game = []
