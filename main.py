import string

import pygame
from sys import exit
from random import randint

from pip import main


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('Visuals/graphics/Jotaro/frame_01_delay-0.1s.gif').convert_alpha()
        player_walk_2 = pygame.image.load('Visuals/graphics/Jotaro/frame_02_delay-0.1s.gif').convert_alpha()
        player_walk_3 = pygame.image.load('Visuals/graphics/Jotaro/frame_03_delay-0.1s.gif').convert_alpha()
        player_walk_4 = pygame.image.load('Visuals/graphics/Jotaro/frame_04_delay-0.1s.gif').convert_alpha()
        player_walk_5 = pygame.image.load('Visuals/graphics/Jotaro/frame_05_delay-0.1s.gif').convert_alpha()
        player_walk_6 = pygame.image.load('Visuals/graphics/Jotaro/frame_06_delay-0.1s.gif').convert_alpha()
        player_walk_7 = pygame.image.load('Visuals/graphics/Jotaro/frame_07_delay-0.1s.gif').convert_alpha()
        player_walk_8 = pygame.image.load('Visuals/graphics/Jotaro/frame_08_delay-0.1s.gif').convert_alpha()
        player_walk_9 = pygame.image.load('Visuals/graphics/Jotaro/frame_09_delay-0.1s.gif').convert_alpha()
        player_walk_10 = pygame.image.load('Visuals/graphics/Jotaro/frame_10_delay-0.1s.gif').convert_alpha()
        player_walk_11 = pygame.image.load('Visuals/graphics/Jotaro/frame_11_delay-0.1s.gif').convert_alpha()
        player_walk_12 = pygame.image.load('Visuals/graphics/Jotaro/frame_12_delay-0.1s.gif').convert_alpha()
        player_walk_13 = pygame.image.load('Visuals/graphics/Jotaro/frame_13_delay-0.1s.gif').convert_alpha()
        player_walk_14 = pygame.image.load('Visuals/graphics/Jotaro/frame_14_delay-0.1s.gif').convert_alpha()
        player_walk_15 = pygame.image.load('Visuals/graphics/Jotaro/frame_15_delay-0.1s.gif').convert_alpha()
        self.player_jump = pygame.image.load('Visuals/graphics/Jotaro/jotaro jump.png').convert_alpha()

        self.player_walk = [player_walk_1, player_walk_2, player_walk_3, player_walk_4, player_walk_5, player_walk_6,
                            player_walk_7,
                            player_walk_8, player_walk_9, player_walk_10, player_walk_11, player_walk_12,
                            player_walk_13,
                            player_walk_14, player_walk_15]
        self.player_index = 0

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(100, 650))
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound('Visuals/audio/Mario Jump Sound Effect.mp3')

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 645:
            self.gravity = -23
            self.jump_sound.play()
            self.jump_sound.set_volume(0.03)

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom > 650:
            self.rect.bottom = 650

    def update(self):
        self.apply_gravity()
        self.player_input()
        self.player_animate()

    def player_animate(self):

        # walking
        if self.rect.bottom < 650:
            self.image = self.player_jump

        else:
            self.player_index += 0.24
            if self.player_index > len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'fly':
            fly1 = pygame.image.load('Visuals/graphics/Fly/Fly1.png').convert_alpha()
            fly2 = pygame.image.load('Visuals/graphics/Fly/Fly2.png').convert_alpha()
            self.frames = [fly1, fly2]
            y_pos = 400
        else:
            dio_1 = pygame.image.load('Visuals/graphics/dio/frame_00_delay-0.34s.gif').convert_alpha()
            dio_2 = pygame.image.load('Visuals/graphics/dio/frame_02_delay-0.04s.gif').convert_alpha()
            dio_3 = pygame.image.load('Visuals/graphics/dio/frame_03_delay-0.02s.gif').convert_alpha()
            dio_4 = pygame.image.load('Visuals/graphics/dio/frame_04_delay-0.04s.gif').convert_alpha()
            dio_6 = pygame.image.load('Visuals/graphics/dio/frame_06_delay-0.02s.gif').convert_alpha()
            dio_8 = pygame.image.load('Visuals/graphics/dio/frame_08_delay-0.06s.gif').convert_alpha()
            dio_9 = pygame.image.load('Visuals/graphics/dio/frame_09_delay-0.02s.gif').convert_alpha()
            dio_10 = pygame.image.load('Visuals/graphics/dio/frame_10_delay-0.04s.gif').convert_alpha()
            dio_12 = pygame.image.load('Visuals/graphics/dio/frame_12_delay-0.26s.gif').convert_alpha()
            self.frames = [dio_1, dio_2, dio_3, dio_4, dio_6, dio_8, dio_9, dio_12]
            y_pos = 645

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(1300, 1618), y_pos))

    def obstacle_animate(self):
        self.animation_index += 0.24
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.obstacle_animate()
        self.rect.x -= 11.618033988749
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()


