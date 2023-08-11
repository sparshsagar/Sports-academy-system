#Sparsh Sagar



#admin login function
def adminlogin():
    adminuserID = "a"
    adminpwd = "admin@123"
    while True:
        adminusername = input("Enter admin username:\n")
        if len(str(adminusername)) == 0:
            print("No value is entered. Please enter correct username.")
            continue
        elif adminusername == adminuserID:
            print ("Username is correct")
            break
        else:
            print(" Wrong username \n Please enter correct username.")
            continue
        
    while True:
        adminpassword = input("Enter admin password:\n")
        if len(str(adminpassword)) == 0:
            print("No value entered !! type again")
            continue
        elif adminpassword == adminpwd:
            print ("Password is correct")
            print (" Login verfied ")
            print("-------Welcome to Admin page-------")
            break
        else:
            print(" Wrong password \n Please enter correct password.")
            continue
#add records of sport
def addrecordssport():
    cnt = 0
    while True:
        try:
            loop = int(input("Enter number of sports you want to add:"))
            break
        except ValueError:
            print("Value entered is not valid")
            continue
    for cnt in range(loop):
        print("Enter sport", cnt+1, "details---")
        while True:
            sportname = input("Enter sport name:")
            if len(sportname) == 0:
                print("No value is entered.")
                continue
            else:
                break
        while True:
            sportID = input("Enter Sport ID:")
            if len(sportID) == 0:
                print("No value is entered.")
                continue
            else:
                break
        
        print("Checking if Sport ID already exists in database\n ---------------")
        sportfile = open("sportdetailfile.txt","r")
        for line in sportfile:
                lines = line.strip()
                row = lines.split("\t")
                if sportID == row[0]:
                    print("Sport ID already exists.")
                    adminuser()
                else:
                    break
        print("Sport ID is unique")
        while True:
            sportcentername = ""
            sportcenterID = ""
            user = int(input("Choose a Sport center: \n1. Royal Champions Sports Academy Bukit Jalil \n2. Royal Champions Sports Academy Kuala Lumpur \n3. Royal Champions Sports Academy Damansara \n :"))
            if user == 1:
                print("Sport center chosen - Royal Champions Sports Academy Bukit Jalil")
                sportcenterID = " RCSA BKJ "
                sportcentername = "Royal Champions Sports Academy Bukit Jalil"
                print ("Sport center ID is:",sportcenterID)
                break
            elif user == 2:
                print("Sport center chosen - Royal Champions Sports Academy Kuala Lumpur")
                sportcenterID = " RCSA KUL "
                sportcentername = "Royal Champions Sports Academy Kuala Lumpur"
                print ("Sport center ID is:",sportcenterID)
                break
            elif user == 3:
                print ("Sport center chosen - Royal Champions Sports Academy Damansara")
                sportcenterID = "RCSA DMS"
                sportcentername = "Royal Champions Sports Academy Damansara"
                print ("Sport center ID is:",sportcenterID)
                break
            else:
                print (" Number is not valid. \n Please choose again")
                continue
        
        sportfile = open("sportdetailfile.txt","a")
        sportfile.write(sportID+"\t"+sportname+"\t"+sportcentername+"\t"+sportcenterID+"\n")
        sportfile.close()
