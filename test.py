import pygame
from pygame.locals import *
import sys
import random



def sound_effect(sound):
    se = pygame.mixer.Sound(sound)
    se.play()



def main():
    pygame.init()  # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 400 x 300の大きさの画面を作る
    pygame.display.set_caption("いけめんがつくったげえむ")  # 画面上部に表示するタイトルを設定

    rect_x = 20  # 長方形左上のｘ座標
    rect_y = 400  # 長方形左上のｘ座標
    rect_width = 800 - (rect_x * 2)  # 長方形の幅
    rect_height = 600 - (rect_y + 20)  # 長方形の高さ
    slyme_image = pygame.image.load("image/slyme.png")
    slymeX = 200

    font = pygame.font.Font("font/DragonQuestFC.ttf", 30)

    action_number = 0  # 選択肢の番号
    white = (255, 255, 255)
    yellow = (255, 255, 0)

    # 効果音
    pygame.mixer.init()

    # HP
    hit_point = 530000

    run = False

    attack = 0
    attackY = -100


    while (1):

        """
        一度全部白にしてから、指定の部分だけ黄色にする
        """
        # リスト:
        colors = [white, white, white]
        colors[action_number] = yellow

        screen.fill((0, 0, 0))  # 画面を黒色に塗りつぶし
        screen.blit(slyme_image, (slymeX, 0))

        pygame.draw.rect(screen, (255, 255, 255), Rect(rect_x, rect_y, rect_width, rect_height), 10)
        text = font.render("りっきーが　あらわれた！", True, (255, 255, 255))

        attack_text = font.render(str(attack).translate(str.maketrans({chr(0x0021 + i): chr(0xFF01 + i) for i in range(94)})),True,yellow)
        screen.blit(attack_text, (380, attackY))
        if attackY > -100:
            attackY -= 1

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

        if run:
            slymeX -= 2

        pygame.display.update()  # 画面を更新
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()  # Pygameの終了(画面閉じられる)
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_DOWN:
                    if action_number == 2:
                        action_number = 0
                    else:
                        action_number += 1
                    sound_effect("sound/select_se.mp3")
                elif event.key == K_UP:
                    if action_number == 0:
                        action_number = 2
                    else:
                        action_number -= 1
                    sound_effect("sound/select_se.mp3")

                # エンターキーが押されたとき
                elif event.key == K_RETURN:
                    # 「たたかう」のBGM
                    if action_number == 0:
                        sound_effect("sound/battle.mp3")
                        attack = random.randint(10000, 30000)
                        hit_point -= attack
                        attackY = 300



                    # 「じゅもん」のBGM
                    elif action_number == 1:
                        sound_effect("sound/spell.mp3")
                        attack = random.randint(29999, 80000)
                        hit_point -= attack
                        attackY = 300 

                    # 「にげる」のBGM
                    elif action_number == 2:
                        sound_effect("sound/run.mp3")
                        run = True
                        print(run)

                    if hit_point <= 0:
                        print("りっきーを たおした！ けいけんちを １００００ てにいれた！")
                    else:
                        print(hit_point)

if __name__ == "__main__":
    main()