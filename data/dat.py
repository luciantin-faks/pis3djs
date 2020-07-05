import json

IPS = [
    'Analiza i planiranje poslovanja',
    'Nabava i ulazna logistika',
    'Proizvodnja',
    'Prodaja i ulazna logistika',
    'Racunovodstvo i upravljanje financijama poduzeca',
    'Upravljanje ljudskim resursima',
    'Upravljanje trajnom poslovnom imovinom',
]

MODULI = {
    IPS[0] : [ 'Strateško Planiranje Poslovanja', 'Analitika i planiranje rada zaposlenika', 'Operativna analitika poslovanja', 'Financijska analitika i planiranje' ],
    IPS[1] : [ 'Priprema nabave i naloga za nabavu', 'Suradnja s dobavljacima', 'Upravljanje zalihama i skladisnim poslovanjem', 'Ulazna logistika', ],
    IPS[2] : [ 'Upravljanje Proizvodnjom', 'Planiranje i priprema proiyvodnje', 'Upravljanje kvalitetom i razvojem proizvoda', ],
    IPS[3] : [ 'Upravljanje narudzbama u prodaji', 'Upravljanje izlaznom logistikom i transportom', 'Potpora postprodajnim uslugama', 'Pruzanje strucnih savjeta i usluga', 'Poticanje na kupnju i sofisticirani oblici prodaje' ],
    IPS[4] : [ 'Modul glavne knjige', 'Moduli analitickog knjigovodstva i ostalih poslovnih knjiga' ],
    IPS[5] : [ 'Upravljanje talentima i razvoj ljudskih potencijala', 'Upravljanje radnim i poslovnim procesima ljudi' ],
    IPS[6] : [ 'Tehnicko upravljanje i odrzavanje TPI-a','Upravljanje portfeljem TPI-a', 'Pribavljanje i deaktiviranje TPI-a' ],
}

APLIKACIJE = {
    MODULI[IPS[0]][0] : [],
    MODULI[IPS[0]][1] : [],
    MODULI[IPS[0]][2] : [],
    MODULI[IPS[0]][3] : [],

    MODULI[IPS[0]][0] : [],
    MODULI[IPS[0]][1] : [],
    MODULI[IPS[0]][2] : [],
    MODULI[IPS[0]][3] : [],
}

def clean():
    jdata = json.dumps({
        'IPS':IPS,
        'MODULI':MODULI,
    })
    data  = json.loads(jdata)
    with open('PISDATA.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


clean()

def load():
    with open('host_data.json', 'r') as myfile:
        data=myfile.read()
    return json.loads(data)


def step():
    data = load()

    with open('host_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

