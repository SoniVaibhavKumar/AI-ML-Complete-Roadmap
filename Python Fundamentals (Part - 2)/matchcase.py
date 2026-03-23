color = input("Enter a color: ")

match color :
    case "Green":
        print("Go")
    case "Red":
        print("Stop")
    case "Yellow":
        print("Great")
    case _:
        print("Wrong color")