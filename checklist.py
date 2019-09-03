#Liya Tilahun
#checklist.py
#https://stackoverflow.com/questions/7108080/python-get-the-first-character-of-the-first-string-in-a-list (I used this example to
#access each string character)
#https://stackoverflow.com/questions/3559559/how-to-delete-a-character-from-a-string-using-python (Used this example to replace characters in a string
#for the unmarked function)

#empty list
checklist = []

#create
def create(item):
    checklist.append(item)

#READ
def read(index):
    return checklist[index]

#UPDATE
def update(index, item):
    checklist[index] = item

#DESTROY
def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def markCompleted(index):
    for i in range(len(checklist)):
        if index == i:
            print(update(index,"√"+str(read(index))))

def unmarked(index):
    for i in range(len(checklist)):
        if index == i:
            word = read(index)
            if word[0] == "√":
                newStr = word.replace("√", "")
                update (index, newStr)

def index_test(index):
    if index < len(checklist) and index >= 0:
        return True
    else:
         print("index out of bounds, try a number in the range of 0 and %d, not including %d" % (len(checklist), len(checklist)))

def select(function_code):
    if function_code == "A":
        input_item = user_input("Input item: ")
        create(input_item)

    elif function_code == "R":
        item_index = user_input("Index Number?")
        if index_test(int(item_index)) == True:
            print(read(int(item_index)))

    elif function_code == "P":
        list_all_items()

    elif function_code == "M":
        list_all_items()
        marked = int(user_input("select which index you want to mark as complete: "))
        if index_test(marked) == True:
            markCompleted(marked)
            list_all_items()

    elif function_code == "X":
        list_all_items()
        unmark = int(user_input("select which index you want to unmark: "))
        if index_test(unmark) == True:
            unmarked(unmark)
            list_all_items()

    elif function_code == "U":
        list_all_items()
        index = int(user_input("type the index you want to update"))
        if index_test(index) == True:
            item = user_input("type the new item")
            update(index, item)
            list_all_items()

    elif function_code == "Q":
        return False

    elif function_code == "D":
        list_all_items()
        index = int(user_input("which index to delete"))
        if index_test(index) == True:
            destroy(index)

    else:
        print("Unknown Option")
    return True

def user_input(prompt):
    user_input = input(prompt)
    return user_input

#TEST
#def test():
#    print("creating...")
#    create("purple sox")
#    create("red cloak")
    #print("reading and printing...")
    #print(read(0))
    #print(read(1))
    #print("updating...")
    #update(0, "purple socks")
    #print(read(0))
    #print(read(1))
    #print("destroying index #0...")
    #destroy(0)
    #list_all_items()
    #print("printing index #0")
    #print(read(0))
    #list_all_items()
    #select("A")
    #list_all_items()
    #select("R")
    #list_all_items()
    #select("P")
    #markCompleted(0)
    #list_all_items()
    #unmarked(0)
    #list_all_items()
    #user_value = user_input("Please Enter a value:")
    #print(user_value)

#test()
running = True
while running:
    selection = user_input(
    "Press A to add to list, R to Read from list, P to display list, U to update, D to delete, M to mark complete, X to unmark and Q to quit").upper()
    running = select(selection)
