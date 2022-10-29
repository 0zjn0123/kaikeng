import pygame
import sys
#初始化
x = 30
y = 350
pygame.init()
#创建屏幕对象
screen = pygame.display.set_mode((1000,650))
pygame.display.set_caption("跑酷")
wj_rw = pygame.image.load('rw.png')
pk_dm = pygame.image.load('dm1.png')
pk_dm_rect = pk_dm.get_rect()
screen.fill((255,255,255))
wj_rect = wj_rw.get_rect()
class wj(pygame.sprite.Sprite):
    def __init__(self,image_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
    def xj(self,jx):
        global x
        x = x + jx
    def yj(self,jy):
        global y
        y = y + jy
    def xjj(self,jx):
        global x
        x = x + jx
    def yjj(self,jy):
        global y
        y = y + jy


wjf = wj
gq = wj
#窗口主循环
while True:
    #遍历事件队列
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if not wj_rect.colliderect(pk_dm_rect.center):
            #print('碰撞')
            wjf.yjj(0, jy=1)
    #wjf.xj(1, jx=1)移动代码示例
    #wjf.yjj(0,jy=1)
    pygame.draw.rect(screen,[255,255,255],[0,0,1000,650],0)

    #重绘界面
    screen.blit(wj_rw,(x,y))
    screen.blit(pk_dm,(0,600))
    pygame.display.update()


