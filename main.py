import requests
import matplotlib.pyplot as plt
import time
#base api 
url = "https://api.open-meteo.com/v1/forecast?latitude=2.0469&longitude=45.3182&current=temperature_2m&temperature_unit=celsius"

def weather():
  #get response
  response = requests.get(url)

  #convert into python dictionary
  data = response.json()

  #local temperature
  temp = data["current"]["temperature_2m"]
  #real time temp
  print("detecting...")
  time.sleep(3)
  print(f"temperature: {temp}°")
  #deciding
  if temp <= 0:
    print("deceted: Freezing")
  elif temp <=10:
    print("detected: very cold")
  elif temp <= 18:
    print("detected: cold")
  elif temp <= 24:
    print("detected: cool")
  elif temp <= 30:
    print("detected: warm")
  elif temp <= 35:
    print("detected: hot")
  elif temp <= 40:
    print("detected: very hot shit")
  else:
    print("ooommmggg")
  x = temp
  y = temp
  plt.plot(temp,1)
  plt.scatter(temp,1)
  plt.show()

if __name__=="__main__":
    weather()
