#!/usr/local/bin/python

import plot
import web


NAME = 'bandwidth.png'


class Display:
    def GET(self):
        plot.plot(NAME)
        web.header("Content-Type", 'image/png')
        return open(NAME, "rb").read()


if __name__ == '__main__':
    app = web.application(('/', 'Display'), globals())
    app.run()
