#Making a basic Bokeh line graph

#importing Bokeh and pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

#prepare some data
df=pandas.read_csv("bachelors.csv")
x=df['Year']
y=df['Engineering']

#prepare the output file
output_file("Line_wemen.html")

#create a figure object
f=figure()

#create line plot
f.line(x,y)

#write the plot in the figure object
show(f)
