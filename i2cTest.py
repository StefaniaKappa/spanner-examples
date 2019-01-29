import time
from Spanner import Spanner
from Testboard import Testboard

testboard = Testboard("testboard_name")

  
  
def char_count_mock():
  
    my_procedure = testboard.createProcedure('I2C')\
        .setSpeed(100000)\
        .setThreasholds(val < 25)
        .setAssertion()
        .begin()\
        .write(0x18, "acffd")\
        .read(0x18, "dsdsdsd")
        .delay(200)
        .read(0x18, 6, store=True)
        .delay(200)
        .read(0x18, store=True)
        

    # Execute the mock function
    spanner.assertEqual(my_procedure.run(), 0)
    spanner.assertEqual(my_procedure.withResults(), 0)

if __name__ == "__main__":
    # Start the test
    char_count_mock()
#test
