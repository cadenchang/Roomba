import bt_library as btl
from behavior_tree import tree_root
import random

from globals import BATTERY_LEVEL, GENERAL_CLEANING, SPOT_CLEANING, DUSTY_SPOT_SENSOR, HOME_PATH

starting_battery = input("Starting Battery Level (must be between 0 and 100): \n")

current_blackboard = btl.Blackboard()
current_blackboard.set_in_environment(BATTERY_LEVEL, int(starting_battery))
current_blackboard.set_in_environment(SPOT_CLEANING, False)
current_blackboard.set_in_environment(GENERAL_CLEANING, False)
current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, False)
current_blackboard.set_in_environment(HOME_PATH, "")

done = False
while not done:
    
    # change battery
    curr_battery = current_blackboard.get_in_environment(BATTERY_LEVEL, 100)
    current_blackboard.set_in_environment(BATTERY_LEVEL, curr_battery - 1)
    
    command = ""
    if (current_blackboard.get_in_environment(GENERAL_CLEANING, True) == False 
            and current_blackboard.get_in_environment(SPOT_CLEANING, True) == False):
        while not (command == "spot" or command == "general" or command == "done"):
            command = input("Choose Next Command: 'spot', 'general', or 'done'\n")
    if command == "spot":
        current_blackboard.set_in_environment(SPOT_CLEANING, True)
        current_blackboard.set_in_environment(GENERAL_CLEANING, False)
    if command == "general":
        current_blackboard.set_in_environment(GENERAL_CLEANING, True)
        current_blackboard.set_in_environment(SPOT_CLEANING, False)
        rand = random.randint(0,2)
        if rand == 0:
            current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, True)
    if command == "done":
        done = True

    result = tree_root.run(current_blackboard)

    # at the dock and battery needs to get charged
    if (current_blackboard.is_in_states(0) 
        and current_blackboard.get_in_states(0)["result"] == btl.ResultEnum.SUCCEEDED):
        current_blackboard.set_in_environment(BATTERY_LEVEL, 100)


    print("Battery Level: " + str(current_blackboard.get_in_environment(BATTERY_LEVEL, 100)))
    print()
    
    
