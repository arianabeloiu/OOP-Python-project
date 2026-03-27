## RENAME this file YourLastName_OOP_FinalProject_2026.py

##Assignment: Add to the constructor and methods of a parent class and child classes
##            which inherit the base class properties. NOTE: You are not allowed
##            to import any specialized libraries for this project (e.g., no Biopython)
##            The idea is for you to write these methods from scratch.

## Begin with the parent Seq class and the child DNA class we created in lecture below.
## 

### Seq Class
#
#  Constructor:
#  (1) Use the string functions upper and strip to clean up self.sequence.
#  (2) Add a variable self.kmers to the constructor and make it equal to an empty list.

#  Methods:
#  (1) Add a method called make_kmers that makes overlapping kmers of a given length from self.sequence
#      appends these to self.kmers. Default kmer parameter=3.
#  (2) Add a method called fasta that returns a fasta formatted string like this:
#      >species gene
#      AGATTGATAGATAGATAT


### DNA Class: INHERITS Seq class
#   
#  Constructor:
#  Use re.sub to change any non nucleotide characters in self.sequence into an 'N'.
#      re.sub('[^ATGCU]','N',sequence) will change any character that is not a
#      capital A, T, G, C or U into an N. (Seq already uppercases and strips.)

#  Methods:
#  (1) Add a method called print_info that is like print_record, but adds geneid and an
#      empty space to the beginning of the string.
#  (2) Add a method called reverse_complement that returns the reverse complement of
#      self.sequence
#  (3) Add a method called six_frames that returns all 6 frames of self.sequence
#      This include the 3 forward frames, and the 3 reverse complement frames

### RNA Class:  INHERITS DNA class
#  
#  Construtor:
#  Use the super() function (see DNA Class example).
#  (1) Automatically change all Ts to Us in self.sequence. 
#  (2) Add self.codons equals to an empty list

#  Methods:
#  (1) Add make_codons which breaks the self.sequence into 3 letter codons
#      and appends these codons to self.codons unless they are less than 3 letters long.
#  (2) Add translate which uses the Global Variable standard_code below to
#      translate the codons in self.codons and returns a protein sequence.

### Protein Class: INHERITS Seq class
#
#  Construtor:
#  Use the super() function (see DNA Class example).
#  Use re.sub to change any non LETTER characters in self.sequence into an 'X'.

#  Methods:
#  The next 2 methods use a kyte_doolittle and the aa_mol_weights dictionaries.
#  (2) Add total_hydro, which return the sum of the total hydrophobicity of a self.sequence
#  (3) Add mol_weight, which returns the total molecular weight of the protein
#      sequence assigned to the protein object. 


import re

