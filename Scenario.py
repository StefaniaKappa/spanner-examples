import time

from Spanner import Spanner
from Testboard import Testboard
import Device

testboard = Testboard("Tester2")

OUTPUT_PIN = "D7"

def measure_power_consumption():

    # Turn the device off
    testboard.digitalWrite(OUTPUT_PIN, "LOW");

    # Wait for a while for it to shut down

    time.sleep(2)

    # Turn the device back on

    testboard.digitalWrite(OUTPUT_PIN, "HIGH");
    
    time.sleep(2)
        
     # Turn the device off
    testboard.digitalWrite(OUTPUT_PIN, "LOW");

    # Wait for a while for it to shut down

    time.sleep(2)

    # Turn the device back on

    testboard.digitalWrite(OUTPUT_PIN, "HIGH");

    spanner.assertLessThan(100, 20)



if __name__ == "__main__":

    measure_power_consumption()


