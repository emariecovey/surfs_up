###SETTING UP FLASK WEATHER MAP

#make sure to save and kill terminal between times running flask
#export FLASK_APP=app.py
#flask run

#import dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

###SETTING UP ACCESS TO DATABASE
#creates access to database
engine = create_engine("sqlite:///hawaii.sqlite")

#make database into classes
Base = automap_base()

#reflect database
Base.prepare(engine, reflect=True)

#save references to table
Measurement = Base.classes.measurement
Station = Base.classes.station

#create session link from Python to our database
session = Session(engine)

#set up flask (create flask application called "app")
#name value depends on where and how the code is run ex)is it being imported?
#all routes have to go after this next line of code, or it won't run properly
app = Flask(__name__)

#Creating the welcome route (homepage, entryway to rest of analysis)
@app.route("/")

#add routing info for other routes with functions, and return 
# statement has f-strings to reference other routes
#can use f"""stuff between""" for f string on multilines
def welcome(): 
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

#next route: precipitation
@app.route("/api/v1.0/precipitation")

def precipitation():
    #get previous year date
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    #query data to get precipitation for previous year
    precipitation = session.query(Measurement.date, Measurement.prcp)\
        .filter(Measurement.date>=prev_year).all()
    #jsonify precipitation
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)
    

#next route: stations
@app.route("/api/v1.0/stations")

def stations():
    results = session.query(Station.station).all()
    #unravel results into a one-dimensional array
    stations = list(np.ravel(results))
    #makes list into a json. 
    #(stations=stations) same as ({"stations":stations}) (basically making a dictionary out of a list)
    return jsonify(stations=stations)

#next route: monthly temperatures
@app.route("/api/v1.0/tobs")

def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= prev_year).all()
    #unravel list into one-dimensional array
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

#next route: statistics
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def stats(start=None, end=None):
    sel= [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    
    if not end:
        results = session.query(*sel).filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)
    
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)