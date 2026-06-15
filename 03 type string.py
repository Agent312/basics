def main():    
    s = (input("input the string: "))
    print(s)
    print(len(s))
    print(type(s))

    while True :
        print(" "
        "[|Choose the operation that you want to condone on the String|]")
        inpSel = input(
        "1.[|select character|] 2.[|select a range of characters|] 3[|.the amount of reapeats of that string|]"
        " 4.[|add string|] 5.[|display characters from selected one to the end|]"
        "6.[|select every which letter in a string will display|] :   "
    )

        if inpSel == "1" :
            c = int(input("input the string character position number (from 0 to max): "))
            print(s[c])

        elif inpSel == "2" :
            a = int(input("input the string character position number (from 0 to max) [minimal]: "))
            b = int(input("input the string character position number (from 0 to max) [maximal]: "))
            print(s[a:b])

        elif inpSel == "3" :
            d = int(input("input the multiplier number: "))
            print(s*d)

        elif inpSel == "4" :
            strIn = (input("input addition to the existing string: "))
            s = s + strIn
            print(s)

        elif inpSel == "5" :
            e = int(input("input the string character position number (from 0 to max) [beginning selector]: "))
            print(s[e:])

        elif inpSel == "6" :
            f = int(input("input the string character position number (from 0 to max) [every what number of characters a character you want to display]: ")) #:3
            print(s[::f])
        elif inpSel == "7" :
            print("stopping function\n")
            break

        else:
            print("Invalid choice. Please select from 1-7. Repeating menu function\n")
main()