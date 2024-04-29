import socket
import struct
from enum import Enum

class MessageType(Enum):
    TURN_ON_GREEN = 1
    TURN_ON_BLUE = 2
    TURN_OFF_GREEN = 3
    TURN_OFF_BLUE = 4
    ACTUATE_SERVO = 5  
    QUERY_STATUS = 6
    ACKNOWLEDGE = 7
    ERROR = 8
    
    def create_package(action_type, data=''):
        if not data:
            data = str(action_type.value)
            print(f"This is data in create packet before encode------>{data}")
        data_bytes = data.encode('utf-8')
        print(f"This is data in create packet after encode------>{data_bytes}")
        package = struct.pack('>BH', action_type, len(data_bytes)) + data_bytes
        return package
    