#add sport schedule
def addsportschedule():
    cnt = 0
    while True:
        try:
            loop=int(input("Enter number of sports you want to add schedules for:"))
            break
        except ValueError:
            print("Value entered is not valid")
            continue
    for cnt in range(loop):
        print("Enter sport", cnt+1, "schedule---")
        while True:
            sportschedulename = input("Enter sport name:")
            if len(sportschedulename) == 0:
                print("No value is entered.")
                continue
            else:
                break
        while True:
            sportscheduleID = input("Enter Sport ID:")
            if len(sportscheduleID) == 0:
                print("No value is entered.")
                continue
            else:
                break
        print("Checking if Sport ID already exists in database---\n ---------------")
        sportfile = open("sportdetailfile.txt","r")
        for line in sportfile:
            lines = line.strip()
            row = lines.split("\t")
            if sportscheduleID == row[0]:
                print("Sport ID found!")

        print("Enter Sport schedule for:",sportschedulename)
        sportschedule1 = input("Enter schedule for U-9 boys/girls (Example - 8am-11am Friday :")
        sportschedule2 = input("Enter schedule for U-12 boys/girls (Example - 8am-11am Wednesday:")
        sportschedule3 = input("Enter schedule for U-15 boys/girls (Example - 8am-11am Saturday:")
        sportschedule4 = input("Enter schedule for U-17 boys/girls (Example - 8am-11am Monday:")
        schedulefile = open("sportscheduledetailfile.txt","a")
        schedulefile.write(sportscheduleID+"\t"+sportschedulename+"\t"+sportschedule1+"\t"+sportschedule2+"\t"+sportschedule3+"\t"+sportschedule4+"\n")
        schedulefile.close()
        
#add records of coach
def addrecordscoach():
    cnt = 0

    while True:
        try:
            loop = int(input("Enter number of coaches you want to add:"))
            break
        except ValueError:
            print("Value entered is not valid")
            continue
    for cnt in range(loop):
        print("Enter coach", cnt+1, "details---")
        while True:
            coachname = input("Enter Coach name:")
            if len(coachname) == 0:
                print("No value is entered.")
                continue
            else:
                break
        while True:
            coachID = input("Enter Coach ID:")
            if len(coachID) == 0:
                print("No value is entered.")
                continue
            else:
                break
            
        print("Checking if Coach ID already exists in database---\n ---------------")
        coachfile = open("coachdetailfile.txt","r")
        for line in coachfile:
                lines = line.strip()
                row = lines.split("\t")
                if coachID == row[0]:
                    print("Coach ID already exists.")
                    adminuser()
                else:
                    print("")
                
        print("Coach Id is unique!")        
        while True:
            coachdatejoined = input("Enter Coach date joined:")
            if len(coachdatejoined) == 0:
                print("No value is entered.")
                continue
            else:
                break
        while True:
            coachdateterminated = input("Enter Coach date terminated:")
            if len(coachdateterminated) == 0:
                print("No value is entered.")
                continue
            else:
                break
        while True:
            coachhourlyrate = input("Enter Coach hourly rate (in Rm):")
            if len(coachhourlyrate) == 0:
                print("No value is entered.")
                continue
            else:
                break
        while True:
            coachphonenumber = input("Enter Coach phone number:")
            if len(coachphonenumber) == 0:
                print("No value is entered.")
                continue
            else:
                break
        while True:
            coachaddress = input("Enter Coach address:")
            if len(coachaddress) == 0:
                print("No value is entered.")
                continue
            else:
                break
        
        #open sports file and display
        sportsfile = open("sportdetailfile.txt","r")
        for rows in sportsfile:
            print("code\tCoach name\tSport center name\t\t\t\tSport center code")
            print(rows+""+sportsfile.read())

        #ask admin to enter sport related coach stuff
        while True:
            coachsport = input("Enter Coach sport:")
            if len(coachsport) == 0:
                print("No value is entered. Please enter correct username.")
                continue
            else:
                break
        while True:
            coachsportcode = input("Enter code of sport that coach teaches :")
            if len(coachsportcode) == 0:
                print("No value is entered. Please enter correct username.")
                continue
            else:
                break
        while True:
            coachcentername = input("Enter name of sport center where coach teaches :")
            if len(coachcentername) == 0:
                print("No value is entered. Please enter correct username.")
                continue
            else:
                break
        while True:
            coachcentercode = input("Enter code of sport center where coach teaches :")
            if len(coachcentercode) == 0:
                print("No value is entered. Please enter correct username.")
                continue
            else:
                break
        coachrating="0"
        coachfile = open("coachdetailfile.txt","a")
        coachfile.write(str(coachID)+"\t"+coachname+"\t"+coachdatejoined+"\t"+coachdateterminated+"\t"+coachhourlyrate+"\t"+coachphonenumber+"\t"+coachaddress+"\t"+coachsport+"\t"+coachsportcode+"\t"+coachcentername+"\t"+coachcentercode+"\t"+coachrating+"\n")
        coachfile.close()

