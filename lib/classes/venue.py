from classes.concert import Concert
class Venue:

    def __init__(self, title, city ):
        self.title = title
        self.city = city


    # a date (string) as argument
    # finds and returns the first concert on that date at that venue
    # if there is no concert on that date at that venue, returns None
    def concert_on( self, date_given ):
        for concert in self.concerts():
            if concert.date == date_given:
                return concert
        



    def concerts( self ):
   #             us declaring a variable
   #                   |
   #                   V        
        return [ c for c in Concert.all if c.venue == self ]
        #        ^
        #        |
        #    us using that variable
        #    to decide what goes in
        #    the new list

    # The longer way of doing the same as the above list comprehension
        # the_list = []
        # for concert in Concert.all:
        #     if concert.venue == self:
        #         the_list.append( concert )
        # return the_list

    def bands( self ):
        return [ c.band for c in self.concerts() ]

      # another example of how to without the list comprehension
        # band_list = []
        # for concert in Concert.all:
        #     band_list.append( concert.band )
        # return band_list


    def get_title( self ):
        return self._title
    
    def set_title( self, new_title ):
        if type( new_title ) is str:
            if len( new_title ) > 0:
                self._title = new_title
            else:
                raise Exception( 'title must be greater than 0 chararacters')
        else:
            raise Exception( 'title must be a string' )

    title = property( get_title, set_title )
        

    def get_city( self ):
        return self._city
    
    def set_city( self, new_city ):
        if type( new_city ) is str:
            if len( new_city ) > 0:
                self._city = new_city
            else:
                raise Exception( 'city must be greater than 0 chararacters')
        else:
            raise Exception( 'city must be a string' )

    city = property( get_city, set_city )


    def __repr__( self ):
        return f'<Venue title: {self.title}, city: {self.city}>'