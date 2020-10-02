import utils

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
serve = utils.servies(n)

#looping through file lines for commands
for input_line in file_input:
    
    input_line = input_line.split(' ')
    
    # Case 1: Part Command
    if input_line[0]=='Park':
        output_line = serve.park(input_line)


    # Case 2: Leave Command
    elif input_line[0]=='Leave':
        output_line = serve.leave(input_line)

    # Case 3: Slot WRT Vehicle number 
    elif input_line[0]=='Slot_number_for_car_with_number':
        output_line = serve.slot_for_car_number(input_line)


    # Case 4: Slots WRT drive's age
    elif input_line[0]=='Slot_numbers_for_driver_of_age':
        output_line = serve.slots_for_age(input_line)
    

    # Case 5: Vehicle number WRT drive's age
    elif input_line[0]=='Vehicle_registration_number_for_driver_of_age':
        output_line = serve.car_numbers_for_age(input_line)

    print(output_line)
    file_ouput.write(output_line)

#closing the output file
file_ouput.write("\n")
file_ouput.close()