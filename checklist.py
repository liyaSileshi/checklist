checklist=["LIYA","red","redu"]

#create
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[index]

# UPDATE
def update(index, item):
    checklist[index] = item

# DESTROY
def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        #print(str(index) + list_item)
        print("{} {}".format(index, list_item))
        index += 1

def markCompleted(index):
    for i in range(len(checklist)):
        if index==i:
            print(update(index,"√"+str(read(index))))

def index_test(index):
    if index<len(checklist) and index>=0:
        return True
    else:
         print("index out of bounds, try a number in the range of 0 and %d, not including %d" % (len(checklist), len(checklist)))
def select(function_code):
    # Create item
    if function_code == "A":
        input_item = user_input("Input item:")
        create(input_item)
    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")
        if index_test(int(item_index))==True:
            print(read(int(item_index)))

            #else
    # Print all items
    elif function_code == "P":
        list_all_items()

    elif function_code=="M":
        list_all_items()
        marked= int(user_input("select which index you want to mark as complete"))
        if index_test(marked)==True:
            markCompleted(marked)
            list_all_items()

    elif function_code=="U":
        list_all_items()
        index=int(user_input("type the index you want to update"))
        if index_test(index)==True:
            item=user_input("type the new item")
            update(index, item)

    elif function_code=="Q":
        return False

    elif function_code=="D":
        list_all_items()
        index=int(user_input("which index to delete"))
        if index_test(index)==True:
            destroy(index)

    # Catch all
    else:
        print("Unknown Option")
    return True
def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input
#TEST
#def test():
    # Add your testing code here
    #print("creating...")
    #create("purple sox")
    #create("red cloak")
    #print("reading and printing...")
    #print(read(0))
    #print(read(1))
    #print("updating...")
    #update(0, "purple socks"
    #print("destroying index #1...")
    #destroy(1)
    #print("printing index #0")
    #print(read(0))
    #list_all_items()
    #select("C")
    #list_all_items()
    #select("R")
    #list_all_items()
    #markCompleted(0)
    #user_value = user_input("Please Enter a value:")
    #print(user_value)
running = True
while running:
    selection = user_input(
    "Press A to add to list, R to Read from list, P to display list, U to update, D to delete, M to mark complete and Q to quit").upper()
    running = select(selection)
#test()
