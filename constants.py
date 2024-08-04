SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SLOPE = SCREEN_HEIGHT / SCREEN_WIDTH

TURTLE_DEFAULT_WIDTH = 20
TURTLE_DEFAULT_HEIGHT = 20

PADDLE_HEADING = 90
PADDLE_SHAPE = "square"
PADDLE_COLOR = "white"
PADDLE_SPEED = "fastest"
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
PADDLE_WIDTH_FACTOR = PADDLE_WIDTH / TURTLE_DEFAULT_WIDTH
PADDLE_HEIGHT_FACTOR = PADDLE_HEIGHT / TURTLE_DEFAULT_HEIGHT
PADDLE_Y_COR_BOUNDARY = (SCREEN_HEIGHT - PADDLE_HEIGHT) / 2 - 25
PADDLE_MOVING_DISTANCE = 20

RIGHT_PADDLE_XCOR = SCREEN_WIDTH / 2 - 50
RIGHT_PADDLE_YCOR = 0
RIGHT_PADDLE_UP_KEY = "Up"
RIGHT_PADDLE_DOWN_KEY = "Down"

LEFT_PADDLE_XCOR = -RIGHT_PADDLE_XCOR
LEFT_PADDLE_YCOR = 0
LEFT_PADDLE_UP_KEY = "w"
LEFT_PADDLE_DOWN_KEY = "s"

# Ball Properties
BALL_SHAPE = "circle"
BALL_COLOR = "white"
BALL_SPEED = "fast"
BALL_WIDTH = 20
BALL_HEIGHT = 20
BALL_WIDTH_FACTOR = BALL_WIDTH / TURTLE_DEFAULT_WIDTH
BALL_HEIGHT_FACTOR = BALL_HEIGHT / TURTLE_DEFAULT_HEIGHT
BALL_MOVING_DISTANCE = 10
BALL_YCOR_BOUNDARY = SCREEN_HEIGHT / 2 - 20
BALL_RIGHT_PADDLE_BOUNDARY = RIGHT_PADDLE_XCOR - (PADDLE_WIDTH + BALL_WIDTH) / 2
BALL_LEFT_PADDLE_BOUNDARY = LEFT_PADDLE_XCOR + (PADDLE_WIDTH + BALL_WIDTH) / 2
BALL_PADDLE_COLLISION_DISTANCE = PADDLE_HEIGHT / 2

UP = 90
DOWN = 270
