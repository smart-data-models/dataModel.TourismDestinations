# Example code for TourismDwellTimeObserved in dataModel.TourismDestinations
from pysmartdatamodels import pysmartdatamodels as sdm
import subprocess
serverUrl = 'http://localhost:1026'
dateObserved = "2024-12-31T10:30:00Z"
print(sdm.update_broker('TourismDwellTimeObserved', 'dataModel.TourismDestinations', 'dateObserved', dateObserved, serverUrl=serverUrl, updateThenCreate=True))
hour = 10
print(sdm.update_broker('TourismDwellTimeObserved', 'dataModel.TourismDestinations', 'hour', hour, serverUrl=serverUrl, updateThenCreate=True))
locationCode = "CO1313"
print(sdm.update_broker('TourismDwellTimeObserved', 'dataModel.TourismDestinations', 'locationCode', locationCode, serverUrl=serverUrl, updateThenCreate=True))
