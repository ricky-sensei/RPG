"""
11月5日メモ
※実装

プレイやーダメージ機能
    [x]時間経過でダメージ
    [x]負け演出
※リファクタリング
変数名など変更

課題
DragonQuestフォントのカタカナ「ャ」がなぜかない
プレイヤーダメージ用のSEを追加したい
gameover演出の追加(se, 文字表示)
continue機能

"""

import pygame
from pygame.locals import *
import sys
import time
import random


# 効果音
def sound_effect(sound):
    se = pygame.mixer.Sound(sound)
    se.play()

# 半角文字を全角にし、DragonQuestFC.tffに対応させる
def dq_font(number):
    return str(number).translate(str.maketrans({chr(0x0021 + i): chr(0xFF01 + i) for i in range(94)}))

def main():
    pygame.init()  # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 400 x 300の大きさの画面を作る
    pygame.display.set_caption("いけめんがつくったげえむ")  # 画面上部に表示するタイトルを設定

    # 選択肢ボックスの引数
    rectX_select = 20  # 長方形左上のｘ座標
    rectY_select = 400  # 長方形左上のｘ座標
    rectW_select = 800 - (rectX_select * 2)  # 長方形の幅
    rectH_select = 600 - (rectY_select + 20)  # 長方形の高さ

    # 選択ボックス内テキスト
    message = "りっきーが あらわれた！"
    # HPボックスの引数
    rectX_slymeHP = 550
    rectY_slymeHP = 20
    rectX_playerHP = 600
    rectY_playerHP = 200
    rectY_slymeHP = 20
    rectW_HP = 180
    rectH_HP = 100

    slyme_image = pygame.image.load("image/slyme.png")  # スライムの画像
    slymeX = 200  # スライムのx座標

    font = pygame.font.Font("font/DragonQuestFC.ttf", 30)

    # 色
    white = (255, 255, 255)
    yellow = (255, 255, 0)
    red = (255, 0, 0)

    # 効果音
    pygame.mixer.init()

    run = False  # 逃げる
    slyme_HP = 530000  # スライムのHP
    player_HP = 10000
    action_number = 0  # 選択肢の番号
    damage = 0
    damageY = 0  # ダメージ量表示のY座標

    time_start = time.time()

    while (1):
        if message == "スライム:でなおしてきな！":
            time.sleep(3)
            sys.exit()

        time_end = time.time()
        if time_end - time_start > 10.0:
            player_damage = random.randint(8000, 10000)
            player_HP -= player_damage
            message = "リッキーの こうげき プレイヤーに " + dq_font(player_damage) + "のダメージ"

            sound_effect("sound/battle.mp3")
            if player_HP <= 0:
                player_HP = 0
                message = "スライム:でなおしてきな！"

            time_start = time.time()

        # リスト:
        colors = [white, white, white]
        colors[action_number] = yellow

        screen.fill((0, 0, 0))  # 画面を黒色に塗りつぶし
        screen.blit(slyme_image, (slymeX, 0))  # スライムの画像表示

        # HPテキスト表示の枠を表示
        pygame.draw.rect(screen, white, Rect(rectX_slymeHP, rectY_slymeHP, rectW_HP, rectH_HP), 10)
        pygame.draw.rect(screen, white, Rect(rectX_playerHP, rectY_playerHP, rectW_HP, rectH_HP), 10)

        # スライムのHP表示
        slymeHP_text = font.render("ＨＰ：" + dq_font(slyme_HP), True, white)
        slymeHP_rect = slymeHP_text.get_rect(center=(640, 70))
        screen.blit(slymeHP_text, slymeHP_rect)

        # プレイヤーのHP表示
        playerHP_text = font.render("ＨＰ：" + dq_font(player_HP), True, white)
        playerHP_rect = playerHP_text.get_rect(center=(690, 250))
        screen.blit(playerHP_text, playerHP_rect)

        # attackのアニメーション表示
        text_damage = font.render(dq_font(damage), True, red)
        damage_rect = slymeHP_text.get_rect(center=(400, damageY))

        if damageY > 50:
            screen.blit(text_damage, damage_rect)
            damageY -= 1

        # 選択しのウィンドウを表示
        pygame.draw.rect(screen, white, Rect(rectX_select, rectY_select, rectW_select, rectH_select), 10)
        message_text = font.render(message, True, (255, 255, 255))
        battle_text = font.render("たたかう", True, colors[0])
        spell_text = font.render("じゅもん", True, colors[1])
        run_text = font.render("にげる", True, colors[2])

        screen.blit(message_text, (40, 420))
        screen.blit(battle_text, (45, 450))
        screen.blit(spell_text, (45, 480))
        screen.blit(run_text, (45, 510))

        if run == True:
            slymeX -= 2
            if slymeX < -400:
                pygame.quit()

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
                    # 「にげる」のBGM
                    if action_number == 2:
                        sound_effect("sound/run.mp3")
                        run = True
                        continue

                    # 「たたかう」のBGM
                    elif action_number == 0:
                        sound_effect("sound/battle.mp3")
                        # hit_pointの計算
                        damage = random.randint(10000, 30000)

                    # 「じゅもん」のBGM
                    elif action_number == 1:
                        sound_effect("sound/spell.mp3")
                        # hit_pointの計算
                        damage = random.randint(30000, 50000)

                    slyme_HP -= damage
                    damageY = 200
                    message = "リッキーに " + dq_font(damage) + "の ダメージ"
                    if slyme_HP <= 0:
                        slyme_HP = 0


if __name__ == "__main__":
    main()
