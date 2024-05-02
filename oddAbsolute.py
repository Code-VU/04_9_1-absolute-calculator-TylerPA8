def calculateAbsolute():
    
    # This first line is provided for you
    try:
        in_num  = int(input("Enter a number: "))
        absolute = in_num - 21
        absolute = abs(absolute)
        if in_num > 21:
            absolute *= 2
        print('Result: ' + str(absolute))
    except:
        print('Please enter a numbe')
    # end assignment

## If you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    calculateAbsolute()
