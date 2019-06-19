from selenium import webdriver
import argparse, time, re
from leaks import Leaks

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input_file", required=True, help="Path to the emails file")
ap.add_argument("-o", "--output_file", required=True, help="Output file with the leaks")
args = vars(ap.parse_args())

if __name__ == '__main__':
    Leaks(args["input_file"], args["output_file"]).run()
    # os.system("rm ghostdriver.log")

