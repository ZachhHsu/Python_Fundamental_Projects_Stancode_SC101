"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics_ext import BreakoutGraphics

FRAME_RATE = 2000 / 120  # 220 frames per second
NUM_LIVES = 10  # Number of attempts


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
            if graphics.score <= 1200:                                  # in the bound
                graphics.bounce_y()
            else:                                                       # out of bound
                graphics.out_of_bound()
                lives -= 1
        elif graphics.ball.y > graphics.window.height:                  # the bottom of the window
            if graphics.score <= 1200:                                  # out of bound
                graphics.out_of_bound()
                lives -= 1
            else:                                                       # in the bound
                graphics.bounce_y()
        if lives == 0:                                                  # end the game if no attempts are left
            graphics.window.add(graphics.lose, x=(graphics.window.width - graphics.lose.width) / 2,
                                y=(graphics.window.height - graphics.lose.height) / 2)
            break

        # Check whether the upper left corner of the ball hits other objects
        if graphics.upper_left() is not None:
            if graphics.upper_left() is not graphics.dragon:            # ignore the objects from dragon jumping game
                if graphics.upper_left() is not graphics.obstacle_1:
                    if graphics.upper_left() is not graphics.obstacle_2:
                        if graphics.upper_left() is not graphics.paddle:
                            graphics.remove_brick(graphics.upper_left())
                            if graphics.upper_right() is None and graphics.lower_left() is None:
                                graphics.bounce_ignore_scoreboard(graphics.upper_left())

        # Check whether the upper right corner of the ball hits other objects
        if graphics.upper_right() is not None:
            if graphics.upper_right() is not graphics.dragon:           # ignore the objects from dragon jumping game
                if graphics.upper_right() is not graphics.obstacle_1:
                    if graphics.upper_right() is not graphics.obstacle_2:
                        if graphics.upper_right() is not graphics.paddle:
                            graphics.remove_brick(graphics.upper_right())
                            if graphics.lower_right() is None and graphics.lower_left() is None:
                                graphics.bounce_ignore_scoreboard(graphics.upper_right())

        # Check whether the lower left corner of the ball hits other objects
        if graphics.lower_left() is not None:
            if graphics.lower_left() is not graphics.dragon:            # ignore the objects from dragon jumping game
                if graphics.lower_left() is not graphics.obstacle_1:
                    if graphics.lower_left() is not graphics.obstacle_2:
                        if graphics.lower_left() is not graphics.paddle:
                            graphics.remove_brick(graphics.lower_left())
                        if graphics.lower_right() is None:
                            graphics.upward_bounce(graphics.lower_left())

        # Check whether the lower right corner of the ball hits other objects
        if graphics.lower_right() is not None:
            if graphics.lower_right() is not graphics.dragon:           # ignore the objects from dragon jumping game
                if graphics.lower_right() is not graphics.obstacle_1:
                    if graphics.lower_right() is not graphics.obstacle_2:
                        if graphics.lower_right() is not graphics.paddle:
                            graphics.remove_brick(graphics.lower_right())
                        graphics.upward_bounce(graphics.lower_right())

        # Add a dragon jumping game
        if graphics.score > 500:
            # dragon's movement
            if not 0 < graphics.dragon.x < graphics.window.width:
                graphics.window.add(graphics.dragon, x=60, y=420 - graphics.dragon.height)
            if graphics.dragon_jump:                                    # check whether the dragon starts to jump
                if graphics.get_dragon_velocity() < 0:                  # moving upward
                    graphics.dragon.move(0, graphics.get_dragon_velocity())
                    graphics.dragon_speed_control()
                else:                                                   # moving downward
                    graphics.dragon.move(0, graphics.get_dragon_velocity())
                    graphics.dragon_speed_control()
                    if graphics.get_dragon_velocity() == 16:            # stop jumping if dragon is back to origin spot
                        graphics.dragon_jump = False

            # obstacle 1 movement, starting from the rightmost of the window
            if not 0 < graphics.obstacle_1.x < graphics.window.width:
                graphics.window.add(graphics.obstacle_1, x=graphics.window.width - graphics.obstacle_1.width,
                                    y=420 - graphics.obstacle_1.height)
            graphics.obstacle_1.move(graphics.get_obstacle_1_speed(), 0)

            # obstacle 2 movement, starting from the rightmost of the window
            if graphics.score > 1000:                                   # activate 2nd stage of this game
                if 0 < graphics.obstacle_1.x < graphics.window.width / 2:
                    if not 0 < graphics.obstacle_2.x < graphics.window.width:
                        graphics.window.add(graphics.obstacle_2,
                                            x=graphics.window.width - graphics.obstacle_2.width,
                                            y=420 - graphics.obstacle_2.height)
                graphics.obstacle_2.move(graphics.get_obstacle_2_speed(), 0)

        # lose a live if the dragon hits an obstacle
        if not graphics.is_counted:                                     # check if the live reduction is already counted

            # Check whether the lower left corner of the dragon hits the obstacle
            if graphics.lower_left_dragon() is not None:
                if graphics.lower_left_dragon() is not graphics.ball:
                    if graphics.lower_right_dragon() and graphics.upper_right_dragon() is None:
                        lives -= 1

            # Check whether the upper right corner of the dragon hits the obstacle
            if graphics.upper_right_dragon() is not None:
                if graphics.upper_right_dragon() is not graphics.ball:
                    if graphics.lower_right_dragon() is None:
                        lives -= 1

            # Check whether the lower right corner of the dragon hits the obstacle
            if graphics.lower_right_dragon() is not None:
                if graphics.lower_right_dragon() is not graphics.ball:
                    lives -= 1

            # Switch the condition of live reduction to "is counted" if corners are still contacting the obstacle
            if graphics.lower_right_dragon() or graphics.upper_right_dragon() \
                    or graphics.lower_right_dragon() is not None:
                graphics.is_counted = True

        # Switch the condition of live reduction to "not counted" if the corner is not contacting the obstacle
        if graphics.lower_right_dragon() is None:
            graphics.is_counted = False

        # Replace to another paddle on the top of the window
        if not graphics.is_paddle_2:
            if graphics.score > 1200:
                graphics.add_top_paddle()

        # Change pause speed according to the score
        if graphics.score <= 600:
            pause(FRAME_RATE)
        elif 600 <= graphics.score <= 1400:
            pause(FRAME_RATE / 1.5)
        else:
            pause(FRAME_RATE / 2)

        # End the game if no bricks are left
        if graphics.num_brick == 0:
            graphics.window.add(graphics.win, x=(graphics.window.width-graphics.win.width)/2,
                                y=(graphics.window.height-graphics.win.height)/2)
            break


if __name__ == '__main__':
    main()
