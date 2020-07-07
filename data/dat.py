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
    IPS[3] : [ 'Upravljanje narudžbama u prodaji', 'Upravljanje izlaznom logistikom i transportom', 'Potpora poslijeprodajnim uslugama', 'Pružanje strućnih savjeta i usluga', 'Poticanje na kupnju i sofisticirani oblici prodaje' ],
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
    MODULI[IPS[0]][2] : ['Analitika nabave','Analitika zaliha i skladisnog poslovanja','Analitika proizvodnje','Analitika transporta','Analitika prodaje','Analitika usluga pruzanih klijentima', 'Analitika upravljanja kvalitetom'],
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
    IPS[0] : 'Poslovni ciklus započinje analizom postojećeg (aktualnog) stanja poslovanja i planiranjem budućih poslovnih aktivnosti ovisno o rezultatima provedene analize. Moduli IPS-a analize i poslovanja omogućuju menadžmentu poduzeća da jasno spozna kako ostvariti osnovni strateški cilj - profitabilnost poslovanja te da logično i djelotvorno poveže strateške planove poslovanja s operativnom učinkovitošću poslovanja.',
    IPS[1] : """ Nabava je djelatnost poduzeća i drugih poslovnih sustava koja se brine o opskrbi
            materijalima, opremom, uslugama i energijom potrebnim za realizaciju ciljeva poslovnog
            sustava. Nabava u užem smislu podrazumijeva odvijanje operativnih poslova u procesu
            pribavljanja objekata nabave, dok nabava u širem smislu obuhvaća i strategijske zadatke
            o kojima ovise i učinci i dobit poslovnog sustava.
            Poslovna logistika (engl. Business Logistics) obuhvaća sustavno praćenje kretanja roba
            od dobavljača do potrošača u svrhu ostvarenja ravnomjernog i što boljeg iskorištavanja
            kapaciteta sredstava i djelatnika u prijevozu, primanju, skladištenju, držanju zaliha i
            izdavanju robe kao i s njima vezanih procesa pakiranja, označavanja te obrade i tijeka podataka.  """, 
    IPS[2] : """ Informatička potpora proizvodnoj funkciji ostvaruje se putem informacijskog podsustava
            (IPS) proizvodnje. Osnovni je cilj ovoga podsustava ubrzavanje razvoja i proizvodnje
            gotovih proizvoda. U tehnološkom smislu, to je svakako jedan od najsloženijih
            podsustava cjelokupnog poslovnog informacijskog sustava jer zahtjeva često korištenje i
            povezivanje vrlo raznorodnih tehnologija i različitih programskih, proizvodnih i
            tehnoloških rješenja koje treba planirati na jedinstven način, te kojima treba na sličan
            način upravljati, kontrolirati ih i nadzirati.  """,
    IPS[3] : """ Prodaja proizvoda i/ili usluga završni je čin svakog poslovnog ciklusa.
            Lako je proizvesti, teško je proizvedeno prodati!
            Naglasak je na važnosti vještina, znanja, truda, napora i sredstava koje poduzeće treba u
            suvremenom konkurentskom okruženju posjedovati i uložiti u tržišnu realizaciju (prodaju)
            onoga što je proizvelo.
            Informatička potpora funkciji prodaje mora biti kvalitetna, snažna i dobro organizirana.
            Pružit će je informacijski podsustav (IPS) prodaje i izlazne logistike.  """,
    IPS[4] : """ Osnovni je zadatak funkcije računovodstva i upravljanja financijama evidentirati sve
            poslovne događaje u poduzeću u vrijednosnom, odnosno financijskom (novčanom)
            izrazu. IPS računovodstva i upravljanja financijama je modularno ustrojen, a na razvoj i
            organizaciju tih modula utječe organizacija računovodstvene funkcije.  """,
    IPS[5] : """ Funkcija upravljanja ljudskim resursima, odnosno potencijalima ili, kao što se to katkad
            naziva, upravljanje ljudskim kapitalom promatra kao ključna i delikatna poslovna
            funkcija koja traži primjenu mnogo suptilnijih i sofisticiranijih metoda i od koje se očekuju
            daleko veći i kvalitetniji doprinosi uspješnosti sveukupnog poslovanja poduzeća.
            I ova poslovna funkcija mora, dakako, biti popraćena odgovarajućom informacijskom
            potporom. Pružat će joj je IPS upravljanja ljudskim resursima (potencijalima). Sukladno
            suvremenim shvaćanjima ciljeva, uloge i opsega funkcije upravljanja ljudskim resursima,
            njen podržavajući informacijski podsustav trebao bi obuhvaćati sljedeće glavne module:
            upravljanje radnim i poslovnim procesima u kojima sudjeluju ljudi,
            upravljanje talentima i razvojem ljudskih potencijala.  """,
    IPS[6] : """ Pod pojmom trajne (dugotrajne) poslovne imovine podrazumijevaju se materijalna
            dobra koja se koriste u poslovanju, ali se troše razmjerno sporo. Za razliku od materijala i
            sirovina koji će biti "potrošeni" u jednom proizvodnom ciklusu, zgrade, proizvodni
            strojevi, uredska oprema, informatička oprema, prijevozna sredstva i slična materijalna
            dobra "nadživjet" će pojedinačne proizvodne cikluse i bit će ih moguće koristiti tijekom
            dužeg vremena. No, i ta se dobra troše - amortiziraju - pa ih nakon određenog vremena
            treba otpisati.  """,

