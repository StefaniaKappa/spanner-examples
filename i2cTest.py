import time
import Spanner
from Testboard import Testboard

testboard = Testboard("testboard_name")

def char_count_mock():
  my_procedure = testboard.createProcedure('I2C')\
      .setSpeed(100000)\
      .begin()\
      .write(0x18, "¿")\
      .read(0x18, 6)\
      .doWait(1000)\
      .read(0x18, 6)\
      .doWait(1000)\
      .read(0x18, 6)        

  # Execute the mock function
  my_procedure.run(withResults=True)

if __name__ == "__main__":
  # Start the test
  char_count_mock()
