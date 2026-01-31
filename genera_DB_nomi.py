import json
import random

# Cognomi italiani REALI (lista molto lunga, generica/non mirata)
cognomi = [
    "Rossi","Russo","Ferrari","Esposito","Bianchi","Romano","Colombo","Ricci","Marino","Greco",
    "Bruno","Gallo","Conti","De Luca","Mancini","Costa","Giordano","Rizzo","Lombardi","Moretti",
    "Barbieri","Fontana","Santoro","Mariani","Rinaldi","Caruso","Ferrara","Galli","Martini","Leone",
    "Longo","Gentile","Martinelli","Vitale","Lombardo","Serra","Coppola","De Santis","D'Angelo","Marchetti",
    "Parisi","Villa","Conte","Ferraro","Fabbri","Bianco","Marini","Grassi","Valentini","Messina",
    "Sala","De Angelis","Gatti","Pellegrini","Palumbo","Sorrentino","Battaglia","Orlando","Sanna","Ruggeri",
    "De Rosa","Mazza","Brambilla","Sartori","Farina","Caputo","Monti","Ferri","Cattaneo","Piras",
    "Piazza","Giuliani","Neri","Castelli","Landi","Santini","Silvestri","Benedetti","Carbone","D'Amico",
    "Fiore","Basile","Riva","Rizzi","Testa","Bellini","Corsi","Fiorentino","Pellegrino","Pagano",
    "Morelli","Montanari","Costantini","Amato","Bernardi","Rizzi","Fusco","Palmieri","Pozzi","Grimaldi",
    "Sartini","Neri","Vitali","Pinto","Rossetti","Lorusso","Berti","Tassi","Medici","Serafini",
    "Raimondi","Bonaventura","Alberti","De Simone","Lazzari","Rocca","Crisci","Mori","Schiavone","Migliore",
    "Torre","Carli","Guidi","Bertolini","Cavaliere","Graziani","Bianchini","Fiorini","Nicolini","Romagnoli",
    "Cappelli","Ferretti","Pellecchia","Cavalli","Ferrante","Prati","Perrone","Milani","Fiorillo","Reale",
    "Sabatini","Damiani","Puglisi","Mancuso","Lagana","Faraone","Barone","Carbone","Lo Monaco","Lo Russo",
    "Lo Presti","Di Pietro","Di Marco","Di Natale","Di Stefano","Di Fiore","Di Leo","Di Palma","Di Maio","Di Bella",
    "De Martino","De Lorenzo","De Marchi","De Filippo","De Pascalis","De Matteis","De Vita","De Carolis","De Falco","De Cesare",
    "Della Valle","Della Rovere","Della Porta","Del Vecchio","Del Prete","Del Bene","Dell'Orco","D'Elia","D'Errico","D'Onofrio",
    "Benvenuti","Cervi","Cecchini","Cecconi","Cecchi","Ceccarelli","Cecchetti","Bellucci","Bellini","Belloni",
    "Bettini","Betti","Bertini","Bertinelli","Bertoni","Bertoli","Bertolotti","Bertuccelli","Bertuccio","Bertorelli",
    "Vannini","Vannoni","Vannucci","Vianello","Viani","Vichi","Vichi","Viganò","Vigano","Viganotti",
    "Zanetti","Zanetti","Zani","Zanini","Zanoni","Zappa","Zappia","Zappi","Zecchini","Zerbi",
    "Zingaro","Zingari","Zocchi","Zorzi","Zotti","Zullo","Zucca","Zuccaro","Zucconi","Zucchi",
    "Agnelli","Alfieri","Altieri","Ambrosini","Anastasi","Anselmi","Antonucci","Armani","Arrighi","Arcuri",
    "Baldini","Baldi","Balestri","Ballerini","Ballarini","Balsamo","Bandini","Baraldi","Barbato","Barbosa",
    "Baresi","Barilli","Barone","Baroni","Baronti","Barozzi","Bartoli","Bartolini","Bastiani","Bastianelli",
    "Battistini","Battistoni","Bazzani","Bazzichi","Beccaria","Bechini","Beltrame","Beltrami","Benassi","Benati",
    "Benedetto","Benetti","Benini","Benvenuto","Beretta","Bergamaschi","Berger","Berlini","Bernasconi","Bersani",
    "Bertaglia","Bertazzoli","Bertelli","Bertocchi","Bertoldi","Bertolini","Bertone","Bettarini","Bevilacqua","Bezzi",
    "Bianchi","Bianconi","Bianchini","Biavati","Biondi","Bistolfi","Boccardi","Bocchini","Boeri","Boglietti",
    "Bollati","Bonacina","Bonaccorsi","Bonanni","Bonelli","Bonavita","Bonaventura","Bondi","Bonetti","Bongiorno",
    "Bonifazi","Bonini","Bonito","Bonomi","Bontempi","Bordoni","Borrelli","Borselli","Bortolotti","Boscarino",
    "Bosco","Bosio","Bosoni","Bottari","Botticelli","Bove","Bovio","Bracci","Braghin","Brambilla",
    "Branca","Brancati","Brandi","Brandimarte","Brunetti","Brunelli","Bruni","Brunini","Bruno","Bruschi",
    "Bua","Buccellato","Bucci","Bucchi","Bugiardini","Buglioni","Bulgherini","Bullo","Bulgari","Bulgarelli",
    "Buratti","Buratti","Buriani","Burigo","Buscemi","Busetto","Businaro","Busoni","Bussi","Buttò",
    "Cagnoni","Cairoli","Calabrese","Calabro","Calamandrei","Calandra","Calapai","Calati","Calcagni","Calderoni",
    "Callegari","Calligaris","Calogero","Calò","Calvani","Calvi","Calvino","Caminiti","Cammarata","Campagnoli",
    "Campana","Campanella","Campanini","Campi","Campisi","Cantalupo","Cantini","Cantisani","Capaldi","Capasso",
    "Capobianco","Caporale","Capra","Caprari","Caputo","Caracciolo","Caradonna","Caravaggio","Carboni","Cardelli",
    "Carelli","Carfagna","Carli","Carlini","Carmignani","Carnovali","Carone","Carpi","Carraro","Carrera",
    "Caruso","Casadei","Casadio","Casagrande","Casalini","Casati","Cascone","Caselli","Caserta","Casini",
    "Casiraghi","Cassani","Cassano","Cassese","Castagna","Castagnoli","Castaldi","Castellani","Castellini","Castelli",
    "Castiglioni","Catania","Catena","Cattani","Cattaneo","Cavagna","Cavagnaro","Cavalli","Cavallo","Cavallaro",
    "Cavicchioli","Cecchi","Cecconi","Celentano","Centrone","Cerbone","Cercignani","Ceriani","Cerri","Cerutti",
    "Cervantes","Cervelli","Cesari","Cesarini","Chiari","Chiarini","Chiesa","Chiesi","Chiodi","Chirico",
    "Ciacci","Ciampi","Cicala","Ciccarelli","Cicconi","Cingolani","Cipriani","Cirillo","Citro","Civita",
    "Clemente","Clementi","Cocchi","Cocco","Coccia","Cocchiara","Colaianni","Colangelo","Colantuono","Colasanti",
    "Colavita","Coletti","Colletti","Colli","Collina","Colonna","Colombo","Colonna","Colucci","Coluccio",
    "Comi","Conca","Conforti","Congiu","Conte","Contini","Coppola","Coppoli","Corallo","Corazzi",
    "Corbetta","Corbo","Corda","Cordaro","Cordova","Corelli","Corinaldi","Corio","Cornacchia","Coronati",
    "Corrao","Corsi","Corsini","Cortese","Corti","Corvino","Cosentino","Costa","Costanzo","Cotroneo",
    "Coviello","Crippa","Cristiani","Cristiano","Cristofori","Crivelli","Cucchi","Cucchiara","Cucinotta","Cugini",
    "Cuomo","Curcio","Curti","D'Agostino","D'Alessandro","D'Alessio","D'Amato","D'Andrea","D'Angelo","D'Antoni",
    "D'Antonio","D'Auria","D'Avino","D'Errico","D'Esposito","D'Introno","D'Orazio","D'Urso","Dal Bianco","Dal Bo",
    "Dal Corso","Dal Monte","Dalla Costa","Dalla Libera","Dalla Noce","Dalla Torre","De Angelis","De Angelis","De Bellis","De Blasi",
    "De Bonis","De Caro","De Carlo","De Cicco","De Francesco","De Gregorio","De Luca","De Marco","De Maria","De Martino",
    "De Matteis","De Paolis","De Rosa","De Santis","De Simone","De Stefano","De Vito","Del Bene","Del Bianco","Del Bono",
    "Del Carpio","Del Duca","Del Giudice","Del Monte","Del Prete","Del Re","Della Rocca","Della Valle","Di Bartolomeo","Di Battista",
    "Di Benedetto","Di Carlo","Di Chiara","Di Cola","Di Fazio","Di Francesco","Di Giacomo","Di Giovanni","Di Lorenzo","Di Martino",
    "Di Nardo","Di Paola","Di Pinto","Di Rocco","Di Santo","Di Serio","Di Stefano","Di Virgilio","Donati","Donnarumma",
    "Drago","Durante","Elia","Esposito","Fabbri","Fabbro","Fabiani","Fadini","Falaschi","Falcone",
    "Fancellu","Fanfani","Fantini","Farina","Farinelli","Faro","Fasano","Fasoli","Fattori","Favaro",
    "Fedele","Federici","Felici","Felicioli","Ferrante","Ferrari","Ferraro","Ferraris","Ferretti","Ferri",
    "Ferro","Fioravanti","Fiorentino","Fiorini","Fiore","Fiorelli","Fiorillo","Fiorucci","Fois","Fontana",
    "Fornaro","Forte","Forti","Foschi","Franceschi","Franceschini","Franchi","Franchini","Franco","Franzoni",
    "Ravelli","Montesanti","Bellaforte","De Rinaldi","Di Lattanzi","Fioralba","Castelvivo","Paganetti","Rocchitelli","Biancherini",
    "Serranova","Lunardi","Marangoni","Tassineri","Caprilesi","Vallegrandi","Borghesani","Riccardelli","Santamaria","Lombardini",
    "Gualtierotti","Pellegrinati","Farinaccio","Montalvani","Carbonei","Marchettini","Bottarelli","Calderini","Cavazzoni","Corradetti",
    "Giordanelli","Bernasetti","Ferrandini","Palmierini","Orlanducci","Rizzardi","Grassinelli","Vitarelli","Cattarin","Zanettoli",
    "Roccapiana","Dalmonti","Dellafiora","Dellaquercia","Delmonteri","Delrossi","Di Valdieri","Di Fontanile","De Casaroli","De Marchisio",
    "Bergantini","Bertocchini","Brunacci","Brunettiello","Campanari","Campanuzzo","Capobiancati","Caravelli","Carlassini","Carminati",
    "Casalunga","Casaletti","Castellaro","Castelluzzi","Castignani","Cavalluzzi","Ceccaroli","Cerasoni","Cervellati","Chiaromonte",
    "Chiodaroli","Cingolotti","Ciprianelli","Colombari","Contarini","Coppoloni","Corallini","Cordellini","Corsetti","Cortellini",
    "Costarelli","Cotronei","Crivellati","Cucuzzella","Curatelli","D'Argento","D'Aurilio","D'Intino","D'Olivieri","D'Amarco",
    "Dalferro","Dalmasso","Dallaquale","De Belloni","De Caprari","De Corsi","De Ferretti","De Lamberti","De Longhi","Delmarini",
    "Di Bernardi","Di Capraro","Di Ferranti","Di Gualtieri","Di Lombardo","Di Moretti","Donatelli","Durantini","Espositelli","Fabbriani",
    "Fabbrizzi","Farinazzi","Fasanotti","Fattorelli","Federotti","Feliciani","Ferrandino","Ferrattini","Ferrocchi","Fioraschi",
    "Fioravelli","Fiorellati","Fontanesi","Fortunati","Franchesi","Franzetti","Galdieri","Galluzzi","Garofalini","Gentileschi",
    "Giannotti","Giardinelli","Giornelli","Grisanti","Guidotti","Iannarelli","Lambertoni","Lanzarotti","Lattanzioli","Laurenzi",
    "Leonardiello","Lombardazzi","Longarelli","Lucarelli","Mancuselli","Manfredini","Maranghi","Marchettazzo","Marinelli","Martellini",
    "Massarelli","Mazzoleni","Mediciani","Melandri","Merluzzi","Messinelli","Molinariello","Montanesi","Montellini","Morellati",
    "Nardelli","Nerotti","Nicolazzi","Orlandesi","Palmarelli","Pavanelli","Pellegrinetti","Perronelli","Pianetti","Pirozzoli",
    "Raimondini","Raspanti","Ravagnani","Riccardini","Rinaldazzi","Rocchiani","Romanelli","Romagnotti","Rossanelli","Ruggeretti",
    "Sabatelli","Sannetti","Santorelli","Sartorazzi","Serafinetti","Serranelli","Sorrentelli","Tarantelli","Tassonelli","Valentazzi",
    "Vannarelli","Verdolini","Vitaliello","Zanardelli","Zuccarelli","Zanettini","Zorzetti","Zopparelli","Zingarelli","Zanforlin",
    "Almirante","Rauti","Romualdi","Graziani","Fini","La Russa","Pino Rauti", "Meloni", "Bocchino", "Sechi", "Bellucci", "Almici", "Ambrosi",
    "Bignami", "Antoniozzi", "Mussolini", "Caiata", "Ciocchetti", "Colosimo", "De Corato", "Gemmato", "Lancellotta", "Lollobrigida",
    "Kowalski", "Nowak", "Wojcik", "Kaczmarek", "Mazur",
    "Novak", "Horvat", "Popescu", "Ionescu", "Georgescu",
    "Petrov", "Ivanov", "Dimitrov", "Stoianov", "Markovic",
    "Jovanovic", "Kovacevic", "Horvath", "Nagy", "Toth",
    "AlHassan", "AlMansur", "AlFarouk", "AlSabah", "AlKarim",
    "Haddad", "Khalil", "Hamdan", "Rahman", "Salem",
    "Nasser", "Youssef", "Abdallah", "Mahmoud", "Karim",
    "Sharif", "Suleiman", "Zayed", "Bashir", "Omar"
]

