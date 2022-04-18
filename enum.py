import pandas as pd
import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib import style
import os
import glob
style.use('ggplot')
#t = np.linspace(0,1.0,2001)


path = "C:/SEPROM/files/" 
result = glob.glob(path + '/*.csv')
print(result)

path2 = "C:/SEPROM/transposed_files/"
#result1 = glob.glob(path2 + '/*.csv')  
#print(result1)  
#path3 = "C:/SEPROM/plots/"
#path5 = "C:/SEPROM/plots"
#path4 = "/counts/counts/" 



for i, path in enumerate(result):

    data1 = pd.read_csv(path)
    data = data1.T
    #newPath = path.replace(os.sep, '/')
    data.to_csv(path2+"T.csv")


#coloumns =  data.iloc([0,10])
# for col in data.columns:

    data = pd.read_csv(path2+"T.csv")

#index = data.set_index("Unnamed: 0")
# data.drop(index)
    data_df = pd.DataFrame(data)
    data_df.columns = data_df.iloc[0]
    data_df = data_df.iloc[1:, ].reindex()
    del data_df[data_df.columns[0]]
    data_df.dropna()
    for j in data_df.iloc[:, 0:100]:

        # print(data_df.shape)
        # print(data_df)
        input = data_df[j].values.tolist()
#input = data_df.to_numpy()
#input = np.array(data_df)
#newest = [i[0] for i in input]
# print(newest)
    # print(input)

# for i in input.columns(0,1):
    #newtest = [x[0] for x in input]

# print(newtest)
#input = ''.join(str(newest).split(','))
        input = np.array(input)

        print(input)
        print(input.size)
        print(type(input))
        plt.plot(input)
        peaks1b, _ = signal.find_peaks(input , width=35, distance=20)
        #plt.plot(peaks1b, input[peaks1b],'x')
        newPath = path.replace(os.sep, '/')
        #print(path)
        #print(newPath)
        plt.savefig(str(os.path.splitext(newPath)[0])+str(j)+'peak_counter_before_bandpass'+'.png')
        #plt.show()
        count = len(peaks1b)
        print(count)

        #dir = os.mkdirs(path4/ + /str(i))
        try:

            with open('counts_beforebandpass.txt','a') as f2:
                f2.write(str(count)+ str(path)+str(j)+"\n")
                #f.close()
        except FileNotFoundError:
            print("The directory does not exist")

        numtaps = 69
        fs = 1960
        #lpf_cutoff = 500
        #hpf_cutoff = 400
        bp_cutoff1 = 10
        bp_cutoff2 = 30

    #filter = signal.firwin(numtaps,hpf_cutoff,nyq=1000)
        filter = signal.firwin(numtaps, bp_cutoff1, bp_cutoff2, nyq=1960)
        plt.plot(filter)


        # for_high_pass
# filter = signal.firwin(numtaps,bp_cutoff1,bp_cutoff2 ,nyq = 1000) #for_band_pass
        print(type(filter))
        print(filter.size)
        print(filter)

        output = signal.convolve(input, filter, mode='same')
        plt.plot(output)
        #dir = os.chdir(path5)
        #print(dir)
        #dir = os.mkdir(str(os.path.splitext(path)[0])+"/plots/"+str(i))
        #path.replace("\\","/")
        #dir = os.mkdir()
        newPath = path.replace(os.sep, '/')
        #print(path)
        #print(newPath)
        plt.savefig(str(os.path.splitext(newPath)[0])+str(j)+'.png')
        plt.show()
        f, Pxx_den = signal.periodogram(output, fs, 'bartlett', nfft=None,
                                        detrend='constant', return_onesided=True, scaling='density', axis=- 1)
    #f_med, Pxx_den_med = signal.welch(output, fs, nperseg=1024, average='median')
        plt.semilogy(f, Pxx_den)
        #np.sqrt(Pxx_den.max())

    #plt.semilogy(f_med, Pxx_den_med, label='median')
        plt.ylim([1e-20, 1e1])
    #plt.ylim([1e-8, 1e1])
        plt.xlabel('frequency [Hz]')
        plt.ylabel('PSD [V**2/Hz]')
        #plt.savefig("./path1"+str(j)+'.png')
        newPath = path.replace(os.sep, '/')
        #print(path)
        #print(newPath)
        plt.savefig(str(os.path.splitext(newPath)[0])+str(j)+'peridogram'+'.png')
        #plt.show()
        f, Pxx_spec = signal.periodogram(output, fs, 'bartlett', scaling='spectrum')
        #plt.figure()
        plt.semilogy(f, np.sqrt(Pxx_spec))
        plt.ylim([1e-20, 1e1])
        plt.xlabel('frequency [Hz]')
        plt.ylabel('Linear spectrum [V RMS]')
        newPath = path.replace(os.sep, '/')
        #print(path)
        #print(newPath)
        plt.savefig(str(os.path.splitext(newPath)[0])+str(j)+'PSD'+'.png')
        plt.show()
        power = np.sqrt(Pxx_spec.max())
        try:

            with open("power.txt" , 'a') as f1:
                f1.write(str(power)+ str(path)+str(j)+"\n")
        except FileNotFoundError:
            print("The directory does not exist")
        peaks1, _ = signal.find_peaks(output, width=35, distance=20)
        count = len(peaks1)
        print(count)

        #dir = os.mkdirs(path4/ + /str(i))
        try:

            with open('counts.txt','a') as f:
                f.write(str(count)+ str(path)+str(j)+"\n")
                #f.close()
        except FileNotFoundError:
            print("The directory does not exist")

        #with ()


        #plt.plot(input)
        #plt.plot(output)
        #plt.show()
        plt.plot(peaks1, output[peaks1],'x')
        newPath = path.replace(os.sep, '/')
        #print(path)
        #print(newPath)
        plt.savefig(str(os.path.splitext(newPath)[0])+str(j)+'peak_counter_after_bandpass'+'.png')
        #plt.show()
    os.remove(path2+"T.csv")

    '''

		ax1, ax2 = plt.subplots(3, 2, sharey =True,sharex=True)
		ax1.suptitle("RESULT")
	#ax2.set_title("INPUT SIGNAL")
		ax2[0,0].plot(input, color = 'cyan')

	#ax2.set_title("IMPULSE RESPONSE")
		ax2[1,1].plot(filter,color = 'green')
	#ax2.set_title("OUTPUT SIGNAL")
		ax2[2,1].plot(output,color = 'magenta')
	'''
    # plt.savefig("./aa"+str(i)+'.png',ax1)

    #fig = plt.gcf()
    # plt.show()
    # plt.draw()

    # plt.clear()
