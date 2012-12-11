#! /usr/bin/env python
# plot.py

"""plot.py ploy cpu usage graph


"""

import Gnuplot, Gnuplot.funcutils

def plot(data):
    """Demonstrate the Gnuplot package."""

    # A straightforward use of gnuplot.  The `debug=1' switch is used
    # in these examples so that the commands that are sent to gnuplot
    # are also output on stderr.
    g = Gnuplot.Gnuplot(debug=1)
    output = 'set output "%s.jpg"' %data 
    plotline = '"%s.data" using 1:2 with lines' %data
    g.title('CPU usage') 
    g('set autoscale') 
    g('set terminal jpeg')
    g(output)
    g.plot(plotline)

    #g.reset()
if __name__ == '__main__':
    plot()

