#this is a calculator to determine the flight time between any two medium or large
#airports in the world. Input all speeds in terms of miles and use ICAO codes of airports
#currently supports 5178 airports around the world(large and medium airports)
#encoding utf-8

import math
import tkinter as tk
import json
import requests

apiKey = 'ENTER API KEY HERE'
#insert free checkwx api key here
#sign up at www.checkwx.com for a free api key


def apiStationGet():
    global initialTarget
    global destinationTarget
    global initialAirportGetName
    global initialName
    global destinationName
    global initialCountryName
    global destinationCountryName
    global apiKey
    global latitude1
    global latitude2
    global longitude1
    global longitude2
    global initialNameID
    global destinationNameID
    global initialAirportGetCountryStr
    global destinationAirportGetCountryStr
    global initialAirportGetCity
    global destinationAirportGetCity
    hdr = { 'X-Api-Key': apiKey }
    baseUrlStation = 'https://api.checkwx.com/station/'
    initialStationIcao = initialTarget.lower()
    destinationStationIcao = destinationTarget.lower()
    combinedStationUrl = baseUrlStation + initialStationIcao + "," + destinationStationIcao
    stationReq = requests.get(combinedStationUrl, headers=hdr)
    jsonData = json.loads(stationReq.text)
    jsonFinalData = jsonData.get('data')
    initialAirportGet = jsonFinalData[0]
    initialLatitudeGet = initialAirportGet['latitude']
    initialLatitudeGetFloat = float(initialLatitudeGet['decimal'])
    initialLongitudeGet = initialAirportGet['longitude']
    initialLongitudeGetFloat = float(initialLongitudeGet['decimal'])
    destinationAirportGet = jsonFinalData[1]
    destinationLatitudeGet = destinationAirportGet['latitude']
    destinationLatitudeGetFloat = float(destinationLatitudeGet['decimal'])
    destinationLongitudeGet = destinationAirportGet['longitude']
    destinationLongitudeGetFloat = float(destinationLongitudeGet['decimal'])
    initialAirportGetName = initialAirportGet['name']
    destinationAirportGetName = destinationAirportGet['name']
    initialAirportGetCountryCode = initialAirportGet['country']
    initialAirportGetCountryCodeStr = str(initialAirportGetCountryCode['code'])
    destinationAirportGetCountryCode = destinationAirportGet['country']
    destinationAirportGetCountryCodeStr = str(destinationAirportGetCountryCode['code'])
    initialAirportGetCity = initialAirportGet['city']
    destinationAirportGetCity = destinationAirportGet['city']
    if initialAirportGetCountryCodeStr == 'US':
        initialAirportGetCountry = initialAirportGet['state']
        initialAirportGetCountryStr = initialAirportGetCountry['name']
    else:
        initialAirportGetCountry = initialAirportGet['country']
        initialAirportGetCountryStr = initialAirportGetCountry['name']
    if destinationAirportGetCountryCodeStr == 'US':
        destinationAirportGetCountry = destinationAirportGet['state']
        destinationAirportGetCountryStr = destinationAirportGetCountry['name']
    else:
        destinationAirportGetCountry = destinationAirportGet['country']
        destinationAirportGetCountryStr = destinationAirportGetCountry['name']
    initialNameID = str(initialAirportGetName) + ' Airport'
    destinationNameID = str(destinationAirportGetName) + ' Airport'
    latitude1 = initialLatitudeGetFloat
    latitude2 = destinationLatitudeGetFloat
    longitude1 = initialLongitudeGetFloat
    longitude2 = destinationLongitudeGetFloat


radius = 3958 #radius of earth(in miles)
icaoList = []
latitudeList = []
longitudeList = []
airportNameList = []
codeList= []
countryList = []
orderedCodeList = []
cityNameList = []
intervalLatList = []
intervalLonList = []
source = "CHECKWX"

def airportDistance():
    global distance
    global dlon
    global dlat
    global lat1
    global lat2
    global lon1
    global lon2
    global c
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


def manualWindVectorAddition():
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
gui.title("Flight Distance Calculator")
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
    global initialTarget
    global repetitionConstant
    global destinationTarget
    global indicatedAirSpeed
    global windAngleDifference
    global windSpeed
    global flightHours
    global flightMinutes
    global initialName
    global destinationName
    global intervalFraction
    global latitude1, latitude2, longitude1, longitude2
    global source
    global initialNameID
    global destinationNameID
    global initialAirportGetCity
    global destinationAirportGetCity
    global initialAirportGetCountryStr
    global destinationAirportGetCountryStr
    initialTarget = str(initialInput.get())
    destinationTarget = str(destinationInput.get())
    indicatedAirSpeed = float(speedInput.get())
    windSpeed = float(windSpeedInput.get())
    windAngleDifference = float(windAngleInput.get())
    if source == "CHECKWX":
        apiStationGet()
    airportDistance()
    manualWindVectorAddition()
    flightTime()
    finalTimeString = tk.StringVar()
    finalDistanceString = tk.StringVar()
    groundSpeedString = tk.StringVar()
    initialLocationString = tk.StringVar()
    initialNameString = tk.StringVar()
    destinationNameString = tk.StringVar()
    destinationLocationString = tk.StringVar()
    groundSpeedString = round(groundSpeed,2), "mph"
    if source == "CHECKWX":
        initialNameString = initialNameID
        destinationNameString = destinationNameID
        initialCity = initialAirportGetCity
        destinationCity = destinationAirportGetCity
        initialCountryName = initialAirportGetCountryStr
        destinationCountryName = destinationAirportGetCountryStr
    initialLocationString = "↑ {}, {}".format(initialCity, initialCountryName)
    destinationLocationString = "↓ {}, {}".format(destinationCity, destinationCountryName)
    finalDistanceString = round(distance, 2), "miles"
    if timeOfFlight < 1:
        finalTimeString = round(flightMinutes, 1), "minutes"
    else:
        finalTimeString = flightHours , "hours" , flightMinutes, "minutes"
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

























