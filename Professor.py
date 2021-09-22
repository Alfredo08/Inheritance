from Person import Person

class Professor( Person ):
    def __init__( self, fN, lN, age, title ):
        super().__init__( fN, lN, age )
        self.title = title

    def test( self ):
        print( self.title ) 