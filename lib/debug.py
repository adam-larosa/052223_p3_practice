#!/usr/bin/env python3

from random import randint, choice as rc

from faker import Faker
import ipdb

from classes.band import Band
from classes.concert import Concert
from classes.venue import Venue

if __name__ == '__main__':
    fake = Faker()



    chum = Band( 'Chumbawumba', 'Dublin' )
    motley = Band( 'Motley Crue', 'LA' )

    viper = Venue( 'The Viper Room', 'LA' )
    rick = Venue( 'The Rickshaw Stop', 'SF' )

    red = Venue( 'Red Rocks', 'Denver' )


    c1 = Concert( 'next week', chum, viper )
    c2 = Concert( 'yesterday', chum, rick )

    c3 = Concert( 'next week', motley, viper )


    ipdb.set_trace()
