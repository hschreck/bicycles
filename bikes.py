class Bicycle:

    def __init__(self):
        self._frontChainrings = 2
        self._cassetteGears = 10
        self._presentFrontGear = 1
        self._presentRearGear = 1
        self._rimDiameter = 622
        self._tireDiameter = 35
        self._frontRings = [39, 53]
        self._rearGears = [12, 13, 14, 15, 16, 17, 19, 21, 23, 25]


    @property
    def frontChainrings(self):
        return self._frontChainrings

    @frontChainrings.setter
    def frontChainrings(self, value):
        self._frontChainrings = value

    @property
    def cassetteGears(self):
        return self._cassetteGears

    @cassetteGears.setter
    def cassetteGears(self, value):
        self._cassetteGears = value

    @property
    def frontRings(self):
        return self._frontRings

    @frontRings.setter
    def frontRings(self, value):
        self._frontRings = value

    @property
    def rearGears(self):
        return self._rearGears

    @rearGears.setter
    def rearGears(self, value):
        self._rearGears = value

    @property
    def presentFrontGear(self):
        return self._presentFrontGear

    @presentFrontGear.setter
    def presentFrontGear(self, value):
        self._presentFrontGear = value

    @property
    def presentRearGear(self):
        return self._presentRearGear

    @presentRearGear.setter
    def presentRearGear(self, value):
        self._presentRearGear = value


    def upshiftFront(self):
        self._presentFrontGear = min(self._frontChainrings, self._presentFrontGear+1)

    def downshiftFront(self):
        self._presentFrontGear = max(1, self._presentFrontGear - 1)

    def upshiftRear(self):
        self._presentRearGear = min(self._cassetteGears, self._presentRearGear + 1)

    def downshiftRear(self):
        self._presentRearGear = max(1, self._presentRearGear - 1)

    def rearTeeth(self):
        return self._rearGears[self._presentRearGear - 1]

    def frontTeeth(self):
        return self._frontRings[self._presentFrontGear - 1]

    def gearRatio(self):
        return self.frontTeeth() / self.rearTeeth()

    def wheelDiameter(self):
        return self._rimDiameter + 2 * (self._tireDiameter)

    def wheelCircumference(self):
        return 3.14159 * self.wheelDiameter()

    def distancePerPedalRev(self):
        return self.gearRatio() * self.wheelCircumference()

    def distancePerMinute(self, cadence):
        return self.distancePerPedalRev() * cadence