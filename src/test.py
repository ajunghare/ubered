from src.models import Address
from src.util import do_get
from datetime import datetime
from datetime import timedelta

def tryme():
    source = Address("12.927880,77.627600")
    dest = Address("13.035542,77.597100")
    email = "ajunghare123@gmail.com"
    td = {"hh":20,"mm":30}

    source = Address("19.0607926,73.002986")
    dest = Address("19.1173159,72.866745")
    met(source,dest,td,email)

def get_uber_time(location):
    url_uber = "https://rr1iky5f5f.execute-api.us-east-1.amazonaws.com/api/estimate/time?start_longitude={0}&start_latitude={1}"
    url_uber = url_uber.format(location.long, location.lat)
    print(url_uber)
    details = do_get(url_uber)["times"]
    estimate = 9999999 # setting maximum integer for this use case
    print ("uber time", details)
    if len(details) == 0:
        # case: no uber
        return -1
    else:
        for uber in details:
            # considering uberGo only as per assumption
            if int(uber["estimate"]) >= 0 and uber["localized_display_name"]=="uberGO":
                # skipping negative time
                if estimate > int(uber["estimate"]):
                    estimate = int(uber["estimate"])
    if estimate == -2:
        # case when all Ubers gives -1
        return -1

    return estimate

def get_map_time(src, dest, key="AIzaSyAQB4eiCnuP8RXt0xPLYmsCDqrWX4iFKGc"):

    url_map = "https://maps.googleapis.com/maps/api/directions/json?origin={0},{1}&destination={2},{3}&key={4}"
    url_map = url_map.format(src.long, src.lat, dest.long, dest.lat, key)
    print (url_map)
    details = do_get(url_map)
    #as 0th index will have one with minimum time
    time_for_shortest_distance = details['routes'][0]['legs'][0]['duration']['value']

    return time_for_shortest_distance



def met(source, destination, time_of_day, email):

    uber_arrival_time = get_uber_time(source)
    #print ("uber_arrival_time",uber_arrival_time)
    if uber_arrival_time != -1:
        # call map API
        actual_arrival_time = get_map_time(source,destination)
        total_time = uber_arrival_time + actual_arrival_time
        #print ("absolute time to reach destination",total_time/60)
        today = datetime.now()
        #print ("^^^^^^^^^^^^^^^^^^",time_of_day)
        today.replace(hour=time_of_day["hh"])
        today.replace(minute=time_of_day["mm"])
        time_to_book = today-timedelta(seconds=total_time)
        print( time_to_book)
if __name__=="__main__":
    tryme()