nomi = [
    "Luca","Marco","Matteo","Andrea","Francesco","Alessandro","Davide","Simone","Federico","Gabriele",
    "Riccardo","Stefano","Antonio","Giuseppe","Roberto","Paolo","Giovanni","Daniele","Christian","Lorenzo",
    "Emanuele","Nicolo","Tommaso","Samuele","Elia","Edoardo","Giacomo","Filippo","Michele","Claudio",
    "Massimo","Giorgio","Salvatore","Vincenzo","Enrico","Fabio","Sergio","Domenico","Raffaele","Bruno",
    "Angelo","Pietro","Alberto","Giulio","Leonardo","Cristiano","Valerio","Maurizio","Mirko","Damiano",
    "Carmine","Luigi","Cesare","Diego","Ignazio","Manuel","Kevin","Yuri","Omar","Karim",
    "Adam","Noah","Elias","Ismael","Youssef","Karol","Marek","Ivan","Lukas","Andrej",
    "Giulia","Chiara","Francesca","Martina","Alessia","Sara","Valentina","Elisa","Anna","Federica",
    "Silvia","Claudia","Laura","Elena","Marta","Giorgia","Ilaria","Arianna","Beatrice","Camilla",
    "Aurora","Greta","Noemi","Sofia","Alice","Veronica","Serena","Gloria","Irene","Caterina",
    "Carlotta","Gaia","Viola","Ludovica","Rebecca","Miriam","Nadia","Cristina","Angela","Monica",
    "Daniela","Patrizia","Simona","Barbara","Rita","Teresa","Lucia","Paola","Marianna","Vanessa",
    "Yasmine","Fatima","Amina","Samira","Layla","Mariam","Nour","Karima","Anastasia","Katarina",
    "Olga","Natalia","Irina","Milena","Daria","Svetlana","Tatiana","Zuzana","Kinga","Mirela",
    "Alessandro","Mattia","Ettore","Achille","Leone","Jacopo","Ruggero","Sebastiano","Gianluca","Pierluigi",
    "Pierpaolo","Gianmarco","Giancarlo","Gianni","Umberto","Aldo","Tiziano","Corrado","Emiliano","Saverio",
    "Marcello","Orlando","Renato","Flavio","Cosimo","Gennaro","Gaetano","Pasquale","Alfonso","Ciro",
    "Salvo","Tancredi","Ottavio","Adriano","Loris","Dario","Nicolò","Enzo","Rodolfo","Tobia",
    "Bianca","Angelica","Margherita","Costanza","Ginevra","Eleonora","Matilde","Vittoria","Nicole","Melissa",
    "Asia","Debora","Dalila","Rossella","Sabrina","Adele","Emma","Isabella","Viola","Benedetta",
    "Annalisa","Alina","Maddalena","Cecilia","Livia","Agata","Rachele","Letizia","Sveva","Noa",
    "Milos", "Radek", "Tomasz", "Pawel", "Krzysztof","Nadia", "Farah", "Iman", "Lina", "Maha",
    "Bogdan", "Viktor", "Mihail", "Andrei", "Sergei","Aleksandr", "Denis", "Oleg", "Vladislav", "Stanislav",
    "Katarzyna", "Magdalena", "Agnieszka", "Ewa", "Monika","Elzbieta", "Aneta", "Iwona", "Ludmila", "Alena",
    "Irina", "Natalya", "Oksana", "Yelena", "Milica","Ahmed", "Mohamed", "Mustafa", "Hassan", "Hussein",
    "Ali", "Ibrahim", "Tariq", "Bilal", "Adel","Rashid", "Khaled", "Samir", "Faisal", "Hamza",
    "Aisha", "Khadija", "Salma", "Rania", "Zahra","Huda", "Amal", "Sahar", "Dina", "Leila"
]

    # Keyword per nickname (ideologiche, storiche, tecniche)
