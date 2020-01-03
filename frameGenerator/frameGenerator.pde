//import various classes for file operations
import java.io.DataOutputStream;
import java.io.BufferedOutputStream;
import java.io.FileOutputStream;
import java.io.ObjectOutputStream;

//variable to toggle exporting. nice feature to have for testing animations without exporting.
boolean doExport = false;

//this is the number of frames you want.
//modify it accordingly
int targetFrames = 127;

//this is a PImage object I used for the DVD logo, if you want to load an image you can use it or whatever.
PImage img;

//coordinates for the image
int x = 0; 
int y = 1;

//direction of the image's movement for simple 90 degree bouncing
int xdir = 1; 
int ydir = 1;

//set up for size, framerate and load image
void setup() {
  size(48, 32);
  frameRate(10);
  img = loadImage("dvd.png");
  deleteFolder(new File(sketchPath() + "/frames"));
  if (new File(sketchPath() + "/frames").mkdir()) {
    println("Created frames folder successfully");
  }
  else {
    println("Couldn't create frames folder. Exiting...");
    exit();
  }
}

void draw() {
  
  //set background to white
  background(255);
  
  //set stroke and fill to 0
  stroke(0);
  fill(0);

  //if img is outside the screen, invert the respective direction variables
  if (!isWithin(x, 0, width-img.width)) xdir *= -1;
  if (!isWithin(y, 0, height-img.height)  ) ydir *= -1;
  
  //put image on the screen
  image(img, x, y);
  
  //increment variables with direction
  x+=xdir;
  y+=ydir;
  
  //loop as long as we get the number of frames we want and dump them, otherwise stop
  if (frameCount <= targetFrames) {
    if (doExport) getScreen();
  }
  else noLoop();
}

//screen dumping function
void getScreen() {
  //prepare file name string
  String fileName = sketchPath() + "/frames/frame" + String.format("%03d", frameCount) + ".bin";

  try {
    //allocate file streams
    FileOutputStream fstream = new FileOutputStream(fileName);
    BufferedOutputStream bstream = new BufferedOutputStream(fstream);
    DataOutputStream dstream = new DataOutputStream(bstream);

    //load pixels into pixels[] array
    loadPixels();
    
    //for every pixel output a byte containing either 0 or 255 according to its color. NOTE: -1 is white
    for (color c : pixels) {
      dstream.writeByte( c >= -1 ? 0 : 255);
    }
    
    //close file streams
    dstream.close();
  }
  catch(IOException e) {
    println("IOException");
  }
}

//quick function for inclusive bounds check
boolean isWithin(int val, int min, int max) {
  return (val >= min && val <= max);
}

void deleteFolder(File folder) {
    File[] files = folder.listFiles();
    if(files!=null) { //some JVMs return null for empty dirs
        for(File f: files) {
            if(f.isDirectory()) {
                deleteFolder(f);
            } else {
                f.delete();
            }
        }
    }
    folder.delete();
}
