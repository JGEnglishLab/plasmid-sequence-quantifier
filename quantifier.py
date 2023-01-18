import os
from os.path import exists
import sys
from Bio import SeqIO
import re
import pandas as pd

################################################################################################
#
# Data Loading and Processing
#
################################################################################################


# Changing column names
fragmentDf = pd.read_csv('data/InteinsFragmentList.csv')
fragmentDf.columns=['SequenceName', 'FragmentLength_bp', 'InteinFragmentSequence']
seqs = fragmentDf['InteinFragmentSequence']
seqs = [x[20:-20] for x in seqs]
lengths = [len(x) for x in seqs]
fragmentDf['InteinFragmentSequence'], fragmentDf['FragmentLength_bp'] = seqs, lengths
fragmentDf.to_csv('data/seqs.csv', index=False)
frags = [x[-100:-80] for x in seqs]
print(len(set(frags)))
print(sorted(set(frags)))

'''
# Get the plasmid reads
readFile = [barcodeDir + 'SequenceData/' + file for file in os.listdir(barcodeDir + 'SequenceData/') if file.split('.')[-1]=='fastq' or file.split('.')[-1]=='fq'][0]
readRecords = [record for record in SeqIO.parse(readFile, "fastq")]
print(f'Initial Number of Reads: {len(readRecords)}')

# reorder each plasmid read so the starting index matches the reference sequence
# NOTE: because the plasmids are circular, the start of the read may not
#   correspond to the reference. Here we are reordering them to match, and
#   removing reads where the start of the reference sequence cannot be identified
#   (first 15 nucleotides exact match).
# NOTE: We also remove any reads that significantly deviate in size from the
#   reference (200 tolerance).
nMatch = 15
lengthTolerance = 200
beginOfRef = str(refRecord[:nMatch].seq)
for i in range(len(readRecords)-1, -1, -1):
    readSeq = str(readRecords[i].seq)
    a = re.search(beginOfRef, readSeq)
    if not a or abs(len(readSeq) - len(refRecord)) > lengthTolerance: del readRecords[i]
    elif a.start() != 0: readRecords[i] = readRecords[i][a.start():] + readRecords[i][:a.start()]

print(f'Number of Remaining Processed Reads: {len(readRecords)}')

# Write the processed data to an output folder for future reference.
outputDir = sys.argv[2]
if outputDir[-1] != '/': outputDir += '/'
assert not exists(outputDir)
os.mkdir(outputDir)
os.mkdir(outputDir + 'delete')
with open(outputDir + 'delete/seq_bin0.fq', "w") as output_handle:
    SeqIO.write(readRecords, output_handle, "fastq")

################################################################################################
#
# Consensus Generation
#
################################################################################################

# Code taken from pipeline.py and tweaked for current use.
binFiles = [outputDir + 'delete/seq_bin0.fq']
consensusMethod = 'lamassemble'
records = ConsensusContext(consensusMethod).generate_consensus_sequences(binFiles)

# Consensus file written.
consensusFile = 'consensus_' + consensusMethod + '.fasta'
with open(outputDir + consensusFile, "w") as output_handle:
    SeqIO.write(records, output_handle, "fasta")
'''
