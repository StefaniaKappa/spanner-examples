
import time
from Spanner import Spanner
from Testboard import Testboard

testboard = Testboard("testboard_name")


def read_in_chunks(file_object, chunk_size):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


def myMockTest():
    
    Serial = Testboard.Serial
    my_procedure = testboard.createProcedure('UART').\
        setup(9600, Serial.DATA_BITS_8 | Serial.STOP_BITS_1 | Serial.PARITY_NO)
    
    with open("spannerci.bmp", "r+") as f:
        for piece in read_in_chunks(f, my_procedure.MAX_PAYLOAD_LEN):
            my_procedure = my_procedure.doSerialWrite(piece)
   
    spanner.assertEqual(my_procedure.run(), 0)

if __name__ == "__main__":
    myMockTest()
