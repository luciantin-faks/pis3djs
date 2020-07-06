import json

FILE_NAME = 'PISDATA.json'
SAMPLE_TEXT = 'asdk asdk jas asdjklf agnf jbs  jksfnd js nlsbn jklsfg ngjfnlsb aw fahjlb wefhawb fgb aergbl erbag hbaerhg baerlb '


IPS = [
    'Analiza i planiranje poslovanja',
    'Nabava i ulazna logistika',
    'Proizvodnja',
    'Prodaja i izlazna logistika',
    'Računovodstvo i upravljanje financijama poduzeća',
    'Upravljanje ljudskim resursima',
    'Upravljanje trajnom poslovnom imovinom',
]

MODULI = {
    IPS[0] : [ 'Strateško Planiranje Poslovanja', 'Analitika i planiranje rada zaposlenika', 'Operativna analitika poslovanja', 'Financijska analitika i planiranje' ],
    IPS[1] : [ 'Priprema nabave i naloga za nabavu', 'Suradnja s dobavljacima', 'Upravljanje zalihama i skladisnim poslovanjem', 'Ulazna logistika', ],
    IPS[2] : [ 'Upravljanje Proizvodnjom', 'Planiranje i priprema proizvodnje', 'Upravljanje kvalitetom i razvojem proizvoda', ],
    IPS[3] : [ 'Upravljanje narudžbama u prodaji', 'Upravljanje izlaznom logistikom i transportom', 'Modul upravljanja poslijeprodajnim uslugama', 'Pružanje strućnih savjeta i usluga', 'Poticanje na kupnju i sofisticirani oblici prodaje' ],
    IPS[4] : [ 'Glavna knjiga', 'Analiticko knjigovodstvo i ostale poslovne knjige' ],
    IPS[5] : [ 'Upravljanje talentima i razvoj ljudskih potencijala', 'Upravljanje radnim i poslovnim procesima ljudi' ],
    IPS[6] : [ 'Tehničko upravljanje i održavanje TPI-a','Upravljanje portfeljem TPI-a', 'Pribavljanje i deaktiviranje TPI-a' ],
}

PODMODULI = {
    MODULI[IPS[4]][1] : ['Modul racunovodstvenog pracenja dugotrajne imovine', 'Modul racunovodstvenog pracenja zaliha sirovina i materijala', 'Modul obracuna placa djelatnika', 'Modul racunovodstvenog pracenja proizvodnje i zaliha gotovih proizvoda', 'Modul racunovodstvenog pracenja zaliha trgovacke robe']
}

