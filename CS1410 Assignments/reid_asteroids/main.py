import pygame
import game
import asteroids

# window title bar text
TITLE = "asteroids"
# pixels width
WINDOW_WIDTH  = 700
# pixels high
WINDOW_HEIGHT = 600
# frames per second
DESIRED_RATE  = 30

class PygameApp( game.Game ):

    def __init__( self, title, width, height, frame_rate ):

        super().__init__( title, width, height, frame_rate )
        
        # create a game instance
        # YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
        self.mGame = asteroids.Asteroids( width, height )
        
        
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
        # Use 1, 2, 3 as the mouse buttons
        # if 3 in buttons:
        #    The user is holding down the right mouse button
        #
        # mouse_position contains x and y location of mouse in window
        # dt contains the number of seconds since last frame
        
        x = mouse_position[ 0 ]
        y = mouse_position[ 1 ]

        # Update the state of the game instance
        # YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
        if pygame.K_w in keys or pygame.K_UP in keys:
            self.mGame.accelerateShip(10)
        if pygame.K_d in keys or pygame.K_RIGHT in keys:
            self.mGame.turnShipRight(5)
        if pygame.K_a in keys or pygame.K_LEFT in keys:
            self.mGame.turnShipLeft(5)
        if pygame.K_SPACE in newkeys:
            self.mGame.fire()
        self.mGame.evolve( dt )
    
    def paint( self, surface ):
        # Draw the current state of the game instance
        self.mGame.draw( surface )
        return

def main( ):
    pygame.font.init( )
    game = PygameApp( TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE )
    game.main_loop( )
    
if __name__ == "__main__":
    main( )
