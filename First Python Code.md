
# Background
Sample code and markdown file
- Simple Hello World program
- Simple Fibonacci sequence program



    #Hello world
    print 'Hello world!'

    Hello world!
    


    #Fibonacci
    y = input("Enter end number for Fibonacci sequence: ")
    
    fibonacci = 0
    trail = 1
    
    while fibonacci < y:
        print(fibonacci)
        fibonacci = fibonacci + trail
        trail = fibonacci - trail

    Enter end number for Fibonacci sequence: 29
    0
    1
    1
    2
    3
    5
    8
    13
    21
    
