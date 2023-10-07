import matplotlib.pyplot as plt


def main():

    x = [1]
    y = [0]
    
    iterations = int(0)
    step = int(1)
    s = step

    

    while True:
        try:
            i = int(input("Input a positive integer as a max. value to be checked by the 3x+1 conjecture: "))
            if i <= 0:
                print("Invalid Input...")
                main()
            else:
                break
            
        except ValueError:
            print('Please enter an integer.')

    for step in range(1, i+1):

        iterations = 0
        #print("iterations: ", iterations)
        
        s = step
        #print(s)
        
        while s != 1:

            if s % 2 == 0:

                s /= 2


                iterations += 1

                if s == 1:

                    x.append(step)

                    y.append(iterations)

                    #print(iterations, "iterations taken for step ", step)

                    break


            if s % 2 != 0:
        
                s *= 3
                s += 1


                iterations += 1

                if s == 1:

                    x.append(step)

                    y.append(iterations)

                    #print(iterations, "iterations taken for step ", step)

                    break





    plt.scatter(x, y, label = "point", color= "blue", 
            marker= ".")

    #-------------------------------------------
    #See Data Points:

    #print(*x, sep = ', ')
    #print(*y, sep = ', ')

    #c = 0

    #for j in x:
            #print("(", j, ",", y[c], ")")

            #c += 1
    

    #-------------------------------------------

    
    plt.axhline(y=1, color='red')
    #plt.axhline(y=10, color='green')

    #plt.axhline(x=, color = 'green')


   
    # x-axis label
    plt.xlabel('number of steps')

    # frequency label
    plt.ylabel('number of iterations')

    # plot title
    plt.title('Collatz Conjecture')

    # showing legend
    plt.legend()
  
    # function to show the plot
    plt.show()
    
    #print("number of iterations taken to reach 1: ", iterations)
    

while True:
    main()
    
    
        

