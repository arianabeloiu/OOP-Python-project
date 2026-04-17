#------------------------------------------------------------------------------------------------
#PYTHON REFRESHER
#------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
#== FUNCTION 1 ==
#Write a function called find_motifs two argument:
#  1) a motif
#  2) a dictionary of sequences
#and returns a dictionary that only includes sequences that match the motif 

def find_motifs():
    return result 
          
m='C[CG]'
test_data={0:'AGAC',1:'AGTCCC',2:'GAA',3:'GGCGG',4:'ATTAGGA'}

#Test the function with the motif and test_data
#It should return: {1: 'AGTCCC', 3: 'GGCGG'}
#print(find_motifs(m, test_data))
#----------------------------------------------------------------------------------------------------
#== FUNCTION 2 ==
#Write a function called extract_pept that takes a sequence dictionary as an argument
#and returns a dictionary with only the key value pairs that have sequence that 
#begin with a start codon "ATG" or "AUG". However, the returned dictionary needs to contain
#only RNA seqeunces. In other words, all the T's need to be changed to U's.

def extract_pept():
    return
          

test_data={0:'AGTACG',1:'AUGCCC',2:'GAA',3:'GGCGG',4:'ATGAGGGCG',5:'AUGGGGGAA'}

#Test the function with sequence_names, sequence_data.
#It should return: {1: 'AUGCCC', 4: 'AUGAGGGCG', 5: 'AUGGGGGAA'}
#print(extract_pept(test_data))

#----------------------------------------------------------------------------------------------------
#== FUNCTION 2 ==
#Write a function called bray curtis that takes in a two lists of samples counts
#and returns the bray-curtis distance. Make sure to check that the list lengths
#are equal before doing the calculation. If they are not equal, print "The samples
#do not have the name number of features." and return 0

def bray_curtis():
   return

sampleA=[10, 50, 100, 150]
sampleB=[150, 100, 50, 10]

#Test the function with sampleA and sampleB
#It should return: 0.6129032258064516
#print(bray_curtis(sampleA, sampleB))

#----------------------------------------------------------------------------------------------------
#== FUNCTION GROUP 3 ==
# the clr tranform!!

## Write a function that returns the centered log-ratio given
## a value and the geometric mean
def clr():
   return

## Use the clr function above in a function that transforms
## a list of values (e.g., sampleA above)

def clr_transform():
   return

## Write a function that calculates the euclidean distance between
## two lists of values (see bray curtis above)

def euclidean():
   return