#search data
def searchdata():
    print("1. Coach \n2. Sport \n3. Student \nPress any other key to terminate\n")
    while True:
        try:
            data = int(input("Which records do you want to search: \n"))
            break
        except ValueError:
            print("Value entered is not valid")
            continue
    if data >= 1 and data <= 3:
        if data == 1:
            print(" 1. By Coach ID \n 2. By Coach rating")
            search = int(input(" How would you like to search data: \n"))
            if search == 1:
                datasearch = input("Enter coach ID to search:")
                coachfile = open("coachdetailfile.txt","r")
                for line in coachfile:
                    lines = line.rstrip()
                    row = lines.split("\t")
                    if datasearch == row[0]:
                        print("Coach ID found!")
                        print(row)
                        adminuser()
                else:
                    print("Coach ID not found in database")
                    adminuser()
                coachfile.close()
            else:
                datasearch = input("Enter coach rating to search:")
                coachfile = open("coachdetailfile.txt","r")
                for line in coachfile:
                    lines = line.strip()
                    row = lines.split("\t")
                    if datasearch == row[11]:
                        print(row)
                        adminuser()
                else:
                    print("Coach rating not found in database")
                    adminuser()
                coachfile.close()  
        elif data ==2:
            datasearch = input("Enter Sport ID to search:")
            sportfile = open("sportdetailfile.txt","r")
            for line in sportfile:
                lines = line.strip()
                row = lines.split("\t")
                if datasearch == row[0]:
                    print("Sport ID found!")
                    print("code\tSport name\tSport center name\t\t\t\tSport center code")
                    print(row)
                    adminuser()
               
            else:
                print("Sport ID not found in database")
                adminuser()
        elif data==3:
            datasearch = input("Enter student ID to search student")
            studentfile = open("newstudentfile.txt","r")
            for line in studentfile:
                lines = line.rstrip()
                row = lines.split("\t")
                if datasearch == row[0]:
                    print(row)
                    adminuser()
            else:
                print("Student ID not found in database")
                adminuser()
            
    else:
        print("")
        print("Are you sure you wan to exit? \nPress 1 to restart from where you left off or 0 to Exit")
        restart = int(input("Enter your decision"))
        if restart == 1:
            searchdata()

