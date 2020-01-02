data = [];
tmpArr = [];
out = [];

with open("out.bmp", "rb") as f:
    byte = f.read(1)
    while byte:
        # Do stuff with byte.
        data.append(byte)
        byte = f.read(1)
    f.close()
            

pos = 0;
while (data[pos] != b'\xFF'):
    pos+= 1;
pos += 4

tmpP = pos;
while (tmpP < len(data)):
    tmpArr.append( (0xFF, 0x00)[data[tmpP] == b'\xFF'] )
    tmpP+= 1

tmpArr.reverse()

out = bytearray(tmpArr);

with open ("out.bin", "wb+") as f:
    f.write(out)
    f.close()