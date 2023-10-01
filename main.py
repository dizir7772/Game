import random
import os

from vars import *


label_restart_rect = label_restart.get_rect(
    topleft=(
        WIDTH // 2 - label_restart.get_width() // 2,
        HEIGHT // 2 - label_restart.get_height() // 2 - 25,
    )
)
label_exit = FONT_MENU.render("EXIT", False, COLOR_ORANGE)
label_exit_rect = label_restart.get_rect(
    topleft=(
        WIDTH // 2 - label_exit.get_width() // 2,
        HEIGHT // 2 - label_exit.get_height() // 2 + 65,
    )
)

walk_right_path = "Assets/Enemies/assassin/PNG/Mage/RunRight/"
walk_right = [
    pygame.image.load(walk_right_path + filename)
    for filename in os.listdir(walk_right_path)
]

walk_left_path = "Assets/Enemies/assassin/PNG/Mage/RunLeft/"
walk_left = [
    pygame.image.load(walk_left_path + filename)
    for filename in os.listdir(walk_left_path)
]


ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 2500)


bonus_timer = pygame.USEREVENT + 2
pygame.time.set_timer(bonus_timer, 5500)


health_pic_timer = pygame.USEREVENT + 3
pygame.time.set_timer(health_pic_timer, 25000)


fire_pic_bonus_timer = pygame.USEREVENT + 4
pygame.time.set_timer(fire_pic_bonus_timer, 15000)


while True:
    keys = pygame.key.get_pressed()

    main_display.blit(bg, (0, 0))

    if gameplay:
        player_rect = walk_right[0].get_rect(topleft=(player_x, player_y))

        if ghost_list_in_game:
            if health == 0:
                gameplay = False
            for enemy in ghost_list_in_game:
                main_display.blit(ghost, enemy)
                enemy.x -= 10

                if enemy.x < -10:
                    ghost_list_in_game.pop(ghost_list_in_game.index(enemy))
                if player_rect.colliderect(enemy):
                    ghost_list_in_game.pop(ghost_list_in_game.index(enemy))
                    health -= 1

        if bonus_list_in_game:
            for el in bonus_list_in_game:
                main_display.blit(bonus, el)
                el.y += 10
                if el.y > HEIGHT:
                    bonus_list_in_game.pop(bonus_list_in_game.index(el))
                if player_rect.colliderect(el):
                    bonus_list_in_game.pop(bonus_list_in_game.index(el))
                    score += 150

        if health_pic_list_in_game:
            for el in health_pic_list_in_game:
                main_display.blit(health_pic, el)
                el.y += 10
                if el.y > HEIGHT:
                    health_pic_list_in_game.pop(health_pic_list_in_game.index(el))
                if player_rect.colliderect(el):
                    health_pic_list_in_game.pop(health_pic_list_in_game.index(el))
                    if health < 5:
                        health += 1

        if fire_pic_bonus_list_in_game:
            for el in fire_pic_bonus_list_in_game:
                main_display.blit(fire_pic_bonus, el)
                el.y += 10
                if el.y > HEIGHT:
                    fire_pic_bonus_list_in_game.pop(
                        fire_pic_bonus_list_in_game.index(el)
                    )
                if player_rect.colliderect(el):
                    fire_pic_bonus_list_in_game.pop(
                        fire_pic_bonus_list_in_game.index(el)
                    )
                    if max_fire_pic < 3:
                        max_fire_pic += 1

        if keys[pygame.K_LEFT]:
            main_display.blit(walk_left[player_anim_count], (player_x, player_y))

        elif keys[pygame.K_RIGHT]:
            main_display.blit(walk_right[player_anim_count], (player_x, player_y))

        else:
            main_display.blit(player, (player_x, player_y))
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < WIDTH - 100:
            player_x += player_speed

        if not is_jump:
            if keys[pygame.K_UP]:
                is_jump = True
        else:
            if jump_count >= -10:
                if jump_count > 0:
                    player_y -= (jump_count**2) / 2
                else:
                    player_y += (jump_count**2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 10

        if player_anim_count == 7:
            player_anim_count = 0
        else:
            player_anim_count += 1

        main_display.blit(
            FONT.render("SCORE: " + str(score), True, COLOR_GREEN), (WIDTH - 300, 20)
        )
        main_display.blit(
            FONT.render("HEALTH: " + str(health), True, COLOR_GREEN), (WIDTH - 1450, 20)
        )
        main_display.blit(
            FONT.render("FIRE BULLET: " + str(max_fire_pic), True, COLOR_GREEN),
            (WIDTH // 2 - 125, 20),
        )
        bg_x -= 2
        if bg_x == -WIDTH:
            bg_x = 0

        if fire_pic_list:
            for el in fire_pic_list:
                main_display.blit(fire_pic, (el.x, el.y))
                el.x += 5
                if el.x > WIDTH:
                    fire_pic_list.pop(fire_pic_list.index(el))
                if ghost_list_in_game:
                    for enemy in ghost_list_in_game:
                        if el.colliderect(enemy):
                            fire_pic_list.pop(fire_pic_list.index(el))
                            ghost_list_in_game.pop(ghost_list_in_game.index(enemy))

        FPS.tick(30)
    else:
        main_display.blit(bg_lose, (0, 0))
        main_display.blit(
            label,
            (
                WIDTH // 2 - label.get_width() // 2,
                HEIGHT // 2 - label.get_height() // 2 - 120,
            ),
        )
        main_display.blit(label_restart, label_restart_rect)
        main_display.blit(label_exit, label_exit_rect)
        mixer.music.stop()

        mouse = pygame.mouse.get_pos()
        if label_restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = WIDTH // 2
            health = 5
            max_fire_pic = 3
            ghost_list_in_game.clear()
            bonus_list_in_game.clear()
            fire_pic_list.clear()
            mixer.music.play(-1)
        if label_exit_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            pygame.quit()
            quit()

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == ghost_timer:
            ghost_list_in_game.append(
                ghost.get_rect(topleft=(random.randint(1520, 1680), 685))
            )
        if event.type == bonus_timer:
            bonus_list_in_game.append(
                bonus.get_rect(
                    topleft=(random.randint(WIDTH // 2 - 200, WIDTH // 2 + 200), 0)
                )
            )
        if event.type == health_pic_timer:
            health_pic_list_in_game.append(
                health_pic.get_rect(
                    topleft=(random.randint(WIDTH // 2 - 200, WIDTH // 2 + 200), 0)
                )
            )
        if (
            gameplay
            and event.type == pygame.KEYUP
            and event.key == pygame.K_SPACE
            and max_fire_pic > 0
        ):
            fire_pic_list.append(fire_pic.get_rect(topleft=(player_x + 30, player_y)))
            max_fire_pic -= 1
        if event.type == fire_pic_bonus_timer:
            fire_pic_bonus_list_in_game.append(
                fire_pic_bonus.get_rect(
                    topleft=(random.randint(WIDTH // 2 - 200, WIDTH // 2 + 200), 0)
                )
            )
