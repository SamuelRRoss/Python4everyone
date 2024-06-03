largest = None
smallest = None
num_array = ()

while True:
    num = input("Enter a number:")
    

    if num == "done":
        break
    print(num)

    try:
        num = float(num)
    except:
        print("num must be a number or done")

print("Maximum", largest)
