import arcade
class MyFace(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.ALLOY_ORANGE)
        arcade.draw_circle_filled(300,300,200,arcade.color.ANTI_FLASH_WHITE)
        arcade.draw_circle_outline(380,350,20,arcade.color.AIR_FORCE_BLUE)
        arcade.draw_circle_outline(220,350,20,arcade.color.AIR_FORCE_BLUE)
        arcade.draw_arc_outline(300,230,150,80,arcade.color.BRICK_RED,180,360,10)
        arcade.draw_circle_filled(380,350,15,arcade.color.AIR_FORCE_BLUE)
        arcade.draw_circle_filled(220,350,15,arcade.color.AIR_FORCE_BLUE)
window = MyFace(600,600,'Face')
arcade.run()