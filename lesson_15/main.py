from lesson_15.user import Person
from lesson_15.base import Base
from lesson_15.inventory import get_prihod
from lesson_15.lift import Elevator

if __name__ == '__main__':
    suez = Base("Suez Canal")
    suez.add_asset_tag(get_prihod())
    vlad = Person("Vlad")
    vlad.take_inv(suez)
    lift = Elevator()
    lift.go_ride(vlad)




