import matplotlib.pyplot as plt
from collections import Counter
import sys
import numpy as np

def start_plot(emails_file):
    set_plot_leak(read_email_file(emails_file))

def autolabel(rects, ax, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(offset[xpos]*3, 3),  # use 3 points offset
                    textcoords="offset points",  # in both directions
                    ha=ha[xpos], va='bottom')

def read_email_file(emails):
    leak_per_email = []

    with open(emails, "r") as f:
        for i in f.readlines():
            temp = int(i.strip("\n").split(" ")[1])
            # if temp != 0:# and temp != 1:
            leak_per_email.append(temp)
    
    leak_per_email.sort()
    return leak_per_email


def set_plot_leak(leak_per_email):
    amount_same_leak = list(Counter(leak_per_email).values())


    num_leak_without_duplicades = list(set(leak_per_email))
    num_leak_without_duplicades.sort()

    xpos = np.arange(len(num_leak_without_duplicades))

    fig, ax = plt.subplots()
    bars = ax.bar(xpos, amount_same_leak)

    ax.set_ylabel("Frequence of Leaks")
    ax.set_xlabel("Number of Leaks")
    ax.set_title(f'Leaks of {len(leak_per_email)} emails')
    ax.set_xticks(xpos)
    ax.set_xticklabels(num_leak_without_duplicades)

    autolabel(bars, ax, "center")
    fig.tight_layout()

    plt.show()
