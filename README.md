# squadstack_assessment
## This is my submission to take-home assessment for SquadStack.

## Getting started
### Requirements
- Python 3
- macOS or Linux

### File System Description
- There are 2 python files ```main.py``` & ```utils.py``` and 1 text file ```input.txt```.
- The ```main.py``` file takes the user input for filename (file of commands) and ```utils.py``` contains the class and funtions related to ticketing system.
- I am here reading the 1st input command to CREATE THE PARKING LOT and initialise the variables using __init__ function
- After that I am passing the input (line-to-line) according to 5 cases (explained below)

### Data Structure Explanaion
- ```slots``` list in which 0 represent the unavailability of the slot i at slots[i], and 1 represent the availability 
- ```slot_map``` dictionary in which key:represents the slot, and value:is the list of [drive_age,car_number]
- ```age_map``` dictionary in which key:represents the age, and value:is the list of [slot,car_number]
- ```queue``` queue in which will contain the list of car which is waiting, in case of non-availability of slots

### Pipeline Explanaion:
I have considered 5 cases (according to given description) as per input command.

#### 1. Park
- Park the incoming car
- check if any slot is available of not: If no, store the [drive_age,car_number] in queue and move to next command
- else if yes, see the first available slot in the ```slots``` list and find its index (```ind```)
- change the index value from 1 to 0 in ```slots``` list (as that slot it now unavaibale),
- Edit the ```slot_map``` for ind+1 to store the current [drive_age,car_number]
- If the driver age is present in ```age_map``` as key, append current [ind,car_number]
- If not present make a new key as driver age and give value as current [drive_age,car_number]
- Write the output in the file

#### 2. Leave
- Letting go the outgoing car (reversing the above scenario)
- change the index value from 0 to 1 in ```slots``` list (as that slot it now avaibale),
- Edit the ```slot_map``` for ind+1 to store the empty list []
- Remove the nested list from ```age_map``` where driver_age is key and where the car_number matches with the outgoing car's number & delete the key-value pair if the value list is empty for current driver_age key.
- check if any car is present in queue, if not do nothing, else PARK that CAR according to above case
- Write the output in the file 

#### 3. Slot with respect to car_number
- Trace the ```slot_map``` for each key and match it with given car_number
- If it matched return the key
- Write the output in the file

#### 4. Slots with respect to driver_age
- Check if ```age_map``` has any key driver_age, if no, do nothing
- If yes, iterate through every age_map[drive_age] list and append all the slots (1st element of the list) in the temporary list
- At last Write the output in the file using join function

#### 5. Vehicle number with respect to driver_age
- Same as previous
- Check if ```age_map``` has any key driver_age, if no, do nothing
- If yes, iterate through every age_map[drive_age] list and append all the car_number (2nd element of the list) in the temporary list
- At last Write the output in the file using join function

### Run
Simply run the ```main.py``` file and enter ```input.txt```

### ouput/result
- You will see in terminal for the expected output line by line
- An output file named as ```output.txt``` will be formed and all the outputs are appended line-by-line


Regards: Himanshu Khairajani