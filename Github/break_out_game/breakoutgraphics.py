"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height,)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, x=(window_width-self.paddle.width)/2, y=window_height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, x=(window_width-self.ball.width)/2, y=(window_height-self.ball.height)/2)

        # Default initial velocity for the ball
        self._dx = 0
        self._dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)
        self.is_game_started = False                                    # a switch to control the start of the game
        onmouseclicked(self.handle_click)

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):

                # Top rows colored with red
                if 0 <= j < brick_cols/5:
                    self.red_brick = GRect(brick_width, brick_height)
                    self.red_brick.filled = True
                    self.red_brick.fill_color = 'red'
                    self.window.add(self.red_brick, x=brick_width*i+brick_spacing*i,
                                    y=brick_offset+brick_height*j+brick_spacing*j)

                # Middle top rows colored with orange
                if brick_cols/5 <= j < brick_cols*2/5:
                    self.orange_brick = GRect(brick_width, brick_height)
                    self.orange_brick.filled = True
                    self.orange_brick.fill_color = 'orange'
                    self.window.add(self.orange_brick, x=brick_width*i+brick_spacing*i,
                                    y=brick_offset+brick_height*j+brick_spacing*j)

                # Middle rows colored with yellow
                if brick_cols*2/5 <= j < brick_cols*3/5:
                    self.yellow_brick = GRect(brick_width, brick_height)
                    self.yellow_brick.filled = True
                    self.yellow_brick.fill_color = 'yellow'
                    self.window.add(self.yellow_brick, x=brick_width*i+brick_spacing*i,
                                    y=brick_offset+brick_height*j+brick_spacing*j)

                # Middle bottom rows colored with green
                if brick_cols*3/5 <= j < brick_cols*4/5:
                    self.green_brick = GRect(brick_width, brick_height)
                    self.green_brick.filled = True
                    self.green_brick.fill_color = 'green'
                    self.window.add(self.green_brick, x=brick_width*i+brick_spacing*i,
                                    y=brick_offset+brick_height*j+brick_spacing*j)

                # Bottom rows colored with blue
                if brick_cols*4/5 <= j < brick_cols:
                    self.blue_brick = GRect(brick_width, brick_height)
                    self.blue_brick.filled = True
                    self.blue_brick.fill_color = 'blue'
                    self.window.add(self.blue_brick, x=brick_width*i+brick_spacing*i,
                                    y=brick_offset+brick_height*j+brick_spacing*j)

        # Count the number of bricks left
        self.num_brick = brick_cols * brick_rows

    # locate the x coordinate of mouse to the middle of paddle
    def move_paddle(self, mouse):
        if 0 + self.paddle.width/2 < mouse.x < self.window.width - self.paddle.width/2:
            self.paddle.x = mouse.x - self.paddle.width/2

    # start the game as soon as users click
    def handle_click(self, event):
        if not self.is_game_started:                                    # check whether the game isn't started
            self.set_ball_velocity()
            self.is_game_started = True                                 # ignore clicking after the game starts

    # set up the velocity for the initial ball movement
    def set_ball_velocity(self):
        self._dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:                                       # diversify horizontal direction
            self._dx = -self._dx
        self._dy = INITIAL_Y_SPEED

    # Getter for horizontal velocity
    def get_x_velocity(self):
        return self._dx

    # Getter for vertical velocity
    def get_y_velocity(self):
        return self._dy

    # Change the direction of horizontal velocity
    def bounce_x(self):
        self._dx = -self._dx

    # Change the direction of vertical velocity
    def bounce_y(self):
        self._dy = -self._dy

    # Upper left corner of the ball image
    def upper_left(self):
        return self.window.get_object_at(self.ball.x, self.ball.y)

    # Upper right corner of the ball image
    def upper_right(self):
        return self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)

    # Lower left corner of the ball image
    def lower_left(self):
        return self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)

    # Lower right corner of the ball image
    def lower_right(self):
        return self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)

    # Remove the brick when hit by the ball
    def remove_brick(self, brick):
        self.window.remove(brick)
        self.num_brick -= 1                                             # update the counter for the number of bricks

    # bounce the ball upward when the ball faces downward to the paddle
    def upward_bounce(self):
        if self._dy > 0:                                                # make sure the ball won't stick on the paddle
            self.bounce_y()







