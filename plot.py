#!/usr/local/bin/python

from matplotlib import rcParams
from matplotlib import dates

import matplotlib.pyplot as plt
import pandas as pd

import os


def main():
    filename = 'bandwidth.png'
    plot(filename)
    os.system('open ' + filename)


def plot(filename):
    graph(read(), filename)


def graph(timeframe, filename):  # refactor to do 59 minute intervals instead
    rcParams['xtick.labelsize'] = 'xx-small'
    plt.plot(timeframe['timestamp'], timeframe['download'], 'b-')
    plt.plot(timeframe['timestamp'], timeframe['upload'], 'b-')
    plt.title('Bandwidth Grapher')
    plt.ylabel('Bandwidth in MBps')
    plt.yticks(xrange(0, 400))
    plt.ylim(0.0, 200.0)
    plt.xlabel('Timeframe in Minutes')
    plt.xticks(rotation='45')
    plt.grid()
    plt.gca().xaxis.set_major_formatter(dates.DateFormatter('%m/%d %H:%M'))
    plt.gcf().subplots_adjust(bottom=.25)
    loc = plt.gca().xaxis.get_major_locator()
    loc.maxticks[dates.HOURLY] = 1
    loc.maxticks[dates.MINUTELY] = 60
    plt.savefig(filename)


def read():
    df = pd.io.parsers.read_csv(
        'speeds.log',
        names='date time ping download upload'.split(),
        header=None,
        sep=r'\s+',
        parse_dates={'timestamp': [0, 1]},
        na_values=['TEST', 'FAILED'],
    )
    print df
    return df[-48:]
