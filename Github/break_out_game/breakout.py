"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    # Add animation loop here!
    while True:
        # Update ball movement
        if graphics.is_game_started:                                    # check if the game is started
            graphics.ball.move(graphics.get_x_velocity(), graphics.get_y_velocity())

        # Bounce back if the ball reaches borders of the window
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.bounce_x()
        elif graphics.ball.y <= 0:                                      # the top of the window
            graphics.bounce_y()
        elif graphics.ball.y > graphics.window.height:                  # the bottom of the window(out of bound)
            graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) / 2,
                                y=(graphics.window.height - graphics.ball.height) / 2)
            graphics.is_game_started = False                            # turn off the game
            lives -= 1                                                  # loose one attempt
            if lives == 0:                                              # end the game if no attempts are left
                break

        # Check whether the upper left corner of the ball hits other objects
        if graphics.upper_left() is not None:
            if graphics.upper_left() is not graphics.paddle:            # make sure the ball won't stick on the paddle
                graphics.remove_brick(graphics.upper_left())
                if graphics.upper_right() is None \
                        and graphics.lower_left() is None:              # make sure the ball won't overly advance
                    graphics.bounce_y()

        # Check whether the upper right corner of the ball hits other objects
        if graphics.upper_right() is not None:
            if graphics.upper_right() is not graphics.paddle:           # make sure the ball won't stick on the paddle
                graphics.remove_brick(graphics.upper_right())
                if graphics.lower_right() is None \
                        and graphics.lower_left() is None:              # make sure the ball won't overly advance
                    graphics.bounce_y()

        # Check whether the lower left corner of the ball hits other objects
        if graphics.lower_left() is not None:
            if graphics.lower_left() is not graphics.paddle:            # remove bricks if not encountering paddle
                graphics.remove_brick(graphics.lower_left())
            if graphics.lower_right() is None:                          # make sure the ball won't overly advance
                graphics.upward_bounce()

        # Check whether the lower right corner of the ball hits other objects
        if graphics.lower_right() is not None:
            if graphics.lower_right() is not graphics.paddle:           # remove bricks if not encountering paddle
                graphics.remove_brick(graphics.lower_right())
            graphics.upward_bounce()

        # Pause
        pause(FRAME_RATE)

        # End the game if no bricks are left
        if graphics.num_brick == 0:
            break

if __name__ == '__main__':
    main()
