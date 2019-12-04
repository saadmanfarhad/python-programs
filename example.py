noOfCats = input()
try:
    if int(noOfCats) < 0:
        print('You have entered a negative number')
    elif int(noOfCats) < 5:
        print('Not many')
    else:
        print('Many')
except:
    print('Invalid input')
