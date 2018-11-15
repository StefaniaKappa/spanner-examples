
import time
from Spanner import Spanner
from Testboard import Testboard

testboard = Testboard("testboard_name")

def myMockTest():
    
    Serial = Testboard.Serial
    my_procedure = testboard.createProcedure('UART').\
        setup(9600, Serial.DATA_BITS_8 | Serial.STOP_BITS_1 | Serial.PARITY_NO).\
        doAssertSerialRead('Hello Testboard\n').\
        doWait(1000).\
        doSerialWrite('Hello Device\n')
    
    spanner.assertEqual(my_procedure.run(), 0)

if __name__ == "__main__":
    myMockTest()