#modify records for admin
def modifydataadmin():
    print("-----------Welcome to Modify records-----------")
    print("1.Coach\n2.Sport\n3.Sport Schedule")
    while True:
        try:
            modify_admin = int(input("Which records do you want to modify: \n"))
            break
        except ValueError:
            print("Value entered is not valid")
            continue
    if modify_admin >=1 and modify_admin <=3:
        if modify_admin ==1:
            datasearch = input("Enter Coach ID to search:")
            coachfile = open("coachdetailfile.txt","r")
            new=[]
            for line in coachfile:
                lines = line.strip()
                row = lines.split("\t")
                if datasearch == row[0]:
                    print("Coach ID found!")
                    print("code\tCoach name\tSport center name\t\t\t\tSport center code")
                    print(row)
                    print("1. Code\n2.Sport name\n3. Sport center name \n4. Sport center code")
                    while True:
                        choice = int(input("Enter your choice to modify:"))
                        if choice ==1:
                            ele = row[0]
                            newcoachcode = input("Enter new coach code:")
                            row.remove(ele)
                            row.insert(0,newcoachcode)
                            break
                        elif choice ==2:
                            ele = row[1]
                            newcoachname = input("Enter new coach name:")
                            row.remove(ele)
                            row.insert(1,newcoachname)
                            break
                        elif choice ==3:
                            ele = row[9]
                            newsportcentername = input("Enter new sport center name:")
                            row.remove(ele)
                            row.insert(9,newsportcentername)
                            break
                        elif choice ==4:
                            ele =row[10]
                            newsportcentercode = input("Enter new sport center code:")
                            row.remove(ele)
                            row.insert(10,newsportcentercode)
                            break
                        else:
                            print("Wrong input")
                            continue
                new.append(row)
            coachfile=open("coachdetailfile.txt","w")
            for data in new:
                for data2 in data:
                    coachfile.write(data2)
                    coachfile.write("\t")
                coachfile.write("\n")
            coachfile.close()
            adminuser()
            
        if modify_admin ==2:
            datasearch = input("Enter Sport ID to search:")
            sportfile = open("sportdetailfile.txt","r")
            new=[]
            for line in sportfile:
                lines = line.strip()
                row = lines.split("\t")
                if datasearch == row[0]:
                    print("Sport ID found!")
                    print("code\tSport name\tSport center name\t\t\t\tSport center code")
                    print(row)
                    print("1. Code\n2.Sport name\n3. Sport center name \n4. Sport center code")
                    while True:
                        choice = int(input("Enter your choice to modify:"))
                        if choice ==1:
                            ele = row[0]
                            newsportcode = input("Enter new sport code:")
                            row.remove(ele)
                            row.insert(0,newsportcode)
                            break
                        elif choice ==2:
                            ele = row[1]
                            newsportname = input("Enter new sport name:")
                            row.remove(ele)
                            row.insert(1,newsportname)
                            break
                        elif choice ==3:
                            ele = row[2]
                            new_sportcentername = input("Enter new sport center name:")
                            row.remove(ele)
                            row.insert(2,new_sportcentername)
                            break
                        elif choice ==4:
                            ele =row[3]
                            new_sportcentercode = input("Enter new sport center code:")
                            row.remove(ele)
                            row.insert(3,new_sportcentercode)
                            break
                        else:
                            print("Wrong input")
                            continue
                new.append(row)
            sportfile=open("sportdetailfile.txt","w")
            for data in new:
                for data2 in data:
                    sportfile.write(data2)
                    sportfile.write("\t")
                sportfile.write("\n")
            sportfile.close()
            adminuser()
            
        if modify_admin ==3:
            datasearch = input("Enter Sport ID to search:")
            sportschedulefile = open("sportscheduledetailfile.txt","r")
            new=[]
            for line in sportschedulefile:
                lines = line.strip()
                row = lines.split("\t")
                if datasearch == row[0]:
                    print("Sport ID found!")
                    print("code\tSport name\tSport schedule 1\t\tSport schedule 2\t\tSport schedule 3\t\tSport schedule 4")
                    print(row)
                    print("1. Code\n2.Sport name\n3.Sport schedule 1 \n4. Sport schedule 2\n5. Sport schedule 3\n6. Sport schedule 4")
                    while True:
                        choice = int(input("Enter your choice to modify:"))
                        if choice ==1:
                            ele = row[0]
                            newsportcode = input("Enter new sport code:")
                            row.remove(ele)
                            row.insert(0,newsportcode)
                            break
                        elif choice ==2:
                            ele = row[1]
                            newsportname = input("Enter new sport name:")
                            row.remove(ele)
                            row.insert(1,newsportname)
                            break
                        elif choice ==3:
                            ele = row[2]
                            new_sportschedule1 = input("Enter new sport schedule:")
                            row.remove(ele)
                            row.insert(2,new_sportschedule1)
                            break
                        elif choice ==4:
                            ele =row[3]
                            new_sportschedule2 = input("Enter new sport schedule:")
                            row.remove(ele)
                            row.insert(3,new_sportschedule2)
                            break
                        elif choice ==5:
                            ele =row[4]
                            new_sportschedule3 = input("Enter new sport schedule:")
                            row.remove(ele)
                            row.insert(4,new_sportschedule3)
                            break
                        elif choice ==6:
                            ele =row[5]
                            new_sportschedule4 = input("Enter new sport schedule:")
                            row.remove(ele)
                            row.insert(5,new_sportschedule3)
                            break
                        else:
                            print("Wrong input")
                            continue
                new.append(row)
            sportschedulefile=open("sportscheduledetailfile.txt","w")
            for data in new:
                for data2 in data:
                    sportschedulefile.write(data2)
                    sportschedulefile.write("\t")
                sportschedulefile.write("\n")
            sportschedulefile.close()
            adminuser()    
