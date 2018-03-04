import scipy as sp
import scipy.optimize as op
import numpy as np
import subprocess

def getEnergy(pdb):
	proc = subprocess.Popen(['./calRW',pdb], stdout=subprocess.PIPE)
	stdout = proc.communicate()[0]
	return float(stdout[15:29])  #index in outputstring of energ kcal/mol 
	
#def acceptanceProb(newConf, ):
#	alpha = np.exp(((-1)*changInE)/t)

oldNRG = 0;
def getDeltaNRG(pdb,oldNRG):
	newNRG = getEnergy(pdb)
	diff = newNRG - oldNRG
	oldNRG = newNRG
	return [diff, oldNRG]



print(getEnergy("pro.pdb"))
print(getEnergy("pro2.pdb"))
[diff, oldNRG] = getDeltaNRG("pro.pdb",oldNRG)
print(diff)
[diff, oldNRG] = getDeltaNRG("pro.pdb",oldNRG)
print(diff)


###THIS IS WHERE WE MAKE ADJUSTMENTS
def makeConformationAdjustments()
	return "pro.pdb"


#needs adjustment
def simmulateThatAnnealing(startPDB, startingNRG, startTemp, endingTemp):
	currentPDB = startPDB
	temperature = startTemp
	oldNRG = getEnergy(pdb)
	while temperature > endingTemp:
		currentPDB =  makeConformation()  ##WHATEVER PARAMETERS WE NEED
		delta = getDeltaNRG(currentPDB, oldNRG)
		prob = np.exp((-1)*delta*(1/temperature))
		alpha = min(1, prob)
		
	
