import pyxel

GAME_TITLE = "Shingan"

font = pyxel.Font("assets/k8x12S.bdf")

class Game:
    def __init__(self):
        # Pyxelを読み込む
        pyxel.init(150, 100, title=GAME_TITLE)

        #リソースファイルを読み込む
        pyxel.load("assets/hatsuka.pyxres")

        #ゲームをリセットする
        self.is_title = True
        pass #self.reset_game()

        #アプリの実行を開始する
        pyxel.run(self.update, self.draw)

    #アプリを更新する
    def update(self):
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            pyxel.cls(0)
            pyxel.text(43,50,"右かな？ ", 7, font)

        elif pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            pyxel.cls(0)
            pyxel.text(43, 50, "左だ！", 7, font)

        elif pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            pyxel.cls(0)
            pyxel.text(43, 50, "上でしょ！", 7, font)

        elif pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            pyxel.cls(0)
            pyxel.text(43, 50, "うーん、下！", 7, font)



    def draw_title(self):
        for i in range(1, -1, -1):
            pyxel.text( 43, 20, "方向キーを　どれかひとつ\n押してください", 7, font)


        # 人物の描画
    def draw_chara(self):
        pyxel.blt(10,30,0,0,0,24,32)

    #アプリを描画する
    def draw(self):
        #画面を描画する
        self.draw_chara()

        if self.is_title:
            self.draw_title()


Game()
