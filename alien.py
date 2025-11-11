import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #表示单个外星人的类

    def __init__(self, ai_game):
        #初始化外星人并设置其起始位置

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        #加载外星人图像并且设置其rect属性
        try:
            self.image = pygame.image.load('images/alien.bmp')
        except:
            print("外星人图片加载失败，使用替代图形")
            self.image = pygame.Surface((60,60))
            self.image.fill((0,255,0))
            
        self.rect = self.image.get_rect()

         #每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人的精确水平位置
        self.x = float(self.rect.x)