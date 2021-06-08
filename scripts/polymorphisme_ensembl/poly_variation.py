import requests
import sys
import json
from pprint import pprint



def set_api (server, request, content_type):
    """
    Set Ensembl APi to get variation information according to gene ID.
    :param server: Ensembl REST API server
    :param request: API specific request
    :param content_type: .json
    :return: Variant ID, DB source and Consequence type of the variation
    """
    r = requests.get(server + request, headers={"Accept": content_type})

    if not r.ok:
        r.raise_for_status()
        sys.exit()

    if content_type == 'application/json':
        return r.json()
    else:
        return r.text


def run_api_variation (inputID):

    print("Variant_ID\tSource\tconsequence_type")
    # define the general URL parameters
    server = "http://rest.ensembl.org/"
    ext_overlap = "overlap/id/" + str(inputID) + "?feature=variation"
    con = "application/json"

    # submit the query to server
    get_overlap = set_api(server, ext_overlap, con)

    # to show all the results
    # pprint(get_overlap)

    # to filter results for 3 parameters :
    for variant in get_overlap:
        variant_id = variant['id']
        source = variant['source']
        consequence_type = variant['consequence_type']

        print(variant_id + "\t" + source+ "\t" + consequence_type)

if __name__ == '__main__':
    # input exemple : ENST00000354646
    input_gene_ID = input(" Please enter your gene ID : ")
    run_api_variation(input_gene_ID)
