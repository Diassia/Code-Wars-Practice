def solution(A):
    A.sort()
    A.reverse()
    for number in A:
        if number % 3 == 0:
            return number

A = [-6, -91, 1011, -100, 84, -22, 0, 1, 473]

print(solution(A))