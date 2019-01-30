import time
import Spanner
from Testboard import Testboard

testboard = Testboard("testboard_name")

def char_count_mock():
  my_procedure = testboard.createProcedure('I2C')\
      .setSpeed(100000)\
      .begin()
  
  for _ in range(10):
      my_procedure\
        .write(0x18, bytearray([168]))\
        .read(0x18, 6)\
        .doWait(200)

  # Execute the mock function
  exit_code, results = my_procedure.run(withResults=True)
  for r in results:
    print(r)

if __name__ == "__main__":
  # Start the test
  char_count_mock()
