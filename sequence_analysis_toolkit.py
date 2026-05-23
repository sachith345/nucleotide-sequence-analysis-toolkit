from Bio.Seq import Seq
import os
import sys

#paste your FASTA sequence inside the triple quotes without any header
your_fasta = """ """

#FASTA might have line breakes, spaces
clean = your_fasta.replace("\n","").replace(" ","")
fasta = Seq(clean)

#identify whether the sequence is a valid DNA or RNA sequence, if it is not a valid sequence exit
if "U" in fasta and "T" in fasta:
    sys.exit("The sequence is not valid")
# identify whether the sequence is DNA or RNA
elif "T" in fasta:
    print("It is a DNA sequence")
elif "U" in fasta :
    print("It is a RNA sequence")

length = len(fasta) #length of the DNA
print('Nucleotide count:',length)

#check G,A,C,T or U content in sequence
G = fasta.count('G')
print("Number of Guaninie residues in sequence:", G)
A = fasta.count('A')
print("Number of Adenine residues in sequence:", A)
C = fasta.count('C')

print("Number of Cytosine residues in sequence:", C)
if "U" in fasta:
    U = fasta.count("U")
    print("Number of Uracil residues in sequence:", U)
if "T" in fasta:
    T = fasta.count("T")
    print("Number of Thymine residues in sequence:", T)

purines = fasta.count("A") + fasta.count("G") #purines content in percentage
purine_percentage = purines / length * 100
print("Purines (Adenine + Guanine) content %:",purine_percentage)
pyrimidines = fasta.count("C") #pyrimidines content in percentage
if "U" in fasta:
    pyrimidines += fasta.count("U")
if "T" in fasta:
    pyrimidines += fasta.count("T")
pyrimidines_percentage = pyrimidines / length * 100
print("Pyrimidines (Cytosine + (Uracil or Thymine) content %:",pyrimidines_percentage)

print("Complement of the sequence:", fasta.complement()) #complement of sequence
print("Reverse complement of the sequence:", fasta.reverse_complement()) #reverse complement of sequence
if "U" in fasta: #transcription of sequence
    RNA_transcribe = fasta.transcribe()
    print("RNA to DNA back transcription:", RNA_transcribe)
if "T" in fasta:
    print("DNA to RNA transcription:", fasta.transcribe())
if "T" in fasta: #translation of nucleotide sequence into protein sequence
    print("DNA to protein translation:", fasta.translate())
if "U" in fasta:
    RNA_trans = RNA_transcribe.translate()
    print("RNA to protein translation:", RNA_trans)

#to check for start and stop codons in sequence
start_position = []
stop_position = []
if "T" in fasta:
    start_codon = "ATG"
    stop_codon = ["TAA", "TAG", "TGA"]
    for i in range(0, len(fasta) - 2, 3):
        codon = str(fasta[i:i + 3])
        if codon == start_codon:
            start_position.append(i)
        if codon in stop_codon:
            stop_position.append(i)
if "U" in fasta:
    start_codon = "AUG"
    stop_codon = ["UAA", "UAG", "UGA"]
    for i in range(0, len(fasta) - 2, 3):
        codon = str(fasta[i:i + 3])
        if codon == start_codon:
            start_position.append(i)
        if codon in stop_codon:
            stop_position.append(i)
print("start codon positions:",start_position)
print("stop codon positions:",stop_position)

#check for restricition sites in sequence
seq = str(fasta)
restriction_sites = {
     "EcoRI":  "GAATTC",
    "HindIII": "AAGCTT",
    "BamHI": "GGATCC",
    "NotI": "GCGGCCGC",
    "PstI": "CTGCAG",
    "SphI": "GCATGC"
}
for name, site in restriction_sites.items():
    start = 0
    while True:
        pos = seq.find(site, start)
        if pos == -1:
            break
        print(f"{name} ({site}) found at position {pos}")
        start = pos + 1

#plot Nucleotide composotion bar graph
import matplotlib.pyplot as plt
from collections import Counter
seq = str(fasta)
counts = Counter(seq)
bases = sorted(counts.keys())
values = [counts[b] for b in bases]
plt.figure(figsize=(6,3))
plt.bar(bases, values)
plt.title("Nucleotide composition")
plt.xlabel("Nucleotide Bases")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
