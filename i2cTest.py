import Spanner
from multiprocessing import Process
from Testboard import Testboard

testboard = Testboard("testboard_name")
slave_testboard = Testboard("slave_testboard")

def init_slave():
  my_procedure = slave_testboard.createProcedure('I2C-Slave')\
      .setSpeed(100000)\
      .begin(0x19)\
      .write(bytearray([10] * 6))\
      .write(bytearray([11] * 6))\
      .write(bytearray([12] * 6))
  
  exit_code = my_procedure.run(timeout=50000)
  print("Slave ended with %d\n" % (exit_code,))

def z_axis_check():
  my_procedure = testboard.createProcedure('I2C-Master')\
      .setSpeed(100000)\
      .begin()
  
  for _ in range(3):
      my_procedure\
        .write(0x19, bytearray([168]))\
        .read(0x19, 6)\
        .doWait(1000)

  # Execute the mock function
  exit_code, results = my_procedure.run(withResults=True)
  
  for result in results:
    x = int.from_bytes(result[0:2], byteorder='little', signed=True)
    y = int.from_bytes(result[2:4], byteorder='little', signed=True)
    z = int.from_bytes(result[4:6], byteorder='little', signed=True)
    print("X: %.2f, Y: %.2f, Z: %.2f" % (x, y, z))
    Spanner.assertLessThan(100, abs(z - 8000))

if __name__ == "__main__":
  p = Process(target=init_slave)
  p.start()
  z_axis_check()
  p.join()
