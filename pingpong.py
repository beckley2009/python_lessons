import arcade
TITLE = 'pingpong'
SCREEN_WIDTH = 600  # this is a constant
SCREEN_HEIGHT = 600


# evaluate if there is no attempts, then stop the game
# implement levels in your game.



class Ball(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if(self.left < 0 or self.right > SCREEN_WIDTH):
            self.change_x = -self.change_x
        if(self.bottom < 0 or self.top > SCREEN_HEIGHT):
            self.change_y = -self.change_y


class Bar(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if(self.left < 0):
            self.left = 0
        elif(self.right > SCREEN_WIDTH):
            self.right = SCREEN_WIDTH

        
class Mygame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        self.ball = Ball('ball.png',0.7)
        self.bar = Bar('bar.png',0.7)
        self.score = 0
        self.speed = 5
        self.level = 1
        self.attempts= 10
        

    def setup(self):
        self.ball.center_x = SCREEN_WIDTH/2
        self.ball.center_y = SCREEN_HEIGHT - 100
        self.bar.center_x = SCREEN_WIDTH/2
        self.bar.center_y = SCREEN_HEIGHT//6
        self.ball.change_x = self.speed
        self.ball.change_y = self.speed

    
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHEAT)
        arcade.draw_text(f"Score: {self.score}", 20, 550, arcade.color.BLACK, 16)
        arcade.draw_text(f"Speed: {self.speed}", 20, 530, arcade.color.BLACK, 16)
        arcade.draw_text(f"Level: {self.level}", 20, 510, arcade.color.BLACK, 16)
        arcade.draw_text(f"Attempts: {self.attempts}", 20, 490, arcade.color.BLACK, 16)
        self.ball.draw()
        self.bar.draw()

    def update(self, delta_time):
        self.bar.update()
        self.ball.update()
        if(self.ball.bottom < 0):
            self.attempts -= 1
            self.setup()
        elif(self.attempts == 0):
            self.ball.stop()
            self.bar.stop()
            # self.ball.stop()
            # self.bar.stop()
        if(self.score >= 20 and self.score <= 30):
            self.level = 2
            self.speed = 7
        elif(self.score >= 31 and self.score <= 40):
            self.level = 3
            self.speed = 9
        elif(self.score >= 41 and self.score <= 50):
            self.level = 4
            self.speed = 9
            
        if(arcade.check_for_collision(self.ball, self.bar)):
           self.ball.bottom -  self.bar.top
           self.ball.change_y = -self.ball.change_y
           self.score += 1

    def on_key_press(self, symbol: int, modifiers: int):
        if(symbol ==  arcade.key.LEFT):
            self.bar.change_x = -5

        if(symbol ==  arcade.key.RIGHT):
            self.bar.change_x = 5

    def on_key_release(self, symbol: int, modifiers: int):
        if(symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT):
            self.bar.change_x = 0
        



game = Mygame(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
game.setup()
arcade.run()



