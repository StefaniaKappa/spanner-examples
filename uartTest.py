import time
import gzip
from Spanner import Spanner
from Testboard import Testboard

testboard = Testboard("testboard_name")

def read_in_chunks(file_object, chunk_size):
    while data = file_object.read(chunk_size):
        yield data

def myMockTest():
    
    Serial = Testboard.Serial
    my_procedure = testboard.createProcedure('UART').\
        setup(9600, Serial.DATA_BITS_8 | Serial.STOP_BITS_1 | Serial.PARITY_NO)
    
    # Compress image
    with open("logo.png", "rb") as f:
        with gzip.open("logo.gzip", "wb") as fgzip:
            fgzip.writelines(f)
    
    # Send it 
    with gzip.open("logo.gzip", "rb") as f:
        for piece in read_in_chunks(f, my_procedure.MAX_PAYLOAD_LEN):
            my_procedure = my_procedure.doSerialWrite(piece)
    
    # Exec
    spanner.assertEqual(my_procedure.run(), 0)

if __name__ == "__main__":
    myMockTest()
