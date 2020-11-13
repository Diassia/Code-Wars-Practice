def solution(phone_numbers, phone_owners, number):
    phone_number_index = 0

    for phone_number in phone_numbers:
        if phone_number == number:
            return phone_owners[phone_number_index]
        else:
            phone_number_index += 1
    return number


phone_numbers = ["234-567-890", "444-444-444", "321-543-234"]
phone_owners = ["Harry", "Nick", "Michael"]
number = "445-444-444"

print(solution(phone_numbers, phone_owners, number))