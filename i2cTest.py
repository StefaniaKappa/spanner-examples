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
  
  for result in results:
    x = int.from_bytes(result[0:2], byteorder='little', signed=False)
    y = int.from_bytes(result[2:4], byteorder='little', signed=False)
    z = int.from_bytes(result[4:6], byteorder='little', signed=False)
    X_g = x / 8190.0
    Y_g = y / 8190.0
    Z_g = z / 8190.0
    

if __name__ == "__main__":
  # Start the test
  char_count_mock()
