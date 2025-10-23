import sys
import pygame

pygame.init()

#屏幕设置
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Alien Invasion")

#颜色定义
bg_color = (230, 230, 230)
bullet_color = (60, 60, 60)

#飞船设置
ship_image = pygame.image.load('images/ship.bmp')
ship_rect = ship_image.get_rect()
ship_rect.midbottom = (screen_width // 2, screen_height -10)

#子弹列表
bullets =[]

#子弹速度

bullet_speed =5
bullet_width = 3
bullet_height = 15

#主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #按空格发射子弹
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #创建子弹矩形
                new_bullet = pygame.Rect(ship_rect.centerx - bullet_width //2,ship_rect.top-bullet_height, bullet_width, bullet_height)
                bullets.append(new_bullet)

    #更新子弹位置
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.bottom < 0:
            bullets.remove(bullet)

    #填充背景
    screen.fill(bg_color)

    #绘制飞船
    screen.blit(ship_image,ship_rect)

    #绘制子弹
    for bullet in bullets:
        pygame.draw.rect(screen, bullet_color, bullet)

    #绘制屏幕
    pygame.display.flip()