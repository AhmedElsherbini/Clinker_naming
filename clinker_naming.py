#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 10:19:45 2025

@author: ahmed
"""

from Bio import SeqIO
import argparse
import warnings
#########################################
my_parser = argparse.ArgumentParser(description='Welcome!')
#print("example: $ python bakta_stat.py -i ./txt")



my_parser.add_argument('-i','--input_file',
                       action='store',
                        metavar='input_file',
                       type=str,
                       help="input_file")

my_parser.add_argument('-o','--outfile',
                       action='store',
                        metavar='outfile',
                       type=str,
                       help="outfile")

args = my_parser.parse_args()

###########################################

input_file = args.input_file
outfile = args.outfile

warnings.filterwarnings("ignore")



#input_file = "CA_I.gbk"
#outfile = "SS.gbk"

# Parse, remove features, and write to new file

with open(input_file, "r") as infile, open(outfile, "w") as outfile:
    for record in SeqIO.parse(infile, "genbank"):
        for feature in record.features:
            if "transl_table" in feature.qualifiers:
                # Replace 11 with '*'
                feature.qualifiers["transl_table"] = [
                    "*" if val == "11" else val
                    for val in feature.qualifiers["transl_table"]
                ]
        SeqIO.write(record, outfile, "genbank")
        

print(f"All features removed. Output saved to {outfile}")

