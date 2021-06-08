"""
Script to run local blast against Human genome to get
significant Self-peptidome
"""

import subprocess


# get reference genome all fasta protein file from NCBI
# command_get_refgenome = 'wget -P Human_fasta_prot https://www.ncbi.nlm.nih.gov/genome/?term=homo+sapiens'
# subprocess.call(command_get_refgenome, shell= True)


def creat_blast_db():
    """creat local database with reference genome
    protein Fasta file for blastp execution"""


command_create_db = 'makeblastdb -in homo_sap_local_db/homo_sapien_genome.fasta' + \
                    ' -parse_seqids -dbtype prot -out homo_sap_local_db//DB'
subprocess.call(command_create_db, shell=True)


def run_blast(filein, fileout):
    """Run BLASTp for short sequence in command line
    @filein : file.fasta of queries
    @fileout : file.txt of BLASTp resuslts """
    command_run_blast = "blastp -task blastp-short -query" + \
                        str(filein) \
                        + "-db homo_sap_local_db/DB -outfmt \"7 qstart qend sacc sstart send length evalue bitscore " \
                          "sseq" + \
                        "qcovs pident\" -max_target_seqs 3 -out results_blast/" \
                        + str(fileout)
    subprocess.call(command_run_blast, shell=True)