#sorting function for coach
def sortdatacoach():
    while True:
        try:
            user= int(input("1. Coaches in ascending order by name \n2. Coaches by hourly pay rate in ascending order \n3. Coaches by overall perfomace in ascending order \n Enter any other number to exit\nEnter how you would like to sort:\n"))
            break
        except ValueError:
            print (" Oops! That is not a valid input. Enter again.")
            continue
    if user >= 1 and user <= 3:
        if user == 1:
            coachfile = open("coachdetailfile.txt","r")
            test  = coachfile.readlines()
            namelist = []
            for lines in test:
                line=lines.strip()
                op=line.split("\t")
                namelist.append(op[1])

            for element in range(len(namelist)):
                for j in range(element+1, len(namelist)):
                    if namelist[element] < namelist[j]:
                        print("")
                    else:
                        num = namelist[element]
                        namelist[element] = namelist[j]
                        namelist[j] = num
        
            coachfile=open("coachdetailfile.txt","r")
            testing=coachfile.readlines()
            for li in namelist:
                for lines in testing:
                    line=lines.strip()
                    ops=line.split("\t")
                    if (ops[1] in li):
                        print(line)
                        adminuser()
                        
        if user == 2:
            coachfile = open("coachdetailfile.txt","r")
            test  = coachfile.readlines()
            paylist = []
            for lines in test:
                line=lines.strip()
                op=line.split("\t")
                paylist.append(op[4])

            for element in range(len(paylist)):
                for j in range(element+1, len(paylist)):
                    if paylist[element] < paylist[j]:
                        print("")
                    else:
                        num = paylist[element]
                        paylist[element] = paylist[j]
                        paylist[j] = num
                        print(paylist)
        
            coachfile=open("coachdetailfile.txt","r")
            testing=coachfile.readlines()
            for li in paylist:
                for lines in testing:
                    line=lines.strip()
                    ops=line.split("\t")
                    print(ops)
                    if (ops[4] in li):
                        print(ops)
                        adminuser()
        if user == 3:
            coachfile = open("coachdetailfile.txt","r")
            test  = coachfile.readlines()
            namelist = []
            for lines in test:
                line=lines.strip()
                op=line.split("\t")
                namelist.append(op[11])

            for element in range(len(namelist)):
                for j in range(element+1, len(namelist)):
                    if namelist[element] < namelist[j]:
                        print("")
                    else:
                        num = namelist[element]
                        namelist[element] = namelist[j]
                        namelist[j] = num
                        print("")
        
            coachfile=open("coachdetailfile.txt","r")
            testing=coachfile.readlines()
            for li in namelist:
                for lines in testing:
                    line=lines.strip()
                    ops=line.split("\t")
                    if (ops[11] in li):
                        print(line)
                        adminuser()
    else:
        print("")
        print("Are you sure you wan to exit? \nPress 1 to restart from where you left off or 0 to Exit")
        restart = int(input("Enter your decision"))
        if restart == 1:
            sortdatacoach()
        else:
            adminuser()

#display coach file
def opencoachfile():
    print("Code 	name  	Date joined Date terminated Hourly rate: phone number: 	address: 	Sport: 		Sport code: 	Center name: 					Center code: 	 Rating ")
    coachfile = open("coachdetailfile.txt","r")
    print(coachfile.read())
    coachfile.close()
#display sport file
def opensportfile():
    sportfile = open("sportdetailfile.txt","r")
    print(sportfile.read())
    sportfile.close()
#display sport schedule
def opensportschedulefile():
    print(" -----------------Sport Schedule -----------------")
    sportschedulefile = open("sportscheduledetailfile.txt","r")
    print(sportschedulefile.read())
    sportschedulefile.close()
