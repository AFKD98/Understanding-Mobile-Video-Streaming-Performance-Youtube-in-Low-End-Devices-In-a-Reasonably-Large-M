
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
roundtriptimes= [2099,2692,2135,1996,1619,1590,1622]
roundtriptimes2 = [885,854,1010,854,982,907]



sortedtime = np.sort(roundtriptimes)
p = 1. * np.arange(len(roundtriptimes))/(len(roundtriptimes) - 1)

sortedtime2 = np.sort(roundtriptimes2)
p2 = 1. * np.arange(len(roundtriptimes2))/(len(roundtriptimes2) - 1)

plt.plot(sortedtime2, p2,'-r')
plt.plot(sortedtime, p,'-b')
red_patch = mpatches.Patch(color='red', label='512 MB RAM')
blue_patch = mpatches.Patch(color='blue', label='362 MB RAM')



plt.tick_params(labelsize=20)
plt.subplots_adjust( bottom=0.135)
plt.legend(handles=[red_patch,blue_patch],fontsize = 20)



plt.xlabel('Total Dropped Frames',fontsize =20)
plt.ylabel('CDF',fontsize = 20)
plt.title('Frame Drops on same video when RAM is reduced',fontsize = 20)
plt.show()