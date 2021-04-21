"""
Do Not Edit this file. You may and are encouraged to look at it for reference.
"""

import unittest
import math
import ship

class TestShipEvolve( unittest.TestCase ):

    def setUp( self ):
        self.expected_x = 100
        self.expected_y = 200
        self.expected_dx = 0.0
        self.expected_dy = 0.0
        self.expected_rotation = 0
        self.expected_world_width = 600
        self.expected_world_height = 400

        self.constructed_obj = ship.Ship( self.expected_x, self.expected_y, self.expected_world_width, self.expected_world_height )
        
        return

    def tearDown( self ):
        return

    def test001_evolveMovesShip( self ):
        delta_velocity = 10.0
        expected_x = self.expected_x + 2.5
        expected_y = self.expected_y
        expected_dx = delta_velocity
        expected_dy = 0
        expected_rotation = 0
        self.constructed_obj.accelerate( delta_velocity )
        
        dt = 0.25
        self.constructed_obj.evolve( dt )
        
        self.assertAlmostEqual( self.constructed_obj.getX( ), expected_x )
        self.assertAlmostEqual( self.constructed_obj.getY( ), expected_y )
        self.assertAlmostEqual( self.constructed_obj.getDX( ), expected_dx )
        self.assertAlmostEqual( self.constructed_obj.getDY( ), expected_dy )
        self.assertAlmostEqual( self.constructed_obj.getRotation( ), expected_rotation )
        return
    
    def test002_evolveMovesShip( self ):
        delta_velocity = 10.0
        expected_x = self.expected_x + 2.5 * math.sqrt( 2 ) / 2
        expected_y = self.expected_y + 2.5 * math.sqrt( 2 ) / 2
        expected_dx = delta_velocity * math.sqrt( 2 ) / 2
        expected_dy = delta_velocity * math.sqrt( 2 ) / 2
        expected_rotation = 45
        self.constructed_obj.rotate( expected_rotation )
        self.constructed_obj.accelerate( delta_velocity )
        
        dt = 0.25
        self.constructed_obj.evolve( dt )
        
        self.assertAlmostEqual( self.constructed_obj.getX( ), expected_x )
        self.assertAlmostEqual( self.constructed_obj.getY( ), expected_y )
        self.assertAlmostEqual( self.constructed_obj.getDX( ), expected_dx )
        self.assertAlmostEqual( self.constructed_obj.getDY( ), expected_dy )
        self.assertAlmostEqual( self.constructed_obj.getRotation( ), expected_rotation )
        return
    
   
def suite( ):
    return unittest.TestLoader( ).loadTestsFromTestCase( TestShipEvolve )

if __name__ == '__main__':
    runner = unittest.TextTestRunner( )
    runner.run( suite( ) )
