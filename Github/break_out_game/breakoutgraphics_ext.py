"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon
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

        # Create two paddles
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, x=(window_width-self.paddle.width)/2, y=window_height-paddle_offset)

        self.paddle_2 = GRect(paddle_width, paddle_height)
        self.paddle_2.filled = True
        self.paddle_2.fill_color = 'black'

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, x=(window_width-self.ball.width)/2, y=(window_height-self.ball.height)/2)

        # Default initial velocity for the ball
        self._dx = 0
        self._dy = 0

        # Initialize our mouse listeners
        self.is_paddle_2 = False                                        # a switch determining which paddle is presented
        onmousemoved(self.move_paddle)
        self.is_game_started = False                                    # a switch controlling the start of the game
        self.dragon_jump = False                                        # a switch controlling dragon's movement
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

        # Create a scoreboard
        self.score = 0
        self.scoreboard = GLabel('Score: ' + str(self.score))
        self.scoreboard.font = '-20'
        self.window.add(self.scoreboard, 0, self.window.height - self.scoreboard.height + 15)

        # Draw a dragon
        self.dragon = GOval(ball_radius*2, ball_radius*2)
        self.dragon.filled = True
        self.dragon.fill_color = 'magenta'
        self._leap = 0                                                  # initial velocity of the dragon
        self._gravity = 0

        # Draw obstacles
        self.obstacle_1 = GRect(ball_radius, ball_radius*4)             # shorter but faster obstacle
        self.obstacle_1.filled = True
        self.obstacle_1.fill_color = 'magenta'
        self._obstacle_1_speed = -5

        self.obstacle_2 = GRect(ball_radius, ball_radius*7)             # longer but slower obstacle
        self.obstacle_2.filled = True
        self.obstacle_2.fill_color = 'magenta'
        self._obstacle_2_speed = -3

        # Determine if the dragon is already hit by the obstacle to count live reduction
        self.is_counted = False

        # Win Message
        self.win = GLabel('You Win!! Congratz!')
        self.win.font = '-30'

        # Lose Message
        self.lose = GLabel('You Lose!! Try Again!')
        self.lose.font = '-30'

    # locate the x coordinate of mouse to the middle of paddle
    def move_paddle(self, mouse):
        if not self.is_paddle_2:                                        # if the first paddle(bottom) is presented
            if 0 + self.paddle.width/2 < mouse.x < self.window.width - self.paddle.width/2:
                self.paddle.x = mouse.x - self.paddle.width/2
        else:                                                           # if the second paddle(top) is presented
            if 0 + self.paddle_2.width/2 < mouse.x < self.window.width - self.paddle_2.width/2:
                self.paddle_2.x = mouse.x - self.paddle_2.width/2

    # Start the game as soon as users click
    def handle_click(self, event):
        if not self.is_game_started:                                    # check whether the game isn't started
            self.set_ball_velocity()
            self.is_game_started = True                                 # ignore clicking after the game starts
        if self.score > 500:
            if not self.dragon_jump:                                    # check whether the dragon jumping isn't started
                self._leap = -15
                self._gravity = 1
                self.dragon_jump = True                                 # ignore clicking after dragon starts jumping

    # Getter for dragon's vertical velocity
    def get_dragon_velocity(self):
        return self._leap

    # Control dragon's vertical speed
    def dragon_speed_control(self):
        self._leap += self._gravity

    # Getter for obstacle 1's horizontal velocity
    def get_obstacle_1_speed(self):
        return self._obstacle_1_speed

    # Getter for obstacle 2's horizontal velocity
    def get_obstacle_2_speed(self):
        return self._obstacle_2_speed

    # Set up the velocity for the initial ball movement
    def set_ball_velocity(self):
        self._dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:                                       # diversify horizontal direction
            self._dx = -self._dx
        self._dy = INITIAL_Y_SPEED

    # Getter for horizontal velocity of the ball
    def get_x_velocity(self):
        return self._dx

    # Getter for vertical velocity of the ball
    def get_y_velocity(self):
        return self._dy

    # Change the direction of horizontal velocity
    def bounce_x(self):
        self._dx = -self._dx

    # Change the direction of vertical velocity
    def bounce_y(self):
        self._dy = -self._dy

    # Add a new ball if the ball is out of bound
    def out_of_bound(self):
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)
        self.is_game_started = False                                    # turn off the game

    # Replace the paddle at the bottom with a second paddle at the top of the window
    def add_top_paddle(self):
        self.window.remove(self.paddle)
        self.is_paddle_2 = True
        self.window.add(self.paddle_2, x=(self.window.width - self.paddle.width) / 2, y=0)

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
        if brick is not self.scoreboard:                                # ignore the scoreboard
            if brick is not self.paddle_2:                              # avoid eliminating the second paddle
                self.window.remove(brick)
                self.num_brick -= 1                                     # update the counter for the number of bricks
                self.update_score()

    # Bounce only if the ball hits other objects rather than scoreboard
    def bounce_ignore_scoreboard(self, collide):
        if collide is not self.scoreboard:
            self.bounce_y()

    # Bounce the ball upward when the ball faces downward to the paddle
    def upward_bounce(self, paddle):
        if self._dy > 0:                                                # make sure ball won't stick on first paddle
            if paddle is not self.paddle_2:                             # make sure ball won't stick on second paddle
                self.bounce_ignore_scoreboard(paddle)

    # Update scores when the ball hit bricks
    def update_score(self):
        self.score += 20
        self.scoreboard.text = 'Score: ' + str(self.score)

    # Upper left of the dragon
    def upper_left_dragon(self):
        return self.window.get_object_at(self.dragon.x, self.dragon.y)

    # Upper right of the dragon
    def upper_right_dragon(self):
        return self.window.get_object_at(self.dragon.x+self.dragon.width, self.dragon.y)

    # Lower left of the dragon
    def lower_left_dragon(self):
        return self.window.get_object_at(self.dragon.x, self.dragon.y+self.dragon.height)

    # Lower right of the dragon
    def lower_right_dragon(self):
        return self.window.get_object_at(self.dragon.x+self.dragon.width, self.dragon.y+self.dragon.height)








