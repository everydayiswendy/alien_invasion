import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
import os


class AlienInvasion:
    #管理游戏资源和行为的类
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        #屏幕设置
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets =pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

    def run_game(self):
        #开始游戏的主循环
        while True:
            #监视键盘和鼠标事件
            self._check_events()
            self.ship.update()
            self._update_bullets()

            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        #相应按键
        if event.key == pygame.K_RIGHT:
            # 向右移动飞船
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            pygame.quit()
            os._exit(0)
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    def _check_keyup_events(self, event):
        #相应松开
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        #创建一颗子弹，并将其加入编组bullets中。
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet) 

    def _update_bullets(self):
        self.bullets.update()

        #删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)
            #print(len(self.bullets))
    
    def _create_fleet(self):
        #创建外星人群
        #创建第一个外星人
        alien =Alien(self)
        self.aliens.add(alien)

    def _update_screen(self):
        # 每次循环时都重新绘制屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #让最近绘制的屏幕可见
        pygame.display.flip()

if __name__ =='__main__':
    ai = AlienInvasion()
    ai.run_game()
