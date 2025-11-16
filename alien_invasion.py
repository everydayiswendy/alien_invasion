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

        self._create_fleet()

    def run_game(self):
        #开始游戏的主循环
        while True:
            #监视键盘和鼠标事件
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()

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
        self._check_bullet_alien_collisions()
       
    def _check_bullet_alien_collisions(self):
        #检查是否有子弹击中了外星人。
        #如果是，就删除相应的子弹和外星人
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            #删除现有的子弹并新建一群外星人
            self.bullets.empty()
            self._create_fleet()
    
    def _create_fleet(self):
        #创建一行外星人并计算一行可以容纳多少个外星人
        #外星人的间距为外星人宽度
        alien =Alien(self)
        alien_width , alien_height= alien.rect.size
        available_sapce_x =self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_sapce_x //(2 * alien_width)

        #计算屏幕可以容纳多少行外星人
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows =available_space_y // (2 * alien_height)


        #创建外星人群
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                #创建一个外星人并将其加入当前行
                self._create_alien(alien_number, row_number)
    def _create_alien(self, alien_number, row_number):
        alien =Alien(self)
        alien_width , alien_height= alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
     
    def _update_aliens(self):
        #更新外星人群中所有外星人的位置
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        #有外星人到达边缘时采取相应的措施
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        #将整群外星人下降，并且改变运行方向
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
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
