#this is a calculator to determine the flight time between any two medium or large
#airports in the world. Input all speeds in terms of miles and use ICAO codes of airports
#currently supports 5178 airports around the world(large and medium airports)
#encoding utf-8

import math
import tkinter as tk

radius = 3958 #radius of earth(in miles)
icaoList = []
latitudeList = []
longitudeList = []
airportNameList = []
codeList= []
countryList = []
orderedCodeList = []
cityNameList = []
source = "DESKTOP"
#if source is personal desktop, enter DESKTOP for source
#if source is personal laptop, enter LAPTOP for source
#currently this program only works with two of my personal computers because the data required to run the program is stored only on these two computers. 
#full external support coming soon

def airportListSetup():
    if source == "LAPTOP":
        f = open("C:\\Users\\siddh\\Documents\\Python\\Flight Distance Calculator\\icao.txt", 'r')
        for line in f:
            icaoList.append(line.strip())
    
        latitudeSetup = open("C:\\Users\\siddh\\Documents\\Python\\Flight Distance Calculator\\latitudes.txt", 'r')
        for line in latitudeSetup:
            latitudeList.append(line.strip())
    
        longitudeSetup = open("C:\\Users\\siddh\\Documents\\Python\\Flight Distance Calculator\\longitudes.txt", 'r')
        for line in longitudeSetup: 
            longitudeList.append(line.strip())

        nameSetup = open("C:\\Users\\siddh\\Documents\\Python\\Flight Distance Calculator\\airportNames.txt", 'r', encoding="utf8")
        for line in nameSetup:
            airportNameList.append(line.strip())
    
        codeSetup = open("C:\\Users\\siddh\\Documents\\Python\\Flight Distance Calculator\\codes.txt", 'r', encoding = "utf8")
        for line in codeSetup:
            codeList.append(line.strip())
        
        countrySetup = open("C:\\Users\\siddh\\Documents\\Python\\Flight Distance Calculator\\countries.txt", 'r', encoding="utf8")
        for line in countrySetup:
            countryList.append(line.strip())

        orderedAirportSetup = open("C:\\Users\\siddh\\Documents\\Python\\Flight Distance Calculator\\orderedairportcodes.txt", 'r', encoding="utf8")
        for line in orderedAirportSetup:
            orderedCodeList.append(line.strip())
    
        cityNameSetup = open("C:\\Users\\siddh\\Documents\\Python\\Flight Distance Calculator\\citynames.txt", 'r', encoding="utf8")
        for line in cityNameSetup:
            cityNameList.append(line.strip())
    if source == "DESKTOP":
        f = open("D:\\Documents\\School\\Code\\FlightDistanceCalculator\\icao.txt", 'r')
        for line in f:
            icaoList.append(line.strip())
    
        latitudeSetup = open("D:\\Documents\\School\\Code\\FlightDistanceCalculator\\latitudes.txt", 'r')
        for line in latitudeSetup:
            latitudeList.append(line.strip())
    
        longitudeSetup = open("D:\\Documents\\School\\Code\\FlightDistanceCalculator\\longitudes.txt", 'r')
        for line in longitudeSetup: 
            longitudeList.append(line.strip())

        nameSetup = open("D:\\Documents\\School\\Code\\FlightDistanceCalculator\\airportNames.txt", 'r', encoding="utf8")
        for line in nameSetup:
            airportNameList.append(line.strip())
    
        codeSetup = open("D:\\Documents\School\\Code\\FlightDistanceCalculator\\codes.txt", 'r', encoding = "utf8")
        for line in codeSetup:
            codeList.append(line.strip())
        
        countrySetup = open("D:\\Documents\School\\Code\\FlightDistanceCalculator\\countries.txt", 'r', encoding="utf8")
        for line in countrySetup:
            countryList.append(line.strip())

        orderedAirportSetup = open("D:\\Documents\School\\Code\\FlightDistanceCalculator\\orderedairportcodes.txt", 'r', encoding="utf8")
        for line in orderedAirportSetup:
            orderedCodeList.append(line.strip())
    
        cityNameSetup = open("D:\\Documents\\School\\Code\\FlightDistanceCalculator\\citynames.txt", 'r', encoding="utf8")
        for line in cityNameSetup:
            cityNameList.append(line.strip())
    
      

#imports information for all large and medium airports in the world and appends each piece
# of information into a separate list for later reference. 

