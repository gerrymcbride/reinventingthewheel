
def mean():
    #run function for user input and empty list to sort data    
    x_list = []
    run = True
    while run == True:
        sum_1 = input("List your numbers: Type finish to stop")
        x_list.insert(1, str(sum_1))
        print (x_list)
        #exit while loop and remove 'finish' from input list
        if sum_1 == ('finish'):
            x_list.remove('finish')
            run = False
            #algorithm for average
            x_list = [int(x) for x in x_list]
            print (sum(x_list)/len(x_list))


            
def median ():
 #run function for user input and empty list to sort data
    x_list = []
    run = True
    while run == True:
        sum_1 = input("List your numbers: Type finish to stop")
        x_list.insert(1, str(sum_1))
        print (x_list)
        
        # sorts list 
        
        if sum_1 == ('finish'):
            x_list.remove('finish')
            x_list = [int(x) for x in x_list]
            x_list = sorted(x_list)
            x_list1 = len(x_list)
            run = False
        #if even sum of list is even:    
            if x_list1 % 2 == 0:
                x = x_list1 / 2
                #algorithm to establish which integer + x forms the mid point of set
                if len(range(x_list[round(x)], x_list1)) <= len(range(x_list[round(x)-1],x_list1)):
                    result = x_list[int(x)] + x_list[int(x-1)]
                    print (result/2)
                elif len(range(x_list[round(x)], x_list1)) >= len(range(x_list[round(x)-1],x_list1)):
                    result = x_list[int(x)] + x_list[int(x-1)]
                    print (result/2)
            # odd sum list
            else:
                x = x_list1 /2
                print (x_list[int(x)])

   

    
    
