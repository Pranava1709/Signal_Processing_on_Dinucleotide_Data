import pandas as pd 
import numpy as np
from scipy import signal 
from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')
#t = np.linspace(0,1.0,2001)

data = pd.read_csv("Test(inc_pos).csv",usecols = ['1'] )
data_df = pd.DataFrame(data)
data_df.dropna()
#print(data_df.shape)
#print(data_df)
input = data_df.values.tolist()
#input = data_df.to_numpy()
#input = np.array(data_df)
#newest = [i[0] for i in input]
#print(newest)
newtest = [x[0] for x in input]

#print(newtest)
#input = ''.join(str(newest).split(','))
input = np.array(newtest)

print(input)
print(input.size)
print(type(input))


numtaps = 69
lpf_cutoff = 7
hpf_cutoff = 50
bp_cutoff1 = 40
bp_cutoff2 = 100

filter = signal.firwin(numtaps,lpf_cutoff,nyq = 1000)
print(type(filter))
print(filter.size)
print(filter)


output = signal.convolve(input,filter,mode = 'same')

ax1, ax2 = plt.subplots(3, 2, sharey =True,sharex=True)
ax1.suptitle("RESULT")
#ax2.set_title("INPUT SIGNAL")
ax2[0,0].plot(input, color = 'cyan')
#ax2.set_title("IMPULSE RESPONSE")
ax2[1,1].plot(filter,color = 'green')
#ax2.set_title("OUTPUT SIGNAL")
ax2[2,1].plot(output,color = 'magenta')


plt.show()

#print(input)

