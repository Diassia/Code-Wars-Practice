# Write a function named setAlarm which receives two parameters. The first parameter, employed, is true whenever you are employed and the second parameter, vacation is true whenever you are on vacation.

# The function should return true if you are employed and not on vacation (because these are the circumstances under which you need to set an alarm). It should return false otherwise. Examples:

# setAlarm(true, true) -> false
# setAlarm(false, true) -> false
# setAlarm(false, false) -> false
# setAlarm(true, false) -> true

# def set_alarm(employed, vacation):
#     if employed == True and vacation == True:
#         return False
#     elif employed == True and vacation == False:
#         return True
#     elif employed == True and vacation == False:
#         return False
#     elif employed == False and vacation == False:
#         return False
#     else:
#         return False

def set_alarm(employed, vacation):
    if employed == True and vacation == False:
        return True
    else:
        return False

employed = False
vacation = False

print(set_alarm(employed, vacation))

# CodeWars solution:
#     def set_alarm(employed, vacation):
#         return employed and not vacation