# lee bernard
# calculator
import test

def list_for_selection():
    print("this is whole whole number calculator meaning every number inputted needs be be whole, no decimal.")
    print("+ for addition")
    print("- for subtraction")
    print("* for multiplication")
    print("/ for division")
    print("^ for power")
    print("% for whole number and remainder")
    print("list for list option")
    print("type the word [stop] to stop ")
    print("\n")
def main():

    x = 0
    while not x == 1:
        list_for_selection()
        operation = input("what operation do you want to do: ")
    # addition
        if operation == "+":
            print("this part does addition")
            add_number_1 = int(input("first number you want to add: "))
            add_number_2 = int(input("second number you want to add: "))
            def add_par(num1, num2):
                num3 = num1 + num2
                print(num1, "+", num2, "is", num3)
                if num3 == 42069 or num3 == 420 or num3 == 69:
                    print("stop"*100)

            add_par(add_number_1, add_number_2)
        # subtraction
        elif operation == "-":
            print("this part does subtraction")
            sub_number_1 = input("first number you want to subtract: ")
            sub_number_2 = input("second number you want to subtract: ")

            sub_real_number_1 = int(sub_number_1)
            sub_real_number_2 = int(sub_number_2)

            subtraction = sub_real_number_1 - sub_real_number_2
            print(sub_number_1, "-", sub_number_2, "is", subtraction)

        # multiplication
        elif operation == "*":
            print("this part does multiplication")
            multi_number_1 = input("first number you want to multiply: ")
            multi_number_2 = input("second number you want to multiply: ")

            multi_real_number_1 = int(multi_number_1)
            multi_real_number_2 = int(multi_number_2)

            k = "1"

            if multi_number_2 == k:
                print("the answer is what you" + " put in the first input but if you really "
                                                 "need the answer it's", multi_real_number_1)
            else:
                multiplication = multi_real_number_1 * multi_real_number_2
                print(multi_number_1, "*", multi_number_2, "is", multiplication)

        # division
        elif operation == "/":
            print("this part does division")

            divide_number_1 = input("first number you want to divide: ")
            divide_number_2 = input("second number you want to divide: ")

            divide_real_number_1 = int(divide_number_1)
            divide_real_number_2 = int(divide_number_2)
            k = "1"

            if divide_number_2 == k:
                print("the answer is what you put in the first input but if you can't "
                      "do basic division it's", divide_real_number_1)
            else:
                division = divide_real_number_1 / divide_real_number_2
                print(divide_number_1, "/", divide_number_2, "is", division)

        # power
        elif operation == "^":
            print("this part allows you to power numbers")
            pow_number_1 = input("the number you want to be powered: ")
            pow_number_2 = input("how much power do you want: ")

            pow_real_number_1 = int(pow_number_1)
            pow_real_number_2 = int(pow_number_2)

            power = pow_real_number_1 ** pow_real_number_2
            print(pow_number_1, "to he power of", pow_number_2, "is", power)

            hj = "20"

            if pow_number_2 >= hj:
                print("no one man should have all that power "*2)
            # lyric from Kanye West - POWER

        # whole number and remainder
        elif operation == "%":

            print("this part tell you how many times the first "
                  "number can go into the second number and what the remainder is")

            whole_number_1 = input("the first number you want to divide: ")
            whole_number_2 = input("the second number you want to divide: ")

            whole_real_number_1 = int(whole_number_1)
            whole_real_number_2 = int(whole_number_2)

            whole_number = whole_real_number_1 // whole_real_number_2
            rest_number = whole_real_number_1 % whole_real_number_2
            if whole_real_number_1 < whole_real_number_2:
                print("first number needs to be greater than the second one")
            elif rest_number == 0:
                print(whole_number_1, "can be " + "divided by", whole_number_2, "a grand total of", whole_number,
                      "times and there isn't any remainder")
            else:
                print(whole_number_1, "can be " + "divided by", whole_number_2, "a grand total of", whole_number,
                      "times" + " and the remainder is", rest_number)
        elif operation == "stop":
            x += 1
        elif operation == "list":
            print("> to find the greatest in a list with a known length")
            print("< to find the smallest in a list with a known length")
            print(">? to find the greatest in a list with a unknown length")
            print("<? to find the smallest in a list with a unknown length")
            print("type the word [stop] to stop ")
            operation = input("what operation do you want to do: ")
            if operation == ">":
                test.known_great()
            elif operation == "<":
                test.known_small()
            elif operation == ">?":
                test.unknown_great()
            elif operation == "<?":
                test.unknown_small()
            elif operation == "stop":
                x -= -1
        else:
            print("please read carefully ", end="")
            print("choose a valid option", " or make sure you only put the symbol in the list above", sep="")
            list_for_selection()
            operation = input("what operation do you want to do: ")
            print("\n")
main()
