#Marty Wallace CIS261 MovieGuidePart1

def menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add - Add a movie")
    print("del - Delete a movie")
    print("exit - Exit program")
    print()
    command()
    
def command():
    selection = input("Command:")
    if selection.lower() == "list":
        list_movies(contents)
    elif selection.lower() == "add":
        add(contents)
    elif selection.lower() == "del":
        delete(contents)
    elif selection.lower() == "exit":
        end()
    else:
        print("Please enter a valid command from command menu")
        menu()
    
def movie_list():
    global contents
    contents = [
        "Monty Python and the Holy Grail",
        "On the Waterfront",
        "Cat on a Hot Tin Roof"
        ]
    return contents
    
def list_movies(items):
    for index, val in enumerate(items):
        print(f"{index + 1}. {val}")
        print()
    command()

def add(items):
    new_movie = input("Name: ")
    items.append(new_movie)
    print(f"{new_movie} was added.")
    print()
    command()

def delete(item):
    del_movie = int(input("Number: ")) - 1
    if del_movie + 1 <= len(item):
        print(f"{item[del_movie]} was removed.")
        item.remove(item[del_movie])    
        print()
        command()
    else:
        print("Invalid movie number")
        print()
        command()

def end():
    print("Bye!")
    
if __name__ == "__main__":
    movie_list()
    menu()    