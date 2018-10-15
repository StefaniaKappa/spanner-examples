import time

from Spanner import Spanner

from Testboard import Testboard

import Device



device = Device.Particle("FirstDev")
testboard = Testboard("Tester2")



# Our Testboard's D3 Pin is connected to a power switching circuit that controls

# the power going to the device. When we toggle it HIGH, the device will be

# powered, when LOW, the device will shut down

OUTPUT_PIN = "D7"


def measure_power_consumption():

    # Turn the device off
    testboard.digitalWrite(OUTPUT_PIN, "LOW");

    # Wait for a while for it to shut down

    time.sleep(2)

    # Turn the device back on

    testboard.digitalWrite(OUTPUT_PIN, "HIGH");


    # The device runs some initialization actions in the beginning, which are

    # not indicative of the true power consumption. Therefore we wait for a

    # while for the initial conditions to pass

    #     time.sleep(5)



    # Start measuring power consumption

    #     testboard.startPowerMeasurement()



    # Measure for 5 minutes

    #     time.sleep(10)



    # Stop measuring power consumption

    #     testboard.stopPowerMeasurement()



    #     res = testboard.measuredPowerConsumption()

    #     print('res')

    #     print(str(res))

    # Make sure the total power consumption didn't exceed 100mAh. The

    # measuredPowerConsumption() will return the total power consumption

    # measured in the measuring period, in mAh. Then we use the assertLessThan()

    # function to assert that this is less than the target value of 100.

    #spanner.assertLessThan(100, 20)



if __name__ == "__main__":

    measure_power_consumption()