keywords = [
    # Animali
    "fenicottero", "tasso", "falco", "riccio", "gabbiano",
    "pinguino", "orso", "lupo", "lontra", "gufo",
    "cormorano", "scoiattolo", "ghepardo", "colibri", "istrice",
    # Sport / movimento
    "rugby", "maratoneta", "portierone", "velocista", "skipper",
    "judoka", "ciclista", "surfista", "pilota", "scalatore",
    "canottiere", "arcere", "pattinatore", "sprinter", "nuotatore",
    # Mestieri / ruoli
    "cuoco", "fabbro", "viaggiatore", "cartografo", "narratore",
    "giardiniere", "artigiano", "bibliotecario", "meccanico", "astronomo",
    "esploratore", "costruttore", "programmatore", "archivista", "fotografo",
    # Natura
    "tempesta", "brezza", "fulmine", "quercia", "tundra",
    "vulcano", "oceano", "deserto", "nebbia", "radice",
    "valanga", "meteora", "tramonto", "aurora", "monsonico",
    # Cibo
    "lasagna", "cannolo", "peperoncino", "basilico", "mirtillo",
    "caramello", "zenzero", "nocciola", "panzerotto", "focaccia",
    "mozzarella", "tiramisu", "raviolo", "cioccolato", "mandorla",
    # Oggetti / cose
    "martello", "lanterna", "orologio", "compasso", "binario",
    "zaino", "cuscino", "aquilone", "ingranaggio", "mattoncino",
    "ombrello", "tastiera", "satellite", "lampadina", "cavatappi",
    # Aggettivi / ironici
    "instancabile", "silenzioso", "ribelle", "nomade", "curioso",
    "misterioso", "sgusciante", "testardo", "galattico", "lunatico",
    "sbadato", "tenace", "bradipo", "dinamico", "eccentrico", 
    "dux", "legio", "ardito", "fante", "scudo", "torre", "marcia", "piave", "decima", 
    "italo", "tricolore", "fiamma", "memento", "vincere", "aquila", "daga", "balilla",
    "manipolo", "camicia", "littore", "avanguardia", "centurione", "falange"
    ]



