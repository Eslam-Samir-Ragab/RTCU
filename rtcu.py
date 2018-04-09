#!/usr/bin/env python
from __future__ import print_function
import argparse
from Bio.Seq import Seq
from Bio import SeqIO
import itertools

def get_manual_dict(manual_file):
    with open(manual_file) as f:
        manual_dict={}
        for line in f:
            items = line.rstrip().split()
            manual_dict[items[0]]=items[2:]
    return manual_dict

def get_prot(input_file):
    seq=SeqIO.read(input_file,'fasta').seq
    return seq

def build_construct(working_dict,prot):
    construct = [working_dict[aa] for aa in prot]
    return construct

def get_variable_spots(construct):
    final,variations='',[]
    for i in range(len(construct)):
        codon=construct[i]
        if len(codon)>1:
            variations.append([var for var in codon])
            final+="%s"
        else:
            codon="".join(codon)
            final+=codon
    spots=final.count("%s")
    return final,variations,spots

def write_output(output_file,final,variations,spots):
    m=0
    with open(output_file,"w") as f:
        variations=(itertools.product(*variations))
        for new in variations:
            m+=1
            f.write(">sequence_%s\n" %m)
            f.write(final %new)
            f.write("\n")
        f.write("\n\nNumber of the changed codons = %s" %spots)


parser = argparse.ArgumentParser(prog='Protein to DNA converter by codon usage',usage='\n%(prog)s : uses the codon usage preference of your choice to reverse translate a protein or DNA sequence.\n\n Eslam S.Ibrahim\n\n eslam.ebrahim@pharma.cu.edu.eg')
parser.add_argument('-in',dest='input_file',type=argparse.FileType('r'),required=True,help='Input file containing your sequence (protein or DNA')
parser.add_argument('-out',dest='output_file',required=True,help='Your output file')
parser.add_argument('-codon_usage',dest='manual_file',required=True,help='Your manually selected codon usage')
args=parser.parse_args()

input_file=args.input_file
output_file=args.output_file
manual_file=args.manual_file


#Core program !!
working_dict=get_manual_dict(manual_file)
prot=get_prot(input_file)
construct=build_construct(working_dict,prot)
final,variations,spots=get_variable_spots(construct)
write_output(output_file,final,variations,spots)