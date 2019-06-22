# Test of E-mails Leaks 
System to get statistics of leaks from e-mails list.

## Getting Started
These instructions will tell you what do you need to get a copy set and run on your system.


## Prerequisites
Things you need to install to run the script and how install them.
* [Python 3.6+](https://www.python.org/) - Used to run the script.
* [Selenium](https://www.seleniumhq.org/) - Library to automate task on browsers.
* [Matplotlib](https://matplotlib.org/) - Used to plot the leak graph.
* [Numpy](https://www.numpy.org/) - Used integrated with matplotlib.

### Install 
To install **python**, in case that you don't have a Unix/Linux system go to the [downloads](https://www.python.org/downloads/) section. 
To install **selenium** library, case you have [pip](https://pypi.org/project/pip/) on your system: 

> pip install selenium 

or with [Anaconda](https://www.anaconda.com/): 

> conda install selenium

## How to run
Example without the plot: 
> python main.py -i <input_file> -o \<output_file>
 
Example with the plot:
> python main.py -i <input_file> -o \<output_file> -p \<True>
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
