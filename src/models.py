class Address:
    lat = "0.0"
    long = "0.0"

    def __init__(self, longlat):
        splitted = longlat.split(",")
        self.long = splitted[0].strip()
        self.lat = splitted[1].strip()
