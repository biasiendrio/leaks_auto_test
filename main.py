from selenium import webdriver
import argparse, time, re
from lib.leaks import Leaks
from lib.plot_leaks import start_plot

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input_file", required=True, help="Path to the emails file")
ap.add_argument("-o", "--output_file", required=True, help="Output file with the leaks")
ap.add_argument("-p", "--show_plot", default=False, type=bool, help="Set as True to see the plot of leak")
args = vars(ap.parse_args())

if __name__ == '__main__':
    Leaks(args["input_file"], args["output_file"]).run()
    if args["show_plot"]:
        start_plot(args["output_file"])

