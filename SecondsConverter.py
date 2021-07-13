print()
print("===============================================================================")
print("This program converts a value in seconds to days, hours, minutes and seconds.")
print("===============================================================================")
print()

Input = int(input("Please, enter a value that you want to convert, in seconds: "))

### Explains what the program do, then, asks and stores the value given by the user.

Days = Input // 86400 # How many integer days there is.
Hours = (Input % 86400) // 3600 # The rest of the above division divided by 3600 (correspondent value of 1 hour in seconds). 
Minutes = ((Input % 86400) % 3600) // 60 # The rest of the above division divided by 60 (correspondent value of 1 minute in seconds). 
Seconds = (((Input % 86400) % 3600) % 60) # The rest of the above division

### Calculates the values.

print("*****************************************************************************")
print(Days, "days,", Hours, "hours,", Minutes, "minutes and", Seconds, "seconds.")

## Shows the results.