standard_code = {
     "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S",
     "UCC": "S", "UCA": "S", "UCG": "S", "UAU": "Y", "UAC": "Y",
     "UAA": "*", "UAG": "*", "UGA": "*", "UGU": "C", "UGC": "C",
     "UGG": "W", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
     "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "CAU": "H",
     "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R",
     "CGA": "R", "CGG": "R", "AUU": "I", "AUC": "I", "AUA": "I",
     "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
     "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S",
     "AGC": "S", "AGA": "R", "AGG": "R", "GUU": "V", "GUC": "V",
     "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A",
     "GCG": "A", "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
     "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

kyte_doolittle={'A':1.8,'C':2.5,'D':-3.5,'E':-3.5,'F':2.8,'G':-0.4,'H':-3.2,'I':4.5,'K':-3.9,'L':3.8,
                'M':1.9,'N':-3.5,'P':-1.6,'Q':-3.5,'R':-4.5,'S':-0.8,'T':-0.7,'V':4.2,'W':-0.9,'X':0,'Y':-1.3}

aa_mol_weights={'A':89.09,'C':121.15,'D':133.1,'E':147.13,'F':165.19,
                'G':75.07,'H':155.16,'I':131.17,'K':146.19,'L':131.17,
                'M':149.21,'N':132.12,'P':115.13,'Q':146.15,'R':174.2,
                'S':105.09,'T':119.12,'V':117.15,'W':204.23,'X':0,'Y':181.19}


class Seq: 
    """  
    This class will allow you to extract information about the sequence, 
    create k-mers, and print out the information in a fasta format 
    
    """

    def __init__(self,sequence,gene,species): 
        """  
        initalize Seq with sequence, gene, and species
        """
        self.sequence=sequence.upper().strip() #assign sequence input to sequence, uppercase the sequence + strips the beginning & end of the sequence 
        self.gene=gene #assign gene input to gene 
        self.species=species #assign species input to species 
        self.kmers = [] #assign kmers to an empty list 

    def __str__(self): 
        """
        overload the print function so that it prints the sequence 
        """
        return self.sequence #prints the sequence 

    def print_record(self): 
        """
        print information about the Sequence 
        """
        print(self.species + " " + self.gene + ": " + self.sequence) #prints the species, gene and sequence 

    def make_kmers(self, k=3): 
        """
        find all the overlapping k-mers in the sequence, with a default k-mer size = 3. 
        """
        for i in range(len(self.sequence)-k+1): #iterate through the sequence, extracting k-mers of length k 
            kmer=self.sequence[i:i+k] #slice the sequence up until the length of the k-mer size 
            self.kmers.append(kmer) #append to an empty list

    def fasta(self):
        """ 
        print out information in fasta format
        """
        return ">" + str(self.species) + "|" + str(self.gene) + "\n" + str(self.sequence)
    
class DNA(Seq):

    """ 
    
    This class will inherit all the functions of the Seq class + 
    conduct GC count, reverse complement the sequence, and find the first six frames
    of the forward and complementary sequence. 

    """

    def __init__(self,sequence,gene,species,geneid,**kwargs): 
        """ 
        initalize DNA with the same parameters as the Seq class + geneid
        """
        super().__init__(sequence,gene,species) #use super to inherit the previous methods from Seq class 
        self.sequence = re.sub('[^ATGCU]', 'N', self.sequence) #assign sequence input to sequence + use regex package to substitute any character that's not ATGCU as N
        self.geneid=geneid #assign geneid input to gene id
 
    def analysis(self): 
        """ 
        find the GC counts 
        """
        gc=len(re.findall('G',self.sequence) + re.findall('C',self.sequence)) #use regex package to get the sum of G's and C's in the sequence 
        return gc #print the result

    def print_info(self): 
        """ 
        print information about the DNA 
        """
        print(self.geneid + " " + self.species + " " + self.gene + ": " + self.sequence) #prints out the geneid, species name, gene, and sequence 

    def reverse_complement(self):  
        """ 
        reverse complement the sequence 
        """
        complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A','N':'N'} #set up a dictionary of the corresponding base-pairs
        return "".join(complement.get(base,'N') for base in reversed(self.sequence)) #uses the dictionary to get the reverse complement of the sequence 

    def six_frames(self): 
        """
        finds 6 frames of the sequence (3 from the forward sequence, 3 from the reverse complement 
        """
        frames = [] #create an empty list called frames 
        reverse_complement = self.reverse_complement() #assigns reverse complement input to be the reverse complement of the sequence 

        #get the first 3 frames from the forward sequence 
        for i in range(3): 
            frames.append(self.sequence[i:]) 

        #get the first 3 frames from the reverse complement
        for i in range(3): 
            frames.append(reverse_complement[i:]) 
        return frames #print all the 6 frames 


class RNA(DNA):
    """ 
    This class will inherit all the functions of the DNA class +
    get the codons and translate the sequence 
    """
    def __init__(self,sequence,gene,species,geneid,**kwargs): 
        """
        initialize RNA class with the same parameters as the DNA class 
        """
        super().__init__(sequence,gene,species) #use super to inherit the previous methods from the DNA class 
        self.sequence = re.sub('T','U',self.sequence) #replace every T base with a U 
        self.codons = [] #assign codons to an empty list 
        
    def make_codons(self):  
        """
        get the codons from the sequence 
        """
        for i in range(0,len(self.sequence),3): #iterate through the sequence skipping by 3s 
            codon = self.sequence[i:i+3] #splice the sequence by every 3 bases 
            self.codons.append(codon) #add the codons to the empty codons list 
 
    def translate(self): 
        """
        translate the RNA sequence into amino acids 
        """
        protein = "" #assign proteins to an empty string 
        for codon in self.codons: #iterate through each codons in the codons list  
            #use a try & except to translate the codons into amino acids 
            try:
                aa= standard_code[codon] #use the dictionary to get the corresponding amino acid 
            except:
                aa = "X" #if the pattern doesn't exist in the dictionary, denote it as X 
            protein += aa #add the amino acid to the protein string 
        return protein #print out the protein sequence 

class Protein(Seq):
    """
    This class will inherit all the functions of the Seq class +
    calculate the total hydrophobicity and total molecular weight of the protein sequence
    """
    def __init__(self,sequence,gene,species,geneid,**kwargs): 
        """
        initialize the Protein class with the same parameters as the Seq class
        """
        super().__init__(sequence,gene,species) #use super() to inherit the previous methods from the Seq class 
        self.sequence = re.sub('[^0-9a-zA-Z]+', 'X', self.sequence) #use the regex package to substitute any non LETTER characters in the sequence into an 'X'

    def total_hydro(self):  
        """ 
        calculate the total hydrophobicity score
        """
        hydro_score = sum(kyte_doolittle.get(aa, 0) for aa in self.sequence) #sum the hydrophobicity values for all amino acids in the sequence
        return hydro_score 

    def mol_weight(self):
        total_mol_weight = sum(aa_mol_weights.get(aa, 0) for aa in self.sequence) #sum the total molecular weight 
        return total_mol_weight
        

x=DNA("G","tmp","m",000)