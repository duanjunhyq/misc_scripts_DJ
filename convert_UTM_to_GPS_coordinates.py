import utm
import csv
import pandas
df = pandas.read_csv('location.csv', index_col='ID')
for index, row in df.iterrows():
    print row["Easting"], row["Northing"],utm.to_latlon(row["Easting"],row["Northing"],10, 'N')