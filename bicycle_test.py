import unittest
from bikes import Bicycle
from math import pi

class basicBicycleTest(unittest.TestCase):
    def setUp(self):
       self.bike = Bicycle()

    def tearDown(self):
        self.bike = Bicycle()

class testBicycleDefaults(basicBicycleTest):
    def testDefaults(self):
        self.assertEqual(self.bike.frontChainrings, 2)
        self.assertEqual(self.bike.cassetteGears, 10)
        self.assertEqual(self.bike.presentFrontGear, 1)
        self.assertEqual(self.bike.presentRearGear, 1)
        self.assertEqual(self.bike.rearGears, [12, 13, 14, 15, 16, 17, 19, 21, 23, 25])
        self.assertEqual(self.bike.rimDiameter, 622)
        self.assertEqual(self.bike.tireDiameter, 35)

class testBicycleShifting(basicBicycleTest):
    def testFrontShifting(self):
        self.assertEqual(self.bike.presentFrontGear, 1)
        self.bike.upshiftFront()
        self.assertEqual(self.bike.presentFrontGear, 2)
        self.bike.upshiftFront()
        self.assertEqual(self.bike.presentFrontGear, 2)
        self.bike.downshiftFront()
        self.assertEqual(self.bike.presentFrontGear, 1)
        self.bike.downshiftFront()
        self.assertEqual(self.bike.presentFrontGear, 1)

    def testRearShifting(self):
        self.assertEqual(self.bike.presentRearGear, 1)
        for _ in range(4):
            self.bike.upshiftRear()
        self.assertEqual(self.bike.presentRearGear, 5)
        for _ in range(5):
            self.bike.upshiftRear()
        self.assertEqual(self.bike.presentRearGear, 10)
        self.bike.upshiftRear()
        self.assertEqual(self.bike.presentRearGear, 10)
        for _ in range(9):
            self.bike.downshiftRear()
        self.assertEqual(self.bike.presentRearGear, 1)
        self.bike.downshiftRear()
        self.assertEqual(self.bike.presentRearGear, 1)

class testTeeth(basicBicycleTest):
    def testRearTeeth(self):
        self.assertEqual(self.bike.rearTeeth(), 12)

    def testFrontTeeth(self):
        self.assertEqual(self.bike.frontTeeth(), 39)

class testRatio(basicBicycleTest):
    def testRatio(self):
        self.assertEqual(self.bike.gearRatio(), 39/12)
        for _ in range(10):
            self.bike.upshiftRear()
            self.bike.upshiftFront()
        self.assertEqual(self.bike.gearRatio(), 53/25)

class testDiameterAndCircumference(basicBicycleTest):
    def testDiameter(self):
        self.assertEqual(self.bike.wheelDiameter(), 692)

    def testCircumference(self):
        self.assertEqual(self.bike.wheelCircumference(), 692*pi)

class testDistances(basicBicycleTest):
    def testDistPerPedalRev(self):
        self.assertAlmostEqual(self.bike.distancePerPedalRev(), self.bike.wheelCircumference() * 39/12)

    def testDistancePerMinute(self):
        self.assertAlmostEqual(self.bike.distancePerMinute(50), self.bike.distancePerPedalRev()*50)

class testSetters(basicBicycleTest):
    def testFrontChainringsSetter(self):
        self.bike.frontChainrings = 3
        self.assertEqual(self.bike.frontChainrings, 3)

    def testRearCassetteSetter(self):
        self.bike.cassetteGears = 7
        self.assertEqual(self.bike.cassetteGears, 7)

    def testFrontRingsSetter(self):
        self.bike.frontRings = [41, 62]
        self.assertEqual(self.bike.frontRings, [41, 62])

    def testRearGearsSetter(self):
        self.bike.rearGears = [12, 13, 15, 17, 20, 24, 29]
        self.assertEqual(self.bike.rearGears, [12, 13,15, 17, 20, 24, 29])

    def testRimDiameterSetter(self):
        self.bike.rimDiameter = 511
        self.assertEqual(self.bike.rimDiameter, 511)

    def testTireDiameterSetter(self):
        self.bike.tireDiameter = 32
        self.assertEqual(self.bike.tireDiameter, 32)



if __name__ == '__main__':
    unittest.main()