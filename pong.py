# Implementation of classic arcade game Pong

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

paddle1_pos = HEIGHT /2
paddle2_pos = HEIGHT /2

ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0, 0 ]

paddle1_vel = 0
paddle2_vel = 0

player1 = 0
player2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    global player1, player2
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == True:
        ball_vel[0] = random.randrange(2, 4)
        ball_vel[1] = - random.randrange(1, 3)   
    elif direction == False:
        ball_vel[0] = - random.randrange(2, 4)
        ball_vel[1] = - random.randrange(1, 3)
        


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, WIDTH, HEIGHT  # these are numbers
    global player1, player2  # these are ints
    
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    player1 = 0
    player2 = 0
    
    spawn_ball(True)

def draw(canvas):
    global player1, player2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
            
    # draw ball
    canvas.draw_circle(ball_pos, 18, 2, "White", "White")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    #collision with top and bottom
    
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        
        
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos], [PAD_WIDTH, paddle1_pos], [PAD_WIDTH, paddle1_pos - PAD_HEIGHT], [0, paddle1_pos - PAD_HEIGHT]], 1, "White", "White")  
    canvas.draw_polygon([[WIDTH - PAD_WIDTH, paddle2_pos], [WIDTH, paddle2_pos], [WIDTH, paddle2_pos - PAD_HEIGHT], [WIDTH - PAD_WIDTH, paddle2_pos - PAD_HEIGHT]], 1, "White", "White") 
    
    # determine whether paddle and ball collide
        
    if ball_pos[0] <= BALL_RADIUS:
        if (ball_pos[1] <= paddle1_pos):
            if (ball_pos[1] >= paddle1_pos - PAD_HEIGHT):
                ball_vel[0] = - ball_vel[0]
                ball_vel[0] = ball_vel[0] * 1.1
                
            else:
                player2 += 1
                spawn_ball(True)
     
    elif ball_pos[0] >= WIDTH - BALL_RADIUS:
        if (ball_pos[1] <= paddle2_pos):
            if (ball_pos[1] >= paddle2_pos - PAD_HEIGHT):
                ball_vel[0] = - ball_vel[0]
                ball_vel[0] = ball_vel[0] * 1.1
                
            else:
                player1 += 1
                spawn_ball(False)
    
    # update paddle's vertical position, keep paddle on the screen
    
    if paddle1_pos < HALF_PAD_HEIGHT * 2:
        paddle1_vel = 0
        paddle1_pos += 1
    
    elif paddle1_pos > HEIGHT:
        paddle1_vel = 0
        paddle1_pos -= 1
        
    else:
        paddle1_pos += paddle1_vel
        
    if paddle2_pos <= HALF_PAD_HEIGHT * 2:
        paddle2_vel = 0
        paddle2_pos += 1
        
    elif paddle2_pos >= HEIGHT:
        paddle2_vel = 0
        paddle2_pos -= 1
        
    else:
        paddle2_pos += paddle2_vel
        
    # draw scores
    
    canvas.draw_text(str(player1), [WIDTH / 5, HEIGHT / 4], 50, "White")
    canvas.draw_text(str(player2), [WIDTH - WIDTH / 4, HEIGHT / 4], 50, "White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 5
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -5
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 5
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -5
     
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)


# start frame
new_game()
frame.start()