#display regesitered student
def openregisteredstudentfile():
    registeredstudentfile = open("newstudentfile.txt","r")
    print(registeredstudentfile.read())
    registeredstudentfile.close()
    
#login for registered student
def loginoldstudent():
    while True:
        success = False
        file = open("studentuserpass.txt","r")
        studentname = input("Enter student username:")
        studentpassword = input("Enter student password:")
        for i in file:
            a,b = i.split(",")
            b = b.strip()
            if (a==studentname and b==studentpassword):
                success = True
                break
        file.close()
        if (success):
            print("Login successful")
            print("-------Welcome to Student page-------")
            oldstudent_user()
            break
        
        else:
            print ("Wrong username or password")
            continue
        
#new student register 
def newstudentregister():
    studentuserpass = open("studentuserpass.txt","a")
    while True:
        studentname = input("Enter your username:")
        if len(studentname) == 0:
            print("No value is entered.")
            continue
        else:
            break
    while True:
        studentpassword = input("Enter your password:")
        if len(studentpassword) == 0:
            print("No value is entered.")
            continue
        else:
            break
    
    studentuserpass.write(studentname +","+ studentpassword + "\n")
    studentuserpass.close()
    while True:
        studentID = input("Enter your ID (example - student1):")
        if len(studentID) == 0:
            print("No value is entered.")
            continue
        else:
            break
    print("Checking if student ID already exists in database---\n ---------------")
    newstdregister = open("newstudentfile.txt","r")
    for line in newstdregister:
        lines = line.strip()
        row = lines.split("\t")
        if studentID == row[0]:
            print("Student ID already exists.")
            newstudentregister()
        else:
            print("")
            
    print("Student ID was unique!")
    while True:
        student_name = input("Enter name:")
        if len(student_name) == 0:
            print("No value is entered.")
            continue
        else:
            break
    while True:
        studentgender = input("Enter Male or Female:")
        if len(studentgender) == 0:
            print("No value is entered.")
            continue
        else:
            break
    while True:
        studentage = input("Enter age:")
        if len(studentage) == 0:
            print("No value is entered.")
            continue
        else:
            break
    while True:
        studentphone = input("Enter phone number:")
        if len(studentphone) == 0:
            print("No value is entered.")
            continue
        else:
            break
    sportfile = open("sportdetailfile.txt","r")
    print("code\tSport name\tSport center name\t\t\t\tSport center code")
    print(sportfile.read())
    studentsportcode = input("Enter the Sport code:")
    studentsportname = input("Enter corresponding Sport name:")
    studentsportcentername= input("Enter Sport center name:")
    studentsportcentercode = input("Enter Sport center code:")
    print("Coach's code\tCoach's name\tHourly rate")
    coachfile=open("coachdetailfile.txt","r")
    for element in coachfile:
        lines = element.strip()
        line= lines.split("\t")
        if (studentsportcode == line[8]):
            print(line[0]+"\t\t"+line[1]+"\t\t"+line[4])
    studentcoachname = input("Enter coach name:")
    studentcoachID = input("Enter coach ID:")
    studentcoachfee = input("Enter coach fee:")
    print("The Sport schedule is:")
    sportschedule = open("sportscheduledetailfile.txt","r")
    for line in sportschedule:
        lines = line.strip()
        row = lines.split("\t")
        if studentsportcode == row[0]:
            print(row)
    studentsportschedule = input("Enter your sport schedule:")
    newstdregister = open("newstudentfile.txt", "a")
    newstdregister.write(studentID+"\t"+student_name+"\t"+studentgender+"\t"+studentage+"\t"+studentphone+"\t"+studentsportcode+"\t"+studentsportname+"\t"+studentsportcentername+"\t"+studentsportcentercode+"\t"+studentcoachname+"\t"+studentcoachID+"\t"+"Rm"+studentcoachfee+"\t"+studentsportschedule+"\n")
    newstdregister.close()
        
    print ("Successfully registered!")
    print("-------------Redirecting to Login page---------------")
    loginoldstudent()
