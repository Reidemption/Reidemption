import pygame
import game
import picture

TITLE = "Illustrate by Reid Gubler"
WINDOW_WIDTH  = 1250
WINDOW_HEIGHT = 900
# frames per second
DESIRED_RATE  = 60

class PygameApp( game.Game ):

    def __init__( self, title, width, height, frame_rate ):
        game.Game.__init__( self, title, width, height, frame_rate )
        self.game = picture.Picture( width, height )        
        
    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):
        self.game.evolve( dt )
    
    def paint( self, surface ):
        self.game.draw( surface )

def main( ):
    pygame.font.init( )
    game = PygameApp( TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE )
    game.main_loop( )
    
if __name__ == "__main__":
    main( )
