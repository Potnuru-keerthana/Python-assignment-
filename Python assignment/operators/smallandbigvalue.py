# Find the smaller and biggest value

def find_min_max(num1, num2):
    if num1 < num2:
        smaller = num1
        larger = num2
    else:
        smaller = num2
        larger = num1
    print("smaller",smaller)
    print("larger",larger)

#example
find_min_max(20, 8)