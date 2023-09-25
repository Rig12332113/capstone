import random
import tkinter as tk
import time
POINT_SIZE = 8
LINE_WIDTH = 6
def main():
    """
    generate canvas
    """
    windows = tk.Tk()
    windows.title("Simulation")
    canvas = tk.Canvas(windows, width = 300, height = 200)
    canvas.pack()
    
    """
    Define map, inclding roads and intersections.
    Also, define route to specific destination.
    """ 
    print("simulation start")
    map = Map()
    map.intersect.append(Node("nodeA", 50, 10, canvas))
    map.intersect.append(Node("nodeB", 50, 50, canvas))
    map.intersect.append(Node("nodeC", 50, 90, canvas))
    map.intersect.append(Node("nodeD", 10, 50, canvas))
    void = Road(map.intersect[0], map.intersect[0], 0, 0, canvas)
    map.road.append(Road(map.intersect[0], map.intersect[1], 30, 2, canvas))
    map.road.append(Road(map.intersect[1], map.intersect[2], 25, 3, canvas))
    map.road.append(Road(map.intersect[1], map.intersect[3], 25, 5, canvas))
    road_list1 = []
    road_list2 = []
    road_list1.append(void)
    road_list1.append(map.road[0])
    road_list1.append(map.road[1])
    road_list2.append(void)
    road_list2.append(map.road[0])
    road_list2.append(map.road[2])

    """
    Start simulation:
    generate vehicle --> run simulation in time interval
    """
    vehicle_list = []
    vehicle_list.append(Vehicle(map.intersect[2], 0, road_list1, random.randint(0, 15)))
    vehicle_list.append(Vehicle(map.intersect[3], 2, road_list2, random.randint(0, 15)))
    for times in range(15):
        for vehicle in vehicle_list:
            if times >= vehicle.clock:
                vehicle.moveforward()
        map.checkmap(vehicle_list, times)
        for intersect in map.intersect:
            canvas.tag_raise(intersect.image)
        map.printmap(times)
        time.sleep(1)
        windows.update()
    print("finish simulation")
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
        self.image = canvas.create_line(self.start.location_x, self.start.location_y, 
                                        self.end.location_x, self.end.location_y, width = LINE_WIDTH, fill = self.color)
        pass
    def printcurrent(self, time):
        print("Time " + str(time) + " at the road from " + self.start.name + " to " + self.end.name + " has " + str(self.inside) + " cars.")
        pass
    def checkcurrent(self, vehicle_list, time):
        self.inside = 0
        for vehicle in vehicle_list:
            if vehicle.current.end.name == vehicle.destination.name and time >= vehicle.clock and vehicle.current == self:
                print("vehicle arrive to its destination " + vehicle.destination.name)
                print("Arrived at : " + str(vehicle.clock))
            elif vehicle.current == self:
                self.inside += vehicle.number
        self.actualspend = self.timespend * (1 + self.inside / self.capacity)
        if self.inside / self.capacity >= 0 and self.inside / self.capacity < 0.2:
            self.canvas.itemconfig(self.image, fill = "white")
        elif self.inside / self.capacity >= 0.2 and self.inside / self.capacity < 0.5:
            self.canvas.itemconfig(self.image, fill = "yellow")
        else:
            self.canvas.itemconfig(self.image, fill = "red")
        pass
    
class Vehicle:
    def __init__(self, destination, time, route, number):
        self.current = route.pop(0)
        self.destination = destination
        self.clock = time + self.current.actualspend
        self.road = route
        self.number = number
        pass
    def moveforward(self):
        if len(self.road) != 0:
            self.current = self.road.pop(0)
            self.clock += self.current.actualspend
        pass
            

if __name__ == '__main__':
    main()