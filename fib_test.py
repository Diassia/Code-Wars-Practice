def fizz_buzz(fibonacci):
    fb_fibonacci = []
    for number in fibonacci:
        if number % 3 == 0 and number % 5 == 0:
            fb_fibonacci.append('FizzBuzz')
        elif number % 3 == 0:
            fb_fibonacci.append('Fizz')
        elif number % 5 == 0:
            fb_fibonacci.append('Buzz')
        else:
            fb_fibonacci.append(number)
    return fb_fibonacci

fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

print(fizz_buzz(fibonacci))