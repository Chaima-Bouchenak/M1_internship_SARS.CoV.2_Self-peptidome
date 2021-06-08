import requests
import sys
from poly_variation import set_api


def run_api_tx (inputID):
    print("Trasncript_ID\tTx_version")

    # define the general URL parameters
    server = "http://rest.ensembl.org/"
    ext_tx = "overlap/id/" + str(inputID) + "?feature=transcript"
    con = "application/json"

    # submit the query
    get_tx = set_api(server, ext_tx, con)

    # to show all the results
    # pprint(get_tx)

    # to filter results for 2 parameters :
    for transcript in get_tx:
        transcript_id = transcript['id']
        transcript_version = transcript['version']

        print(transcript_id+ "\t" + str(transcript_version))


if __name__ == '__main__':
    # input exemple : ENST00000354646
    input_gene_ID = input(" Please enter your gene ID : ")
    run_apitx(input_gene_ID)

