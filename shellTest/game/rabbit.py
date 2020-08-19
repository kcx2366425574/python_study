import pygame
from pygame.locals import *

# 初始化
pygame.init()
width, height = 720, 640
screen = pygame.display.set_mode((width, height))

# keys用来记录按键情况，wasd依次对应
keys = [False, False, False, False]

# playerpos表示玩家位置
playerpos = [100, 100]
# 加载图片
rabbit = pygame.image.load('./rabbit.jpeg')
grass = pygame.image.load('./grass.jpeg')
catsle = pygame.image.load('./catsle.jpeg')

# 不停的循环执行
while True:
    # 再给屏幕化任何东西之前先填充为黑色
    screen.fill(0)

    # 添加草和城堡
    for x in range(width//grass.get_width()+1):
        for y in range(height//grass.get_height()+1):
            screen.blit(grass, (x*100, y*100))

    screen.blit(catsle, (0, 0))
    screen.blit(catsle, (0, 150))
    screen.blit(catsle, (0, 300))
    screen.blit(catsle, (0, 450))
    # 在屏幕的(100, 100)处添加兔子
    screen.blit(rabbit, playerpos)

    # 更新屏幕
    pygame.display.flip()
    # 检查一些新的事件，如果有退出命令，则停止程序的运行
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # 根据按下的键来更新按键记录数组
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            if event.key == K_a:
                keys[1] = True
            if event.key == K_s:
                keys[2] = True
            if event.key == K_d:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                keys[0] = False
            if event.key == K_a:
                keys[1] = False
            if event.key == K_s:
                keys[2] = False
            if event.key == K_d:
                keys[3] = False
    # 移动玩家
    if keys[0]:
        playerpos[1] -= 5
    if keys[2]:
        playerpos[1] += 5
    if keys[1]:
        playerpos[0] -= 5
    if keys[3]:
        playerpos[0] += 5
