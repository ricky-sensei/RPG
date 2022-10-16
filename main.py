import pygame
from pygame.locals import *
import sys

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

def main():
    # Pygameの初期化
    pygame.init()
    # 400 x 300の大きさの画面を作る
    screen = pygame.display.set_mode((800,600))
    # 画面上部に表示するタイトルを設定
    pygame.display.set_caption("いけめんがつくったげえむ")

    # 画像をフォルダからロードする
    slyme_image = pygame.image.load("image/slyme.png")
    # フォントをフォルダからロードする
    font = pygame.font.Font("font/DragonQuestFC.ttf", 30)

    base_rect = pygame.Rect(20, 400, 760, 180)
    menu_height = 100 / 3
    menu_width = 580
    menu_between = 20

    # メニューボタンの作成
    menu1_rect = pygame.Rect(110, 400 + menu_between, menu_width, menu_height)
    menu2_rect = pygame.Rect(110, 400 + menu_between * 2 + menu_height, menu_width, menu_height)
    menu3_rect = pygame.Rect(110, 400 + menu_between * 3 + menu_height * 2, menu_width, menu_height)
    # メニューボタンの文字を作成
    menu1_textBattle = font.render("たたかう", True, white)
    menu2_textBattle = font.render("じゅもん", True, white)
    menu3_textBattle = font.render("にげる", True, white)


    while (1):
        """
        大きい四角をbase
            rectオブジェクトをbase_rect
        選択肢のボタンをmenu1, menu2, menu3
            rectオブジェクトをmenu_rect
            表示テキストをmenu1_battle, menu2_magic, menu3_run
            それぞれ たたかう まほう にげる
            
        """
        screen.fill(black)  # 画面を黒色に塗りつぶし
        # スライムの表示
        screen.blit(slyme_image, (400 - (400 / 2), 0))

        pygame.draw.rect(screen, white, base_rect, 10)
        text = font.render("りっきーが　あらわれた！", True, white)
        screen.blit(text, (40, 420))


        # メニューボタンを表示
        pygame.draw.rect(screen, red, menu1_rect)
        pygame.draw.rect(screen, red, menu2_rect)
        pygame.draw.rect(screen, red, menu3_rect)
        screen.blit(menu1_textBattle, (menu1_rect.x, menu1_rect.y))
        screen.blit(menu2_textBattle, (menu2_rect.x, menu2_rect.y))
        screen.blit(menu3_textBattle, (menu3_rect.x, menu3_rect.y))


        pygame.display.update()     # 画面を更新
        # イベント処理
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                # if button.collidepoint(event.pos):
                #     print("あたり！")
                # else:
                #     print("ばー－－－－－－－－－か！目んたまついてんのかｗｗｗｗ")

            if event.type == pygame.QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了(画面閉じられる)
                sys.exit()



if __name__ == "__main__":
    main()


