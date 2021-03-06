import re
import requests

def MWcalculator(input):
    atom_mass = {'H': 1.0078, 'C': 12.011, 'N': 14.007, 'O': 15.999, 'F': 18.998403, 'Cl': 35.453}
    mw = 0
    for x in re.findall(r'(([A-Z][a-z]?)(\d{1,})?)', input):
        if not x[2]:
            count = 1
        else:
            count = int(x[2])
        mw += atom_mass[x[1]] * count
    return str(mw)



def APImw(input):
    pubchem_molecular_weight = requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/inchikey/"+input+"/property/MolecularWeight/json")
    regex = r'(\d+)\.(\d+)'
    check = re.search(regex, pubchem_molecular_weight.text)
    return str(check.group(0))
