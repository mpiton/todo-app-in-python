FILENAME = "todoList.txt"

f = open(FILENAME, "a")
f.close()


def add_todo():
    """
    Ajouter une tâche au fichier todoList.txt
    """
    file = open(FILENAME, "a")
    todo = input("Quelle est votre tâche à ajouter ? : ")
    file.write(str(todo))
    file.close()
    print("Todo added with success")


def todo_list():
    """
    Affiche le contenu du fichier todoList.txt
    """
    file = open(FILENAME, "r")
    print("Todo List: ")
    for todo in file:
        print(todo)
    file.close()


def search_todo():
    """
    La fonction recherche une tâche dans le fichier et renvoie un message si elle est trouvée ou non
    """
    file = open(FILENAME, "r")
    searched_todo = input("Entrer la tâche à chercher : ")
    if searched_todo in file.read():
        print(searched_todo, " est dans ma liste")
    else:
        print(searched_todo, " n'est pas dans la liste")
        print("\n")
        yes_or_not = input("L'ajouter ?")
        if yes_or_not.lower() == "oui":
            file.close()
            file = open(FILENAME, "w")
            file.write("\n")
            file.write(str(searched_todo))
    file.close()


def menu():
    """
    Affiche le menu
    Demande à l'utilisateur de choisir un numéro
    Selon le choix, effectue l'une des actions suivantes:
    Ajoute une tâche
    Recherche une tâche
    Affiche la liste des tâches
    Quitte le programme
    """
    print("1- Ajouter une tâche")
    print("2- Rechercher une tâche")
    print("3- Voir la liste des tâches")
    print("4- Quitter !")

    choice = input("Que veux tu faire ? (De 1 à 4) ")

    if choice == "1":
        add_todo()
        menu()
    elif choice == "2":
        search_todo()
        menu()
    elif choice == "3":
        todo_list()
        menu()
    elif choice == "4":
        print("Au revoir")
    else:
        print("Votre choix est invalide")
        menu()


# Appel du menu
menu()
