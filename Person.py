
class Person:
    def __init__( self, fN, lN, age ):
        self.firstName = fN
        self.lastName = lN
        self.age = age
    
    def printInfo( self ):
        print( "Printing from person" )
        print( f"First name: {self.firstName} Last name: {self.lastName} Age: {self.age}")

    def test( self ):
        raise NotImplementedError
