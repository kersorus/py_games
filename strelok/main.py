from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint
 
class PongPaddle(Widget):
    score = NumericProperty(0) ## î÷êè èãðîêà
 
    ## Îòñêîê ìÿ÷èêà ïðè êîëëèçèè ñ ïàíåëüêîé èãðîêà
    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
 
            ball.velocity = vel.x, vel.y + offset
 
 
class PongBall(Widget):
 
    # Ñêîðîñòü äâèæåíèÿ íàøåãî øàðèêà ïî äâóì îñÿì
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
 
    # Ñîçäàåì óñëîâíûé âåêòîð
    velocity = ReferenceListProperty(velocity_x, velocity_y)
 
    # Çàñòàâèì øàðèê äâèãàòüñÿ
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
 
class PongGame(Widget):
    ball = ObjectProperty(None) # ýòî áóäåò íàøà ñâÿçü ñ îáúåêòîì øàðèêà
    player1 = ObjectProperty(None) # Èãðîê 1
    player2 = ObjectProperty(None) # Èãðîê 2
 
    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = Vector(vel[0], vel[1]).rotate(randint(0, 360))
 
    def update(self, dt):
        self.ball.move() # äâèãàåì øàðèê â êàæäîì îáíîâëåíèè ýêðàíà
 
        # ïðîâåðêà îòñêîêà øàðèêà îò ïàíåëåê èãðîêîâ
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)
 
        # îòñêîê øàðèêà ïî îñè Y
        if(self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1 # èíâåðñèðóåì òåêóùóþ ñêîðîñòü ïî îñè Y
 
        # îòñêîê øàðèêà ïî îñè X
        # òóò åñëè øàðèê ñìîã óéòè çà ïàíåëüêó èãðîêà, òî åñòü èãðîê íå óñïåë îòáèòü øàðèê
        # òî ýòî çíà÷èò ÷òî îí ïðîèãðàë è ìû äîáàâèì +1 î÷êî ïðîòèâíèêó
        if self.ball.x < self.x:
            # Ïåðâûé èãðîê ïðîèãðàë, äîáàâëÿåì 1 î÷êî âòîðîìó èãðîêó
            self.player2.score += 1
            self.serve_ball(vel=(4,0)) # çàíîâî ñïàâíèì øàðèê â öåíòðå
 
        if self.ball.x > self.width:
            # Âòîðîé èãðîê ïðîèãðàë, äîáàâëÿåì 1 î÷êî ïåðâîìó èãðîêó
            self.player1.score += 1
            self.serve_ball(vel=(-4,0)) # çàíîâî ñïàâíèì øàðèê â öåíòðå
 
    # Ñîáûòèå ïðèêîñíîâåíèÿ ê ýêðàíó
    def on_touch_move(self, touch):
        # ïåðâûé èãðîê ìîæåò êàñàòüñÿ òîëüêî ñâîåé ÷àñòè ýêðàíà (ëåâîé)
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
 
        # âòîðîé èãðîê ìîæåò êàñàòüñÿ òîëüêî ñâîåé ÷àñòè ýêðàíà (ïðàâîé)
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y
 
class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60) # 60 FPS
        return game
 
if __name__ == '__main__':
    PongApp().run()
