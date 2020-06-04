#import matplotlib
import matplotlib
from awesome_colors import kite_blue

kite_smarts = [1, 10, 9, 1000] #etc

matplotlib.pyplot.plot(kite_smarts, color=kite_blue())
matplotlib.pyplot.savefig("out.png")

###Added from web
