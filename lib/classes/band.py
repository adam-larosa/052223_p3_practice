from classes.concert import Concert

class Band:
    def __init__( self, name, hometown ):
        self.name = name
        self.hometown = hometown
    
    # takes a venue and date (as a string) as arguments, and creates a new 
    # concert for the band in that venue on that date
    def play_in_venue( self, venue, date ):
        Concert( date, self, venue )

    # returns a list of strings representing all the introductions for this 
    # band each introduction is in the form "Hello {insert city name 
    # here}!!!!!, we are {insert band name here} and we're from 
    # {insert hometown here}"
    def all_introductions( self ):
        return [ c.introduction() for c in self.concerts() ]
    
    def concerts( self ):
        return [ concert for concert in Concert.all if concert.band == self ]
    

    def get_name( self ):
        return self._name
    
    def set_name( self, new_name ):
        if type( new_name ) == str and len( new_name ) > 0:
            self._name = new_name
        else:
            raise Exception( 'must be string > 0' )
            
    name = property( get_name, set_name )


    def get_hometown( self ):
        return self._hometown
    
    def set_hometown( self, new_hometown ):
        if type( new_hometown ) is str:
            if len( new_hometown ) > 0:
                self._hometown = new_hometown
            else:
                raise Exception( 'string must be greater than 0 chararacters')
        else:
            raise Exception( 'must be a string' )
    
    hometown = property( get_hometown, set_hometown )

    def __repr__( self ):
        return f'<Band name: {self.name}, hometown: {self.hometown}>'