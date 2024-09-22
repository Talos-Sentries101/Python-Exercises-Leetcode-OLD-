import pygame
from sys import exit
# For range of enemy swap
from random import randint


def display_score():
    time = int(pygame.time.get_ticks() / 1000) - initial_time
    score_surface = font.render(f'Score: {time}', True, (127, 225, 0), None)
    rect_score = score_surface.get_rect(center=(600, 150))
    screen.blit(score_surface, rect_score)


def enemy_movement(enemy_list):
    if enemy_list:
        rect: object
        for rect in enemy_list:
            rect.x -= 5
            screen.blit(surface_enemy, rect)
        enemy_list = [enemy for enemy in enemy_list if enemy.x > -100]
        return enemy_list
    # Safeguard against the initial empty list when starting the program
    else:
        return []


def collision(player, enemy):
    if enemy:
        for rect in enemy:
            if player.colliderect(rect):
                return False

    return True


def player_animation():
    global player_walk_index, surface_player, player_jump_index
    if rect_player.bottom < 610:
        surface_player = player_jump_
    else:
        player_walk_index += 0.1
        if player_walk_index >= len(player_walk_list):
            player_walk_index = 0
        surface_player = player_walk_list[int(player_walk_index)]


pygame.init()
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption('Gold Chase ')
frames = pygame.time.Clock()
# Ground
surface_ground = pygame.image.load('GoldChase/sprites/background/Ground1.jpg').convert_alpha()
surface_ground = pygame.transform.smoothscale(surface_ground, (1200, 90))
# Sky
surface_sky = pygame.image.load('GoldChase/sprites/background/Sky1.png')
surface_sky = pygame.transform.smoothscale(surface_sky, (1200, 610)).convert_alpha()
# Enemy
surface_enemy = pygame.image.load('GoldChase/sprites/enemy.jpg')
surface_enemy = pygame.transform.scale(surface_enemy, (200, 210))
rect_enemy = surface_enemy.get_rect(topleft=(600, 530))
# creating empty list for enemy rectangles
enemy_list = []

# PLayer
# surface_player = pygame.transform.smoothscale(surface_player, (90, 140))
surface_player_walk_1 = pygame.transform.smoothscale(
    pygame.image.load('GoldChase/sprites/player/player_walk1.png').convert_alpha(), (110, 140))
surface_player_walk_2 = pygame.transform.smoothscale(
    pygame.image.load('GoldChase/sprites/player/player_walk2.png').convert_alpha(), (110, 140))
surface_player_walk_3 = pygame.transform.smoothscale(
    pygame.image.load('GoldChase/sprites/player/player_walk3.png').convert_alpha(), (110, 140))
surface_player_walk_4 = pygame.transform.smoothscale(
    pygame.image.load('GoldChase/sprites/player/player_walk4.png').convert_alpha(), (110, 140))
surface_player_walk_5 = pygame.transform.smoothscale(
    pygame.image.load('GoldChase/sprites/player/player_walk5.png').convert_alpha(), (110, 140))
surface_player_walk_6 = pygame.transform.smoothscale(
    pygame.image.load('GoldChase/sprites/player/player_walk6.png').convert_alpha(), (110, 140))
surface_player_walk_7 = pygame.transform.smoothscale(
    pygame.image.load('GoldChase/sprites/player/player_walk7.png').convert_alpha(), (110, 140))
surface_player_walk_8 = pygame.transform.smoothscale(
    pygame.image.load('GoldChase/sprites/player/player_walk8.png').convert_alpha(), (110, 140))
player_walk_list = [surface_player_walk_1, surface_player_walk_2, surface_player_walk_3, surface_player_walk_4,
                    surface_player_walk_5, surface_player_walk_6, surface_player_walk_7, surface_player_walk_8, ]
player_walk_index = 0
player_jump_ = pygame.transform.smoothscale(
    pygame.image.load('GoldChase/sprites/player/player_jump.png').convert_alpha(), (100, 140))

# player_jump_2 = pygame.image.load('GoldChase/sprites/player/player_jump2.jpg').convert_alpha()
# player_jump_3 = pygame.image.load('GoldChase/sprites/player/player_jump_fall1.jpg').convert_alpha()
# player_jump_4 = pygame.image.load('GoldChase/sprites/player/player_jump_fall2.jpg').convert_alpha()
# player_jump_list = [player_jump_1, player_jump_2, player_jump_3, player_jump_4]
# player_jump_index = 0
surface_player = player_walk_list[player_walk_index]
rect_player = surface_player.get_rect(topleft=(50, 490))
game_state = False
gravity = 0
initial_time = 0
# Font
font = pygame.font.Font('GoldChase/Font/font.ttf', 50)
# timer
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 1400)
# Title/Game Over screen
title_player = pygame.transform.smoothscale(
    pygame.image.load('GoldChase/sprites/player/titlepostor.jpg').convert_alpha(), (200, 260))
title_player_rect = title_player.get_rect(center=(600, 350))
title_Game = font.render('Robot Frenzy', True, (127, 225, 0))
title_Game_rect = title_Game.get_rect(center=(600, 100))
while True:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and rect_player.bottom == 610:
                gravity = -9.8
        # To check within Event loop
        if event.type == pygame.MOUSEBUTTONDOWN and rect_player.bottom == 610:
            gravity = -9.8
        if event.type == pygame.KEYDOWN and game_state is False:
            if event.key == pygame.K_r:
                game_state = True
                rect_enemy.right = 900
                initial_time = int(pygame.time.get_ticks() / 1000)
        if event.type == enemy_timer and game_state is True:
            enemy_list.append(surface_enemy.get_rect(topleft=(randint(1100, 1200), 460)))

    if game_state is True:
        # Importing all surfaces
        screen.blit(surface_ground, (0, 609))
        screen.blit(surface_sky, (0, 0))
        player_animation()
        screen.blit(surface_player, rect_player)
        # Creating player gravity
        gravity += 0.2
        rect_player.y += gravity
        if rect_player.bottom >= 610:
            rect_player.bottom = 610
        display_score()
        # Enemy Mechanics
        enemy_list = enemy_movement(enemy_list)
        # Collision
        game_state = collision(rect_player, enemy_list)
    else:
        screen.fill((255, 64, 64))
        screen.blit(title_player, title_player_rect)
        screen.blit(title_Game, title_Game_rect)
        enemy_list = []

    pygame.display.update()
    frames.tick(80)

# To check outside evnet loop  # if rect_player.collide rect(rect_enemy) is not True:
#   pass
# else:
#   rect_enemy.right -=78##