#admin option select
def adminuser():
    while True:
        try:
            admin_user = int(input("1. Add records \n2. Display records \n3. Search records \n4. Sort records \n5. Modify records \nPress 0 to Exit\n"))
            break
        except ValueError:
            print (" Oops! That is not a valid input. Enter again.")
            continue
    if (admin_user >=1):
        if admin_user == 1:
            print ("1. Coach \n 2. Sport \n 3. Sport schedule")
            addrecordsuser = int(input("Enter correspodning number of which records you would like to add:"))
            if addrecordsuser == 1:
                addrecordscoach()
                adminuser()
            elif addrecordsuser == 2:
                addrecordssport()
                adminuser()
            elif addrecordsuser ==3:
                addsportschedule()
                adminuser()
            else:
                print("Invalid input")
                adminuser()
                
        elif admin_user == 2:
            print ("1. Coach \n 2. Sport \n 3. Registered students")
            displayrecorduser = int(input("Enter corresponding number of which records you would like to display:"))
            if displayrecorduser == 1:
                opencoachfile()
                adminuser()
            elif displayrecorduser == 2:
                opensportfile()
                adminuser()
            elif displayrecorduser == 3:
                openregisteredstudentfile()
                adminuser()
            else:
                print("Invalid input")
                adminuser()
        elif admin_user ==3:
            searchdata()
        elif admin_user ==4:
            sortdatacoach()
        elif admin_user ==5:
            modifydataadmin()
        else:
            admin_user = int(input("Wrong input. Press any number \n"))
            adminuser()
    else:
        print("")
