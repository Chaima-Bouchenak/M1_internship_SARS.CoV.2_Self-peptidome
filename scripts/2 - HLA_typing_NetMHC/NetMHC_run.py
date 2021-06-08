"""
Script to run local NetNHC for CMH search
use this command on command line for either fasta ou peptide files
"""
import subprocess

# def run_cmh_1 (filein , fileout):
fasta_commad = "netMHC" + filein + '>' + fileout
# subprocess.call(fasta_commad, shell=True)

pep_commad = "netMHC -p" + filein + '>' + fileout
# subprocess.call(pep_commad, shell=True)


# def run_cmh_2 (filein , fileout):
fasta_commad_2 = "netMHCII" + filein + '>' + fileout
# subprocess.call(fasta_commad, shell=True)

pep_commad_2 = "netMHCII -p" + filein + '>' + fileout
# subprocess.call(pep_commad, shell=True)

