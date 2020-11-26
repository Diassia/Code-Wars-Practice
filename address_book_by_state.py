def by_state(str):
    number = 1

    ordered_string = '' # the output string with ordered addresses by state

    complete_details_dictionary = {} # will be a numbered nested dictionary with details for all addresses
    states = {
        'AZ': 'Arizona',
        'CA': 'California',
        'ID': 'Idaho',
        'IN': 'Indiana',
        'MA': 'Massachusetts',
        'OK': 'Oklahoma',
        'PA': 'Pennsylvania',
        'VA': 'Virginia'
    }

    split_lines = str.splitlines() # split string into list at new line

    for person_string in split_lines: # for loop will find the state initials and replace with value from dictionary
        person_detail_list = person_string.split(',')
        print(person_detail_list)
        name = person_detail_list[0]
        address = person_detail_list[1]
        city_and_state = person_detail_list[2]
        state_code = city_and_state[-2:]
        complete_details_dictionary[number] = { # creates a nested dictionary for each address with name, address, city, state, state_name and removes commas
            'name': name,
            'address': address,
            'city': city_and_state[:-2],
            'state': state_code,
            'state_name': states[state_code]
        }

        # append dictionary address details to ordered_string outside for loop
        ordered_string += complete_details_dictionary[number]['state_name'] + '\n..... ' + complete_details_dictionary[number]['name'] + ' ' + complete_details_dictionary[number]['address'] + ' ' + complete_details_dictionary[number]['state_name'] + '\n'
        
        number += 1 # will add 1 to number to change nested dictionary to number + 1
        
    print(complete_details_dictionary)

    return ordered_string

# OUTPUT should be:
# Massachusetts
# ..... John Daggett 341 King Road Plymouth Massachusetts
# ..... Sal Carpenter 73 6th Street Boston Massachusetts
# Virginia
# ..... Alice Ford 22 East Broadway Richmond Virginia

case0 = """John Daggett, 341 King Road, Plymouth MA
Alice Ford, 22 East Broadway, Richmond VA
Sal Carpenter, 73 6th Street, Boston MA"""

case1 = """John Daggett, 341 King Road, Plymouth MA
Alice Ford, 22 East Broadway, Richmond VA
Orville Thomas, 11345 Oak Bridge Road, Tulsa OK
Terry Kalkas, 402 Lans Road, Beaver Falls PA
Eric Adams, 20 Post Road, Sudbury MA
Hubert Sims, 328A Brook Road, Roanoke MA
Amy Wilde, 334 Bayshore Pkwy, Mountain View CA
Sal Carpenter, 73 6th Street, Boston MA"""

print(by_state(case0))
