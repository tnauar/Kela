class RandomData():

    """This class contains the data from which the random data is generated.
    """

    VISIT_PORTAL_DIGITAL = [
        "OmaKela", "Kela.fi"
    ]

    VISIT_PORTAL_PERSONAL = [
        "Puhelinpalvelu", "Puhelinajanvaraus", "Palvelupiste"
    ]    

    SERVICE_EVENT = [
        "selvityspyyntö", "tietojen tarkistaminen", "hakemuksen lähettäminen", "liitteiden toimittaminen"
    ]

    BEHAVIOUR = [
        "kohteliasta", "epäkohteliasta", "epävarmaa", "arvostelevaa"        
    ]

    ATTITUDE = [
        "ylimielinen", "lannistava", "rakentava", "väheksyvä", "ystävällinen", "mukava", "kyllästynyt"
    ]

    FUNCTIONALITY = [
        "sujuva", "tahmea", "hidas", "nopea", "epäselvä",
        "monimutkainen", "työläs"
    ]

    """From these templates the free text fields are generated.
    """

    TEMPLATES_SERVICE_EVAL = [
        "{portal_per}-asiointi oli {func}, kun hoidettiin vaihetta: {event}.",
        "{portal_per}-palvelun käyttö oli {func}. Erityisesti kohdassa: {event}.",
        "Kokonaiskokemus oli {att}, ja kohtelu vaikutti olevan {beh}.",
        "Asiakaskohtaaminen oli {beh} ja yleinen asenne oli {att}.",
        "Palvelun sävy oli {att}, mikä teki kokemuksesta {beh}.",
        "Neuvonta oli {beh}, vaikka kyseessä oli {event}.",
        "Asiointi koettiin olevan {beh}, ja palvelun toimintalogiikka oli {func}.",
        "Palvelu oli {att}, kun asiakkaan kanssa käytiin läpi vaihetta: {event}.",
        "{portal_per}-asiointi oli {func}, mutta vuorovaikutus oli {beh}.",
        "Prosessi oli {func} ja työntekijän asenne vaikutti olevan {att}.",
        "Kokemus oli kokonaisuutena {beh}, koska palvelun toteutus oli {func}.",
        "{portal_per}-palvelu oli {func}, kohtaaminen tuntui olevan {beh}.",
        "Asiointitilanteessa asenne oli {att} ja viestintä koettiin olevan {beh}.",
        "Palvelu oli {beh}, kun pyydettiin apua vaiheeseen: {event}.",
        "Käyttökokemus oli {func}, ja palvelun sävy oli {att}.",
        "{portal_per} asiointi oli {func}; kokonaisvaikutelma jäi {att}.",
        "Asiointikokonaisuus oli {beh}, erityisesti palvelutapahtumassa: {event}.",
    ]

    TEMPLATES_DIGITAL_CHANNEL_EVAL = [
        "Sähköinen palvelukanava ({portal_dig}) oli {func} käyttää.",
        "Nettisivun käyttö oli {func}, kun yritin hoitaa kohtaa: {event}.",
        "Järjestelmän käyttöliittymä oli {func} koko asioinnin ajan.",
        "Palvelukanavan rakenne oli {func}, erityisesti vaiheessa: {event}.",
        "Verkkopalvelu vaikutti olevan {func}, mikä vaikeutti asian {event} hoitamista.",
        "Sähköinen asiointi oli {func}, ja tehtävän suorittaminen tuntui työläältä.",
        "{portal_dig} palvelun navigointi oli {func}, eikä tarvittavaa toimintoa löytynyt helposti.",
        "Asiointi verkkopalvelussa oli {func}, mutta lopulta vaihe {event} onnistui.",
        "Digipalvelun käyttökokemus oli {func} asiakkaan näkökulmasta.",
        "Palvelukanava oli {func}, ja ohjeistus jäi epäselväksi.",
        "Järjestelmän toiminta oli {func} etenkin ruuhka-aikana.",
        "Sähköinen palvelu oli {func}, mikä lisäsi asioinnin kuormittavuutta.",
        "Asiointijärjestelmä oli {func}, eikä käyttäjäpolku ollut selkeä.",
        "Palvelualusta vaikutti olevan {func}, mutta tieto löytyi lopulta.",
        "Kokonaisuutena sähköinen asiointi oli {func} ja aikaa vievä.",
        "{portal_dig} digitaalinen palvelukokemus oli {func} vaiheessa: {event}.",
    ]


