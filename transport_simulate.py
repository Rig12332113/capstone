import random
import tkinter as tk
import time
POINT_SIZE = 12
LINE_WIDTH = 6
def route_choose(route_list):
    optimal_choice = []
    minimum_time = 50000
    for road_list in route_list:
        time_count = 0
        for road in road_list:
            time_count += road.actualspend
        if time_count < minimum_time:
            optimal_choice.clear()
            optimal_choice.extend(road_list)
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
    map.intersect.append(Node("middleWest", 50, 150, canvas))

    map.intersect.append(Node("bottomAloneRiverLeft", 120, 290, canvas))
    map.intersect.append(Node("lowAloneRiverLeft", 130, 220, canvas))
    map.intersect.append(Node("middleAlongRiverLeft", 120, 150, canvas))
    map.intersect.append(Node("highAlongRiverLeft", 90, 90, canvas))
    map.intersect.append(Node("topAlongRiverLeft", 120, 20, canvas))

    map.intersect.append(Node("bottomAloneRiverRight", 190, 235, canvas))
    map.intersect.append(Node("middleAlongRiverRight", 200, 150, canvas))
    map.intersect.append(Node("topAlongRiverRight", 180, 70, canvas))

    map.intersect.append(Node("bottomCityCenter", 250, 235, canvas))
    map.intersect.append(Node("middleCityCenter", 250, 150, canvas))
    map.intersect.append(Node("topCityCenter", 250, 70, canvas))

    map.road.append(Road(map.intersect[0], map.intersect[3], 1500, 2, canvas))

    map.road.append(Road(map.intersect[1], map.intersect[2], 1500, 2, canvas))
    map.road.append(Road(map.intersect[2], map.intersect[3], 1000, 5, canvas))
    map.road.append(Road(map.intersect[3], map.intersect[4], 1000, 5, canvas))
    map.road.append(Road(map.intersect[4], map.intersect[5], 1000, 5, canvas))

    map.road.append(Road(map.intersect[2], map.intersect[6], 1200, 5, canvas))
    map.road.append(Road(map.intersect[3], map.intersect[7], 1200, 5, canvas))
    map.road.append(Road(map.intersect[4], map.intersect[8], 1200, 5, canvas))

    map.road.append(Road(map.intersect[6], map.intersect[7], 1000, 5, canvas))
    map.road.append(Road(map.intersect[7], map.intersect[8], 1000, 5, canvas))

    map.road.append(Road(map.intersect[6], map.intersect[9], 1500, 5, canvas))
    map.road.append(Road(map.intersect[7], map.intersect[10], 1500, 5, canvas))
    map.road.append(Road(map.intersect[8], map.intersect[11], 1500, 5, canvas))

    map.road.append(Road(map.intersect[2], map.intersect[7], 600, 5, canvas))

    map.road.append(Road(map.intersect[5], map.intersect[4], 1500, 2, canvas))
    map.road.append(Road(map.intersect[4], map.intersect[3], 1000, 5, canvas))
    map.road.append(Road(map.intersect[3], map.intersect[2], 1000, 5, canvas))
    map.road.append(Road(map.intersect[2], map.intersect[1], 1000, 5, canvas))

    map.road.append(Road(map.intersect[8], map.intersect[7], 1000, 5, canvas))
    map.road.append(Road(map.intersect[7], map.intersect[6], 1000, 5, canvas))
    """
    map.road.append(Road(map.intersect[3], map.intersect[0], 1500, 5, canvas))

    map.road.append(Road(map.intersect[6], map.intersect[2], 1500, 5, canvas))
    map.road.append(Road(map.intersect[7], map.intersect[3], 1500, 5, canvas))
    map.road.append(Road(map.intersect[8], map.intersect[4], 1500, 5, canvas))

    map.road.append(Road(map.intersect[9], map.intersect[6], 1500, 5, canvas))
    map.road.append(Road(map.intersect[10], map.intersect[7], 1500, 5, canvas))
    map.road.append(Road(map.intersect[11], map.intersect[8], 1500, 5, canvas))

    map.road.append(Road(map.intersect[7], map.intersect[2], 600, 5, canvas))
    """
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

    #road to middle city center
    #from 0 to 10
    route_0to10 = []
    road_list1.extend([map.road[0], map.road[6], map.road[11]])
    route_0to10.append(road_list1)
    #from 1 to 10
    route_1to10 = []
    road_list2.extend([map.road[1], map.road[2], map.road[6], map.road[11]])
    road_list3.extend([map.road[1], map.road[5], map.road[8], map.road[11]])
    road_list4.extend([map.road[1], map.road[13], map.road[11]])
    route_1to10.extend([road_list2, road_list3, road_list4])
    #from 5 to 10 
    route_5to10 = []
    road_list5.extend([map.road[14], map.road[7], map.road[18], map.road[11]])
    road_list6.extend([map.road[14], map.road[15], map.road[6], map.road[11]])
    route_5to10.extend([road_list5, road_list6])
    
    #road to top city center
    #from 0 to 11
    route_0to11 = []
    road_list7.extend([map.road[0], map.road[3], map.road[7], map.road[12]])
    road_list8.extend([map.road[0], map.road[6], map.road[9], map.road[12]])
    route_0to11.extend([road_list7, road_list8])
    #from 1 to 11
    route_1to11 = []
    road_list9.extend([map.road[1], map.road[2], map.road[3], map.road[7], map.road[12]])
    road_list10.extend([map.road[1], map.road[2], map.road[6], map.road[9], map.road[12]])
    road_list11.extend([map.road[1], map.road[13], map.road[9], map.road[12]])
    road_list12.extend([map.road[1], map.road[5], map.road[8], map.road[9], map.road[12]])
    route_1to11.extend([road_list9, road_list10, road_list11, road_list12])
    #from 5 to 11
    route_5to11 = []
    road_list13.extend([map.road[14], map.road[7], map.road[12]])
    route_5to11.append(road_list13)

    #road to bottom city 
    #from 0 to 9
    route_0to9 = []
    road_list14.extend([map.road[0], map.road[6], map.road[19], map.road[10]])
    road_list15.extend([map.road[0], map.road[16], map.road[5], map.road[10]])
    route_0to9.extend([road_list14, road_list15])
    #from 1 to 9
    route_1to9 = []
    road_list16.extend([map.road[1], map.road[5], map.road[10]])
    route_1to9.append(road_list16)
    #from 5 to 9
    route_5to9 = []
    road_list17.extend([map.road[14], map.road[15], map.road[16], map.road[5], map.road[10]])
    road_list18.extend([map.road[14], map.road[15], map.road[6], map.road[19], map.road[10]])
    road_list19.extend([map.road[14], map.road[7], map.road[18], map.road[19], map.road[10]])
    route_5to9.extend([road_list17, road_list18, road_list19])

    #from 1 to 5
    route_1to5 = []
    road_list20.extend([map.road[1], map.road[2], map.road[3], map.road[4]])
    route_1to5.append(road_list20)

    #from 5 to 1
    route_5to1 = []
    road_list21.extend([map.road[14], map.road[15], map.road[16], map.road[17]])
    route_5to1.append(road_list21)
    
    """
    Start simulation:
    generate vehicle --> run simulation in time interval
    """
    vehicle_list = []
    for times in range(720):
        vehicle_list.append(Vehicle(map.intersect[10], times, route_choose(route_0to10), random.randint(1, 50)))
        vehicle_list.append(Vehicle(map.intersect[10], times, route_choose(route_1to10), random.randint(1, 50)))
        vehicle_list.append(Vehicle(map.intersect[10], times, route_choose(route_5to10), random.randint(1, 50)))
        vehicle_list.append(Vehicle(map.intersect[11], times, route_choose(route_0to11), random.randint(1, 50)))
        vehicle_list.append(Vehicle(map.intersect[11], times, route_choose(route_1to11), random.randint(1, 50)))
        vehicle_list.append(Vehicle(map.intersect[11], times, route_choose(route_5to11), random.randint(1, 50)))
        vehicle_list.append(Vehicle(map.intersect[9], times, route_choose(route_0to9), random.randint(1, 50)))
        vehicle_list.append(Vehicle(map.intersect[9], times, route_choose(route_1to9), random.randint(1, 50)))
        vehicle_list.append(Vehicle(map.intersect[9], times, route_choose(route_5to9), random.randint(1, 50)))
        vehicle_list.append(Vehicle(map.intersect[5], times, route_choose(route_1to5), random.randint(1, 50)))
        vehicle_list.append(Vehicle(map.intersect[1], times, route_choose(route_5to1), random.randint(1, 50)))
       
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
    