def generate_mega_database(target_size=9000, nomi_base=nomi, cognomi=cognomi, keywords = keywords):
    # Liste espanse per massimizzare le combinazioni
    prefissi_nomi = ["Gian", "Pier", "Carlo", "Vittorio", "Italo"]
    suffissi_nomi = ["maria", "luigi", "antonio", "francesco", "alberto", "manuele"]
    
    db = {}
    
    while len(db) < target_size:
        # Genera un nome composto o singolo
        if random.random() > 0.9:
            nome = random.choice(prefissi_nomi) + random.choice(suffissi_nomi)
        else:
            nome = random.choice(nomi_base)
            
        cognome = random.choice(cognomi)
        # Aggiunta di un secondo cognome occasionale per realismo politico/nobiliare
        if random.random() > 0.99:
            cognome += f" {random.choice(cognomi)}"
            
        full_name = f"{nome} {cognome}"
        
        if full_name not in db:
            # Creazione di 8-12 nickname unici per ogni nome
            nick_list = set()
            while len(nick_list) < 8:
                pattern = random.choice([
                    lambda: f"{nome[0].lower()}{cognome.replace(' ', '').lower()}{random.randint(10, 99)}",
                    lambda: f"{random.choice(keywords)}{random.randint(2, 16)}",
                    lambda: f"{cognome.replace(' ', '').lower()}{random.choice(list(["","","",".",".",".",".","_","X","x","zZz"]))}{nome.replace(' ', '').lower()}",
                    lambda: f"{nome.replace(' ', '').lower()}{random.choice(list(["","","",".",".",".",".","_","X","x","zZz"]))}{cognome.replace(' ', '').lower()}",
                    lambda: f"{cognome.replace(' ', '').lower()}{random.choice(list(["","","",".",".",".",".","_","X","x","zZz"]))}{random.choice(keywords)}",
                    lambda: f"{nome.replace(' ', '').lower()}{random.choice(list(["",".","_","X","x"]))}{random.choice(keywords)}",
                    lambda: f"{nome.replace(' ', '').lower()[:3]}{cognome.replace(' ', '').lower()[:3]}{random.randint(0, 9)}",
                    lambda: f"{nome.replace(' ', '').lower()[:5]}_{cognome.replace(' ', '').lower()[:5]}",
                    lambda: f"{nome.replace(' ', '').lower()[:3]}{random.choice(keywords)}{cognome.replace(' ', '').lower()[:3]}",
                    lambda: f"{random.choice(keywords)}.{nome.replace(' ', '').lower()}{random.choice(list(["",str(random.randint(7,15))]))}",
                    lambda: f"{random.choice(list(["","_",str(random.randint(8,15)) + "_"]))}{nome.replace(' ', '').lower()}{random.choice(list(["","_","_"+str(random.randint(8,15))]))}",
                    lambda: f"{cognome.replace(' ', '').lower()}{nome[0].lower()}",
                ])
                nick_list.add(pattern())
            
            db[full_name] = list(nick_list)
                
    return db

# Genera un database di 5000 voci (puoi aumentare il numero)
database_immenso = generate_mega_database(5000)

with open('database_nomi.json', 'w', encoding='utf-8') as f:
    json.dump(database_immenso, f, indent=4, ensure_ascii=False)