def display_score():
    currenttime = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = font.render(f'Score: {int(currenttime * 1.618033988749)}', False, 'Black')
    score_rect = score_surface.get_rect(center=(1100, 80))
    pygame.draw.rect(screen, '#EEA3D8', score_rect)
    pygame.draw.rect(screen, '#EEA3D8', score_rect, 15)

    screen.blit(score_surface, score_rect)
    return currenttime * 1.618033988749


def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        player.sprite.rect.bottom = 650
        return False
    else:
        return True


pygame.init()
w = 1200
h = 677
game_active = False
start_time = 0
final_score = 0
bg_music = pygame.mixer.Sound('Visuals/audio/Bloody Stream 2 bit.mp3')
bg_music.play(loops = -1).set_volume(0.01618033988749)
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Oh ho your approaching me?')
clock = pygame.time.Clock()
font = pygame.font.Font('Visuals/font/Pixeltype.ttf', 50)
# surfaces
ground = pygame.image.load('Visuals/graphics/background.png')

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

jojo = pygame.image.load('Visuals/graphics/jojo.png').convert_alpha()
width_jojo = jojo.get_rect().width
height_jojo = jojo.get_rect().width
jojo = pygame.transform.scale(jojo, (width_jojo / 12, height_jojo / 30))
jojo_rec = jojo.get_rect(midbottom=[550, 200])

# Start Screen
player_stand = pygame.image.load('Visuals/graphics/player/SeekPng.com_jojo-menacing-png_338390.png')
player_stand_rect = player_stand.get_rect(center=(600, 300))

game_name = font.render('Jojo Run', False, '#DFDD1E')
game_name_rect = game_name.get_rect(center=(600, 100))

game_message = font.render('Press 1 to begin', False, '#DFDD1E')
game_message_rect = game_message.get_rect(center=(600, 500))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:

            if event.type == obstacle_timer:
                if randint(0, 2):
                    obstacle_group.add(Obstacle('dio'))
                else:
                    obstacle_group.add(Obstacle('fly'))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        # display the snail and player rectangles and surfaces
        screen.blit(ground, (0, 0))
        screen.blit(jojo, jojo_rec)
        final_score = int(display_score())

        player.draw(screen)
        player.update()
        obstacle_group.draw(screen)
        obstacle_group.update()
        game_active = collision_sprite()
    else:
        screen.fill((94, 129, 162))
        screen.blit(game_name, game_name_rect)
        screen.blit(player_stand, player_stand_rect)

        score_message = font.render(f'Your score:{final_score}     Press 1 to restart', False, '#DFDD1E')
        score_message_rect = score_message.get_rect(center=(600, 550))

        if final_score == 0:
            screen.blit(game_message, game_message_rect)
        else:

            screen.blit(score_message, score_message_rect)

    # maintain frame rate and update display
    pygame.display.update()
    clock.tick(60)


