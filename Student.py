from Person import Person

class Student( Person ):
    def __init__( self, fN, lN, age, id ):
        super().__init__( fN, lN, age )
        self.identifier = id

    def printInfo( self ):
        print( "Printing from student" )
        print( f"FirstName: {self.firstName} LastName: {self.lastName}  Identifier: {self.identifier}")

    def printStudentInfo( self ):
        #super().printInfo()
        #print( "Printing from student ")
        self.printInfo()
        super().printInfo()
        #print( f"FirstName: {super().firstName} LastName: {self.lastName}  Identifier: {self.identifier}")

    def test( self ):
        print( 1, 2, 3 ) 