#student user after logging in 
def oldstudent_user():
    print ("----------Welcome to Registered Student Page-----------")
    while True:
        try:
            oldstudentuser = int(input("1. Display records \n2. Modify your record \n3. Provide feedback to coach \nPress any other key to Exit\n"))
            break
        except ValueError:
            print (" Oops! That is not a valid input. Enter again.")
            continue
    if oldstudentuser == 1:
        search = int(input("1. Display record of Coach \n2. Display self-record \n3. Display registered schedule"))
        if search ==1:
            datasearch = input("Enter your coach's ID to display records:")
            coachfile = open("coachdetailfile.txt","r")
            for line in coachfile:
                lines = line.rstrip()
                row = lines.split("\t")
                if datasearch == row[0]:
                    print(row)
                    oldstudent_user()
                else:
                    print("not found")
                    oldstudent_user()
                    
        elif search ==2:
            datasearch = input("Enter your student ID to display your records:")
            studentfile = open("newstudentfile.txt","r")
            for line in studentfile:
                lines = line.rstrip()
                row = lines.split("\t")
                if datasearch == row[0]:
                    print(row)
                    oldstudent_user()
                    break
                
                    
        elif search ==3:
            datasearch = input("Enter your sport ID to display your schedule:")
            sportschedulefile = open("sportschedulefile.txt","r")
            for line in sportschedulefile:
                lines = line.rstrip()
                row = lines.split("\t")
                if datasearch == row[0]:
                    print(row)
                    oldstudent_user()
                
                    
        else:
            print("Wrong input")
            oldstudent_user()
            
    elif oldstudentuser == 2:
        datasearch = input("Enter your student ID :")
        studentfile = open("newstudentfile.txt","r")
        new=[]
        for line in studentfile:
            lines = line.strip()
            row = lines.split("\t")
            if datasearch == row[0]:
                print("Student ID found!")
                print(row)
                print("1. Code\n 2. Name \n3.Gender \n4. Age \n5. Phone number\n6. Sport \n7. Sport Center name \n8. Sport center code \n9. Sport schedule")
                while True:
                    choice = int(input("Enter your choice to modify:"))
                    if choice ==1:
                        ele = row[0]
                        newstudentcode = input("Enter new student code:")
                        row.remove(ele)
                        row.insert(0,newstudentcode)
                        break
                    elif choice ==2:
                        ele = row[1]
                        newstudentname = input("Enter new student name:")
                        row.remove(ele)
                        row.insert(1,newstudentname)
                        break
                    elif choice ==3:
                        ele = row[2]
                        newstudentgender = input("Enter new student gender:")
                        row.remove(ele)
                        row.insert(2,newstudentgender)
                        break
                    elif choice ==4:
                        ele =row[3]
                        newstudentage = input("Enter new age:")
                        row.remove(ele)
                        row.insert(3,newstudentage)
                        break
                    elif choice ==5:
                        ele =row[4]
                        new_studentphone = input("Enter new student phone:")
                        row.remove(ele)
                        row.insert(4,new_studentphone)
                        break
                    elif choice ==6:
                        ele =row[5]
                        new_sport = input("Enter new sport:")
                        row.remove(ele)
                        row.insert(5,new_sport)
                        break
                    elif choice ==7:
                        ele =row[6]
                        new_studentsportcentername = input("Enter new sport center name:")
                        row.remove(ele)
                        row.insert(6,new_studentsportcentername)
                        break
                    elif choice ==8:
                        ele =row[7]
                        new_studentsportcentercode = input("Enter new sport center code:")
                        row.remove(ele)
                        row.insert(7,new_studentsportcentercode)
                        break
                    elif choice ==9:
                        ele =row[8]
                        new_studentsportschedule = input("Enter new sport schedule:")
                        row.remove(ele)
                        row.insert(8,new_studentsportschedule)
                        break
                    else:
                        print("Wrong input")
                        oldstudent_user()
            new.append(row)
        studentfile=open("newstudentfile.txt","w")
        for data in new:
            for data2 in data:
                studentfile.write(data2)
                studentfile.write("\t")
            studentfile.write("\n")
        studentfile.close()
        oldstudent_user()
    elif oldstudentuser ==3:
        new=[]
        studentsportcode = input("Enter your sport code:")
        coachfile=open("coachdetailfile.txt","r")
        for element in coachfile:
            lines = element.strip()
            line= lines.split("\t")
            if (studentsportcode == line[8]):
                print("Coach's code\tCoach's name\tcoach rating")
                print(line[0]+"\t\t"+line[1]+"\t\t"+line[11])
                while True:
                    ele = line[11]
                    newcoachrating = int(input("Enter number out of 5 to rate your coach:"))
                    newcr1 = newcoachrating + 0
                    newcr2 = newcr1/2
                    newcr3 = str(newcr2)
                    line.remove(ele)
                    line.insert(11,newcr3)
                    break
            new.append(line)
        coachfile = coachfile=open("coachdetailfile.txt","w")
        for data in new:
            for data2 in data:
                coachfile.write(data2)
                coachfile.write("\t")
            coachfile.write("\n")
        coachfile.close()
        oldstudent_user()
                
    else:
        print("Wrong input")
        oldstudent_user()
    
#student user
def studentuser():
    print ("1.View details of Sport \n2. View details of Sport Schedule \n3. Register (only for new students) \n4. Login ( for existing students ) \n5. Press 5 to Exit") 
    while True:
        try:
            student_user = int(input("Enter your option:"))
            break
        except ValueError:
            print ("oops! not a valid number! Enter your option again.")
            continue
    if student_user == 1:
        opensportfile()
        studentuser()
    elif student_user == 2:
        opensportschedulefile()
        studentuser()
    elif student_user == 3:
        newstudentregister()
    elif student_user == 4:
        loginoldstudent()
    elif student_user == 5:
        print("")
    else:
        print(" Wrong input ")
        studentuser()
        
#main function with all other functions
def mainfunction():
    while True:
        print ("-------Welcome to Real Champions Sports Academy-------")
        print (" 1. Admin \t 2. Student \t 0-to exit")
        while True:
            try:
                user = int(input("Enter the corresponding number to select the user:"))
                break
            except ValueError:
                print("oops! not a valid number! Enter your option again.")
    
        if user == 1:
            adminlogin()
            adminuser()
            
        elif user == 2:
            studentuser()
        else:
            print ("oops! not a valid number! Enter your option again.")
        if user == 0:
            break
            

#mainfunction()
#everything global here
mainfunction()
