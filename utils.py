class servies:
    def __init__(self,n):
        self.slots = [1]*n
        self.age_map = {}

        self.slot_map = {}
        for i in range(1,n+1):
            self.slot_map[i] = []
    
    # Case 1: Park Command
    def park(self,input_line):
        drive_age = int(input_line[3].rstrip("\n"))
        car_number = input_line[1]

        ind = self.slots.index(1)

        self.slot_map[ind+1] = [drive_age,car_number]
        self.slots[ind] = 0

        if drive_age in list(self.age_map.keys()):
            self.age_map[drive_age].append([ind+1,car_number])

        else:
            self.age_map[drive_age] = [[ind+1,car_number]]

        # print("Parking..")
        # print(self.slots)
        # print(self.slot_map)
        # print(self.age_map)        
        output_line = "Car with vehicle registration number \""+car_number+"\" has been parked at slot number "+str(ind+1)+"\n"
        return output_line

    # Case 2: Leave Command
    def leave(self,input_line):
        ind = int(input_line[1].rstrip("\n"))
        output_line="\n"

        self.slots[ind-1] = 1

        drive_age = int(self.slot_map[ind][0])
        car_number = self.slot_map[ind][1]

        self.slot_map[ind] = []


        if drive_age in list(self.age_map.keys()):
            for i in range(len(self.age_map[drive_age])):
                if self.age_map[drive_age][i][0]==ind:
                    self.age_map[drive_age].pop(i)
                    break    

            if len(self.age_map[drive_age])==0:
                self.age_map.pop(drive_age, None)

        # print("Leaving..")
        # print(self.slots)
        # print(self.slot_map)
        # print(self.age_map)
        
        output_line = "Slot number "+str(ind)+" vacated, the car with vehicle registration number \""+car_number+"\" left the space, the driver of the car was of age "+str(drive_age)+"\n"
        return output_line
    
    # Case 3: Slot WRT Vehicle number command
    def slot_for_car_number(self,input_line):
        car_number = str(input_line[1].rstrip("\n"))
        output_line=" \n"

        for key in list(self.slot_map.keys()):

            if car_number in self.slot_map[key][1]:
                output_line = "Slot number for car with vehicle registration number \""+car_number+"\" is "+str(key)+"\n"
                break

        return output_line

    # Case 4: slots WRT drive's age command
    def slots_for_age(self,input_line):
        drive_age = int(input_line[1].rstrip("\n"))
        output_line="\n"

        temp = []
        for ls in self.age_map[drive_age]:
            temp.append(str(ls[0]))
        
        temp = ",".join(temp)
        output_line = "Slot numbers for the driver of age "+str(drive_age)+" are "+temp+"\n"
        return output_line
    
    # Case 5: Vehicle number WRT drive's age command
    def car_numbers_for_age(self,input_line):
        drive_age = int(input_line[1].rstrip("\n"))
        output_line="\n"
        
        temp = []
        if drive_age in list(self.age_map.keys()):
            for ls in self.age_map[drive_age]:
                temp.append(ls[1])

            temp = ",".join(temp)
            output_line = "Vehicle registration numbers for driver of age "+str(drive_age)+" are "+temp+"\n"

        return output_line