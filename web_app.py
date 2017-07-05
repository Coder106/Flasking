from flask import Flask, render_template
import pygal
from pygal.style import DarkColorizedStyle
import urllib
import json



app = Flask(__name__)


 
# defining varilable which is equivalent to API address
url = 'http://api.openweathermap.org/data/2.5/forecast?q=Bratislava,sk&APPID=da7ef3742e9243a184bbea82fc508775&mode=json&units=metric'

# downloading the data from url and reading
raw_data = urllib.urlopen(url)
data = raw_data.read()

# loading the downloaded data to a json object divided by each day of the whole 5 total
json_data = json.loads(data)

# filtering out the most important data sets for day-1
city = json_data['city']['name']

# to get the min temperature for each of the 5 days
# for i in range(0,4):
# 	day_1_5_min_temp = json_data['list'][i]['main']['temp_min']

day_1_5_min_temp = []
for i in range(0,5):
	day_1_5_min_temp.append(json_data['list'][i]['main']['temp_min'])
	i = i + 1

# to get the max temperarture for each of the 5 days
# for i in range(0,4):
# 	day_1_5_max_temp = json_data['list'][i]['main']['temp_max']

day_1_5_max_temp = []
for j in range(0,5):
	day_1_5_max_temp.append(json_data['list'][j]['main']['temp_max'])
	j = j + 1

# to get the average temperature for each of the 5 
# for i in range(0,4):
# 	day_1_5_avg_temp = json_data['list'][i]['main']['temp']

day_1_5_avg_temp = []
for k in range(0,5):
	day_1_5_avg_temp.append(json_data['list'][k]['main']['temp_max'])
	k = k + 1

# to get the humidity for each of the 5 days
# for i in range(0,4):
#     day_1_5_humidity = json_data['list'][i]['main']['humidity']


day_1_5_humidity = []
for l in range(0,5):
	day_1_5_humidity.append(json_data['list'][l]['main']['humidity'])
	l = l + 1


# day1_minimum_temp = json_data['list'][0]['main']['temp_min']
# day1_maximum_temp = json_data['list'][0]['main']['temp_max']
# day_1_average_temp = json_data['list'][0]['main']['temp']
# day_1_humidity = json_data['list'][0]['main']['humidity']


  
                                                                                             
@app.route('/')
def pygalexample():
	graph = pygal.StackedLine(fill=True, interpolate='cubic', style=DarkColorizedStyle)
	graph.title = 'A web scraped weather data showing the current weather in our beloved city of Braislava.'
	graph.x_labels = ['Day0','Day1','Day2','Day3','Day4']
	graph.add('Minimum Temp',[day_1_5_min_temp[0],day_1_5_min_temp[1],day_1_5_min_temp[2],day_1_5_min_temp[3],day_1_5_min_temp[4]])
	graph.add('Maximum Temp',[day_1_5_max_temp[0],day_1_5_max_temp[1],day_1_5_max_temp[2],day_1_5_max_temp[3],day_1_5_max_temp[4]])
	graph.add('average_temp',[day_1_5_avg_temp[0],day_1_5_avg_temp[1],day_1_5_avg_temp[2],day_1_5_avg_temp[3],day_1_5_avg_temp[4]])
	graph.add('Humidity',[day_1_5_humidity[0],day_1_5_humidity[1],day_1_5_humidity[2],day_1_5_humidity[3],day_1_5_humidity[4]])
	
	graph_data = graph.render_data_uri()
	return render_template("index.html", graph_data = graph_data)













# @app.route('/')
# def homepage():
#     return render_template("index.html")


@app.route('/tutorials/')
def tutorials():
	return get_weather()

@app.route('/journal/')
def journal():
	return render_template("journal.html")


@app.route('/discussion_points/')
def discussion_points():
	render_template("discussion_points.html")


#if __name__ == "__main__":
 #   app.run(debug=True)
