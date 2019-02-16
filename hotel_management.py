hotel = {
  '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
  },
  '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
  },
  '3': {
    '333': ['Neo', 'Trinity', 'Morpheus']
  }
}

import time






# Write a program that works with this hotel data:

# Display a menu asking whether to check in or check out.
# Prompt the user for a floor number, then a room number.
# If checking in, ask for the number of occupants and what their names are.
# If checking out, remove the occupants from that room.
# Do not allow anyone to check into a room that is already occupied.
# Do not allow checking out of a room that isn't occupied.
next_user = True

while next_user:
    print(hotel)
    #print(next_user)

    # Keep track of occupied rooms
    occupied_rooms = []
    for floor in hotel:
        for room in hotel[floor]:
            occupied_rooms.append(room)
    print('Occupied rooms are:',occupied_rooms)

    # Keep track of occupied floors
    occupied_floors = []
    for room in occupied_rooms:
        if room[0] not in occupied_floors:
            occupied_floors.append(room[0])
    print('Occupied floors are: ',occupied_floors)

    check_in_or_out = input('Would you like to check in or out?: ').lower()



    def check_in():

        #Initialize variables
        room_check = True
        occupant_count = 0
        occupants = []


        # Handle room already occupied
        while room_check:
            floor_number = input('What floor number?: ')
            room_number = input('What room number?: ')

            if room_number in occupied_rooms:
                print('Sorry, this room is occupied. Please pick again: ')
            else:
                room_check = False
                    

            if floor_number not in occupied_floors:
                hotel[floor_number] = {}


        # Add occupants
        occupants_number = int(input('How many occupants? '))
        while occupant_count < occupants_number:
            occupant_name = input('Occupant name: ')
            occupants.append(occupant_name)

            occupant_count += 1

        # Add occupants to correct floor and room number
        hotel[floor_number][room_number] = occupants
        print(hotel)
        print('You are checked in! \nPlease proceed to your room.')
        time.sleep(4)
        # Clears terminal
        print(chr(27) + "[2J")
        print('Welcome next guest')



    def check_out():
        # Initialie variables
        while True:
            room_number = input('What room number were you: ')
            floor_number = room_number[0]

            if room_number in occupied_rooms:
                del hotel[floor_number][room_number]
                print('Thank you for staying with us.')
                break
            else:
                print('Sorry, that room is not occupied. Pick again please')
        time.sleep(4)
        print('Welcome next guest')









    # Handle check-in or check-out
    if check_in_or_out == 'check in':
        check_in()
    elif check_in_or_out == 'check out':
        check_out()
    elif check_in_or_out == 'shutdown':
        print('Confirmed hotel management. Shutting down...')
        next_user = False





