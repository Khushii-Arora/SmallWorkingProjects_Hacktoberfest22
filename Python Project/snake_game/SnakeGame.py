# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 13:41:04 2022

@author: Souvik Bhattacharya
"""
import pygame, random, sys

pygame.init()
pygame.mixer.init()

sc_width = 800
sc_height = 500

foodPX = 770
foodPY = 470

screen = pygame.display.set_mode((sc_width,sc_height))
pygame.display.set_caption('Snakes By Souvik')
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

try:
    bg_home = pygame.image.load('home_bg.png')
    bg_home = pygame.transform.scale(bg_home, (300,300)).convert_alpha()
except Exception as e:
    pass
try:
    bg_game = pygame.image.load('game_bg.jpg')
    bg_game = pygame.transform.scale(bg_game, (sc_width,sc_height)).convert_alpha()
except Exception as e:
    pass
try:
    bg_over = pygame.image.load('over_bg.png')
    bg_over = pygame.transform.scale(bg_over, (300,300)).convert_alpha()
except Exception as e:
    pass

def plot(screen,color,snake_co,snakeL, snakeW):
    for x,y in snake_co:
        pygame.draw.rect(screen, color, [x, y, snakeL, snakeW])

def scores(text,color,x,y):
    t = font.render(text, True, color)
    screen.blit(t, [x,y])
    
def home():
    exit_game = False
    while not exit_game:
        screen.fill((55, 109, 62))
        try:
            screen.blit(bg_home, (250,20))
        except Exception as e:
            pass
        scores('Welcome! To Snakes By Souvik!', (254, 212, 42), 260, 350)
        scores('Press Enter To Start!', (254, 212, 42), 320, 380)
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                exit_game = True
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_RETURN :
                    gameloop()
        pygame.display.update()
        clock.tick(30)
    pygame.quit()
    sys.exit()

def gameloop():
    
    exit_game = False
    end_game = False
    snakeX = random.randint(20, 770)
    snakeY = random.randint(20, 470)
    foodX = random.randint(20, foodPX)
    foodY = random.randint(20, foodPY)
    velocityX = 0
    velocityY = 0
    snakeL = 10
    snakeW = 10
    fps = 30
    score = 0
    try:
        with open('snake_scores.txt','r') as f:
            high_score = f.read()
    except Exception as e:
        with open('snake_scores.txt','w') as f:
            f.write('0')
            high_score = 0
    snake_co = []
    snake_length = 1
    
    while not exit_game:
        if end_game:
            screen.fill((171, 204, 255))
            try:
                screen.blit(bg_over, (250,20))
            except Exception as e:
                pass
            scores('Game Over! Press Enter To Restart!', (139, 23, 36), 240, 360)
            scores('Your Score is : '+str(score)+' & High Score is : '+str(high_score), (35, 85, 0), 235, 330)
            with open('snake_scores.txt','w') as f:
                f.write(str(high_score))
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    exit_game = True
                elif event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_RETURN :
                        gameloop()
        else:
            if not pygame.mixer.Channel(0).get_busy():
                try:
                    pygame.mixer.Channel(0).play(pygame.mixer.Sound('bg.mp3'))
                except Exception as e:
                    pass
            else:
                pass
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    exit_game = True
                elif event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_RIGHT :
                        velocityX = 4
                        velocityY = 0
                    elif event.key == pygame.K_LEFT :
                        velocityX = -4
                        velocityY = 0
                    elif event.key == pygame.K_UP :
                        velocityX = 0
                        velocityY = -4
                    elif event.key == pygame.K_DOWN :
                        velocityX = 0
                        velocityY = 4
                    elif event.key == pygame.K_k:
                        velocityX = 0
                        velocityY = 0
            try:
                screen.blit(bg_game, (0,0))
            except Exception as e:
                screen.fill((24,24,24))
            
            snakeX += velocityX
            snakeY += velocityY
            
            if abs(snakeX - foodX)<6 and abs(snakeY - foodY)<6:
                try:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound('beep.mp3'))
                except Exception as e:
                    pass
                score += 10
                if score > int(high_score):
                    high_score = score
                fx = foodX
                fy = foodY
                foodX = random.randint(20, foodPX)
                while foodX == fx:
                    foodX = random.randint(20, foodPX)
                foodY = random.randint(20, foodPY)
                while foodY == fy:
                    foodY = random.randint(20, foodPY)
                snake_length += 3    
                
            pygame.draw.rect(screen, (255, 69, 0), [foodX, foodY, 10, 10])
            scores('Your Score is : '+str(score)+' & High Score is : '+str(high_score)+' & Press k To Pause', (255, 99, 4), 150, 5)
            
            if snakeX >= sc_width or snakeX <= 0 or snakeY >= sc_height or snakeY <= 0:
                try:
                    pygame.mixer.Channel(0).stop()
                    pygame.mixer.music.load('hit.mp3')
                    pygame.mixer.music.play()
                except Exception as e:
                    pass
                end_game = True
                
            head = []
            head.append(snakeX)
            head.append(snakeY)
            snake_co.append(head)
            
            if len(snake_co) > snake_length:
                snake_co.remove(snake_co[0])
            
            if head in snake_co[:-1]:
                if (velocityX == 0 and velocityY != 0) or (velocityX != 0 and velocityY == 0):
                    try:
                        pygame.mixer.Channel(0).stop()
                        pygame.mixer.music.load('hit.mp3')
                        pygame.mixer.music.play()
                    except Exception as e:
                        pass
                    end_game = True
            
            plot(screen,(0, 255, 0),snake_co,snakeL,snakeW)
            if velocityX == 0 and velocityY == 0:
                scores('Game Paused! Press Any Arrow Key To Continue', (255, 99, 4), 185, 250)
        pygame.display.update()
        clock.tick(fps)
    
    pygame.quit()
    sys.exit()

home()