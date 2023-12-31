import allRoom as room #mport the allroom that I write array there
import member as mem #import member as mem for member point payment
import temp as tm #import temp to add temp array to it

def showAll(): #this is show all the room that we have
    print("")
    number = 1 # make up some number to make it look good
    for element in room.roomAll: # loop to print data in array
        print(number , end = " ")
        print(element)
        number += 1

def showAllTrueRoom():
    print("")
    number = 1 
    tm.check_true()
    for element in tm.temp_array:
        print(number , end = " ")
        print(element)
        number += 1
    

def add(): # this is function write to add new room to array and dict on allRoom.py
    showAll()
    rAdd = input("\nAdd room and number of it : ") # ask staff to enter the new room to add it in to array
    room.roomAll.append(rAdd)

    ##make it have price and bol 

    roomindex = len(room.roomAll) - 1 
    newroom = room.roomAll[roomindex]
    room.roomPrice[newroom] = 300
    room.roomStatus[newroom] = True

    staff_ui() # make programstill runing by going back to staff page

def delete(): # same as add but this time to delete it
    showAll()
    rDel = input("\nWhich you want to delete : ") # same as add but this time aask to delete data in array
    if rDel in room.roomAll:
        print(f"{rDel} has already delete\n")
        room.roomAll.remove(rDel)
        del room.roomPrice[rDel]
        del room.roomStatus[rDel]

        staff_ui() # make programstill runing by going back to staff page

    else:
        print("Invalid variable")
        delete()

def checkIN(): # this function to make room can be avilable and unavilable
    showAll()
    CheckN = input("\nWhich room user wanna check in : ") # ask which room user check in and make it off for people who wanna stay next
    if CheckN in room.roomAll: # check for is the room that staff enter is there or not
        print(f"{CheckN} has already check in\n") # is on == make that room status false
        room.roomStatus[CheckN] = False

        staff_ui()# make programstill runing by going back to staff page

    elif CheckN == "99" : # this is how to go back to menu
        staff_ui()

    else: # is not on == go back to Checkin page again
        print("Invalid variable")
        checkIN()

def checkOut(): # same as check in but this time when user are check out
    showAll()
    CheckO = input("\nWhich room user wanna check out : ")
    if CheckO in room.roomAll: # check is input is on array or not
        print(f"{CheckO} has already check in\n")
        room.roomStatus[CheckO] = True # make status of that room go to True

        staff_ui()# make programstill runing by going back to staff page

    elif CheckO == '99':
        staff_ui()

    else:
        print("Invalid variable")
        checkOut()

def roomInfo(): # just make up room info
    print("## Type 1 ##")
    print("1 King Bed")
    print("1 Bathtub")
    print("with Balcony")

    print("")

    print("## Type 2 ##")
    print("2 Bed") 
    print("1 Bathtub")
    print("with Balcony")

def internetbanking(): # this is for internet banking playment
    print("\nYou choose internet banking")
    print("scan this QR")
    print("this is QR.jpg not text")
    print("are you done with payment")
    answer = input("(yes/no) : ")
    if answer == "yes":
        print(f"complete booking {tm.get_temp()}") # make user know that they already complete booking
        room.roomStatus[tm.get_temp()] = False # set status to false
    elif answer == "no":
        print("Are you really going to cancel the payment")
        answert = input("yes/no : ")
        if answert == "yes":
            print("going back to main menu\n")
            user_ui()
        elif answert == "no":
            print("going back to internet backing page\n")
            internetbanking()
        else:
            print("invalid variable")
            internetbanking()
    else:
        print("invalid variable")
        internetbanking()

def memberP(): # for people who use member point for payment
    print("\nYou choosing member point payment")
    print("You need to enter id and password first")
    print("Enter 99 to id to cancel everything")

    id = input("ID : ") # enter ID
    password = input("Password : ") # enter password

    if id in mem.member: # check id which thatin array of ID or not
        if mem.member[id] in password: # same as ID but password
            if mem.memberPoint[id] >= 10: #check is there have enough point to pay or not
                print("you already pay 10 point") 
                mem.memberPoint[id] -= 10 # minus 10 point for payment
                print(f"you have {mem.member[id]}")
            else:
                print("you dont have enough member point")
                print("going back to payment page")
                payment()
        else:
            print("Worng Password!")
            memberP()

    elif id == '99':
        print("Going back to User menu")
        user_ui()
    else:
        print("Worng ID!")
        memberP()

def payment(): # select payment for self booking user
    print("\nChoose Payment for booking this room")
    print("300 Bath for Money")
    print("10 point for Member")
    print("")
    print("1 Internet Banking")
    print("2 Member Point")
    print("Enter 99 to go back to main menu")
    payment = input("")

    if payment == "1": # 1 go to internet banking
        internetbanking()
    elif payment == "2": # 2 go to memberpoint payment
        memberP()
    elif payment == "99":
        user_ui()
    else:
        print("Invalid variable")
        payment()

def room_booking(): #self booking
    showAllTrueRoom()
    print("You are in room booking right now")
    print("Enter 99 to go back to main menu")
    rbooking = input("Which room you wanna booking : ")

    if rbooking in room.roomAll: # check is input are in the array or not
        print(f"are you going to booking {rbooking}")
        yon = input("(yes/no) : ")

        if yon == "yes":
            tm.set_temp(rbooking)
            print(f"you booking {rbooking}")
            payment()

        elif yon == "no":
            print(f"you cancel booking {rbooking}")
            print(f"Going back to room booking {rbooking}")
            user_ui()

        else:
            print("invalid Variable")
            room_booking()

    else:
        print("Invalid variable")
        room_booking()

def staff_ui(): # just staff text interface
    print("## Welcome to Staff UI ##")
    print("1 Check in")
    print("2 Check out")
    print("3 Delete")
    print("4 Add")
    print("## Type all the name of room colectly ##")
    staff = input("")

    if(staff == '1'):
        checkIN()
    elif(staff == '2'):
        checkOut()
    elif (staff == '3'):
        delete()
    elif(staff == '4'):
        add()
    elif(staff == '99'):
        role_selecter()
    else:
        print("Invalid valiable\n")
        staff_ui()

def user_ui(): # just user text interface
    print("## Welcome User ##")
    print("Which room size that you want to book in")
    print("1 Show all room")
    print("2 Show room info")
    print("3 Book Room")
    user = input("")

    if(user == '1'):
        showAll()
        user_ui()
    elif(user == '2'):
        roomInfo()
        user_ui()
    elif(user == '3'):
        room_booking()
        user_ui()
    elif (user == '99'):
        role_selecter()
    else:
        print("Invalid valiable\n")
        user_ui()

def role_selecter(): # role select to make user determine that this code use for user or staff
    print("Who use this")
    print("1 User")
    print("2 Staff")
    select = input("")

    if(select == '1'):
        print("")
        user_ui()
    elif(select == '2'):
        print("")
        staff_ui()
    else:
        print("Invalid valiable\n")
        role_selecter()

def main(): # main function to make it complex
    role_selecter()

main() # only run main