APLIKACIJE = {

    MODULI[IPS[0]][0] : ['Uskladivanje s pravnom regulativom i standardima struke', 'Opce stratesko planiranje', 'Stratesko financijsko planiranje', 'Planiranje unutarnjih ulaganja (investicija)', 'Planiranje vanjskih ulaganja (investicija)'],
    MODULI[IPS[0]][1] : ['Planiranje potreba za zaposljavanjem', 'Planiranje troskova rada', 'Analitika i mjerenje procesa upravljanja ljudskim resursima','Analitika za potrebe upravljanja talentima'],
    MODULI[IPS[0]][2] : ['Analitika nabave','Analitika zaliha i skladisnog poslovanja','Analitika proizvodnje','Analitika transporta','Analitika prodaje','Analiitika usluga pruzanih klijentima', 'Analitika upravljanja kvalitetom'],
    MODULI[IPS[0]][3] : ['Financijsko i upravljacko izvjestavanje','Financijsko planiranje, budzetiranje i predvidanje','Analitika profitabilnosti', 'Analitika troskova proizvoda i usluga', 'Analitika ponasanja prilikom placanja'],

    MODULI[IPS[1]][0] : ['Analiza potreba u potrosnim dobrima', 'Konsolidacija potreba u potrosnim dobrima i planiranje nabave', 'Priprema naloga za nabavu potrosnih dobara'],
    MODULI[IPS[1]][1] : ['Uspostavljanje i razvoj suradnje s dobavljacima', 'Organizacija drazbe i prikupljanje ponuda','Izrada narudzbe za nabavu','Potvrda narudzbe','Obrada ulaznih racuna'],
    MODULI[IPS[1]][2] : ['Prijam i kontrola ulaza potrosnih dobara', 'Pracenje zaliha i upravljanje skladistem','Izlaz dobara iz skladista'],
    MODULI[IPS[1]][3] : ['Utvrdivanje redoslijeda dostava', 'Prihvat isporuka', 'Obrada dostavne i transportne dokumentacije'],

    MODULI[IPS[2]][0] : ['Upravljanje zlihama u proizvodnji','Upravljanje proizvodnim procesima'],
    MODULI[IPS[2]][1] : ['Izrada glavnog plana proizvodnje','Signal s trzista','Kombinacija'], #nacini planiranja a ne aplikacije 
    MODULI[IPS[2]][2] : ['Upravljanje kvalitetom','Razvoj novih proizvoda'],

    MODULI[IPS[3]][0] : ['Upravljanje profilima klijenata','Organizacija i upravljanje aukcijama','Obrada upita klijenata','Podnosenje konkretnih ponuda','Upravljanje kupoprodajnim ugovorima','Fakturiranje','Upravljanje povraton ambalazom'],
    MODULI[IPS[3]][1] : ['Upravljanje zalihama i skladistenjem gotovih proizvoda','Upravljanje isporukom','Upravljanje transportom'],
    MODULI[IPS[3]][2] : ['Rjesavanje reklamacije kupaca', 'Evidencija intervencija u jamstvenom roku', 'Potpora uslugama odrzavanja i popravaka nakon isteka jamstvenog roka','Potpora uslugama nadogradnje i prosirenja funckionalnosti'],
    MODULI[IPS[3]][3] : ['Strucno savjetovanje','Obrazovanje i uvjezbavanje korisnika'],
    MODULI[IPS[3]][4] : ['Planiranje akcija poticanja na kupnju', 'Potpora akcijama poticanja na kupnju','Potpora sofisticiranim oblicima prodaje'],
    
    MODULI[IPS[4]][0] : ['Obrada knjigovodstvenih isprava poduzeca','Kontrolni postupci na razini glavne knjige','izvjestavanje iz glavne knjige'],
    PODMODULI[MODULI[IPS[4]][1]][0] : ['Knjiga inventara','Analiticko knjigovodstvo dugotrajne imovine', 'Kontrola poslovanja s dugotrajnom imovinom', 'Izvjestavanje o dugotrajnoj imovini'],
    PODMODULI[MODULI[IPS[4]][1]][1] : ['Evidencija zaliha sirovina i materijala u poslovnim knjigama', 'Kontrola materijalnog poslovanja', 'Izvjestavanje o materijalnom poslovanju'],
    PODMODULI[MODULI[IPS[4]][1]][2] : ['Analiticko knjigovodstvo', 'Kontrolni postupci', 'Izvjestavanje o troskovima placa'],
    PODMODULI[MODULI[IPS[4]][1]][3] : ['Evidencija proizvodnje i zaliha gotovih proizvoda u poslovnim knjigama', 'Kontrolni postupci na razini proizvodnje i zaliha gotovih proizvoda', 'Izvjestavanje o proizvodnji i gotovim proizvodima'],
    PODMODULI[MODULI[IPS[4]][1]][4] : ['Evidencija trgovacke robe u poslovnim knjigama', 'Kontrola robnog poslovanja', 'Izvjestavanje o robnom poslovanju'],

    MODULI[IPS[5]][0] : ['Upravljanje zaposljavanjem','Upravljanje karijerom', 'Ucenje i uvjezbavanje', 'Upravljanje ucinkovitoscu zaposlenika','Kompenzacijski menadzment'],
    MODULI[IPS[5]][1] : ['Maticna evidencija i administracija zaposlenika', 'Organizacijsko upravljanje','Upravljanje radnim vremenom', 'Obracun placa i ostalih naknada za rad'],

    MODULI[IPS[6]][0] : ['Planiranje redovitog, povremenog i prigodnog odrzavanja TPI-a', 'Planiranje modernizacje TPI-a', 'Pracenje postupaka odrzavanja i popravaka TPI-a', 'Pracenje i analiza ukupnih troskova TPI-a'],
    MODULI[IPS[6]][1] : ['Pracenje i ocjenjivanje vrijednosti TPI-a', 'Izvjestavanje o znacajnim obiljezjima TPI-a', 'Upravljanje odnosima s dobavljacima TPI-a, suvlasnicima i partnerima', 'Graficko prikazivanje portfelja TPI-a'],
    MODULI[IPS[6]][2] : ['Priprema javnog natjecaja za pribavljanje TPI-a', 'Provedba javnog natjecaja za pribavljanje TPI-a', 'Ugovor s odabranim dobavljacima', 'Otpis dijela vrijednosti TPI-a', 'Deaktiviranje TPI-a'],
}

