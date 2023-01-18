# plasmid-sequence-quantifier

In a nutshell, what we want this program to do:

0. Data Collection: Plasmids with peptide fragment nucleotide sequence inserts will be nanopore sequenced.
1. Data Preprocessing: Because the sequencing starts at a random location of the plasmid, the data needs to be reoriented.
2. The backbone plasmid sequences need to be extracted.
3. Count the quantity of each peptide sequence.

The intention is to determine that (A) all peptide sequences from the library appear in the nanopore sequence run and (B) their quantities are relatively evenly distributed.
