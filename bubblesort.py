# Main function
def bubblesort(list):
    for i in range(len(list) - 1,0,-1):
        for x in range(i):
            if list[x] > list[x+1]:
                temp = list[x]
                list[x] = list[x+1]
                list[x+1] = temp
    return list

# Input loop
sort = []
num = int(input("Enter number of inputs: "))
for n in range(0,num):
    ele = int(input("Element : "))
    sort.append(ele)

print("After sorted ",bubblesort(sort)) # Output
