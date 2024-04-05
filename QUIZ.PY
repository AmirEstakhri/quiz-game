def main():
    qusation = { 
        "is bmw in germnay?" :"yes" ,
        "is benz is germany?"  :"yes" , 
        "is sony in germnay?"  : "no" }  
    options =  ["yes", "no"] 

    score = 0 
    qusation_num = 1 

    for q in qusation : 
        print (f"ur at  qusation #{ qusation_num} " ) 
        qusation_num += 1
        print ("-----------------------------------") 
        print(q)
        awnser  = input ("write ur awnser(yes or no) :")
        awnser = awnser.lower()
        if awnser == qusation[q] : 
            print ("correct!!!")     
            score += 1
            
        else :
            print ("worng!!!")
    
    print (f"ur score is : 3/{score}")


    play_again = input(" do u want to play again ? (yes or no) :")
    while play_again == "yes":
            print("ok  we start again :") 
            main()
    else:
         print("ok gl ")
         exit
main()