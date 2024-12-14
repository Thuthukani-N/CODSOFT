def main():

    while True:
        print("MENU")
        print("1. ADDITION")
        print("2. SUBTRACTION")
        print("3. MULTIPLICATION")
        print("4. DIVISION")
        print("5.EXIT")

        choice= input("ENTER YOUR CHOICE : ")

        if choice =="1" :
            num1= float(input("ENTER THE FIRST NUMBER : "))
            num2= float(input("ENTER THE SECOND NUMBER : "))

            result = num1 + num2

            print(f"The answer is : {result}")

        elif choice=="2":
            num1= float(input("ENTER THE FIRST NUMBER : "))
            num2= float(input("ENTER THE SECOND NUMBER : "))

            result = num1 - num2

            print(f"The answer is : {result}")

        elif choice=="3":
            num1= float(input("ENTER THE FIRST NUMBER : "))
            num2= float(input("ENTER THE SECOND NUMBER : "))

            result = num1 * num2

            print(f"The answer is : {result}")

        elif choice=="4":
            num1= float(input("ENTER THE FIRST NUMBER : "))
            num2= float(input("ENTER THE SECOND NUMBER : "))

            if num2!=0 :
                result = num1 / num2
                print(f"The answer is : {result}")

            else:
                print("UNDEFINED")

        elif choice=="5":
            print("EXITING...")
            break

        else :
            print ("INVALID OPTION")

main()



