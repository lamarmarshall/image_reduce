from PIL import Image
import os
import sys

def get_size_in_mb(file):
    return round( os.stat(file).st_size / (1024*1024),2 ) 

def get_size_in_kb(file):
    return round( os.stat(file).st_size / 1024, 2 )

def image_reduce(file, out=None):
    if out == None:
        compressed_file="compressed-" + file.split(".")[0] +".jpg"
    else:
        compressed_file=out
    im = Image.open(file)
    print("original image size: "+ str( get_size_in_kb(file) ) + "KB")
    print("original dimesions ", im.width, "X", im.height)
    div_width = im.width / 1200
    div_height = im.height / 630
    
    im_resize = im.resize(( round(im.width / div_width), round(im.height / div_height) ))
    im_resize.save(compressed_file, optimize=True, quality=65 )
    print("compressed image size: "+ str( get_size_in_kb(compressed_file) ) + "KB")
    print("compressed dimesions ", im_resize.width, "X", im_resize.height)


if __name__ == '__main__':
    if sys.argv[1] == None:
        file='casa bioceramic dome.jpg'
    else:
        file=sys.argv[1]
    image_reduce(file)
    
    #print("compressed-" + file.split(".")[0] +".jpg");
    #im.close()

