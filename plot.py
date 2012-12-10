#! /usr/bin/env python
# plot.py

"""plot.py ploy cpu usage graph


"""

# If the package has been installed correctly, this should work:
import Gnuplot, Gnuplot.funcutils


def demo():
    """Demonstrate the Gnuplot package."""

    # A straightforward use of gnuplot.  The `debug=1' switch is used
    # in these examples so that the commands that are sent to gnuplot
    # are also output on stderr.
    g = Gnuplot.Gnuplot(debug=1)
    g.title('A simple example') # (optional)
    g('set autoscale') # give gnuplot an arbitrary command
    g('set terminal jpeg')
    g('set output "plot.jpeg"')
    g.plot('"cpu-1.data" using 1:2 with linespoints')

    #g.reset()
# when executed, just run demo():
if __name__ == '__main__':
    demo()

