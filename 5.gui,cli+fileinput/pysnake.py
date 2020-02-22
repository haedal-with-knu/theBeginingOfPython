# 파이썬으로 Snake 게임 만들기
# 참조 : https://python.bakyeono.net/chapter-12-1.html

import pygame              # ❶ 파이게임 모듈 임포트하기
import time

SCREEN_WIDTH = 400         # ❷ 게임 화면의 너비
SCREEN_HEIGHT = 80         #   게임 화면의 높이
BLOCK_SIZE = 20            # 뱀이 먹을 블록 크기

RED   = (255,   0,   0)    # 적색:   적 255, 녹   0, 청   0
GREEN = (  0, 255,   0)    # 녹색:   적   0, 녹 255, 청   0
WHITE = (255, 255, 255)    # 하얀색: 적 255, 녹 255, 청 255

def draw_background(screen):
    """게임의 배경을 그린다."""
    background = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.draw.rect(screen, WHITE, background)

def draw_block(screen, color, position):
    """position 위치에 color 색깔의 블록을 그린다."""
    block = pygame.Rect((position[1] * BLOCK_SIZE, position[0] * BLOCK_SIZE),
                        (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)


pygame.init()              # ❸ 파이게임을 사용하기 전에 초기화한다.


# ❹ 지정한 크기의 게임 화면 창을 연다.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 화면 전체에 하얀 사각형 그리기
rect = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)  # ❶
pygame.draw.rect(screen, WHITE, rect)  # ❷

# 화면 왼쪽 위에 녹색 정사각형 그리기
rect_g = pygame.Rect(0, 0, 40, 40)
pygame.draw.rect(screen, GREEN, rect_g)

# 화면 오른쪽 아래에 적색 직사각형 그리기
rect_r = pygame.Rect(340, 60, 60, 20)
pygame.draw.rect(screen, RED, rect_r)

# draw_background(screen)
# draw_block(screen, RED, (1, 1))
# draw_block(screen, RED, (3, 1))
# draw_block(screen, RED, (5, 1))
# draw_block(screen, RED, (7, 1))
# draw_block(screen, GREEN, (12, 10))
# draw_block(screen, GREEN, (12, 11))
# draw_block(screen, GREEN, (12, 12))
# draw_block(screen, GREEN, (12, 13))

pygame.display.update()  # ❸ 화면 새로고침

time.sleep(3)              # ❺ 3초동안 기다린다