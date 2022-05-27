# add the variables score, level, attempts, and display them on the screen
# create a new game, using different picture(car, wall, and background).

import arcade
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Game cars"
class Car(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if(self.left < 50):
            self.left = 50
        if(self.right > SCREEN_WIDTH -50):
            self.right = SCREEN_WIDTH -50
class Bar(arcade.Sprite):
    def update(self):
        self.center_y -= self.change_y
        if(self.center_y < 0):
            self.center_y = SCREEN_HEIGHT
            self.center_x = random.randint(130,SCREEN_WIDTH-130)


class OurGame(arcade.Window):
    def __init__(self,width, height, title):
        super().__init__(width, height, title)
        self.background = arcade.load_texture('background.png')
        self.car = Car('my_car.png', 0.2)
        self.score = 0
        self.attemps = 10
        self.level = 0
        self.bar = Bar('wall.png',0.5)

    def setup(self):
        self.car.center_x = SCREEN_WIDTH/2
        self.car.center_y = 100
        self.bar.center_x = random.randint(130,SCREEN_WIDTH-130)
        self.bar.center_y = SCREEN_HEIGHT
        self.bar.change_y = 5
        
       

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,self.background)
        self.car.draw()
        self.bar.draw()
        arcade.draw_text(f"Score: {self.score}", 60, 550, arcade.color.BLACK, 16)
        arcade.draw_text(f"attemps: {self.attemps}", 60, 530, arcade.color.BLACK, 16)
        arcade.draw_text(f"Level: {self.level}", 60, 510, arcade.color.BLACK, 16)
        
    def update(self, delta_time):
        self.car.update()
        self.bar.update()
        if(arcade.check_for_collision(self.bar,self.car)):
            self.attemps -= 1
            self.setup()
        if(self.attemps == 0):
            self.car.stop()
            self.bar.stop()

    def on_key_press(self, key, modifiers):
        if(key == arcade.key.RIGHT):
            self.car.change_x = 5
            self.car.angle = -10
        if(key == arcade.key.LEFT):
            self.car.change_x = -5
            self.car.angle = 10

    def on_key_release(self, key, modifiers):
        if(key == arcade.key.RIGHT or key == arcade.key.LEFT):
            self.car.change_x = 0
            self.car.angle = 0


game = OurGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
game.setup()
arcade.run()

