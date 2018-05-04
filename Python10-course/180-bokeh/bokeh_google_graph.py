#Making a basic Bokeh line graph

#importing Bokeh and pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

#prepare some data
df=pandas.read_csv("http://www.google.com/finance/historical?q=NASDAQ:ADBE&startdate=Jan+01%2C+2009&enddate=Aug+2%2C+2012&output=csv", parse_dates=['Date'])

p=figure(width=500,height=500,x_axis_type="datetime")
p.line(df["Date"],df['Close'],alpha=0.5)

#prepare the output file
output_file("Timeseries.html")


#write the plot in the figure object
show(f)
