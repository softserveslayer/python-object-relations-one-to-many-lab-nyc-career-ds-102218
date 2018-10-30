class Trip:
    _all = []

    def __init__(self, start, destination, driver):
        Trip._all.append(self)
        self._start = start
        self._destination = destination
        self._driver = driver
	    # remember to associate a trip with a driver

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, start):
        self._start = start

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, destination):
        self._destination = destination

    @property
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self, driver):
        self._driver = driver
