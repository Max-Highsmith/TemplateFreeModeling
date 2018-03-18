import os

#To Obtain target.ss, go to http://scratch.proteomics.ics.uci.edu/ and check SSpro: Secondary Structure (3 Class).
#I did install the library on my computer and generate the target.ss file but it took 1 minute. Also the library was 2.7Gb for linux.
#This just makes sense that we should just give the ssFile as an input.
def generateFragments(fastaFile,ssFile,fragSize):
    os.system("./FRAGSION -f "+fastaFile+" -s "+ssFile+" -m IOHMM.dat -z "+str(fragSize)+" -n 1 -o fragments.txt")
    return

#Returns an array of [phi, psi, omega] for fragment starting at fragmentNumber
def getFragment(fragSize,fragmentNumber):
    fragmentAngles = []
    increment = (fragSize+3)
    lineNumber = increment*(fragmentNumber-1)+1
    with open('fragments.txt') as f:
        for i in range(lineNumber+1):
            f.readline()
        for i in range(0,increment-3):
            data = f.readline().split()
            print(str(data[5])+" "+str(data[6])+" "+str(data[7]))
            fragmentAngles.append([data[5],data[6],data[7]])
        f.close()

#Test code
generateFragments('target.fasta','target.ss',5)
getFragment(5,100)
    