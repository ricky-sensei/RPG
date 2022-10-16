import pygame
from pygame.locals import *
import sys

def main():
    pygame.init()                                   # Pygameの初期化
    screen = pygame.display.set_mode((800,600))    # 400 x 300の大きさの画面を作る
    pygame.display.set_caption("いけめんがつくったげえむ")              # 画面上部に表示するタイトルを設定

    rect_x = 20 #長方形左上のｘ座標
    rect_y = 400  #長方形左上のｘ座標
    rect_width = 800 - (rect_x * 2)  #長方形の幅
    rect_height = 600 - (rect_y + 20) #長方形の高さ
    slyme_image = pygame.image.load("image/slyme.png")

    font = pygame.font.Font("font/DragonQuestFC.ttf", 30)
    while (1):
        screen.fill((0,0,0))  # 画面を黒色に塗りつぶし
        screen.blit(slyme_image, (400 - (400 / 2), 0))

        pygame.draw.rect(screen,(255, 255, 255), Rect(rect_x, rect_y, rect_width, rect_height), 10)
        text = font.render("りっきーが　あらわれた！", True, (255, 255, 255))
        screen.blit(text, (40, 420))
        pygame.display.update()     # 画面を更新
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了(画面閉じられる)
                sys.exit()


if __name__ == "__main__":
    main()