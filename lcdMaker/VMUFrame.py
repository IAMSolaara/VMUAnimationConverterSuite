class VMUFrameClass:
    # frame size
    __WIDTH = 48
    __HEIGHT = 32
    __SIZE = __WIDTH * __HEIGHT

    # constructor given duration and frame path
    def __init__(self, path, duration):
        self.duration = duration
        self.data = [];
        self.loadFromRawFile(path);
        

    # load frame data from raw bin file
    def loadFromRawFile(self, path):
        with open(path, "rb") as f:
            byte = f.read(1)
            while byte:
                # Do stuff with byte.
                if (byte == b'\x00'):
                    self.data.append(0x00)
                else:
                    self.data.append(0x08)
                byte = f.read(1)

    # get duration
    def getDelay(self):
        return self.duration

    # get info as byteArray
    def getInfoToByteArray(self):
        return bytearray([0x00, self.duration, 0x00, 0x00])

    # get raw frame data as bytearray
    def getDataToByteArray(self):
        return bytearray(self.data)

    # get frame size
    def getSize(self):
        return self.__SIZE
