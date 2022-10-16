import pygame
from pygame.locals import *
import sys


def main():
    pygame.init()  # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 400 x 300の大きさの画面を作る
    pygame.display.set_caption("いけめんがつくったげえむ")  # 画面上部に表示するタイトルを設定

    rect_x = 20  # 長方形左上のｘ座標
    rect_y = 400  # 長方形左上のｘ座標
    rect_width = 800 - (rect_x * 2)  # 長方形の幅
    rect_height = 600 - (rect_y + 20)  # 長方形の高さ
    slyme_image = pygame.image.load("image/slyme.png")

    font = pygame.font.Font("font/DragonQuestFC.ttf", 30)

    action_number = 0  # 選択肢の番号
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    """
    メインループ内で決めればいいので、削除
    color0 = white
    color1 = white
    color2 = white
    """

    while (1):

        """
        一度全部白にしてから、指定の部分だけ黄色にする
        """
        colors = [white, white, white]
        colors[action_number] = yellow

        screen.fill((0, 0, 0))  # 画面を黒色に塗りつぶし
        screen.blit(slyme_image, (400 - (400 / 2), 0))

        pygame.draw.rect(screen, (255, 255, 255), Rect(rect_x, rect_y, rect_width, rect_height), 10)
        text = font.render("りっきーが　あらわれた！", True, (255, 255, 255))

        """
        colorsリストから、それぞれの文字の色を取得する
        """
        battle_text = font.render("たたかう", True, colors[0])
        spell_text = font.render("じゅもん", True, colors[1])
        run_text = font.render("にげる", True, colors[2])

        screen.blit(text, (40, 420))
        screen.blit(battle_text, (45, 450))
        screen.blit(spell_text, (45, 480))
        screen.blit(run_text, (45, 510))

        pygame.display.update()  # 画面を更新
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()  # Pygameの終了(画面閉じられる)
                sys.exit()

            elif event.type == KEYDOWN:
                if action_number == 2:
                    action_number = 0
                else:
                    action_number += 1


if __name__ == "__main__":
    main()
