import requests

url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

location = str(input("Enter City Name: "))

querystring = {"q": location}

headers = {
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
	"X-RapidAPI-Key": "f686a67b07mshb0a429c52c9a635p1d1aa8jsnb4b44c442673"
}

response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.text)

# extracting data in json format
data = response.json()

# extracting latitude, longitude and formatted address
# of the first matching location
city = data['location']['name']
region = data['location']['region']
country = data['location']['country']
temp_c = data["current"]["temp_c"]
weather = data["current"]["condition"]["text"]

# printing the output
print("City: %s\nState: %s\nCountry: %s\nTemperature(C) - Current: %s\nWeather Condition - Current: %s"
		% (city, region, country, temp_c, weather))
