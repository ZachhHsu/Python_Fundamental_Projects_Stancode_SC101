"""
File: bouncing_ball.py
Name: Zach Hsu
-------------------------
TODO: This program simulates trajectory of a bouncing ball based on the given velocity and gravity.
      Users have only three times to initiate the bounce by clicking the mouse.
      If the ball moves beyond the right border of the window, it will restart at the starting point.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 5                                                                  # constant that controls the horizontal velocity
DELAY = 20                                                              # constant that controls the delay for animation
GRAVITY = 1                                                             # constant that controls the vertical velocity
SIZE = 30                                                               # constant that determines the size of the ball
REDUCE = 0.9                                                            # constant that reduces vertical velocity
START_X = 30                                                            # constant indicating the starting coordinate
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')                    # global variable that creates a window
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)                          # global variable that creates a ball
click = 3                                                               # global variable of available clicks remaining


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True                                                  # fill the color in the ball
    ball.fill_color = 'black'
    window.add(ball)                                                    # include the ball in the window
    onmouseclicked(bounce)                                              # initiate the function while clicking the mouse


def bounce(mouse):
    if window.get_object_at(START_X+SIZE/2, START_Y+SIZE/2) is None:    # invalidate clicking if the ball is moving
        return None

    global click                                                        # emphasize the global variable
    if click > 0:                                                       # continue if the number of clicks still remains
        click -= 1                                                      # lose one chance upon clicking once
        speed = 0                                                       # variable to record proceeding vertical speed
        while True:
            if ball.x > window.width:                                   # if the ball is out of the bound on the right
                window.add(ball, x=START_X, y=START_Y)                  # include a new ball in the window
                break

            ball.move(VX, speed)                                        # move the ball
            speed += GRAVITY                                            # vertical speed gradually increases
            pause(DELAY)                                                # delay the animation
            if ball.y + SIZE >= window.height and speed > 0:            # check whether the ball reaches the bound below
                speed *= -REDUCE




if __name__ == "__main__":
    main()