#######################################

    MODULI[IPS[0]][0] : """ Analitički moduli prikazani u prethodnim odjeljcima stvaraju informacijsku podlogu
                        potrebnu pretežito za stvaranje kratkoročnih, detaljnih planova. No, svako poduzeće
                        mora, kako bi u najvećoj mogućoj mjeri kontroliralo svoje djelovanje i upravljalo vlastitim
                        razvojem, i strateški, dakle dugoročno, planirati svoje aktivnosti.  """,
    MODULI[IPS[0]][1] : """ Modul analitike i planiranja rada zaposlenika u uskoj je vezi s odgovarajućim modulima
                        IPS-a upravljanja ljudskim resursima.  """,
    MODULI[IPS[0]][2] : """ Ovo je obično u praksi najsloženiji modul IPS-a analize i planiranja poslovanja jer se
                        njime nastoje stvoriti analitičke podloge za planiranje svih operativnih aspekata
                        poslovanja, od nabave do prodaje, usluga pružanih klijentima i upravljanja kvalitetom
                        poslovanja.  """,
    MODULI[IPS[0]][3] : """ Financijska analitika omogućuje definiranje konkretnih financijskih ciljeva, stvaranje
                        realističnih poslovnih planova te praćenje troškova i prihoda (dohotka) poduzeća. Ovaj
                        modul IPS-a analize i planiranja poslovanja omogućuje kreiranje i simuliranje tokova
                        vrijednosti u poduzeću i u odnosima tog poduzeća s drugim subjektima (kupcima,
                        dobavljačima, poslovnim partnerima, državnim i javnim institucijama itd.).  """,

    MODULI[IPS[1]][0] : """ Budući da naručena roba tijekom transporta može promijeniti više načina prijevoza,
                        primjerice, cestovnog, željezničkog, morskog i zračnog te više špeditera, pitanje
                        praćenja transporta, popratne dokumentacije, carinskih deklaracija, koordinacije
                        prijevoznika i sličnih aktivnosti postaje ozbiljan problem.
                        Modul ulazne logistike IPS-a nabave i ulazne logistike mora odgovoriti takvim izazovima.  """,
    MODULI[IPS[1]][1] : """ Proces upravljanja zalihama i skladištenjem potrošnih dobara obuhvaća evidentiranje
                        stanja zaliha i praćenja materijalnih tokova u količinskom i vrijednosnom izrazu.
                        Na informacijskoj razini potporu upravljanju zalihama i skladišnom poslovanju pružat će
                        tri osnovne softverske aplikacije:
                        Prijam i kontrola ulaza potrošnih dobara
                        Praćenje zaliha i upravljanje skladištem
                        Izlaz dobara iz skladišta  """,    
    MODULI[IPS[1]][2] : """ U pripremi i provedbi procesa nabave potrošnih dobara važno je voditi računa o
                        podacima o dobavljačima, o njihovim cijenama, izračunu nabavnih cijena u koje ulaze i
                        svi zavisni troškovi nabave (primjerice, transportni troškovi i troškovi osiguranja, carine
                        itd.) i o izradi različitih vrsta pregleda cijena. Osim toga, modul suradnje s dobavljačima
                        IPS-a nabave i ulazne logistike mora biti od pomoći u određivanju odgovarajućih
                        vremena (termina) nabave robe, poštujući potrebe poduzeća, ali uzimajući u obzir i
                        vrijeme dobave, optimalne veličine narudžbe i promjene u tržišnoj potražnji.  """,    
    MODULI[IPS[1]][3] : """ Priprema nabave polazi od analize potreba funkcije proizvodnje i ostalih poslovnih
                        funkcija za nabavom potrebnih sirovina, materijala i ostalih potrošnih dobara (uredskog
                        materijala, informatičkog potrošnog materijala, sredstava za čišćenje prostorija itd.).
                        Krajnji je cilj izrada naloga za nabavu, kao jednog od osnovnih dokumenata korištenih u
                        nabavnom poslovanju.  """,

    MODULI[IPS[2]][0] : """ Upravljanje proizvodnjom obuhvaća:
                        upravljanje zalihama u priozvodnji
                        upravljanje proizvodnim procesima  """,
    MODULI[IPS[2]][1] : """ Prije no što se pristupi samoj proizvodnji, trebat će donijeti određene planove i izvršiti
                        detaljne pripreme kako bi se sam proizvodni proces kasnije odvijao nesmetano, bez
                        zastoja i nepotrebnih nedoumica. Priprema proizvodnje ne znači samo praćenje
                        proizvoda i potrebnih sirovina, nego i planiranje rasporeda proizvodnih procesa.
                        Poduzeća rasporede proizvodnih procesa pripremaju na tri različita načina planiranja:
                        Prvi način planiranja uključuje izradu glavnog plana proizvodnje (engl. Master
                        Production Schedule, MPS) koji se temelji na analizi podataka o prodaji artikala za
                        protekla razdoblja, uzimajući u obzir i pretpostavke buduće potražnje. Kako se u
                        ovom slučaju gotovi artikli "guraju" u prodaju, takav se način zove planiranje
                        proizvodnje guranjem (engl. Push Production Planning).
                        5

                        Drugi način planiranja proizvodnje zahtijeva da se s proizvodnjom započne kada se
                        dobije odgovarajući "signal" s tržišta. Signali su zapravo zahtjevi potencijalnih
                        kupaca. Kao naziv za ovaj se način proizvodnje često koristi japanska riječ kanban.
                        Kada pristigne zahtjev kupca, odnosno kada se pojavi potreba za određenom
                        komponentom proizvoda kao posljedica potražnje za proizvodom u koji se ta
                        komponenta ugrađuje, tek tada se pokreće proces njegove proizvodnje. Budući da
                        se proizvodnja pokreće na poticaj tržišta, ovakav se proces planiranja naziva
                        planiranjem proizvodnje povlačenjem (engl. Pull Production Planning).
                        Treći način planiranja predstavlja kombinaciju prethodnih dvaju načina planiranja
                        proizvodnje. Sjedne strane, izrađuje se glavni plan proizvodnje, ali se on može
                        prilagoditi, odnosno promijeniti zahvaljujući "kanban signalima" kojima se iskazuju
                        potrebe kupaca s druge strane. Ovaj je način upravljanja proizvodnjom najsloženiji i
                        zahtijeva korištenje vrlo kompleksnih informatičkih rješenja.  """,
    MODULI[IPS[2]][2] : """ Svako poduzeće koje teži rastu i razvoju mora ulagati znatne napore i sredstva u
                        kontrolu kvalitete postojećih i razvoj novih proizvoda. Na taj način ne samo da će
                        nastojati zadržati svoju tržišnu poziciju, nego će je i unaprijediti, osvajati nova tržišta,
                        pridobivati nove kupce te stvarati konkurentsku prednost. U suvremenim uvjetima
                        poslovanja takvu poslovnu filozofiju trebala bi prihvatiti i podržavati sva poduzeća jer će
                        u protivnome, zbog globalizacije i jačanja konkurencije, biti ugrožen i sam njihov
                        opstanak.  """,

    MODULI[IPS[3]][0] : """ Modul upravljanja narudžbama u prodaji informatički ne podržava isključivo čin
                        kupoprodaje, nego se sastoji od niza aplikacija koje, svaka na svoj način, pridonose što
                        kvalitetnijoj obradi narudžbi klijenata.  """,
    MODULI[IPS[3]][1] : """ Izlazna logistika obuhvaća sve aktivnosti vezane uz isporuku, odnosno dostavu gotovih
                        proizvoda izravno iz proizvodnje ili iz skladišta gotovih proizvoda na adresu kupca ili na
                        drugu lokaciju na kojoj on želi preuzeti robu. Za razliku od ulazne logistike, kojom će se
                        najčešće baviti dobavljač ulaznih sirovina, materijala i ostalih potrošnih dobara, izlazna je
                        logistika najčešće zadatak prodavatelja. On može isporuku organizirati tako što će je
                        prepustiti nekom drugom specijaliziranom poduzeću (prijevozniku, špediteru) ili će pak
                        koristiti vlastite logističke resurse (sredstva i ljude).  """,
    MODULI[IPS[3]][2] : """ Suvremeni pristup prodaji zastupa stajalište prema kojemu odnosi prodajne službe s
                        kupcem ne bi smjeli prestati samim kupoprodajnim činom. Upravo suprotno, te odnose
                        treba vremenski neograničeno dugo njegovati i unapređivati jer je to pravi put prema
                        zadržavanju i stvaranju lojalnih (privrženih) kupaca koji će i dalje nešto kupovati od
                        odnosnog poduzeća. Jedan od načina održavanja dobrih odnosa s klijentima, odnosno
                        kupcima jest pružanje poslijeprodajnih usluga, kada prodavatelj nudi određene usluge
                        nakon prodaje koje kupac može smatrati korisnima i za koje vjeruje da dodaju vrijednost
                        kupljenoj robi.
                        Među najvažnije tipove poslije prodajnih usluga mogu se uvrstiti:
                        usluge rješavanja reklamacija kupaca na isporučenu robu,
                        usluge otklanjanja nedostataka i popravaka kupljene robe u jamstvenom roku,
                        usluge redovitog održavanja i popravaka kupljenih proizvoda,
                        usluge nadogradnje i proširenja funkcionalnosti kupljenih proizvoda (Industry 4.0).  """,
    MODULI[IPS[3]][3] : """ Ovaj modul valja smatrati komplementom prethodnog modula IPS-a prodaje i izlazne
                        logistike. Riječ je, doduše, također o uslugama koje poduzeće pruža svojim klijentima, ali
                        ovoga puta o jednoj specifičnoj vrsti usluga - onih intelektualnih. Osnovna razlika
                        između "klasičnih" poslijeprodajnih usluga i intelektualnih usluga ogleda se u tome što
                        se u slučaju poslijeprodajnih usluga, koje su izvrsnoga tipa, očekuju egzaktno mjerljivi
                        učinci u razmjerno kratkom vremenu nakon što je takva usluga pružena (primjerice, ako
                        je kupac reklamirao kupljeni proizvod zbog oštećenja, on očekuje da mu se reklamacija
                        riješi u roku od nekoliko dana, tj. da mu se oštećeni proizvod popravi ili zamijeni drugim,
                        ispravnim), dok su učinci intelektualnih usluga (primjerice, bolja informiranost,
                        povećanje znanja, vještina i kompetencija, bolje snalaženje u nepoznatim situacijama,
                        brze reagiranje na neočekivane događaje itd.) daleko teže mjerljivi, nastupaju s
                        određenom vremenskom odgodom, a mogu čak i izostati bez krivnje pružatelja usluga.  """,
    MODULI[IPS[3]][4] : """ Uz uobičajene marketinške aktivnosti poput promidžbe i oglašavanja, potencijalne i
                        postojeće klijente poduzeća trebat će nerijetko poticati i nekim suptilnijim mjerama,
                        zasnovanima na osobnom obraćanju i personalizaciji. To će obično biti nuđenje nekih
                        dodatnih pogodnosti prilikom kupnje, poput popusta, poklona, nagradnih igara itd.
                        S druge strane, suvremeni strateški menadžment kao bolju alternativu bespoštednoj
                        konkurentskoj borbi vidi u strateškim dogovorima i savezima koje kompanije sklapaju s
                        komplementarnim, ali i konkurentskim kompanijama i drugim organizacijama. Takav
                        pristup omogućuje razvoj i primjenu sve sofisticiranijih oblika prodaje od kojih se,
                        dakako, očekuje poboljšanje poslovnih rezultata. Pri realizaciji takvih inicijativa i planova
                        suvremena informatička tehnologija može imati neprocjenjivo veliku ulogu i važnost primjerice, uvođenjem koncepta elektroničkog poslovanja, koji uključuje i neke potpuno
                        nove oblike elektroničke prodaje, poput suradničke ( engl. affiliate) prodaje, obrnutih
                        aukcija, agregacije ponuda različitih poduzeća itd.  """,

    MODULI[IPS[4]][0] : """ Modul glavne knjige osnovni je modul IPS-a računovodstva i upravljanja financijama u
                        kojemu se sažimaju sve detaljne informacije o svakom segmentu poslovanja poduzeća.
                        Glavna knjiga je sustavna, sveobuhvatna, zbirna i kronološki organizirana evidencija
                        poslovnih događaja nastalih u cjelokupnom poduzeću, pa se očekuje da rezultat njegova
                        djelovanja budu zbirne informacije o stanju i kretanju imovine, obveza, kapitala, prihoda,
                        rashoda i financijskog rezultata poduzeća.  """,
    MODULI[IPS[4]][1] : """ Skupina modula analitičkog knjigovodstva i ostalih pomoćnih knjiga.  """,
    PODMODULI[MODULI[IPS[4]][1]][0] : """ U ovaj modul "slijevat" će se informacije iz informacijskog podsustava upravljanja
                                    trajnom poslovnom imovinom. Procesi poslovanja s trajnom (neki autori nazivaju je i
                                    dugotrajnom) poslovnom imovinom određuju način funkcioniranja ovog modula, što
                                    znači da će se njime evidentirati procesi nabave, korištenja i otuđenja trajne poslovne
                                    imovine.  """,
    PODMODULI[MODULI[IPS[4]][1]][1] : """ Iz vremena kada su se računovodstveni poslovi obavljali ručno preuzet je naziv ovoga
                                    modula, tako da se u praksi on još uvijek često spominje pod nazivom materijalno
                                    knjigovodstvo. Zalihe sirovina i materijala pripadaju skupini kratkotrajne imovine,
                                    odnosno potrošnih dobara pa će između ovog modula poslovnog informacijskog
                                    sustava poduzeća i njegova modula nabave i ulazne logistike postojati vrlo tijesne
                                    dvosmjerne informacijske veze.  """,
    PODMODULI[MODULI[IPS[4]][1]][2] : """ Modul obračuna plaća djelatnika usko je povezan s IPS-om upravljanja ljudskim
                                    resursima. U IPS-u upravljanja ljudskim resursima generirat će se pravila obračuna plaća
                                    i ostalih naknada za rad (primjerice, utvrđivanje odnosa fiksnog i varijabilnog dijela plaća,
                                    bonusa, oblika i načina stimulacije za dobro obavljen ili penalizacije za loše obavljen
                                    posao, ostalih naknada itd.), dok će se u modulu obračuna plaća djelatnika ta pravila
                                    operativno primjenjivati onom vremenskom dinamikom kojom se određeni oblici zarade
                                    djelatnika trebaju isplaćivati (tjedno, mjesečno, tromjesečno itd.). Obračunate će se
                                    isplate evidentirati kao troškovi plaća.  """,
    PODMODULI[MODULI[IPS[4]][1]][3] : """ U procesu proizvodnje troše se sirovine i materijali. No, u cijenu određenog proizvoda
                                    ulaze i drugi resursi pa je u okviru informacijskog podsustava računovodstva i upravljanja
                                    financijama potrebno ustrojiti i modul računovodstvenog praćenja proizvodnje i zaliha
                                    gotovih proizvoda kako bi se na jednom mjestu prikupili podaci o svim troškovima koji
                                    ulaze u cijenu proizvodnje. Nadalje, nakon završetka procesa proizvodnje poduzeće će
                                    raspolagati izvjesnom količinom gotovih proizvoda spremnih za plasman na tržištu.
                                    Informacije o troškovima sadržanima u gotovim proizvodima mogu se također osigurati
                                    primjenom ovog modula.  """,
    PODMODULI[MODULI[IPS[4]][1]][4] : """ Važan dio računovodstvenog sustava za poduzeća čija je primarna djelatnost
                                    kupoprodaja trgovačke robe jest praćenje zaliha trgovačke robe. Valja računovodstveno
                                    pratiti poslovne procese nabave i prodaje, odnosno učinke ulaganja i rezultate procesa
                                    prodaje, jer se zalihe robe u roku kraćem od jednog poslovnog ciklusa transformiraju u
                                    novac kojim poduzeće može raspolagati po volji i prema potrebama poslovanja.  """,

    MODULI[IPS[5]][0] : """ Ovaj je modul rezultat primjene jednog razmjerno novog pristupa upravljanju ljudskim
                        resursima koji zahtijeva ne samo poklanjanje podjednake pozornosti svakom zaposleniku
                        nego otkrivanje posebno nadarenih djelatnika kojima će se nastojati pružiti prilika da te
                        svoje posebne sposobnosti i realiziraju, na dobrobit njih samih ali i cjelokupne
                        organizacije (poduzeća) u kojoj djeluju. Takav pristup upravljanje ljudskim resursima
                        pretvara iz podržavajuće, drugorazredne, u stratešku, prvorazrednu poslovnu funkciju,
                        jer otvara prostor za zapošljavanje i stvaranje najkompetentnijih stručnjaka što će se u
                        konačnici na tržištu odraziti kao konkurentska prednost poduzeća.  """,
    MODULI[IPS[5]][1] : """ Upravljanje radnim i poslovnim procesima u kojima, na ovaj ili onaj način, manje ili više
                        intenzivno sudjeluju ljudi u okviru ovoga modula IPS-a upravljanja ljudskim resursima.  """,

    MODULI[IPS[6]][0] : """ Ovaj modul informacijski podržava sve procese vezane uz korištenje, upravljanje i
                        održavanje trajnih poslovnih dobara poduzeća. Struktura ovog modula varirat će od
                        poduzeća do poduzeća ovisno o njegovoj veličini, brojnosti, prirodi i raznovrsnosti
                        korištenih trajnih poslovnih dobara, njihovu vijeku trajanja (dužini životnog ciklusa),
                        složenosti operacija održavanja i popravaka te o mnogim drugim čimbenicima.  """,
    MODULI[IPS[6]][1] : """ Upravljanje portfeljem trajne poslovne imovine zahtijeva stalnu procjenu i provjeru
                        vrijednosti elemenata trajne poslovne imovine jer ona iz mnogo razloga varira: mijenjaju
                        se tržišne cijene, unapređuje se tehnologija, imovina "stari" i gubi na vrijednosti, u
                        poduzeću se događaju promjene koje utječu na važnost ili irelevantnost posjedovanja
                        određenih vrsta trajne poslovne imovine, s vremenom se mijenja i poslovna strategija
                        poduzeća itd.
                        Situaciju još i vise komplicira činjenica da su neka trajna dobra u suvlasništvu
                        promatranog poduzeća i njegovih poslovnih partnera, a gdjekad i nekih trećih strana
                        (poduzeća ili pojedinaca). Upravljanje portfeljem trajne poslovne imovine iz svih
                        navedenih razloga zahtjeva stalnu modifikaciju i prilagodbe promjenjivim uvjetima
                        poslovanja.  """,
    MODULI[IPS[6]][2] : """ Zbog velike vrijednosti TPI postupak njena pribavljanja obično je mnogo složeniji od,
                        primjerice, nabave materijala i sirovina. Osim toga, pri pribavljanju ove vrste dobara, uz
                        uobičajenu kupnju i preuzimanje u trajno vlasništvo, javljaju se i neke druge mogućnosti
                        kao što su najam, zakup, leasing, koncesije, dugotrajna posudba uz odgovarajuću
                        naknadu itd.
                        Prestanak korištenja ili deaktiviranje TPI također ima određenih specifičnosti. I ovdje se
                        poduzeću otvara veći broj mogućnosti - od prodaje u slučaju da su neka trajna dobra još
                        upotrebljiva pa ima za njih zainteresiranih kupaca, preko iznajmljivanja i ustupanja na
                        korištenje do jednostavnog odbacivanja ili uništavanja imovine (primjerice, uredske
                        opreme, računala itd.) koja je "dala svoje".  """,

