import kivy
from kivy.app import App
from kivy.lang import Builder

kivy.require("2.0.0")


class MyApp(App):
    current_stage = 0

    def build(self):
        return Builder.load_file("myapp.kv")

    def change_text_and_button(self):
        self.current_stage += 1

        if self.current_stage == 1:
            self.root.ids.label.text = "Мне передали, \nчто если на заднем\n фоне Ваше фото\n - надо нажмать на кнопку..."
            self.root.ids.button1.text = "я кнопка, я кнопка"
            self.root.ids.button1.background_color = (0, 0, 1, 1)
            self.root.ids.background.source = "1.png"
        elif self.current_stage == 2:
            self.root.ids.label.text = "Ваш китик передает,\n что очень сильно Вас любит\n и бафает на то,\n чтобы вы не загонялись,\n потому что вы счастливы,\n а значит все образуется"
            self.root.ids.background.source = "2.png"
        elif self.current_stage == 3:
            self.root.remove_widget(self.root.ids.button1)


if __name__ == "__main__":
    MyApp().run()

