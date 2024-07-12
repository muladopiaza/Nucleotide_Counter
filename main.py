from DNAToolkit import *
import random
user_input = int(input("Enter the length of DNA sequence: "))
if user_input == str:
    print("Please enter a +ve number only")
rndDNAstr = ''.join([random.choice(Nucleotides)
                    for nuc in range(user_input)])
DNAstr = validateSeq(rndDNAstr)
print("Random DNA Seq: ",DNAstr)
print("Counts of Individual Nuc: ",countNucFreq(DNAstr))