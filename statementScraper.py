import re


dic = {
    "Supermercado": [
        "AMPM ALAJUELA",
        "AUTO MERCADO",
        "WALMART ALAJUELA",
        "SUPER SUERTE",
        "AM PM ALAJUELA ESTADIO",
        "PRISMART ECOMMERCE 2",
        "PULPE",
        "GUTIE",
        "SENCHA",
        "KILOSOPHY PRODUCTOS",
        "JINCA",
        "PANADERIA",
        "PRICE SMART",
        "CARNES SAN MARTIN",
        "CURCUMA PRODUCTOS NATU",
        "KETO AK",
        "VINDI ALAJUELA",
    ],
    "Otros": [
        "CARGO EXPRESO ALAJUELA",
        "E-TICKET",
        "UNO SPORTS CITYMALL",
        "UNIVERSAL CITY MALL",
        "UNIVERSAL OTRAS",
        "TOYS CITY MALL",
        "ALM EL REY 7 ALAJUELA",
        "Amazon Prime",
        "SKECHERS",
        "GLAMOUR KIDS",
        "LAVACAR",
        "PAYLESS SHOES",
        "SUR QUIMICA",
        "CONSTRUPLAZA",
        "NOVEX",
        "PARQUE DE DIVERSIONES",
        "REPARACION DE LLANTAS",
        "CEMACO CITY MALL",
        "ALM EL REY 8 ALAJUELA",
        "TECNIELECTRIC FAC",
        "CITIGAMES",
        "CITY GAMES",
        "NOVA",
        "PROTECCION-ROBO Y FRAUDE",
        "PROVIDA",
        "SEGURO PRF",
        "MUNICIPALIDAD ALAJUELA",
        "DEKRA02",
        "MINISO",
        "CORREOSCR ALAJUELA",
        "TURRUCARES SHOP",
        "TOP OUTLET",
        "MI TIENDA HOGAR",
        "PARQUEO",
        "COMPASS",
        "COMPA",
        "BARBER",
        "CINEMARK",
        "TOP OUTLET",
        "PEQUENO MUNDO",
        "DEPORTES HURACAN",
        "AMERICAN SHOP",
        "EL LAGAR",
        "PETS PONT",
        "ANFITEATRO",
        "LIBRERIA",
        "VORK BARBIER",
        "ALPISTE",
    ],
    "ComprasOnline": [
        "Amazon.com",
        "PAYPAL",
        "AMZN",
        "APPLE.COM",
        "GOOGLE",
        "COMPUTACION QUIROS",
    ],
    "Restaurantes": [
        "HI KARI",
        "LA GELATERIA",
        "LA FABRICA PIZZERIA",
        "POPS",
        "AUTOSERVICIO SENSACION",
        "CAFETIN",
        "PIZZA GRILL",
        "BARRILES",
        "HELADERIA LA ESTACION ",
        "POSEIDON BY DA LIMANTA",
        "STARBUCKS",
        "LA ESQUINA DE BUENOS AIRES",
        "TACO BELL",
        "MCDONALD",
        "ROSTI",
        "SMASHBURGER",
        "CACHANOS",
        "CENTRO DE CONVENCIONES",
        "CABRA NEGRA",
        "RESTAURANTE COSI PLAZA REAL",
        "MC DONALDS",
        "PUPUSAS",
        "QUIZNOS",
        "SUBWAY",
        "CEVICHERA JUNIOR",
        "JAPAN TICO",
        "FRESAS DEL VOLCAN",
        "PAPA JOHNS",
        "FUSION TRUCK",
        "FRESAS DEL VOLCAN",
        "KFC PLAZA FERIAS",
    ],
    "Gasolina": [
        "DELTA",
        "ESTACION SERVICIO",
        "ESTACION DE SERVICIO",
        "BOMBA LA TROPICANA",
        "COOTAXA",
    ],
    "Internet": ["TELECABLE"],
    "Suscripciones": [
        "IVA -Spotify",
        "Spotify",
        "SPOTIFY",
        "NETFLIX",
        "HELP.HBOMAX.COM",
    ],
    "Pagos": ["PAGO RECIBIDO", "PAGO RED"],
    "Electricidad": ["ICE ELEC"],
    "Telefonos": ["I.C.E. PAGUELO"],
    "Farmacia": [
        "FARMACIA SANTA LUCIA",
        "FARMAVALUE",
        "FISCHEL",
        "MACROBIOTICA",
        "FARMACIA MAROTO",
    ],
    "Salud": [
        "DRA.JIULLIANA MONTENEGRO PEDIA",
        "CONSULTORES MEDICOS",
        "LABIN AUTOMERCADO",
        "MAXILOFACIAL",
        "ODONTOLOGICO",
        "DIGIDENT",
        "DENTIKIDS",
        "ODONTO IMAGEN",
        "MORERA FUJIWARA DENTAL",
        "CLINICA DENTAL DRA.SIMONE FUJI",
    ],
    "Fondo Pension": ["BN-VITAL FONDO"],
    "JP": ["TILO PAY", "KYLOSOPHY", "STEAM", "EPIC GAMES"],
    "Mascotas": ["HVA NUTRICION", "DR JORGE CALDERON", "VETERINARIA"],
}


def getCategoryByDescription(description):
    for key in dic:
        if any(ele in description for ele in dic[key]):
            return key
    return ""


def scraper(filename, month, card):
    mylines = []
    pattern = re.compile(r"(\d{2}\/\d{2}\/\d{4})(.*)\t{1,}(.*)(CRC|USD)")

    with open(filename, "rt") as myfile:
        for myline in myfile:
            match = pattern.search(myline)
            if match is not None:
                if match.group(4) == "CRC":
                    mylines.append(
                        month
                        + ","
                        + match.group(1)
                        + ","
                        + card
                        + ","
                        + getCategoryByDescription(match.group(2).strip())
                        + ","
                        + match.group(3).replace(",", "").strip()
                        + ",0,"
                        + match.group(2).strip()
                    )
                else:
                    mylines.append(
                        month
                        + ","
                        + match.group(1)
                        + ","
                        + card
                        + ","
                        + getCategoryByDescription(match.group(2).strip())
                        + ",0,"
                        + match.group(3).replace(",", "").strip()
                        + ","
                        + match.group(2).strip()
                    )

    for element in mylines:
        print(element)


# print (getCategoryByDescription('TACO BELL TROPICANA'))

print("---------------------------------------------------------------------")
scraper("mastercard.txt", "Noviembre_2023", "MasterCard")
