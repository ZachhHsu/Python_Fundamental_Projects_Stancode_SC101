"""
File: draw_line.py
Name: Zach Hsu
-------------------------
TODO: This program allows users to create straight lines by clicking the mouse.
      The first click creates a circle to indicate the origin of the line, whereas the second click indicates the end.
      As soon as a line is formed, the circle will disappear, leaving the line in the window.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


SIZE = 20                                                       # constant that determines the size of the circle
window = GWindow()                                              # global variable that creates a window
is_first_click = True                                           # switcher that checks the condition of clicks
oval = GOval(SIZE, SIZE)                                        # global variable that creates the circle


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)                                   # initiate the function while the mouse is clicked


def draw_line(mouse):
    """
    :param mouse: position that is clicked by the mouse
    :return: a circle if it's the first click; a line if it's the second click
    """
    global is_first_click, oval                                 # emphasize global variables
    if is_first_click:                                          # check whether it's the first click
        window.add(oval, mouse.x-SIZE/2, mouse.y-SIZE/2)        # include a circle according to the click's position
        is_first_click = False                                  # switch the condition to the second click
    else:                                                       # check whether it's the second click
        window.remove(oval)                                     # remove the circle
        start_x = oval.x + SIZE/2                               # assign the center of the circle as the starting point
        start_y = oval.y + SIZE/2
        line = GLine(start_x, start_y, mouse.x, mouse.y)        # create a line starting from circle to second click
        window.add(line)                                        # include the line in the window
        is_first_click = True                                   # switch the condition back to the first click


if __name__ == "__main__":
    main()
