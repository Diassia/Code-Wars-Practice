def by_state(str):
    number = 1

    ordered_string = ''

    complete_dictionary = {}
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

    for string in split_lines: # for loop will find the state initials and replace with value from dictionary
        # state_slice = string[-2:] # state initial slice
        state_string = states[string[-2:]] # dictionary value from key slice
        # slice_string = string[:-2] + state_string # concat for original string place replacement string

        list_of_details = string.split()
        complete_dictionary[number] = { # creates a nested dictionary for each address with name, address, city, state, state_name and removes commas
            'name': (' '.join(list_of_details[0:2])).replace(',', ''),
            'address': (' '.join(list_of_details[2:5])).replace(',', ''),
            'city': ''.join(list_of_details[5]),
            'state': ''.join(list_of_details[6]),
            'state_name': state_string
        }
        
        # append dictionary address details to ordered_string outside for loop
        ordered_string += complete_dictionary[number]['state_name'] + '\n..... ' + complete_dictionary[number]['name'] + ' ' + complete_dictionary[number]['address'] + ' ' + complete_dictionary[number]['state_name'] + '\n'
        
        number += 1

        

    print(complete_dictionary)

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
