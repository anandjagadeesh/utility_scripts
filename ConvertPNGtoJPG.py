# --------------------------------------------------------------------- #
# Script to convert PNG files to JPG using Python Image Library         #
# AUTHOR: ANAND JAGADEESH                                               #
# AUTHOR EMAIL: mail@anandj.xyz                                         #
# --------------------------------------------------------------------- #
# Import libraries
import glob
import sys
import os
from PIL import Image

# Code
def png_to_jpg_converter(path):
    """
    Converter function for PNG to JPG conversion and save the
    converted files to the same path, but in a directry called
    converted.
    Parameter path: The folder where the .png files are located
    """
    files = None
    save_loc = path
    if path[-1] == '/':
        files = glob.glob(path + "*.png")
        save_loc = save_loc + "converted/"
        try:
            os.mkdir(save_loc)
        except:
            print("Note: 'converted' directory already exist")
    else:
        files = glob.glob(path + "/*.png")
        save_loc = save_loc + "/converted/"
        try:
            os.mkdir(save_loc)
        except:
            print("[N]ote: 'converted' directory already exist")
    print("[N]ote: Converting files from path: " + path)
    for each_file in files:
        file_name = (each_file.split(".png")[0]).split("/")[-1]
        print("[C]onverting: " + file_name + ".png | New file: converted/" + file_name + ".jpg")
        (Image.open(each_file, mode='r')).convert('RGB').save(save_loc + file_name + ".jpg")
    print("[N]ote: Converted " + str(len(files)) + " files")
    print("[N]ote: Finished converting files from path: " + path)
    print("[N]ote: Converted files are at path: " + save_loc)

# Entry Point
if __name__ == '__main__':
    png_to_jpg_converter(sys.argv[1])

