import pygame
import sys

# 初始化pygame
pygame.init()

# 创建屏幕
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("外星人测试")

# 创建一个简单的外星人（使用矩形）
alien_rect = pygame.Rect(100, 100, 60, 60)
alien_color = (0, 255, 0)  # 绿色

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 绘制
    screen.fill((0, 0, 0))  # 黑色背景
    pygame.draw.rect(screen, alien_color, alien_rect)  # 绘制外星人
    pygame.display.flip()

pygame.quit()
sys.exit()