OPIS = {
    IPS[0] : SAMPLE_TEXT,
    IPS[1] : SAMPLE_TEXT, 
    IPS[2] : SAMPLE_TEXT,
    IPS[3] : SAMPLE_TEXT,
    IPS[4] : SAMPLE_TEXT,
    IPS[5] : SAMPLE_TEXT,
    IPS[6] : SAMPLE_TEXT,

#######################################

    MODULI[IPS[0]][0] : SAMPLE_TEXT,
    MODULI[IPS[0]][1] : SAMPLE_TEXT,
    MODULI[IPS[0]][2] : SAMPLE_TEXT,
    MODULI[IPS[0]][3] : SAMPLE_TEXT,

    MODULI[IPS[1]][0] : SAMPLE_TEXT,
    MODULI[IPS[1]][1] : SAMPLE_TEXT,
    MODULI[IPS[1]][2] : SAMPLE_TEXT,
    MODULI[IPS[1]][3] : SAMPLE_TEXT,

    MODULI[IPS[2]][0] : SAMPLE_TEXT,
    MODULI[IPS[2]][1] : SAMPLE_TEXT,
    MODULI[IPS[2]][2] : SAMPLE_TEXT,

    MODULI[IPS[3]][0] : SAMPLE_TEXT,
    MODULI[IPS[3]][1] : SAMPLE_TEXT,
    MODULI[IPS[3]][2] : SAMPLE_TEXT,
    MODULI[IPS[3]][3] : SAMPLE_TEXT,
    MODULI[IPS[3]][4] : SAMPLE_TEXT,

    MODULI[IPS[4]][0] : SAMPLE_TEXT,
    PODMODULI[MODULI[IPS[4]][1]][0] : SAMPLE_TEXT,
    PODMODULI[MODULI[IPS[4]][1]][1] : SAMPLE_TEXT,
    PODMODULI[MODULI[IPS[4]][1]][2] : SAMPLE_TEXT,
    PODMODULI[MODULI[IPS[4]][1]][3] : SAMPLE_TEXT,
    PODMODULI[MODULI[IPS[4]][1]][4] : SAMPLE_TEXT,

    MODULI[IPS[5]][0] : SAMPLE_TEXT,
    MODULI[IPS[5]][1] : SAMPLE_TEXT,

    MODULI[IPS[6]][0] : SAMPLE_TEXT,
    MODULI[IPS[6]][1] : SAMPLE_TEXT,
    MODULI[IPS[6]][2] : SAMPLE_TEXT,

#######################################



}


def cleanWrite():
    jdata = json.dumps({
        'IPS':IPS,
        'MODULI':MODULI,
        'PODMODULI':PODMODULI,
        'APLIKACIJE':APLIKACIJE,
        'OPIS':OPIS,
    })
    data  = json.loads(jdata)
    with open('PISDATA.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load():
    with open('host_data.json', 'r') as myfile:
        data=myfile.read()
    return json.loads(data)


def step():
    data = load()

    with open('host_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)



cleanWrite()
