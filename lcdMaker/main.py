# import os package
import os

# import frame class
from VMUFrame import VMUFrameClass

# define error report function


def err(code):
    if (code == -1):
        print("No frames directory!")
        exit(code)
    if (code == -2):
        print("No frames in frames directory!")
        exit(code)

# define frame getter function


def getFramesInDirectory(path):
    files = -1
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        if (not isinstance(files, list)):
            files = []
        for file in f:
            if '.bin' in file:
                files.append(os.path.join(r, file))

    return files

# define main function
def main():
    # declare frames list
    frames = []

    # load ./frames directory listing into listing variable
    files = getFramesInDirectory('./frames')

    # if files listing variable is not of class list, it must be because there is no frames directory
    if (not isinstance(files, list)):
        err(-1)
    else:
        #if files is of length 0 then there are no frame files
        if (len(files) == 0):
            err(-2)
        #if there are frames then continue
        else:
            # load all .bin files in the ./frames directory
            for x in files:
                frames.append(VMUFrameClass(path=x, duration=1))

            # init file data array with header
            out = bytearray("LCDi", "ascii") + bytearray([0x01, 0x00, 0x30, 0x00, 0x20, 0x00, 0x01, 0x00, 0x00, 0x01, len(frames), 0x00])

            # concat frames info to file data array
            for frame in frames:
                out += frame.getInfoToByteArray()

            # concat raw frame data to file data array
            for frame in frames:
                out += frame.getDataToByteArray()

            # concat footer to file data array.
            # you can use any kind of string but this is good for LCD_ANIM,
            # otherwise with that program you will get a incorrects size error.
            out += bytearray("Dream Animator ver.0.50 (C)1999 F.Sahara", "ascii")

            # write file data array to bin file and close it
            with open("./out/out.lcd", "wb+") as f:
                f.write(out)
                f.close()

        # exit with code 0 for successful operation
        exit(0)


if __name__ == '__main__':
    main()
