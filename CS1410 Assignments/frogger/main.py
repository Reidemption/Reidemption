import pygame
import game
import frogger

TITLE = "frogger"
NUM_ROWS = 13
NUM_COLS = 17
CELL_SIZE = 50
# pixels width
WINDOW_WIDTH  = NUM_COLS * CELL_SIZE
# pixels high
WINDOW_HEIGHT = NUM_ROWS * CELL_SIZE
# frames per second
DESIRED_RATE  = 60

class PygameApp( game.Game ):

    def __init__(self, title, width, height, frame_rate):

        super().__init__(title, width, height, frame_rate) 
        self.game = frogger.Frogger(width, height, CELL_SIZE, NUM_ROWS, NUM_COLS)
        
        
    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):
        # keys contains all keys currently held down
        # newkeys contains all keys pressed since the last frame
        # Use pygame.K_? as the keyboard keys.
        # Examples: pygame.K_a, pygame.K_UP, etc.
        # if pygame.K_UP in newkeys:
        #    The user just pressed the UP key
        #
        # buttons contains all mouse buttons currently held down
        # newbuttons contains all buttons pressed since the last frame
        if pygame.K_w in keys or pygame.K_UP in keys:
            self.game.up()
        if pygame.K_s in keys or pygame.K_DOWN in keys:
            self.game.down()
        if pygame.K_d in keys or pygame.K_RIGHT in keys:
            self.game.right()
        if pygame.K_a in keys or pygame.K_LEFT in keys:
            self.game.left()
        self.game.evolve( dt )

    
    def paint( self, surface ):
        # Draw the current state of the game instance
        self.game.draw( surface )
        return

def main( ):
    pygame.font.init( )
    game = PygameApp( TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE )
    game.main_loop( )
    
if __name__ == "__main__":
    main( )
