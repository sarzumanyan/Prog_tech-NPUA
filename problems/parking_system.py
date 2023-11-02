import random
array=[0]*20
vehicle={"a":0.5,"b":1,"c":1.5,"d":2,"e":2.5}
arranged_vehicle=dict()

def enter_vehicle(key):
    if key in vehicle:
        val = vehicle[key]
        n = int(val * 2)
        enter_arr=[0]*n
        global index
        index="no"
        for i in range(len(array)):
            if array[i:i + len(enter_arr)] == enter_arr:
                index = i
                break
        if index=="no":
            return f"No space available for {val}!"
        
        for i in range(index,index+n):
            array[i] = 1
        arranged_vehicle[index]=n
    else:
        return "Invalid key"
    #print(arranged_vehicle)
    return f"A vehicle with a weight of {val} units is entered at index {index} {array}"

def remove_vehicle(index):
    if len(arranged_vehicle)==0:
        return "There are no vehicles to be removed"
    index=random.choice(list(arranged_vehicle.keys()))
    for i in range(index,index+arranged_vehicle[index]):
        array[i] = 0
    del arranged_vehicle[index]
    #print(arranged_vehicle)
    return f"Vehicle is removed from index {index} {array}"
    
print(enter_vehicle("e"))
print(enter_vehicle("a"))
print(remove_vehicle(index))
print(enter_vehicle("d"))
#print(remove_vehicle(index))