import pygame, random

def get_new_value(old_gen, old_automata):
    # TBC - add code to generate the next row of cells,
    # then replace the return statement below to
    # return the updated automata
    return old_automata

# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (25, 25, 25)
MARGIN = 3
SQ_LENGTH = 10
SQ_NUM = 49 # min squares per row/column is 15
WIN_SIZE = (SQ_NUM+1)*MARGIN + SQ_NUM*SQ_LENGTH
BTN_SIZE = 30

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (WIN_SIZE, WIN_SIZE + BTN_SIZE+ 20)
screen = pygame.display.set_mode(size)
automata = [0] * (SQ_NUM*SQ_NUM)
generations = 0
time_step = 5
running = True

# Assign middle of first row to 1
automata[SQ_NUM//2] = 1


# Add a title
pygame.display.set_caption("Wolfram's Rule 126")
 
# Declare some buttons
font = pygame.font.Font('freesansbold.ttf', 16) 

inc_time_step_button = pygame.draw.rect(screen, (175, 203, 255), pygame.Rect(10,WIN_SIZE+10,3*BTN_SIZE, BTN_SIZE))
dec_time_step_button = pygame.draw.rect(screen, (175, 203, 255), pygame.Rect(20+3*BTN_SIZE,WIN_SIZE+10,3*BTN_SIZE, BTN_SIZE))
stop_play_button = pygame.draw.rect(screen, (175, 203, 255), pygame.Rect(30+6*BTN_SIZE,WIN_SIZE+10,3*BTN_SIZE, BTN_SIZE))
restart_button = pygame.draw.rect(screen, (175, 203, 255), pygame.Rect(40+9*BTN_SIZE,WIN_SIZE+10,3*BTN_SIZE, BTN_SIZE))
generation_display = pygame.draw.rect(screen, GRAY, pygame.Rect(60+12*BTN_SIZE,WIN_SIZE+10,3*BTN_SIZE, BTN_SIZE))


# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
          
            # use coordinates to check if a btn clicked
            if inc_time_step_button.collidepoint(click_pos) and time_step < 20:
                time_step += 1
            if dec_time_step_button.collidepoint(click_pos) and time_step > 1:
                time_step -= 1
            if stop_play_button.collidepoint(click_pos):
                running = not running
            if restart_button.collidepoint(click_pos):
                automata = [0] * (SQ_NUM*SQ_NUM)
                # Assign middle of first row to 1
                automata[SQ_NUM//2] = 1
                generations = 0

 
    # --- Game logic should go here
    if running:
        if generations < SQ_NUM:
            generations += 1
            automata = get_new_value(generations-1, automata)
            
        # --- Screen-clearing code goes here
    
        # Here, we clear the screen to gray. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(GRAY)
    
        # --- Drawing code should go here
        y = MARGIN
        i = 0
        while y < WIN_SIZE:
            x = MARGIN
            while x < WIN_SIZE:
                if automata[i] == 0:
                    pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, SQ_LENGTH, SQ_LENGTH))
                else:
                    pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, SQ_LENGTH, SQ_LENGTH))
                i += 1
                x += SQ_LENGTH + MARGIN
            y += SQ_LENGTH + MARGIN
        
        # Update generation count / redraw buttons
        inc_time_step_button = pygame.draw.rect(screen, (175, 203, 255), pygame.Rect(10,WIN_SIZE+10,3*BTN_SIZE, BTN_SIZE))
        text = font.render('Go faster', True, (14, 28, 54) )
        # set the center of the rectangular object. 
        textRect = text.get_rect()  
        textRect.center = (inc_time_step_button.center[0], inc_time_step_button.center[1]) 
        screen.blit(text, textRect) 

        dec_time_step_button = pygame.draw.rect(screen, (175, 203, 255), pygame.Rect(20+3*BTN_SIZE,WIN_SIZE+10,3*BTN_SIZE, BTN_SIZE))
        text = font.render('Go slower', True, (14, 28, 54) )
        # set the center of the rectangular object. 
        textRect = text.get_rect()  
        textRect.center = (dec_time_step_button.center[0], dec_time_step_button.center[1]) 
        screen.blit(text, textRect) 

        stop_play_button = pygame.draw.rect(screen, (175, 203, 255), pygame.Rect(30+6*BTN_SIZE,WIN_SIZE+10,3*BTN_SIZE, BTN_SIZE))
        text = font.render('Stop / Play', True, (14, 28, 54) )
        # set the center of the rectangular object. 
        textRect = text.get_rect()  
        textRect.center = (stop_play_button.center[0], stop_play_button.center[1]) 
        screen.blit(text, textRect) 

        restart_button = pygame.draw.rect(screen, (175, 203, 255), pygame.Rect(40+9*BTN_SIZE,WIN_SIZE+10,3*BTN_SIZE, BTN_SIZE))
        text = font.render('Restart', True, (14, 28, 54) )
        # set the center of the rectangular object. 
        textRect = text.get_rect()  
        textRect.center = (restart_button.center[0], restart_button.center[1]) 
        screen.blit(text, textRect) 

        generation_display = pygame.draw.rect(screen, GRAY, pygame.Rect(60+12*BTN_SIZE,WIN_SIZE+10,3*BTN_SIZE, BTN_SIZE))
        gen_text = str(generations) + ' generations'
        text = font.render(gen_text, True, (175, 203, 255) )
        # set the center of the rectangular object. 
        textRect = text.get_rect()  
        textRect.center = (generation_display.center[0], generation_display.center[1]) 
        screen.blit(text, textRect) 

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # --- Limit to `time_step` frames per second
    clock.tick(time_step)
 
# Close the window and quit.
pygame.quit()