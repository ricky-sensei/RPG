この記事は、岩手県八幡平市のプログラミング教室「アクセルキャンプ」の公開教材です。
[アクセルキャンプ(フリースペースプラウド)のリンク](https://freespaceproud.com)
教材の作成依頼等も承っております。ご意見等は、リンク先の問い合わせ欄からお願いします。
教材の転用・利用等は自由です  
***

# 最近リッキーの気になってるもの
皆さんポケモンGOとかやったことありますか？先生は最初にインストールだけして、ちょっと動かしただけなんですか、最初にやったときは、「すげ！ポケモンいる！カビゴンがうちにいる！」みたいになりました笑
  
でも、あれって携帯通してしか見れないので、しばらくやってるうちに「なんかなー、惜しいよなー」って思った人いません？先生はそうでした。そこで、ついに最近こういうのが出てきたんですよ！！  
https://rental.kikito.docomo.ne.jp/portal/articles/5015/

ついにメガネでARできるようになったわけですよ！ドキがムネムネしませんか？？ヤバくない？？
まだ対応してるアプリが少なかったりするのが何店ですが、そらそうですよ！未来のガジェットだもん！

先生のサイフポイントはもうゼロよ！という状態なのですが、どうする？？買っちゃう？
サンタさんに聞いてみます。  
  
# なんちゃってRPGゲーム、とりあえずここまでとしましょう
今まで作ってきたRPGゲームは、まだまだゲームとしては単純すぎますが、とりあえず今回は「ゲームってこんな感じで動いてるんだぜ！」というのを理解するのが目的なので、授業で扱うのはこんかいまでとします。  
「こんな機能をつけたい！」「改造したい！」というのがあったら、リッキーに相談してください！  

# まずは最終のコードを見てみよう！  
今までは自分でコードを書くのがメインでしたが、人が書いたコードを読むのもものすごく勉強になります！
```python
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
        time_end = time.time()
        if slyme_HP > 0 and time_end - time_start > 10.0:
            player_damage = random.randint(8000, 10000)
            player_HP -= player_damage
            sound_effect("sound/battle.mp3")
            if player_HP <= 0:
                player_HP = 0
                sound_effect("sound/gameover.mp3")
                message = "スライム:でなおしてきな！"

            else:
                message = "リッキーの こうげき プレイヤーに " + dq_font(player_damage) + "のダメージ"

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

        pygame.display.update()  # 画面を更新

        # HP0のときの終了処理
        if message in ("スライム:でなおしてきな！", "リッキーをたおした！ プレイヤーのしょうり！！"):
            time.sleep(10)
            sys.exit()

        if run == True:
            slymeX -= 2
            if slymeX < -400:
                pygame.quit()
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
                    if slyme_HP <= 0:
                        slyme_HP = 0
                        message = "リッキーをたおした！ プレイヤーのしょうり！！"
                        sound_effect("sound/victory.mp3")
                    else:
                        message = "リッキーに " + dq_font(damage) + "の ダメージ"

if __name__ == "__main__":
    main()

```
改めて見てみると、200行くらいのコードになってますね！ここまでよく頑張りました！一生懸命書いたコードがちゃんと動くのを見るのは、気持ちいいですよね！また、うまくいかない原因がわかって解決するのは、また違ったうれしさがありますよね！  
[前回のコード](https://qiita.com/ricky-sensei/items/59132104e884a6fb1979)と見比べてみましょう！いくつかの変更点があります。  
まずは、新機能ではない、前回のコード動きを変更しないコードの変更(リファクタリング)から。
  
### ①dq_font 関数
リッキーがコードを書きながら気づいたのですが、dragonquestFC.ttfは半角の文字に対応していませんでした。対応してるフォントであればこれは必要ない関数ですが、今回は関数を作ることで対応しました。「ググルのめんどくさいからコード書いた」って言えばちょっとかっこいいかな？笑 
```python
def dq_font(number):
    return str(number).translate(str.maketrans({chr(0x0021 + i): chr(0xFF01 + i) for i in range(94)}))
```
辞書型という、まだあんまり勉強してないpythonの文法を使っているので、気になる人は調べているのもいいかもしれません。いろいろ書いてますが、やってることは「半角文字を全角にする」です。
  
### ②HP表示  
前回はprint文でログを出力下だけでしたが、今回はしっかりと画面上に表示するようにしました。
前回はスライムのHPだけ表示してましたが、プレイヤー側にダメージを与える仕組みにしたので(後述)プレイヤー側のHPも表示しています。  
  
```python
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
```  
まず同じ大きさの四角を2つ作り、その中にそれぞれのtextをblitする。  
↑の文章で「なるほど！」とうなずける人は、だいぶpygameがわかってきた証拠です。ダメージが発生するたびに、ここに表示される数が減っていきます。  
  
### ③スライムによる反撃機能の作成  
リッキー(スライム)だって黙ってやられるわけではありません。めんどくさがりのリッキーでも、たまには反撃します。具体的には10秒に一回。
```python
time_end = time.time()
if slyme_HP > 0 and time_end - time_start > 10.0:
    player_damage = random.randint(8000, 10000)
    player_HP -= player_damage
    sound_effect("sound/battle.mp3")
    if player_HP <= 0:
        player_HP = 0
        sound_effect("sound/gameover.mp3")
        message = "スライム:でなおしてきな！"
    else:
        message = "リッキーの こうげき プレイヤーに " + dq_font(player_damage) + "のダメージ"
        
    time_start = time.time()
```
time_start time_endという2つの変数で時間を管理します。time モジュールの使い方はいろいろあり、細かくは説明しませんが、time.time()を実行したときに、その時の時間を設定します。time_endーtime_startを引き算した結果=経過した時間が10秒以上だったとき、スライムは攻撃し、その後time_startをリセットして次の10秒に備えます。  
また、そのときにプレイヤーのHPが0以下になったときに、ゲームオーバー用の音楽を流します。  
  
  
### ④ゲームオーバー、勝利の演出追加
```python
if message in ("スライム:でなおしてきな！", "リッキーをたおした！ プレイヤーのしょうり！！"):
    time.sleep(10)
    sys.exit()
```
このif文だけで、終了したあとに操作しても、HP表示が変化したり、音がなったりしないように制御しています。  
気をつけるべきポイント、と言うか、リッキーが気をつけずにミスってしまったことは、これをpygame.update()のあとに書くことです。こうしないと、終了はするけど、HP表示が変化しないで終わってしまうという、なんとも歯切れの悪い感じになってしまいます。  

今回はぶっちゃけ細かい変更はそれ意外にも結構してるので、アクセルキャンプに参加せずにこの記事だけで勉強してる人(一部いるみたいです！ありがとう！)は、「？？」ってなるところも多いと思いますが、そこはご勘弁を。  


# RPGっぽいなにかの制作、どうだった？
最初に言った通り、今回はゲームを作ったと言うより、ゲームの1シーンをそれっぽく作ってみた感じになりますが、どうだったでしょうか。  
普段勉強していることがこういう感じで生かされているんだな、という視点を持つと、またプログラミングの勉強に対する見方が変わってきませんか？

# アレンジしまくろう！  
せっかく作ったのにここで終わるのはもったいない！って思ってるそこのキミ！まずはアイディアだしからしていって、できそうなところから挑戦してみよう！
  
・オープニング画面などの挿入  
・スライムの次の敵キャラの追加  
・行動の選択肢の追加  
などなど  
  
ではまた来週もPygameで面白いの作っていく予定なので、お楽しみに！





  
