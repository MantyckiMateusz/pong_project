from turtle import Screen

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800
BG_COLOR = "black"
TITLE = "Pong game"
CONTROLS = {
    "P1_up": "Up",
    "P1_down": "Down",
    "P2_up": "w",
    "P2_down": "s"
}

class Config:
    
    def __init__(self, paddle1, paddle2):
        self.screen = Screen()
        self.screen.setup(height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
        self.screen.bgcolor(BG_COLOR)
        self.screen.title(TITLE)
        self.screen.tracer(0)
        self.screen.listen()
        self.screen.onkeypress(paddle1.move_up, CONTROLS["P1_up"])
        self.screen.onkeypress(paddle1.move_down, CONTROLS["P1_down"])
        self.screen.onkeypress(paddle2.move_up, CONTROLS["P2_up"])
        self.screen.onkeypress(paddle2.move_down, CONTROLS["P2_down"])