import pygame
import random

# 初始化 Pygame
pygame.init()

# 设置窗口
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("下雪动画")


# 定义雪花类
class Snowflake:
    def __init__(self):
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.size = random.randint(2, 5)
        self.speed = random.uniform(1, 3)

    def fall(self):
        self.y += self.speed
        if self.y > height:
            self.y = 0
            self.x = random.randint(0, width)

    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.size)


# 创建雪花列表
snowflakes = [Snowflake() for _ in range(100)]

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # 填充背景
    for snowflake in snowflakes:
        snowflake.fall()
        snowflake.draw()

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()