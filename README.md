# surfs_up

## Overview of the statistical analysis:

The purpose of this analysis was to analyze the weather on Oahu, Hawaii throughout the year, to determine if it would be a good location for a surf n' shake shop. The weather data would prove to investors that this location is ideal. 

Weather data was stored in a sqlite database and accessed through sql alchemy. The data included two classes, a measurement class and a station class. The measurement class had information about the date, precipitation amount, temperature, and station for each measurement. The station class had a list of the stations used to collect measurements.  The data was collected between January 1, 2010 and August 23, 2017. The Analysis was performed on jupyter notebook. 


## Results:

This analysis specifically looked at summary statistics for temperature observations for the months of June and December, for the years 2010-2017. The two tables are displayed further down in the results section. 

Three key differences between weather in June and weather in December include:

1. Temperatures are generally colder in December, when compared to June. 
    
    The minimum temperature for December was 56, while mininmum temperature for June was 64. The first quartile, median, third quartile, max, and mean are all lower in December than in January. 

2. Average temperatures in June and December are not significantly different. 
    
    Average temperature in June was 74.9 degrees, while average temperature in December was 71.04. The standard deviation of both months was just over three degrees, so the temperatures are slighlty more than one standard deviation from eachother. This means that even though December is generally cooler than June, the temperature differneces are not significantly different from eachother, as between 68-95% of data falls between 1 and 2 standard deviations from the mean.

3. The average number of measurements taken per day in June and December were both around 7, showing consistency in data collection throughout the year.  

    There were 1517 seperate observations in decembers throughout the years, and 1700 seperate observations in junes throughout the years. The data collected was collected from 8 Junes (2010-2017), and 7 Decembers (2010-2016). On average, each June had 212.5 measurements taken, or about 7 measurements per day. On average, each December had 216.7 measurements taken, or about 6.99 measurements per day. The stations taking measurements seemed to be consistent in the numbers of measurements they took throughout the year. Also, this yielded a large number of measurements, which led to a robust analysis. 

June Summary Statistics:

![June](https://github.com/emariecovey/surfs_up/blob/main/june_sum_statistics.png)

December Summary Statistics:

![December](https://github.com/emariecovey/surfs_up/blob/main/dec_sum_statistics.png)

## Summary:

In summary, Oahu, Hawaii would be an excellent location for a surf n' shake shop. Despite temperatures in December being slightly lower than June, the temperatures were not significantly different, and they were similar enough to show the generally steady climate of Hawaii. Additionally, this was a robust dataset with many seperate weather observations taken many times per day, which should help investors feel confident in the results of the analysis. 

Additional queries could be helpful to gather more data for June and December:

1. Summary statistics for precipitation amount in June and December. The temperature may have been generally steady, but if there is heavy rain, surfers may be scarce. 

2. Average precipitation amounts by station. If stations are positioned throughout the island, looking at precipitation levels by station could show less rainy parts of the island, and may help determine exactly where on the island the surf n' shake shop should be located. 
