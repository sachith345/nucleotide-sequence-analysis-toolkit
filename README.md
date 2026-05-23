# Nucleotide Sequence Analysis Toolkit Using Python and Biopython

A computational biology and bioinformatics toolkit developed using Python and Biopython for FASTA-based nucleotide sequence analysis. The script validates whether the input sequence is DNA or RNA, calculates nucleotide composition and sequence length, analyzes purine and pyrimidine percentages, generates complement and reverse complement sequences, performs transcription and translation, identifies start and stop codons, scans for restriction enzyme recognition sites, and visualizes nucleotide distribution using a matplotlib bar graph.

## Features

- FASTA sequence preprocessing and cleanup
- DNA/RNA sequence validation
- Nucleotide count and sequence length analysis
- Adenine, Guanine, Cytosine, Thymine, and Uracil composition analysis
- Purine and pyrimidine percentage calculation
- Complement and reverse complement generation
- DNA to RNA transcription
- RNA to DNA back transcription
- Protein translation using Biopython
- Start and stop codon detection
- Restriction enzyme site mapping
- Nucleotide composition visualization using matplotlib

## Technologies Used

- Python 3
- Biopython
- Matplotlib

## Restriction Enzymes Included

- EcoRI
- HindIII
- BamHI
- NotI
- PstI
- SphI

## Installation

```bash
pip install biopython matplotlib
```

## Run the Script

```bash
python sequence_analysis_toolkit.py
```

## Input

Paste the nucleotide sequence in FASTA format inside:

```python
your_fasta = """ """
```

## Output

The program generates:

- Sequence type identification (DNA/RNA)
- Nucleotide composition statistics
- Purine and pyrimidine percentages
- Complement and reverse complement sequences
- Transcription and translation results
- Start and stop codon positions
- Restriction enzyme recognition site locations
- Nucleotide composition bar graph

## Author

Sachith  
B.Tech Biotechnology  
Bioinformatics | Computational Biology | AI/ML
