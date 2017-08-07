#!/usr/local/bin/python

import logging
import os


def main():
    log()
    try:
        ping, download, upload = results()
    except ValueError as err:
        logging.info(err)
    else:
        logging.info("%5.1f %5.1f %5.1f", ping, download, upload)


def log():
    logging.basicConfig(
        filename='speeds.log',
        level=logging.INFO,
        format="%(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M"
    )


def results():
    ping = download = upload = None
    with os.popen('/usr/local/bin/speedtest-cli' + ' --simple') as output:
        for line in output:
            label, value, unit = line.split()
            if 'Ping' in label:
                ping = float(value)
            elif 'Download' in label:
                download = float(value)
            elif 'Upload' in label:
                upload = float(value)
    if all((ping, download, upload)):
        return ping, download, upload
    raise ValueError('TEST FAILED')


if __name__ == '__main__':
    main()
