import random
import tkinter as tk
import time
POINT_SIZE = 8
LINE_WIDTH = 4
def route_choose(route_list):
    optimal_choice = []
    minimum_time = 5000000000000
    for road_list in route_list:
        time_count = 0
        for road in road_list:
            time_count += road.actualspend
        if time_count < minimum_time:
            minimum_time = time_count
            optimal_choice.clear()
            optimal_choice.extend(road_list)
        #print("minimum_time: " + str(minimum_time))
        #print(str(road_list) + str(time_count))
    return optimal_choice
    
def main():
    """
    generate canvas
    """
    windows = tk.Tk()
    windows.title("Simulation")
    canvas = tk.Canvas(windows, width = 550, height = 350)
    
    canvas.create_rectangle(300, 100, 320, 120, fill = "white")
    canvas.create_text(330, 100, text = "occupied ratio: x < 20%", anchor = "nw")
    canvas.create_rectangle(300, 130, 320, 150, fill = "green")
    canvas.create_text(330, 130, text = "occupied ratio: 20% <= x < 40%", anchor = "nw")
    canvas.create_rectangle(300, 160, 320, 180, fill = "yellow")
    canvas.create_text(330, 160, text = "occupied ratio: 40% <= x < 60%", anchor = "nw")
    canvas.create_rectangle(300, 190, 320, 210, fill = "orange")
    canvas.create_text(330, 190, text = "occupied ratio: 60% <= x < 80%", anchor = "nw")
    canvas.create_rectangle(300, 220, 320, 240, fill = "red")
    canvas.create_text(330, 220, text = "occupied ratio: 80% <= x", anchor = "nw")

    canvas.pack()
    
    """
    Define map, inclding roads and intersections.
    Also, define route to specific destination.
    """ 
    print("simulation start")
    map = Map()
    #nodes
    map.intersect.append(Node("Xinzhuang_CBD", 40, 280, canvas))
    map.intersect.append(Node("Southern_Xinzhuang", 85, 330, canvas))
    map.intersect.append(Node("bottomAloneRiverLeft", 140, 305, canvas))
    map.intersect.append(Node("lowAloneRiverLeft", 130, 250, canvas))
    map.intersect.append(Node("middleAlongRiverLeft", 70, 170, canvas))
    map.intersect.append(Node("highAlongRiverLeft", 80, 60, canvas))
    map.intersect.append(Node("Bali", 90, 20, canvas))
    map.intersect.append(Node("bottomAloneRiverRight", 215, 285, canvas))
    map.intersect.append(Node("lowAloneRiverRight", 205, 220, canvas))
    map.intersect.append(Node("middleAlongRiverRight", 190, 200, canvas))
    map.intersect.append(Node("highAloneRiverRight", 165, 150, canvas))
    map.intersect.append(Node("topAlongRiverRight", 165, 75, canvas))
    map.intersect.append(Node("Southern_Sanchong", 260, 270, canvas))
    map.intersect.append(Node("Sanchong", 260, 165, canvas))
    map.intersect.append(Node("Luzhou", 260, 100, canvas))
    #road
    map.road.append(Road(map.intersect[0], map.intersect[3], 140, canvas, 2230))

    map.road.append(Road(map.intersect[1], map.intersect[2], 140, canvas, 2310))
    map.road.append(Road(map.intersect[2], map.intersect[3], 70, canvas, 900))
    map.road.append(Road(map.intersect[3], map.intersect[4], 70, canvas, 3810))
    map.road.append(Road(map.intersect[4], map.intersect[5], 70, canvas, 2670))
    map.road.append(Road(map.intersect[5], map.intersect[6], 140, canvas, 2570))
    map.road.append(Road(map.intersect[6], map.intersect[5], 140, canvas, 2570))
    map.road.append(Road(map.intersect[5], map.intersect[4], 70, canvas, 2670))
    map.road.append(Road(map.intersect[4], map.intersect[3], 70, canvas, 3810))
    map.road.append(Road(map.intersect[3], map.intersect[2], 70, canvas, 900))
    map.road.append(Road(map.intersect[2], map.intersect[1], 140, canvas, 2310))

    map.road.append(Road(map.intersect[2], map.intersect[7], 70, canvas, 580))
    map.road.append(Road(map.intersect[3], map.intersect[8], 120, canvas, 700 / 1.4))              
    map.road.append(Road(map.intersect[4], map.intersect[9], 35, canvas, 1920 * 1.2 * 100000))              ############
    map.road.append(Road(map.intersect[4], map.intersect[10], 105, canvas, 730))
    map.road.append(Road(map.intersect[5], map.intersect[11], 70, canvas, 920))
    map.road.append(Road(map.intersect[2], map.intersect[9], 35, canvas, 2140 * 1.2 * 100000))              ############

    map.road.append(Road(map.intersect[7], map.intersect[8], 70, canvas, 1380))
    map.road.append(Road(map.intersect[8], map.intersect[9], 70, canvas, 1540))
    map.road.append(Road(map.intersect[9], map.intersect[10], 70, canvas, 1620))
    map.road.append(Road(map.intersect[10], map.intersect[11], 70, canvas, 1600))
    map.road.append(Road(map.intersect[11], map.intersect[10], 70, canvas, 1600))
    map.road.append(Road(map.intersect[10], map.intersect[9], 70, canvas, 1620))
    map.road.append(Road(map.intersect[9], map.intersect[8], 70, canvas, 1540))
    map.road.append(Road(map.intersect[8], map.intersect[7], 70, canvas, 1380))

    map.road.append(Road(map.intersect[7], map.intersect[12], 140, canvas, 1340))
    map.road.append(Road(map.intersect[10], map.intersect[13], 140, canvas, 1280))
    map.road.append(Road(map.intersect[11], map.intersect[14], 140, canvas, 1750))

    #reverse
    map.road.append(Road(map.intersect[12], map.intersect[7], 140, canvas, 1340))
    map.road.append(Road(map.intersect[13], map.intersect[10], 140, canvas,1280))
    map.road.append(Road(map.intersect[14], map.intersect[11], 140, canvas, 1750))

    map.road.append(Road(map.intersect[7], map.intersect[2], 70, canvas, 580))
    map.road.append(Road(map.intersect[8], map.intersect[3], 120, canvas, 700 / 1.4))
    map.road.append(Road(map.intersect[9], map.intersect[4], 35, canvas, 1920 * 1.2 * 100000))              ############
    map.road.append(Road(map.intersect[10], map.intersect[4], 105, canvas, 730))
    map.road.append(Road(map.intersect[11], map.intersect[5], 70, canvas, 920))
    map.road.append(Road(map.intersect[9], map.intersect[2], 35, canvas, 2140 * 1.2 * 100000))              ############

    map.road.append(Road(map.intersect[3], map.intersect[0], 140, canvas, 2230))

    map.road.append(Road(map.intersect[5], map.intersect[9], 70, canvas, 4210 * 1.2 * 100000))              ############
    map.road.append(Road(map.intersect[9], map.intersect[5], 70, canvas, 4210 * 1.2 * 100000))                      ############

    road_list1 = []
    road_list2 = []
    road_list3 = []
    road_list4 = []
    road_list5 = []
    road_list6 = []
    road_list7 = []
    road_list8 = []
    road_list9 = []
    road_list10 = []
    road_list11 = []
    road_list12 = []
    road_list13 = []
    road_list14 = []
    road_list15 = []
    road_list16 = []
    road_list17 = []
    road_list18 = []
    road_list19 = []
    road_list20 = []
    road_list21 = []
    road_list22 = []
    road_list23 = []
    road_list24 = []
    road_list25 = []
    road_list26 = []
    road_list27 = []
    road_list28 = []
    road_list29 = []
    road_list30 = []
    road_list31 = []
    road_list32 = []
    road_list33 = []
    road_list34 = []
    road_list35 = []
    road_list36 = []
    road_list37 = []
    road_list38 = []
    road_list39 = []
    road_list40 = []
    road_list41 = []
    road_list42 = []
    road_list43 = []
    road_list44 = []
    road_list45 = []
    road_list46 = []
    road_list47 = []
    road_list48 = []

    road_list49 = []
    road_list50 = []
    
    #road to Southern_Sanchong
    #from Southern_Xinzhuang to Southern_Sanchong
    route_1to12 = []
    road_list1.extend([map.road[1], map.road[11], map.road[25]])
    route_1to12.extend([road_list1])
    #from Xinzhuang to Southern_Sanchong
    route_0to12 = []
    road_list2.extend([map.road[0], map.road[12], map.road[17], map.road[25]])
    road_list3.extend([map.road[0], map.road[9], map.road[11], map.road[25]])
    route_0to12.extend([road_list2, road_list3])
    #from Bali to Southern_Sanchong
    route_6to12 = []
    road_list4.extend([map.road[6], map.road[15], map.road[21], map.road[22], map.road[23], map.road[24], map.road[25]])
    road_list5.extend([map.road[6], map.road[7], map.road[14], map.road[22], map.road[23], map.road[24], map.road[25]])
    road_list6.extend([map.road[6], map.road[7], map.road[13], map.road[23], map.road[24], map.road[25]])
    road_list7.extend([map.road[6], map.road[7], map.road[8], map.road[12], map.road[24], map.road[25]])
    road_list8.extend([map.road[6], map.road[7], map.road[8], map.road[9], map.road[11], map.road[25]])
    road_list49.extend([map.road[6], map.road[38], map.road[23], map.road[24], map.road[25]])
    route_6to12.extend([road_list4, road_list5, road_list6, road_list7, road_list8, road_list49])
    
    #road to Sanchong
    #from Southern_Xinzhuang to Sanchong
    route_1to13 = []
    road_list9.extend([map.road[1], map.road[11], map.road[17], map.road[18], map.road[19], map.road[26]])
    road_list10.extend([map.road[1], map.road[2], map.road[12], map.road[18], map.road[19], map.road[26]])
    road_list11.extend([map.road[1], map.road[2], map.road[3], map.road[14], map.road[26]])
    road_list12.extend([map.road[1], map.road[12], map.road[19], map.road[26]])
    route_1to13.extend([road_list9, road_list10, road_list11, road_list12])
    #from Xinzhuang to Sanchong
    route_0to13 = []
    road_list13.extend([map.road[0], map.road[12], map.road[18], map.road[19], map.road[26]])
    road_list14.extend([map.road[0], map.road[3], map.road[14], map.road[26]])
    route_0to13.extend([road_list13, road_list14])
    #from Bali to Sanchong
    route_6to13 = []
    road_list15.extend([map.road[6], map.road[15], map.road[21], map.road[26]])
    road_list16.extend([map.road[6], map.road[7], map.road[14], map.road[26]])
    route_6to13.extend([road_list15, road_list16])

    #road to Luzhou
    #from Southern_Xinzhuang to Luzhou
    route_1to14 = []
    road_list17.extend([map.road[1], map.road[11], map.road[17], map.road[18], map.road[19], map.road[20], map.road[27]])
    road_list18.extend([map.road[1], map.road[12], map.road[19], map.road[20], map.road[27]])
    road_list19.extend([map.road[1], map.road[2], map.road[12], map.road[18], map.road[19], map.road[20], map.road[27]])
    road_list20.extend([map.road[1], map.road[2], map.road[3], map.road[14], map.road[20], map.road[27]])
    route_1to14.extend([road_list17, road_list18, road_list19, road_list20])
    #from Xinzhuang to Luzhou   
    route_0to14 = []
    road_list21.extend([map.road[0], map.road[12], map.road[18], map.road[19], map.road[20], map.road[27]])
    road_list22.extend([map.road[0], map.road[8], map.road[14], map.road[20], map.road[27]])
    route_0to14.extend([road_list21, road_list22])
    #from Bali to Luzhou
    route_6to14 = []
    road_list23.extend([map.road[6], map.road[15], map.road[27]])
    route_6to14.extend([road_list23])

    #from Southern_Xinzhuang to Bali
    route_1to6 = []
    road_list24.extend([map.road[1], map.road[2], map.road[3], map.road[4], map.road[5]])
    route_1to6.extend([road_list24])

    #from Bali to Southern_Xinzhuang
    route_6to1 = []
    road_list25.extend([map.road[6], map.road[7], map.road[8], map.road[9], map.road[10]])
    route_6to1.extend([road_list25])

    #road to Southern_Xinzhuang
    #from Southern_Sanchong to Southern_Xinzhuang
    route_12to1 = []
    road_list26.extend([map.road[28], map.road[31], map.road[10]])
    route_12to1.extend([road_list26])
    #from Sanchong to Southern_Xinzhuang
    route_13to1 = []
    road_list27.extend([map.road[29], map.road[34], map.road[8], map.road[9], map.road[10]])
    road_list28.extend([map.road[29], map.road[22], map.road[36], map.road[10]])
    road_list29.extend([map.road[29], map.road[22], map.road[23], map.road[32], map.road[9], map.road[10]])
    road_list30.extend([map.road[29], map.road[22], map.road[23], map.road[24], map.road[31], map.road[10]])
    route_13to1.extend([road_list27, road_list28, road_list29, road_list30])
    #from Luzhou to Southern_Xinzhuang
    route_14to1 = []
    road_list31.extend([map.road[30], map.road[21], map.road[34], map.road[8], map.road[9], map.road[10]])
    road_list32.extend([map.road[30], map.road[21], map.road[22], map.road[36], map.road[10]])
    road_list33.extend([map.road[30], map.road[21], map.road[22], map.road[23], map.road[32], map.road[9], map.road[10]])
    road_list34.extend([map.road[30], map.road[21], map.road[22], map.road[23], map.road[24], map.road[31], map.road[10]])
    route_14to1.extend([road_list31, road_list32, road_list33, road_list34])

    #road to Xinzhuang
    #from Southern_Sanchong to Xinzhuang
    route_12to0 = []
    road_list35.extend([map.road[28], map.road[31], map.road[2], map.road[37]])
    road_list36.extend([map.road[28], map.road[31], map.road[2], map.road[37]])
    route_12to0.extend([road_list35, road_list36])
    #from Sanchong to Xinzhuang
    route_13to0 = []
    road_list37.extend([map.road[29], map.road[34], map.road[8], map.road[37]])
    road_list38.extend([map.road[29], map.road[22], map.road[23], map.road[32], map.road[37]])
    route_13to0.extend([road_list37, road_list38])
    #from Luzhou to Xinzhuang
    route_14to0 = []
    road_list39.extend([map.road[30], map.road[21], map.road[34], map.road[8], map.road[37]])
    road_list40.extend([map.road[30], map.road[21], map.road[22], map.road[23], map.road[32], map.road[37]])
    route_14to0.extend([road_list39, road_list40])

    #road to Bali
    #from Southern_Sanchong to Bali
    route_12to6 = []
    road_list41.extend([map.road[28], map.road[31], map.road[2], map.road[3], map.road[4], map.road[5]])
    road_list42.extend([map.road[28], map.road[17], map.road[32], map.road[3], map.road[4], map.road[5]])
    road_list43.extend([map.road[28], map.road[17], map.road[18], map.road[33], map.road[4], map.road[5]])
    road_list44.extend([map.road[28], map.road[17], map.road[18], map.road[19], map.road[34], map.road[4], map.road[5]])
    road_list45.extend([map.road[28], map.road[17], map.road[18], map.road[19], map.road[20], map.road[35], map.road[5]])
    road_list50.extend([map.road[28], map.road[17], map.road[18], map.road[39], map.road[5]])
    route_12to6.extend([road_list41, road_list42, road_list43, road_list44, road_list45, road_list50])
    #from Sanchong to Bali
    route_13to6 = []
    road_list46.extend([map.road[29], map.road[34], map.road[4], map.road[5]])
    road_list47.extend([map.road[29], map.road[20], map.road[15], map.road[5]])
    route_13to6.extend([road_list46, road_list47])
    #from Luzhou to Bali
    route_14to6 = []
    road_list48.extend([map.road[30], map.road[35], map.road[5]])
    route_14to6.extend([road_list48])
    
    """
    Start simulation:
    generate vehicle --> run simulation in time interval
    """
    vehicle_list = []
    for times in range(721):
        vehicle_list.append(Vehicle(map.intersect[12], times, route_choose(route_1to12), random.randint(10, 20)))
        vehicle_list.append(Vehicle(map.intersect[12], times, route_choose(route_0to12), random.randint(10, 20)))
        vehicle_list.append(Vehicle(map.intersect[12], times, route_choose(route_6to12), random.randint(10, 20)))
        vehicle_list.append(Vehicle(map.intersect[13], times, route_choose(route_1to13), random.randint(10, 20)))
        vehicle_list.append(Vehicle(map.intersect[13], times, route_choose(route_0to13), random.randint(10, 20)))
        vehicle_list.append(Vehicle(map.intersect[13], times, route_choose(route_6to13), random.randint(10, 20)))
        vehicle_list.append(Vehicle(map.intersect[14], times, route_choose(route_1to14), random.randint(10, 20)))
        vehicle_list.append(Vehicle(map.intersect[14], times, route_choose(route_0to14), random.randint(10, 20)))
        vehicle_list.append(Vehicle(map.intersect[14], times, route_choose(route_6to14), random.randint(10, 20)))

        vehicle_list.append(Vehicle(map.intersect[6], times, route_choose(route_1to6), random.randint(10, 20)))
        vehicle_list.append(Vehicle(map.intersect[1], times, route_choose(route_6to1), random.randint(10, 20)))
        
        vehicle_list.append(Vehicle(map.intersect[1], times, route_choose(route_12to1), random.randint(10, 20)))
        vehicle_list.append(Vehicle(map.intersect[1], times, route_choose(route_13to1), random.randint(10, 20)))
        vehicle_list.append(Vehicle(map.intersect[1], times, route_choose(route_14to1), random.randint(10, 20)))
        vehicle_list.append(Vehicle(map.intersect[0], times, route_choose(route_12to0), random.randint(10, 20)))
        vehicle_list.append(Vehicle(map.intersect[0], times, route_choose(route_13to0), random.randint(10, 20)))
        vehicle_list.append(Vehicle(map.intersect[0], times, route_choose(route_14to0), random.randint(10, 20)))
        vehicle_list.append(Vehicle(map.intersect[6], times, route_choose(route_12to6), random.randint(10, 20)))
        vehicle_list.append(Vehicle(map.intersect[6], times, route_choose(route_13to6), random.randint(10, 20)))
        vehicle_list.append(Vehicle(map.intersect[6], times, route_choose(route_14to6), random.randint(10, 20)))
    
        for vehicle in vehicle_list:
            if times >= vehicle.clock:
                vehicle.moveforward()
        map.checkmap(vehicle_list, times)
        for intersect in map.intersect:
            canvas.tag_raise(intersect.image)
        map.printmap(times)
        time.sleep(0.05)
        if times % 20 == 0:
            windows.update()
        if times % 60 == 0 and times != 0:
            time.sleep(2.5)
    map.printdata()
    stop = input("finish simulation")
    windows.mainloop   