def linearCoordinateSearch():
    global initialTarget
    global destinationTarget
    global initialPosition
    global destinationPosition
    global initialFound
    global destinationFound
    initialPosition = 0
    destinationPosition = 0
    initialFound = False
    destinationFound = False
    while initialPosition < len(icaoList) and not initialFound:
        if icaoList[initialPosition] == initialTarget:
            initialFound = True
        else:
            initialPosition = initialPosition + 1
    while destinationPosition < len(icaoList) and not destinationFound:
        if icaoList[destinationPosition] == destinationTarget:
            destinationFound = True
        else:
            destinationPosition = destinationPosition + 1
    if initialFound == True:
        global latitude1
        global longitude1
        global initialName
        global initialCode
        global initialCity
        latitude1 = latitudeList[initialPosition]
        longitude1 = longitudeList[initialPosition]
        initialName = str(airportNameList[initialPosition])
        initialCode = str(orderedCodeList[initialPosition])
        initialCity = str(cityNameList[initialPosition])
    if destinationFound == True:
        global latitude2
        global longitude2
        global destinationName
        global destinationCode
        global destinationCity
        latitude2 = latitudeList[destinationPosition]
        longitude2 = longitudeList[destinationPosition]
        destinationName = str(airportNameList[destinationPosition])
        destinationCode = str(orderedCodeList[destinationPosition])
        destinationCity = str(cityNameList[destinationPosition])
    
    if initialFound == False:
        print("The initial airport could not be found")
    if destinationFound == False:
        print("The destination airport could not be found")
    
    
def countryCodeInterpreter():
    global initialCode
    global destinationCode
    global initialCountryName
    global destinationCountryName
    initialCodeFound = False
    initialCodePosition = 0
    while initialCodePosition < len(codeList) and not initialCodeFound:
        if codeList[initialCodePosition] == initialCode:
            initialCodeFound = True
        else:
            initialCodePosition = initialCodePosition + 1
    destinationCodeFound = False
    destinationCodePosition = 0
    while destinationCodePosition < len(codeList) and not destinationCodeFound:
        if codeList[destinationCodePosition] == destinationCode:
            destinationCodeFound = True
        else:
            destinationCodePosition = destinationCodePosition + 1
    initialCountryName = countryList[initialCodePosition]
    destinationCountryName = countryList[destinationCodePosition]
    

def airportDistance():
    global distance
    lat1 = float(latitude1)
    lon1 = float(longitude1)
    lat2 = float(latitude2)
    lon2 = float(longitude2)
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = radius * c

#this function calculates the great circle distance between two points on Earth using the 
#haversine formula. 

def windVectorAddition():
    global groundSpeed
    global indicatedAirSpeed
    global windSpeed
    global windAngleDifference
    groundSpeed = math.sqrt(((indicatedAirSpeed ** 2) + windSpeed) - 2 * (indicatedAirSpeed * windSpeed * math.cos(windAngleDifference)))

#this function accounts for the speed of wind affecting the flight of the aircraft using vector addition

def flightTime():
    global timeOfFlight
    global groundSpeed
    global flightHours
    global flightMinutes
    timeOfFlight = ((distance - 100)/groundSpeed) + 0.45

    flightHours = int(timeOfFlight)
    if timeOfFlight >= 1:
        flightMinutes = int((timeOfFlight % flightHours) * 60)
    if timeOfFlight < 1:
        flightMinutes = timeOfFlight * 60

#this function uses the calculated groundspeed and distance to calculate flight time. In this
#function, 45 minutes are accounted for climb and descent where the aircraft isn't travelling
#at maximum cruise speed. 


gui = tk.Tk()
gui.configure(background = "grey17")
gui.title(" ")
gui.geometry("250x150")


initialInput = tk.StringVar()
destinationInput = tk.StringVar()
speedInput = tk.StringVar()
windSpeedInput = tk.StringVar()
windAngleInput = tk.StringVar()



initialField = tk.Entry(gui, textvariable=initialInput, bg="grey30", fg="gray97", bd=0)
destinationField = tk.Entry(gui, textvariable = destinationInput, bg="grey30", fg="gray97", bd=0)
speedField = tk.Entry(gui, textvariable=speedInput, bg="grey30", fg="gray97", bd=0)
windSpeedField = tk.Entry(gui, textvariable=windSpeedInput, bg="grey30", fg="gray97", bd=0)
windAngleField = tk.Entry(gui, textvariable=windAngleInput, bg="grey30", fg="gray97", bd=0)

