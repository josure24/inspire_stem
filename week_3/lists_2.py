friends = ["luta","calz","cate","josiah","bevern"]

for friend in friends:
    print(friend)


    enemies = friends[:] # to copy one list to another
    print(enemies)

    fruits = ["mango","kiwi","ovacado","apple","grapes"]

    # slice`` the list 

    print(fruits[0.3])

    del fruits[0]

    print(fruits)

    squares = [] # initializes at empty list

    for x in range(0,11):
        squares.append(x**2)

        print(squares) 