class Node:
    def __init__(self, name, location_x, location_y, canvas):
        self.name = name
        self.location_x = location_x
        self.location_y = location_y
        self.image = canvas.create_oval(self.location_x - POINT_SIZE / 2, self.location_y - POINT_SIZE / 2, 
                                        self.location_x + POINT_SIZE / 2, self.location_y + POINT_SIZE / 2, fill = "blue")
        pass
    
class Map:
    def __init__(self):
        self.intersect = []
        self.road = []
        pass
    def checkmap(self, vehicle_list, time):
        for road in self.road:
            road.checkcurrent(vehicle_list, time)
        vehicle_list1 = list(filter(lambda vehicle: vehicle.current.end.name != vehicle.destination.name or time < vehicle.clock, vehicle_list))
        vehicle_list.clear()
        vehicle_list.extend(vehicle_list1)
        pass
    def printmap(self, times):
        for road in self.road:
            road.printcurrent(times)
        print("-----------------------------------------------------------")
        pass
    def printdata(self):
        for road in self.road:
            road.printdata()
    
class Road:
    time.sleep(8)
    def __init__(self, start, end, capacity, canvas, length):
        self.start = start
        self.end = end
        self.capacity = capacity
        self.inside = 0
        self.canvas = canvas
        self.color = "white"
        self.length = length
        self.timespend = length / 800
        self.actualspend = self.timespend
        self.congestion_time = 0
        if start.location_y < end.location_y:
            self.image = canvas.create_line(self.start.location_x - LINE_WIDTH / 3.5, self.start.location_y + LINE_WIDTH / 3.5, 
                                            self.end.location_x - LINE_WIDTH / 3.5, self.end.location_y + LINE_WIDTH / 3.5, 
                                            width = LINE_WIDTH, fill = self.color)
        else:
            self.image = canvas.create_line(self.start.location_x + LINE_WIDTH / 3.5, self.start.location_y - LINE_WIDTH / 3.5, 
                                            self.end.location_x + LINE_WIDTH / 3.5, self.end.location_y - LINE_WIDTH / 3.5, 
                                            width = LINE_WIDTH, fill = self.color)
        pass
    def printcurrent(self, time):
        print("Time " + str(time) + " at the road from " + self.start.name + " to " + self.end.name + " has " + str(self.inside) + " cars.")
        pass
    def printdata(self):
        #print("From " + self.start.name + " to " + self.end.name + ", total congestion time is " + str(self.congestion_time))
        print(self.congestion_time)
        pass
    def checkcurrent(self, vehicle_list, time):
        self.inside = 0
        for vehicle in vehicle_list:
            if vehicle.current.end.name == vehicle.destination.name and time >= vehicle.clock and vehicle.current == self:
                print(str(vehicle.number)+ " vehicle arrive to its destination " + vehicle.destination.name)
                print("Arrived at : " + str(vehicle.clock))
            elif vehicle.current == self:
                self.inside += vehicle.number
        self.actualspend = self.timespend * (1 + (self.inside / self.actualspend / self.capacity) ** 2)   
        if self.inside / self.capacity >= 0 and self.inside / self.actualspend / self.capacity < 0.2:
            self.canvas.itemconfig(self.image, fill = "white")
        elif self.inside / self.capacity >= 0.2 and self.inside / self.actualspend / self.capacity < 0.4:
            self.canvas.itemconfig(self.image, fill = "green")
        elif self.inside / self.capacity >= 0.4 and self.inside / self.actualspend / self.capacity < 0.6:
            self.canvas.itemconfig(self.image, fill = "yellow")
        elif self.inside / self.capacity >= 0.6 and self.inside / self.actualspend / self.capacity < 0.8:
            self.canvas.itemconfig(self.image, fill = "orange")
            self.congestion_time += 0.5
        else:
            self.canvas.itemconfig(self.image, fill = "red")
            self.congestion_time += 1
        pass
    
class Vehicle:
    def __init__(self, destination, time, route, number):
        self.current = route[0]
        self.destination = destination
        self.clock = time + self.current.actualspend
        self.road = []
        self.number = number
        self.road.extend(route)
        pass
    def moveforward(self):
        if len(self.road) != 0:
            self.current = self.road.pop(0)
            self.clock += self.current.actualspend
        pass
            

if __name__ == '__main__':
    main()