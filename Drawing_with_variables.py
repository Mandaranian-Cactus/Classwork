import arcade
from sys import stdin

WIDTH = 640
HEIGHT = 480

#Variables

xvar = int(stdin.readline())
yvar = int(stdin.readline())

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()
# Begin drawing

arcade.drawcircle_filled(xvar, yvar, 30, arcade.color.BLUE_GREEN)
arcade.dra

# End drawing
arcade.finish_render()
arcade.run()