import Spanner
from Testboard import Testboard

testboard = Testboard("testboard_name")

def char_count_mock():
  my_procedure = testboard.createProcedure('I2C')\
      .setSpeed(100000)\
      .begin()
  
  for _ in range(3):
      my_procedure\
        .write(0x18, bytearray([168]))\
        .read(0x18, 6)\
        .doWait(1000)

  # Execute the mock function
  exit_code, results = my_procedure.run(withResults=True)
  
  threshold = 100
  for result in results:
    x = int.from_bytes(result[0:2], byteorder='little', signed=True)
    y = int.from_bytes(result[2:4], byteorder='little', signed=True)
    z = int.from_bytes(result[4:6], byteorder='little', signed=True)
    print("X: %.2f, Y: %.2f, Z: %.2f" % (x, y, z))
    Spanner.assertLessThan(threshold, abs(z - 8000))
    

if __name__ == "__main__":
  # Start the test
  char_count_mock()
