
class Concert:
    all = []
    def __init__( self, date, band_instance, venue_instance ):
        self.date = date
        self.band = band_instance
        self.venue = venue_instance
        Concert.all.append( self )
    
    # returns true if the concert is in the band's hometown, false if it is not
    def hometown_show( self ):
        return self.band.hometown == self.venue.city

    # returns a string with the band's introduction for this concert
    # an introduction is in the form: 
    # "Hello {insert city name here}!!!!!, we are {insert band name here} 
    #  and we're from {insert hometown here}"
    def introduction( self ):
        return f"Hello {self.venue.city}!!!!!, we are {self.band.name} " + \
            f"and we're from {self.band.hometown}"

    @property
    def date( self ):
        return self._date

    @date.setter
    def date( self, new_date ):
        if type( new_date ) is str and len( new_date ) > 0:
            self._date = new_date
        else:
            raise Exception( 'NO SOUP' ) 

    def __repr__( self ):
        return f'<Concert date: {self.date}>'