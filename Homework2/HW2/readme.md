Cloud Homework 2 Weather API

This is a python based restful api which uses a csv file to add, delete and show the data. Also an algorithm is used to forecast the weather of seven days, by averaging the temperatures of past three days.
URL of instance: http://ec2-52-15-253-208.us-east-2.compute.amazonaws.com/
Installation process for installing apache server and wsgi server:
$ sudo yum update
$ sudo yum install httpd
$ sudo pip install flask
$ sudo youm install mode_wsgi-python27.x86_64

URL:
Get all dates:
http://ec2-52-15-253-208.us-east-2.compute.amazonaws.com/historical/
Get specific date data:
http://ec2-52-15-253-208.us-east-2.compute.amazonaws.com/historical/YYYYMMDD
Add data using post method
http://ec2-52-15-253-208.us-east-2.compute.amazonaws.com/
Delete data using delete method
http://ec2-52-15-253-208.us-east-2.compute.amazonaws.com/historical/YYYYMMDD
Forecast data
http://ec2-52-15-253-208.us-east-2.compute.amazonaws.com/forecast/YYYYMMDD






