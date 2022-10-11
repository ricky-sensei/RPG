import pygame
from pygame.locals import *
import sys

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

def main():
    pygame.init()                                   # Pygameの初期化
    screen = pygame.display.set_mode((800,600))    # 400 x 300の大きさの画面を作る
    pygame.display.set_caption("いけめんがつくったげえむ")              # 画面上部に表示するタイトルを設定
    slyme_image = pygame.image.load("image/slyme.png")
    font = pygame.font.Font("font/DragonQuestFC.ttf", 30)

    button = pygame.Rect(100, 100, 150, 150)


    while (1):
        screen.fill(black)  # 画面を黒色に塗りつぶし
        screen.blit(slyme_image, (400 - (400 / 2), 0))

        pygame.draw.rect(screen, white, pygame.Rect(20, 400, 760, 180), 10)
        text = font.render("りっきーが　あらわれた！", True, white)
        screen.blit(text, (40, 420))

        pygame.draw.rect(screen, red, button)

        pygame.display.update()     # 画面を更新
        # イベント処理
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                if button.collidepoint(event.pos):
                    print("あたり！")
                else:
                    print("ばー－－－－－－－－－か！目んたまついてんのかｗｗｗｗ")

            if event.type == pygame.QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了(画面閉じられる)
                sys.exit()



if __name__ == "__main__":
    main()


