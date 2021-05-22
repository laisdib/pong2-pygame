import pygame
import random

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
MAX_SPEED = 9.50
SCORE_MAX = 2


r = [-1, 1]
ang = [3, 5, 7, 9, 10]
count_speed = 1


size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MyPong - PyGame Edition - 2021.01.30")

# score text
score_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
score_text = score_font.render('0 x 0', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (512, 50)

# victory text
victory_font = pygame.font.Font('assets/PressStart2P.ttf', 100)
victory_text = victory_font .render('VICTORY', True, COLOR_WHITE, COLOR_BLACK)
victory_text_rect = score_text.get_rect()
victory_text_rect.center = (450, 350)

# sound effects
bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('assets/258020__kodack__arcade-bleep-sound.wav')

# player 1
player_1 = pygame.image.load("assets/player.png")
player_1_y = 300
player_1_move_up = False
player_1_move_down = False

# player 2 - robot
player_2 = pygame.image.load("assets/player.png")
player_2_y = 300

# ball
ball = pygame.image.load("assets/ball.png")
ball_x = 640
ball_y = 360
ball_dx = 5
ball_dy = 5

# score
score_1 = 0
score_2 = 0

# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        #  keystroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_1_move_up = True
            if event.key == pygame.K_DOWN:
                player_1_move_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_1_move_up = False
            if event.key == pygame.K_DOWN:
                player_1_move_down = False

    # checking the victory condition
    if score_1 < SCORE_MAX and score_2 < SCORE_MAX:

        # clear screen
        screen.fill(COLOR_BLACK)

        # ball collision with the wall
        if ball_y > 700:
            ball_dy *= -1
            bounce_sound_effect.play()
        elif ball_y <= 0:
            ball_dy *= -1
            bounce_sound_effect.play()

        # ball collision with the player 1 's paddle
        # Mudança de Velocidade e Angulação, Bug Colisão
        if 90 < ball_x < 100:
            if player_1_y < ball_y + 25:
                if player_1_y + 150 > ball_y:

                    aux = random.randint(0, 1)
                    aux_ang = random.randint(0, 4)

                    if player_1_y < ball_y + 25 < player_1_y + 50 or player_1_y + 100 < ball_y + 25 < player_1_y + 175:
                        if ball_dx > -MAX_SPEED:
                            print(ball_dx)
                            ball_dx *= -1.05
                            ball_dy = ang[aux_ang]
                            ball_dy *= r[aux]
                            count_speed += 1
                            print("Velocidade: %d" % count_speed)

                        else:
                            ball_dx *= -1
                            ball_dy = ang[aux_ang]
                            ball_dy *= r[aux]

                        bounce_sound_effect.play()

                    else:
                        if ball_dx > -MAX_SPEED:
                            print(ball_dx)
                            ball_dx *= -1.25
                            ball_dy = 0
                            count_speed += 1
                            print("Velocidade: %d" % count_speed)

                        else:
                            ball_dx *= -1
                            ball_dy = 0

                        bounce_sound_effect.play()

        # ball collision with the player 2 's paddle
        if 1170 > ball_x > 1160:
            if player_2_y < ball_y + 25:
                if player_2_y + 150 > ball_y:

                    aux = random.randint(0, 1)
                    aux_ang = random.randint(0, 4)

                    if player_2_y < ball_y + 25 < player_2_y + 50 or player_2_y + 100 < ball_y + 25 < player_2_y + 175:
                        if ball_dx < MAX_SPEED:
                            print(ball_dx)
                            ball_dx *= -1.05
                            ball_dy = ang[aux_ang]
                            ball_dy *= r[aux]
                            count_speed += 1
                            print("Velocidade: %d" % count_speed)

                        else:
                            ball_dx *= -1
                            ball_dy = ang[aux_ang]
                            ball_dy *= r[aux]

                        bounce_sound_effect.play()

                    else:
                        if ball_dx < MAX_SPEED:
                            print(ball_dx)
                            ball_dx *= -1.25
                            ball_dy = 0
                            count_speed += 1
                            print("Velocidade: %d" % count_speed)

                        else:
                            ball_dx *= -1
                            ball_dy = 0

                        bounce_sound_effect.play()

        # scoring points
        if ball_x < -50:
            ball_x = 640
            ball_y = 360
            ball_dy *= -1
            ball_dx *= -1
            score_2 += 1
            scoring_sound_effect.play()
        elif ball_x > 1320:
            ball_x = 640
            ball_y = 360
            ball_dy *= -1
            ball_dx *= -1
            score_1 += 1
            scoring_sound_effect.play()

        # ball movement
        ball_x = ball_x + ball_dx
        ball_y = ball_y + ball_dy

        # player 1 up movement
        if player_1_move_up:
            player_1_y -= 10
        else:
            player_1_y += 0

        # player 1 down movement
        if player_1_move_down:
            player_1_y += 10
        else:
            player_1_y += 0

        # player 1 collides with upper wall
        if player_1_y <= 0:
            player_1_y = 0

        # player 1 collides with lower wall
        elif player_1_y >= 560:
            player_1_y = 560

        # player 2 "Artificial Intelligence"
        # Deixar a IA mais fácil
        # delay = random.randint(1, 2)
        # if delay == 1:
        if ball_y >= player_2_y:
            player_2_y += 7
        else:
            player_2_y += 0

        if ball_y <= player_2_y:
            player_2_y -= 7
        else:
            player_2_y -= 0
        # player_2_y = ball_y

        if player_2_y <= 0:
            player_2_y = 0
        elif player_2_y >= 560:
            player_2_y = 560

        # update score hud
        score_text = score_font.render("P1 " + str(score_1) + ' x ' + str(score_2) +
                                       " IA", True, COLOR_WHITE, COLOR_BLACK)

        # drawing objects
        screen.blit(ball, (ball_x, ball_y))
        screen.blit(player_1, (50, player_1_y))
        screen.blit(player_2, (1180, player_2_y))
        screen.blit(score_text, score_text_rect)
    else:
        # drawing victory
        screen.fill(COLOR_BLACK)
        screen.blit(score_text, score_text_rect)
        screen.blit(victory_text, victory_text_rect)

    # update screen
    pygame.display.flip()
    game_clock.tick(60)

pygame.quit()
