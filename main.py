#Author: Joshua Bukuru
#Completed by: 10/02/2021
#Done in python 3


def orient_checker_Left(c):
    """Check orientation of object to rotate by 90 degrees left as determined by input"""
    if c == "E":
        c = "N"
    elif c == "N":
        c = "W"
    elif c == "W":
        c = "S"
    elif c == "S":
        c = "E"
    return c

def orient_checker_right(c):
    """Check orientation of object to rotate by 90 degrees right as determined by input"""
    if c == "E":
        c = "S"
    elif c == "N":
        c = "E"
    elif c == "W":
        c = "N"
    elif c == "S":
        c = "W"
    return c

def move_x(x, c):
    """Move Rover in x direction as determined by input"""
    if c == "E":
        x += 1
    if c == "W":
        x -= 1
    return x

def move_y(y, c):
    """Move Rover in y direction as determined by input"""
    if c == "N":
        y += 1
    if c == "S":
        y -= 1
    return y


if __name__ == '__main__':
    state = True
    print("Rover challenge\n----------------------------------")
    while state:
        try:
            grid_x, grid_y = input("Enter grid size: ").split()
            grid_x = int(grid_x)
            grid_y = int(grid_y)
            if(grid_x < 0 or grid_y < 0):
               v = input("The grid cannot be negative, if you would you like to restart\n"
                     "enter 'r' or to exit the program enter 'q' : ")
               if v == "r":
                   continue
               elif v == "q":
                   state = False

        except ValueError:
           v = input("You made an error with the input, if you would you like to restart\n"
                     "enter 'r' or to exit program enter 'q' : ")
           if v == "r":
               continue
           elif v == "q":
               state = False

        else:

            move = ""
            end_pos = []
            x = 0
            y = 0
            i = 1
            c = ""
            while move != 'q':
                try:
                    x, y, c = input("Enter the position for rover " + str(i) + " : ").split()
                    x = int(x)
                    y = int(y)
                except ValueError:
                    v = input("You made an error with the input, if you would you like to restart\n"
                              "enter 'r' or to go back to the beginning enter 'q' : ")
                    if v == "r":
                        continue
                    elif v == "q":
                        break
                else:
                    move = input("Enter the movements for rover " + str(i) + " : ")
                    if ((move.__contains__("L")) or move.__contains__("R")) and move.__contains__("M"):
                        move_lists = list(move)
                        for move_list in move_lists:
                            if move_list == "L":
                                c = orient_checker_Left(c)

                            elif move_list == "R":
                                c = orient_checker_right(c)

                            elif move_list == "M":
                                if x <= grid_x and y <= grid_y:
                                    x = move_x(x, c)
                                    y = move_y(y, c)
                    else:
                        v = input("You made an error with the input, if you would you like to restart\n"
                                  "enter 'r' or to go back to the beginning enter 'q' : ")
                        if v == "r":
                            continue
                        elif v == "q":
                            break

                    final_move = str(x) + " " + str(y) + " " + c
                    end_pos.append(final_move)
                    final_move = ""
                    i += 1
                    move = input("Enter 'q' to quit or 'c' to continue with the next rover: ")
                    if move == "q":
                        state = False
                #print(end_pos)
    print("----------------------------------\n"
          "The final postion of all rovers are: ")
    for output in end_pos:
        print(output)