#######################################
    APLIKACIJE[MODULI[IPS[0]][0]][0] : """ Ovom će se aplikacijom provjeravati i analizirati je li se poduzeće u svojemu dosadašnjem
                                    radu pridržavalo i u kojoj mjeri pravne regulative i relevantnih standarda struke.
                                    Utvrdi li se da je bilo odstupanja, u strateške planove poslovanja nastojat će se
                                    ugraditi mehanizmi i postupci kojima će se nastojati osigurati da takvih odstupanja u
                                    budućnosti ne bude, odnosno da ih bude što manje.  """,
    APLIKACIJE[MODULI[IPS[0]][0]][1] : """ Svrha je ove aplikacije stvaranje informacijske osnove
                                    za opće (generalno) strateško planiranje poslovanja i njegova razvoja u budućem
                                    dugoročnom razdoblju. Informacije će se odnositi na sve važne čimbenike utjecaja
                                    na poslovanje, kao što su tržišna kretanja, financijski tokovi, tehnološki razvoj,
                                    politička situacija, potrebe u stručnom ljudskom potencijalu, predvidive promjene u
                                    zakonskoj regulativi, razvoj stručnih standarda itd. Potrebno je koristiti suvremene
                                    metode i softverske alate, poput poslovne inteligencije, uravnoteženih usporednih
                                    tablica i elektroničkih kontrolnih ploča.  """,
    APLIKACIJE[MODULI[IPS[0]][0]][2] : """ Informacije potrebne za razvoj strateškog
                                    financijskog plana se trebaju odnositi na izvore financiranja poslovanja, na
                                    predvidive troškove i prihode poslovanja te na financijske politike koje će se koristiti
                                    za kontrolu i upravljanje financijskim tokovima.  """,
    APLIKACIJE[MODULI[IPS[0]][0]][3] : """ nužna su ulaganja (investicije) u
                                    materijalnu i nematerijalnu imovinu poduzeća. Takva će se ulaganja financirati, s
                                    jedne strane, izdvajanjem (a ne raspodjelom) određenog dijela ostvarene dobiti
                                    poduzeća, te s druge strane, pribavljanjem financijskih sredstava iz tuđih izvora
                                    (zaduživanje). Aplikacija planiranja unutarnjih ulaganja poslužit će financijskom i
                                    vrhovnom menadžmentu pri utvrđivanju mogućnosti financiranja unutarnjih
                                    investicija iz vlastitih izvora (izdvojene dobiti u prethodnom razdoblju) i
                                    zaduživanjem (uzimanjem kredita). Isto tako, poslužit će i za utvrđivanje omjera tih
                                    dvaju načina financiranja unutarnjih ulaganja te za određivanje politike raspodjele
                                    raspoloživih sredstava po pojedinim investicijskim projektima.  """,
    APLIKACIJE[MODULI[IPS[0]][0]][4] : """ Poduzeća koja dobro posluju ostvarivat
                                    će profite, odnosno takve prihode koji nadmašuju njihove trenutačne potrebe u
                                    financijskim sredstvima za pokriće svih troškova poslovanja i njegova razvoja.
                                    Elementarna ekonomska logika nalaže da takva "slobodna" financijska sredstva
                                    (kapital) treba plasirati drugim zainteresiranim poduzećima na financijskim tržištima
                                    ili ih investirati u tuđe projekte te ih tako oplođivati. Aplikacija planiranja vanjskih
                                    ulaganja ima za cilj stvoriti informacijsku podlogu koja će vrhovnom menadžmentu
                                    poduzeća poslužiti za utvrđivanje strategije i mogućih politika plasmana
                                    raspoloživih financijskih sredstava kako bi ona na duži rok donijela poduzeću što
                                    veću zaradu.  """,

    APLIKACIJE[MODULI[IPS[0]][1]][0] : """ Oslanja se na procjene stanja i razvoja
                                    poslovanja poduzeća u budućnosti kako bi se utvrdio broj eventualno potrebnih
                                    novih radnih mjesta te odredila kvalifikacijska struktura ljudi koji će biti zaposleni na
                                    tim radnim mjestima. Također treba obuhvatiti i planove obrazovanja zaposlenika u
                                    budućnosti radi usvajanja novih tehnoloških, organizacijskih, poslovnih i drugih
                                    znanja te njihove moguće prekvalifikacije.  """,
    APLIKACIJE[MODULI[IPS[0]][1]][1] : """ Temelji se na analizi postojećih troškova rada (plaće,
                                    naknade, porezi, doprinosi, stimulacije itd.) te procjeni kretanja tih troškova u
                                    budućnosti i utvrđenim planovima zapošljavanja, obrazovanja i prekvalifikacije
                                    zaposlenika. Trendovi: tendencija povećanja pokretljivosti (mobilnosti) zaposlenika i
                                    tendencija sve intenzivnije primjene koncepta rada na daljinu. Pri planiranju troškova
                                    rada valja što točnije procijeniti kakav će u konkretnom slučaju biti utjecaj tih dvaju
                                    suprotstavljenih tendencija i u skladu s tim procjenama izvesti zaključke o mogućem
                                    rastu ili padu troškova rada u budućem planskom razdoblju.  """,
    APLIKACIJE[MODULI[IPS[0]][1]][2] : """ Odnosi se na tipične radne procese upravljanja ljudskim resursima kao što su
                                    evidencija zaposlenika, obračun plaća, upravljanje vremenom i utvrđivanje
                                    stimulacija. No, ova se aplikacija treba proširiti i na analitiku i mjerenje učinkovitosti
                                    organizacijske strukture poduzeća, radnih odnosa te obilježja poslova i zadataka
                                    zaposlenika.  """,
    APLIKACIJE[MODULI[IPS[0]][1]][3] : """ Riječ je o jednom razmjerno novom
                                    pristupu upravljanju ljudskim potencijalima poduzeća koji zahtjeva poklanjanje
                                    posebne pozornosti i vođenje posebne brige o izrazito (natprosječno) nadarenim,
                                    kompetentnim i kreativnim stručnjacima koji već jesu zaposleni u poduzeću ili ih se
                                    nastoji privući i zaposliti, s odgovorima na pitanja: Što su ključna obilježja talenata u
                                    određenim područjima i kako ih prepoznati (identificirati)? Kako im omogućiti
                                    primjereno obrazovanje, odnosno usavršavanje te pratiti njihovo napredovanje?
                                    Kako mjeriti promjene u njihovoj radnoj učinkovitosti te kako ih dodatno stimulirati? """,

    APLIKACIJE[MODULI[IPS[0]][2]][0] : """ Prati sve operacije vezane uz
                                    nabavu dobara i usluga (primjerice, kolika je količina artikala nabavljenih prošloga
                                    mjeseca ili pak koliko je prigovora, odnosno reklamacija klijenata na kvalitetu
                                    pruženih usluga bilo prošlog tjedna). Svrha svega toga jest stvoriti detaljan uvid u
                                    poslovanje nabavne službe, olakšati planiranje nabavnih aktivnosti u budućem
                                    razdoblju i unaprijediti ih.  """,
    APLIKACIJE[MODULI[IPS[0]][2]][1] : """ U svrhu kontrole zaliha nabavljenih artikala primjenjuje se niz
                                    standardiziranih metoda koje analiziraju stvarno stanje zaliha prema količinskim i
                                    vrijednosnim kriterijima. Rezultati takvih analiza predočuju se menadžmentu
                                    poduzeća u obliku izvještaja koje i kakve su oni zahtijevali. S druge strane, analitika
                                    skladišnog poslovanja pomaže pri upravljanju poslovanjem jednog ili više skladišta,
                                    ovisno o tome koliko ih u poduzeću ima, dajući pregled nad troškovima, operacijama
                                    i eventualnim problemima u skladišnom poslovanju.  """,
    APLIKACIJE[MODULI[IPS[0]][2]][2] : """ Pruža različite informacije
                                    i izvještaje potrebne za primjereno upravljanje proizvodnjom dobara ili usluga.
                                    Analizirat će se troškovi proizvodnje, vrijeme potrebno za proizvodnju i/ili pružanje
                                    određenih usluga, utrošak materijala, utrošak energije, zastoji u proizvodnji i njihovi
                                    razlozi, količina škarta, broj nerealiziranih radnih naloga itd.  """,
    APLIKACIJE[MODULI[IPS[0]][2]][3] : """ Analitičkim se obradama
                                    podataka izvode ključni pokazatelji uspješnosti poslovanja (engl. Key Performance
                                    Indicators, KPI) značajni za područje transporta. Ocjenjuje se uspješnost
                                    izvršavanja poslovnih procesa u tom području (primjerice, vrijeme potrebno za
                                    dostavu materijala od lokacije dobavljača do lokacije skladišta promatranog
                                    poduzeća). Analizirat će se i neki daljnji čimbenici, poput troškova transporta,
                                    pogrešnih isporuka, utroška energije, strukture transportnog parka, iskorištenja
                                    kapaciteta vozila itd.  """,
    APLIKACIJE[MODULI[IPS[0]][2]][0] : """ Omogućuje prodajnom menadžmentu i
                                    osoblju razumijevanje aktualnog stanja prodaje proizvoda i usluga (pojedinačno, po
                                    skupinama proizvoda i usluga, po tržištima, prema geografskim lokacijama, prema
                                    kupcima itd.) i ukupne učinkovitosti prodajne službe. Moguće su i analize utjecaja
                                    prodaje na ekonomičnost i profitabilnost ukupnog poslovanja tvrtke te utvrđivanje
                                    potencijalnih pogrešaka, propusta i nedostataka u radu prodajne službe. Krajnji cilj
                                    analitike prodaje jest prepoznavanje važnih tržišnih trendova i stvaranje pretpostavki
                                    za proaktivno djelovanje poduzeća u području prodaje, usklađeno s uočenim
                                    trendovima.  """,
    APLIKACIJE[MODULI[IPS[0]][2]][1] : """ Ima za
                                    cilj otkriti kako se poduzeće stvarno ponaša u različitim situacijama u kojima se
                                    može naći prilikom pružanja usluga klijentima, bilo da je riječ o uslugama koje čine
                                    samu jezgru poslovanja poduzeća ili pak o uslugama koje prate prodaju materijalnih
                                    proizvoda (usluge prije, za vrijeme i nakon prodaje). Analitika usluga pružanih
                                    klijentima omogućuje menadžmentu poduzeća:
                                    utvrđivanje profitabilnosti usluga (troškovi i prihodi od usluga po pojedinim
                                    klijentima, organiziranje usluga, ugovaranje i samo pružanje usluga) radi
                                    otkrivanja profitno uspješnih i neprofitabilnih usluga pružanih klijentima,
                                    analizu zahtjeva klijenata za uslugama (koje vrste usluga, kada, gdje i pod kojim
                                    uvjetima klijenti traže,
                                    analizu jamstvenih (garantnih) uvjeta (za koliko i koje se proizvode pruža
                                    jamstvo, koliki su troškovi pružanja usluga, kakav je utjecaj pružanja jamčenih
                                    usluga na profitabilnost prodaje).  """,
    APLIKACIJE[MODULI[IPS[0]][2]][2] : """ Treba
                                    ostvariti dva glavna cilja: osigurati odgovarajuću razinu proizvedenih dobara i
                                    pruženih usluga, sjedne strane, te dati uvid u troškove osiguranja potrebne razine
                                    kvalitete proizvoda i usluga. Prvi će se cilj ostvariti evidencijom, praćenjem i
                                    analizom reklamacija klijenata, ispitivanjem zadovoljstva klijenata kupljenim
                                    proizvodima i uslugama i analizom načina ostvarivanja potrebne kvalitete proizvoda
                                    i usluga. Drugi cilj - stvaranje uvida u troškove nužne za ostvarivanje potrebne
                                    kvalitete proizvoda i usluga - ostvarit će se analizom izravnih (direktnih) i neizravnih
                                    (indirektnih) troškova ostvarivanja potrebne kvalitete. Među izravnim troškovima
                                    mogu se izdvojiti troškovi stvaranja proizvodnih i općih poslovnih uvjeta u kojima je
                                    moguće postići potrebnu razinu kvalitete proizvoda i usluga (nabava potrebne
                                    tehnologije, angažiranje kompetentnih stručnjaka, automatizacija proizvodnih
                                    procesa, informatizacija poslovnih procesa itd.), dok se među neizravnim
                                    troškovima ističu troškovi dobivanja odgovarajućih certifikata o kvaliteti, atesta,
                                    uporabnih dozvola i sl.  """,
    
    APLIKACIJE[MODULI[IPS[0]][3]][0] : """ Uključuje standardne analize potrebne svim korisnicima, od
                                    financijskog direktora do menadžera i asistenata na nižim razinama, odgovornih za
                                    ostvarivanje financijskih ciljeva i poboljšanje financijskog poslovanja poduzeća.
                                    Primjeri standardnih financijskih izvještaja koji se stvaraju jesu bilance, izvještaji o
                                    stanju imovine poduzeća, izvještaji o naplaćenim i nenaplaćenim potraživanjima,
                                    izvještaji o dugovanjima poduzeća te izvještaji o stanju zaliha. Ovi osnovni izvještaji
                                    mogu biti, prema potrebi, nadopunjeni vrlo detaljnim izvještajima kao što su,
                                    primjerice, struktura ostvarenih troškova prema vrstama, prema mjestima na kojima
                                    su oni nastali, prema proizvedenim proizvodima itd.  """,
    APLIKACIJE[MODULI[IPS[0]][3]][1] : """ Stvara analitičku osnovu za modeliranje različitih
                                    scenarija financijskog planiranja primjerenih različitim poslovnim situacijama u
                                    kojima bi se poduzeće moglo naći u budućnosti. Tako će se, primjerice, simulirati i
                                    modelirati eventualne fluktuacije tečajeva valuta da bi se razmotrilo kakvog utjecaja
                                    one mogu imati na troškove i prihode poduzeća. Razrada takvih scenarija poslužit
                                    će za stvaranje operativnih, vrlo konkretnih planova djelovanja u različitim više ili
                                    manje predvidivim poslovnim situacijama.  """,
    APLIKACIJE[MODULI[IPS[0]][3]][2] : """ Omogućuje
                                    višedimenzionalnu analizu profitabilnosti proizvoda i usluga, primjerice analizu
                                    profitabilnosti kupaca po prodajnim regijama. Pruža dubinski uvid u troškove, što
                                    vodi do boljeg razumijevanja profitabilnosti proizvoda i usluga. Povezuje planiranje
                                    profitabilnosti s drugim aplikacijama za planiranje.  """,
    APLIKACIJE[MODULI[IPS[0]][3]][3] : """ Omogućuje utvrđivanje ukupnih i pojedinačnih troškova po proizvodima i uslugama
                                    te razgraničenje troškova po fazama proizvodnog procesa. Na taj se način stvaraju,
                                    primjerice, pretpostavke za praćenje troškova po pojedinim narudžbama, dakle, na
                                    razini pojedinog poslovnog dokumenta, što je važno sa stajališta operativnog
                                    upravljanja poslovanjem.  """,
    APLIKACIJE[MODULI[IPS[0]][3]][4] : """ Omogućuje uvid u povijest odnosa s pojedinim klijentima kako bi se utvrdilo njihovo
                                    ponašanje pri plaćanju (primjerice, plaćaju li na vrijeme ili ne, traže li i kako često
                                    odgodu plaćanja, koje načine plaćanja koriste itd.). Takvim se uvidom stvara osnova
                                    za utvrđivanje budućih odnosa s klijentima poduzeća.  """,

    APLIKACIJE[MODULI[IPS[1]][0]][0] : """   """,
    APLIKACIJE[MODULI[IPS[1]][1]][0] : """   """,
    APLIKACIJE[MODULI[IPS[1]][2]][0] : """   """,
    APLIKACIJE[MODULI[IPS[1]][3]][0] : """   """,

    APLIKACIJE[MODULI[IPS[2]][0]][0] : """   """,
    APLIKACIJE[MODULI[IPS[2]][1]][0] : """   """,
    APLIKACIJE[MODULI[IPS[2]][2]][0] : """   """,

    APLIKACIJE[MODULI[IPS[3]][0]][0] : """   """,
    APLIKACIJE[MODULI[IPS[3]][1]][0] : """   """,
    APLIKACIJE[MODULI[IPS[3]][2]][0] : """   """,
    APLIKACIJE[MODULI[IPS[3]][3]][0] : """   """,
    APLIKACIJE[MODULI[IPS[3]][4]][0] : """   """,

    APLIKACIJE[MODULI[IPS[4]][0]][0] : """   """,
    APLIKACIJE[PODMODULI[MODULI[IPS[4]][1]][0]][0] : """   """,
    APLIKACIJE[PODMODULI[MODULI[IPS[4]][1]][1]][0] : """   """,
    APLIKACIJE[PODMODULI[MODULI[IPS[4]][1]][2]][0] : """   """,
    APLIKACIJE[PODMODULI[MODULI[IPS[4]][1]][3]][0] : """   """,
    APLIKACIJE[PODMODULI[MODULI[IPS[4]][1]][4]][0] : """   """,

    APLIKACIJE[MODULI[IPS[5]][0]][0] : """   """,
    APLIKACIJE[MODULI[IPS[5]][1]][0] : """   """,

    APLIKACIJE[MODULI[IPS[6]][0]][0] : """   """,
    APLIKACIJE[MODULI[IPS[6]][1]][0] : """   """,
    APLIKACIJE[MODULI[IPS[6]][2]][0] : """   """,
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
