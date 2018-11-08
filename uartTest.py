
import time
from Spanner import Spanner
from Testboard import Testboard

testboard = Testboard("testboard_name")


if __name__ == "__main__":

    Serial = Testboard.Serial

    my_procedure = testboard.createProcedure('UART').\
        setup(9600, Serial.DATA_BITS_8 | Serial.STOP_BITS_1 | Serial.PARITY_NO).\
        doAssertSerialRead('Hello Testboard\n').\
        doWait(1000).\
        doSerialWrite('Hello Device\n')

    my_procedure.execute()
