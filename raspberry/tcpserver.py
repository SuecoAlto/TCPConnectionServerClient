import socket
import struct
import serial
import threading
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
    