"""Health management system """

def getDate():
    import datetime
    return datetime.datetime.now()


def function():
    time = getDate()
    print('Enter The Name: 1.salman , 2.sanjay , 3. suresh')
    name=str(input())

    if name=='salman':
        print(f'Welcome {name} ')
        print('Choose 1. for Exercise 2. for Food')
        diet=int(input())

        if(diet==1):
            exercise=str(input("Enter the Exercise name:"))
            with open('salman.txt','a')as f:
                f.write(exercise)
            print(f'Thanks for visiting our organization {name} we store your data ')

        elif(diet==2):
            food=str(input("Enter the Food Name:"))
            with open('salman.txt','a') as f:
                f.write(food)
            print(f'Thanks for visiting our organization {name} we store your data')

        else:
            print('Invalid Data !!')

    elif name == 'sanjay':
        print(f'Welcome {name} ')
        print('Choose 1. for Exercise 2. for Food')
        diet = int(input())

        if (diet == 1):
            exercise = str(input("Enter the Exercise name:"))
            with open('sanjay.txt', 'a')as f:
                f.write(exercise)
            print(f'Thanks for visiting our organization {name} we store your data')

        elif (diet == 2):
            food = str(input("Enter the Food Name:"))
            with open('sanjay.txt.txt', 'a') as f:
                f.write(food)
            print(f'Thanks for visiting our organization {name} we store your data')

        else:
            print("Invalid Data!!!")

    if name == 'suresh':
        print(f'Welcome {name} ')
        print('Choose 1. for Exercise 2. for Food')
        diet = int(input())

        if (diet == 1):
            exercise = str(input("Enter the Exercise name:"))
            with open('suresh.txt', 'a')as f:
                f.write(exercise)
            print(f'Thanks for visiting our organization {name} we store your data')

        elif (diet == 2):
            food = str(input("Enter the Food Name:"))
            with open('suresh.txt', 'a') as f:
                f.write(food)
            print(f'Thanks for visiting our organization {name} we store your data')

        else:
            print("Invalid Data !!!!")

def retreive():
    print('----------Welcome To The Health Management System By Salman--------------')
    print('Press 1 .for Retrieve the data')
    data= int(input())
    if(data==1):
        try:
            function()
        except Exception as e:
            print(e)
    else:
        print("We find wrong in your body hahahah!!!!")


retreive()



