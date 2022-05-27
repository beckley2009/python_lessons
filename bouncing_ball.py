import arcade

TITLE = 'Bouncing ball'
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Mygame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        self.center_x = 300
        self.center_y = 300
        self.radius = 50
        self.change_x = 40
        self.change_y = 60
    
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)
        arcade.draw_circle_filled(self.center_x,self.center_y,self.radius,arcade.color.BLACK)

    def update(self,delta_time):
        self.center_x += self.change_x
        if(self.center_x > SCREEN_WIDTH - self.radius):
            self.change_x = -self.change_x
        if(self.center_x < self.radius):
            self.change_x = -self.change_x

        self.center_y += self.change_y
        if(self.center_y > SCREEN_HEIGHT - self.radius):
            self.change_y = -self.change_y
        if(self.center_y < self.radius):
            self.change_y = -self.change_y






window = Mygame(SCREEN_WIDTH, SCREEN_HEIGHT,TITLE)
arcade.run()
