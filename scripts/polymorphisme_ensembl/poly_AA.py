import requests, sys
import pprint

server = "http://rest.ensembl.org"


def getList(dict):
    return dict.keys()


def run_api_request (server, url):
    r = requests.get(server + url , headers={"Content-Type": "application/json"})

    if not r.ok:
        r.raise_for_status()
        sys.exit()

    decoded = r.json()
    return decoded
    # print(repr(decoded))


def run_api_aa(variant_ID):
    ext_AA = "/variant_recoder/human"+ str(variant_ID) + "?"
    run_api_request(server, ext_AA)
    for k in decoded:  # filter access
        keys_list = getList(k)
        for index in range(len(keys_list)):
            print("")
            print(k[list(keys_list)[index]]["input"])
            print(k[list(keys_list)[index]]["hgvsp"][0])  # to proteins type SNP and position
            print(k[list(keys_list)[index]]["hgvsc"][0])  # To ENSEMBL corresponded gene ID
            print("\n")
        # print("second_variant")


def run_api_maf (variant_ID):
    ext_maf = "/variation/homo_sapiens/" + str(variant_ID) + "?"
    run_api_request(server, ext_maf)
    print("The global MAF of your sequence is:")
    for key, value in decoded.items():
        if key == "MAF":
            print(value)


if __name__ == '__main__':
    # input exemple : rs782264239
    input_variant_ID = input(" Please enter your variant ID : ")
    run_api_aa(input_variant_ID)
    run_api_maf(input_variant_ID)





