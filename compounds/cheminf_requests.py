from django.conf import settings
import requests
# import forms
# inchikey = str(forms.MWForm.Meta.fields(0))

"""prints the URL to the pubchem rest API for that compound"""
# API_URL_json = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/"+csmiles+"/json"
# print(API_URL_json)

"""Use the request package to access the data at that URL"""
pubchem_molecular_weight = requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/"+inchikey+"/property/MolecularWeight/json")
print(pubchem_molecular_weight.text)
# print(query_json.json())


"""Use the request package to access the synonyms for the compound"""
# synonym_query_json = requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/"+csmiles+"/synonyms/json")
# print(synonym_query_json.json())

# synonyms = synonym_query_json.json()["InformationList"]["Information"][0]["Synonym"]
# print(synonyms)
