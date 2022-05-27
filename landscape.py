import arcade
class Landscape(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
    
    def tree(self, x,y,x2,y2):
        arcade.draw_rectangle_filled(x,y,20,90,arcade.color.BROWN)
        arcade.draw_circle_filled(x2,y2,30,arcade.color.DARK_GREEN)

    def tree2(self, x,y,x2,y2):
        arcade.draw_rectangle_filled(x,y,20,90,arcade.color.BROWN)
        arcade.draw_circle_filled(x2,y2,30,arcade.color.DARK_GREEN)

    def tree3(self, x,y,x2,y2):
        arcade.draw_rectangle_filled(x,y,20,90,arcade.color.BROWN)
        arcade.draw_circle_filled(x2,y2,30,arcade.color.DARK_GREEN)

    def window(self,x,y):
        arcade.draw_rectangle_filled(x,y,30,30,arcade.color.AERO_BLUE)


    def house(self, x, y):
        arcade.draw_rectangle_filled(x,y, 100, 80, arcade.color.CORN)
        arcade.draw_triangle_filled(x1=x, y1=y + 80,x2=x -50, y2=y +40, x3=x +50, y3=y+40, color=arcade.color.BROWN)

    def sun(self, x, y):
        arcade.draw_circle_filled(x,y,20,arcade.color.YELLOW)
        

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AERO_BLUE)
        arcade.draw_rectangle_filled(300, 100, 600, 200, arcade.color.GREEN)
        self.house(330, 125)
        self.tree(100,200,100,220)
        self.sun(70,350)
        self.tree2(130,70,130,90)
        self.tree3(490,120,490,140)
        self.window(330,125)
 



window = Landscape(600,400,'landscape')
arcade.run()
      