class Road:
    def __init__(self, start, end, capacity, timespend, canvas):
        self.start = start
        self.end = end
        self.capacity = capacity
        self.current = 0
        self.timespend = timespend
        self.inside = 0
        self.actualspend = timespend
        self.canvas = canvas
        self.color = "white"
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
    def checkcurrent(self, vehicle_list, time):
        self.inside = 0
        for vehicle in vehicle_list:
            if vehicle.current.end.name == vehicle.destination.name and time >= vehicle.clock and vehicle.current == self:
                print(str(vehicle.number)+ " vehicle arrive to its destination " + vehicle.destination.name)
                print("Arrived at : " + str(vehicle.clock))
            elif vehicle.current == self:
                self.inside += vehicle.number
        self.actualspend = self.timespend * (1 + self.inside / self.capacity)
        if self.inside / self.capacity >= 0 and self.inside / self.capacity < 0.2:
            self.canvas.itemconfig(self.image, fill = "white")
        elif self.inside / self.capacity >= 0.2 and self.inside / self.capacity < 0.4:
            self.canvas.itemconfig(self.image, fill = "green")
        elif self.inside / self.capacity >= 0.4 and self.inside / self.capacity < 0.6:
            self.canvas.itemconfig(self.image, fill = "yellow")
        elif self.inside / self.capacity >= 0.6 and self.inside / self.capacity < 0.8:
            self.canvas.itemconfig(self.image, fill = "orange")
        else:
            self.canvas.itemconfig(self.image, fill = "red")
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