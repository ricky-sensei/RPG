import pygame
from pygame.locals import *
import sys

def main():
    pygame.init()                                   # Pygameの初期化
    screen = pygame.display.set_mode((800,600))    # 400 x 300の大きさの画面を作る
    pygame.display.set_caption("いけめんがつくったげえむ")              # 画面上部に表示するタイトルを設定

    slyme_image = pygame.image.load("image/slyme.png")

    while (1):
        screen.fill((0,0,0))  # 画面を黒色に塗りつぶし
        screen.blit(slyme_image, (400 - (400 / 2), 0))

        pygame.display.update()     # 画面を更新
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了(画面閉じられる)
                sys.exit()


if __name__ == "__main__":
    main()

import pygame
from pygame.locals import *
import sys

def main():
    pygame.init()                                   # Pygameの初期化
    screen = pygame.display.set_mode((400, 300))    # 400 x 300の大きさの画面を作る
    pygame.display.set_caption("クソゲー")              # 画面上部に表示するタイトルを設定

    while (1):
        screen.fill((0,0,0))        # 画面を黒色に塗りつぶし
        pygame.display.update()     # 画面を更新
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了(画面閉じられる)
                sys.exit()


if __name__ == "__main__":
    main()