flightDistanceCalculatorlabel = tk.Label(gui, text="Flight Distance Calculator", bg="grey17", fg="gray97")
initialAirportLabel = tk.Label(gui, text="Starting Airport :                ", bg="grey17", fg="gray97", anchor="e")
destinationAirportLabel = tk.Label(gui, text="Destination Airport :          ", bg="grey17", fg="gray97", anchor="e")
indicatedAirspeedLabel = tk.Label(gui, text="Indicated Airspeed :          ", bg="grey17", fg="gray97", anchor="e")
windSpeedLabel = tk.Label(gui, text="Wind Speed :                      ", bg="grey17", fg="gray97", anchor="e")
angleOfWindLabel = tk.Label(gui, text="Angle of Wind :                  ", bg="grey17", fg="gray97", anchor="e")

initialField.grid(row=1, column=1)
destinationField.grid(row=2, column=1)
speedField.grid(row=3, column=1)
windSpeedField.grid(row=4, column=1)
windAngleField.grid(row=5, column=1)

flightDistanceCalculatorlabel.grid(row=0)
initialAirportLabel.grid(row=1)
destinationAirportLabel.grid(row=2)
indicatedAirspeedLabel.grid(row=3)
windSpeedLabel.grid(row=4)
angleOfWindLabel.grid(row=5)

initialNameDisplay = tk.Label(gui, text="", bg="gray17", fg="gray97")
finalTimeDisplay = tk.Label(gui, text="", bg="gray17", fg="gray97")
finalDistance = tk.Label(gui, text="", bg="gray17", fg="gray97")
ttkgroundSpeed = tk.Label(gui, text="", bg="gray17", fg="gray97")
initialLocation = tk.Label(gui, text="", bg="gray17", fg="gray97", anchor="w")
destinationLocation = tk.Label(gui, text="", bg="gray17", fg="gray97", anchor="w")
destinationNametk = tk.Label(gui, text="", bg="gray17", fg="gray97")

initialNameDisplay.grid(row=0, column=3, columnspan=2)
finalTimeDisplay.grid(row=2, column=3)
finalDistance.grid(row=3, column=3)
ttkgroundSpeed.grid(row=4, column=3)
initialLocation.grid(row=1, column=3)
destinationLocation.grid(row=5, column=3)
destinationNametk.grid(row=6, column=3)

def executeCalculation():
    airportListSetup()
    global initialTarget
    global destinationTarget
    global indicatedAirSpeed
    global windAngleDifference
    global windSpeed
    global flightHours
    global flightMinutes
    global initialName
    global destinationName
    initialTarget = str(initialInput.get())
    destinationTarget = str(destinationInput.get())
    indicatedAirSpeed = float(speedInput.get())
    windSpeed = float(windSpeedInput.get())
    windAngleDifference = float(windAngleInput.get())
    linearCoordinateSearch()
    countryCodeInterpreter()
    airportDistance()
    windVectorAddition()
    flightTime()
    finalTimeString = tk.StringVar()
    finalDistanceString = tk.StringVar()
    groundSpeedString = tk.StringVar()
    initialLocationString = tk.StringVar()
    initialNameString = tk.StringVar()
    destinationNameString = tk.StringVar()
    destinationLocationString = tk.StringVar()
    groundSpeedString = round(groundSpeed,2), "mph"
    initialLocationString = "↑ {}, {}".format(initialCity, initialCountryName)
    destinationLocationString = "↓ {}, {}".format(destinationCity, destinationCountryName)
    finalDistanceString = round(distance, 2), "miles"
    if timeOfFlight < 1:
        finalTimeString = round(flightMinutes, 1), "minutes"
    else:
        finalTimeString = flightHours , "hours" , flightMinutes, "minutes"
    initialNameString = initialName
    destinationNameString = destinationName
    gui.geometry("500x150")
    initialNameDisplay.config(text=initialNameString)
    finalTimeDisplay.config(text=finalTimeString)
    finalDistance.config(text=finalDistanceString)
    ttkgroundSpeed.config(text=groundSpeedString)
    initialLocation.config(text=initialLocationString)
    destinationLocation.config(text=destinationLocationString)
    destinationNametk.config(text=destinationNameString)

    
execute = tk.Button(gui, text="Calculate", command=executeCalculation, width=37, fg="gray97", bg="gray30", bd=0)
execute.grid(row=6, columnspan=2)

gui.mainloop()











