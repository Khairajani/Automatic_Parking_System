#read the file name
fname = input("Enter Input File Name: ")
print()

#open the file
file_input = open(fname, "r")

#create the output file to write the content
file_ouput = open("output.txt", "a")


#reading the first command to create parking slots
n = int(file_input.readline().split(' ')[1])

#writing the first output line
output_line = "Created parking of "+str(n)+" slots\n"
file_ouput.write(output_line)

#initilizing the variables/data-structures
slots = [1]*n
slot_map = {}
for i in range(1,n+1):
    slot_map[i] = []

age_map = {}

#looping through file lines for commands
for input_line in file_input:
    
    input_line = input_line.split(' ')
    
    # Case 1: Part Command
    if input_line[0]=='Park':

        drive_age = int(input_line[3].split('\n')[0])
        car_number = input_line[1]
        output_line="\n"
        
        ind = slots.index(1)

        slot_map[ind+1] = [drive_age,car_number]
        slots[ind] = 0

        if drive_age in list(age_map.keys()):
            age_map[drive_age].append([ind+1,car_number])

        else:
            age_map[drive_age] = [[ind+1,car_number]]

        # print("Parking..")
        # print(slots)
        # print(slot_map)
        # print(age_map)        
        output_line = "Car with vehicle registration number "+car_number+" has been parked at slot number "+str(ind+1)+"\n"


    # Case 2: Leave Command
    elif input_line[0]=='Leave':
        ind = int(input_line[1].rstrip("\n"))
        output_line="\n"

        slots[ind-1] = 1

        drive_age = int(slot_map[ind][0])
        car_number = slot_map[ind][1]

        slot_map[ind] = []


        if drive_age in list(age_map.keys()):
            for i in range(len(age_map[drive_age])):
                if age_map[drive_age][i][0]==ind:
                    age_map[drive_age].pop(i)
                    break    

            if len(age_map[drive_age])==0:
                age_map.pop(drive_age, None)

        # print("Leaving..")
        # print(slots)
        # print(slot_map)
        # print(age_map)
        
        output_line = "Slot number "+str(ind)+" vacated, the car with vehicle registration number "+car_number+" left the space, the driver of the car was of age "+str(drive_age)+"\n"



    # Case 3: Slot WRT Vehicle number 
    elif input_line[0]=='Slot_number_for_car_with_number':
        car_number = str(input_line[1].rstrip("\n"))
        output_line="\n"

        for key in list(slot_map.keys()):

            if car_number in slot_map[key][1]:
                output_line = "Slot number for car with vehicle registration number "+car_number+" is "+str(key)+"\n"
                print(output_line)
                file_ouput.write(output_line)
                break


    # Case 4: Slots WRT drive's age
    elif input_line[0]=='Slot_numbers_for_driver_of_age':
        drive_age = int(input_line[1].rstrip("\n"))
        output_line="\n"

        temp = []
        for ls in age_map[drive_age]:
            temp.append(str(ls[0]))
        
        temp = ",".join(temp)
        output_line = "Slot numbers for the driver of age "+str(drive_age)+" are "+temp+"\n"

    

    # Case 5: Vehicle number WRT drive's age
    elif input_line[0]=='Vehicle_registration_number_for_driver_of_age':
        drive_age = int(input_line[1].rstrip("\n"))
        output_line="\n"
        
        temp = []
        if drive_age in list(age_map.keys()):
            for ls in age_map[drive_age]:
                temp.append(ls[1])

            temp = ",".join(temp)
            output_line = "Vehicle registration numbers for driver of age "+str(drive_age)+" are "+temp+"\n"


    print(output_line)
    file_ouput.write(output_line)

#closing the output file
file_ouput.close()