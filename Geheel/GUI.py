# Voor het maken van deze GUI werd volgende bron meermaals gebruikt: http://flask.pocoo.org/docs/0.12/

from System import *
from flask import Flask, redirect, request, url_for, render_template, make_response, flash

import time
from subprocess import check_call # Nodig voor datastructuren
import pydot  # Nodig voor datastructuren
# import os  # Nodig voor datastructuren

app = Flask(__name__)
app.secret_key = "9j3faDq"


geheel = None
messages = []

# Geen veilige vorm van encryptie, maar doet toch al iets
def encrypt(str):
    encryption = ""
    offset = len(str)*len(str)-len(str)
    i = 1
    for char in str:
        ascii_plaats = ord(char)
        nieuwe_plaats = ascii_plaats + offset*i
        newchar = chr(nieuwe_plaats)
        encryption += newchar
        i += 1
    return encryption

# Gebruik deze functie zo weinig mogelijk
# encrypt(a) = encrypt(b) <=> a=b, enrypt dus liever het 2e lid, dan het eerste te decrypten
def decrypt(str):
    decryption = ""
    offset = len(str)*len(str)-len(str)
    i = 1
    for char in str:
        newchar = chr(ord(char) - offset*i)
        decryption += newchar
        i += 1
    return decryption

@app.route('/')
def index():
    print("Showing the homepage")
    return render_template('index.html')

@app.route('/login')
def login():
    print("Showint the login page")
    return render_template('login.html')

@app.route('/back')
def back():
    return redirect(request.referrer)


# type kan leerling of leerkracht zijn
@app.route('/verifylogin', methods=['POST'])
# @app.route('/verifylogin')
def verifylogin():
    name = request.form['name']
    print("Verifying login:", name)

    if geheel.isLeerkracht(name):
        resp = make_response(redirect('/home'))
        resp.set_cookie('name', encrypt(name))
        resp.set_cookie('type', encrypt("Leerkracht"))
        print("Cookie created")
        return resp
    elif geheel.isLeerling(name):
        resp = make_response(redirect('/home'))
        resp.set_cookie('name', encrypt(name))
        resp.set_cookie('type', encrypt("Leerling"))
        print("Cookie created")
        return resp
    elif name == "admin":
        resp = make_response(redirect('/home'))
        resp.set_cookie('type', encrypt("System Administrator"))
        resp.set_cookie('name', encrypt(name))
        print("Cookie created")
        return resp
    else:
        flash("Login not found.")
        return redirect('/login')


@app.route('/home')
def home():
    print("Showing homepage")
    name = request.cookies.get('name') # bv. HOFKT
    name = decrypt(name)
    if request.cookies.get('type') == encrypt("Leerkracht"):
        leerkracht = geheel.retrieveLeeraar(name)[1]
        naam = leerkracht.getNaam() + " " + leerkracht.getAchternaam()
        return render_template('teacher_home.html', name=naam, puntenlijsten=geheel.puntenLijstenVanLeerkracht(name), login=naam)
    elif request.cookies.get("type") == encrypt("System Administrator"):
        return render_template('admin.html', login=name)
    elif request.cookies.get("type") == encrypt("Leerling"):
        leerling = geheel.retrieveLeerling(name)[1]
        voornaam = leerling.getVoornaam()
        naam = voornaam + " " + leerling.getNaam()
        rapporten = geheel.rapportenMetPuntenVanLeerling(name)
        return render_template('student.html', name=voornaam, login=naam, rapporten=rapporten)
    else:
        flash("No homepage found. Please login first.")
        return redirect('/login')

# @app.route('/puntenlijst?ID=<ID>')
@app.route('/puntenlijst')
def puntenlijst():
    if request.cookies.get("type") != encrypt("Leerkracht"):
        flash("Access denied")
        return redirect("/login")

    ID = request.args.get("ID")
    titel = str(geheel.retrievePuntenlijst(ID)[1])
    toetsen = geheel.toetsenVanPuntenlijst(ID)

    resp = make_response(render_template('puntenlijst.html', title=titel, toetsen=toetsen, IDpuntenlijst=ID))
    resp.set_cookie('puntenlijstID', ID)

    return resp

@app.route('/puntenlijsten')
def puntenlijsten():
    if request.cookies.get("type") != encrypt("Leerkracht"):
        flash("Access denied")
        return redirect("/login")
    name = decrypt(request.cookies.get("name"))
    leerkracht = geheel.retrieveLeeraar(name)[1]
    naam = leerkracht.getNaam() + " " + leerkracht.getAchternaam()
    return render_template('teacher.html', name=naam, puntenlijsten=geheel.puntenLijstenVanLeerkracht(name), login=naam)

@app.route('/toets')
def toets():
    if request.cookies.get("type") != encrypt("Leerkracht"):
        flash("Access denied")
        return redirect("/login")

    naam = request.args.get("naam")
    punten = geheel.puntenVanToets(naam)
    ID = geheel.retrieveToets(naam)[1].getPuntenlijst()

    resp = make_response(render_template('toets.html', title=naam, punten=punten, IDpuntenlijst=ID))
    resp.set_cookie('toetsNaam', naam)

    return resp


@app.route('/removepunt')
def removepunt():
    if request.cookies.get("type") != encrypt("Leerkracht"):
        flash("Access denied")
        return redirect("/login")

    ID = request.args.get("ID")
    geheel.deletePunt(ID)
    geheel.save("system.txt")
    return redirect(request.referrer)

@app.route('/removetoets')
def removetoets():
    if request.cookies.get("type") != encrypt("Leerkracht"):
        flash("Access denied")
        return redirect("/login")

    naam = request.args.get("naam")
    geheel.deleteToets(naam)
    geheel.save("system.txt")
    return redirect(request.referrer)

@app.route('/removepuntenlijst')
def removepuntenlijst():
    if request.cookies.get("type") != encrypt("Leerkracht"):
        flash("Access denied")
        return redirect("/login")

    ID = request.args.get("ID")
    geheel.deletePunt(ID)
    geheel.save("system.txt")
    return redirect(request.referrer)

@app.route('/addpuntenlijst', methods=['GET', 'POST'])
def addpuntenlijst():
    if request.cookies.get("type") != encrypt("Leerkracht"):
        flash("Access denied")
        return redirect("/login")

    ID = request.args.get("ID")
    klas = request.args.get("klas")
    vak = request.args.get("vak")
    rapport = request.args.get("rapport")
    type = rapport[0]
    periode = rapport[1:]
    leerkrachten = request.args.get("leerkrachten")
    uren = request.args.get("uren")
    for message in geheel.addPuntenLijst(ID, type, periode, leerkrachten, vak, klas, uren):
        flash(message)
    geheel.save("system.txt")
    return redirect(request.referrer)

@app.route('/addtoets', methods=['GET', 'POST'])
def addtoets():
    if request.cookies.get("type") != encrypt("Leerkracht"):
        flash("Access denied")
        return redirect("/login")

    naam = request.args.get("naam")
    maximum = request.args.get("maximum")
    puntenlijst = request.cookies.get("puntenlijstID")
    for message in geheel.addToets(puntenlijst, naam, maximum):
        flash(message)
    geheel.save("system.txt")
    return redirect(request.referrer)

@app.route('/addpunt', methods=['GET', 'POST'])
def addpunt():
    if request.cookies.get("type") != encrypt("Leerkracht"):
        flash("Access denied")
        return redirect("/login")

    stamboeknr = request.args.get("stamboeknr")
    waarde = request.args.get("waarde")
    toets = request.cookies.get("toetsNaam")
    leerkracht = decrypt(request.cookies.get("name"))
    geheel.addPunt(stamboeknr, toets, waarde, leerkracht)
    geheel.save("system.txt")
    return redirect(request.referrer)

@app.route('/vakken')
def vakken():
    if request.cookies.get("type") != encrypt("System Administrator"):
        flash("Access denied")
        return redirect("/login")

    return render_template('vakken.html', vakken=geheel.tabelVakken())

@app.route('/addvak', methods=['GET'])
def addvak():
    if request.cookies.get("type") != encrypt("System Administrator"):
        flash("Access denied")
        return redirect("/login")

    afkorting = request.args.get("afkorting")
    vak = request.args.get("vak")
    geheel.addVak(afkorting, vak)
    geheel.save("system.txt")
    return redirect(request.referrer)

@app.route('/removevak')
def removevak():
    if request.cookies.get("type") != encrypt("System Administrator"):
        flash("Access denied")
        return redirect("/login")

    afkorting = request.args.get("afkorting")
    geheel.deleteVak(afkorting)
    geheel.save("system.txt")
    return redirect(request.referrer)


@app.route('/leraars')
def leraars():
    if request.cookies.get("type") != encrypt("System Administrator"):
        flash("Access denied")
        return redirect("/login")

    return render_template('leraars.html', leraars=geheel.tabelLeraars())

@app.route('/addleraar', methods=['GET'])
def addleraar():
    if request.cookies.get("type") != encrypt("System Administrator"):
        flash("Access denied")
        return redirect("/login")

    afkorting = request.args.get("naamcode")
    naam = request.args.get("naam")
    voornaam = naam.split(" ")[0]
    achternaam = naam[len(voornaam)+1:]
    geheel.addLeraar(afkorting, voornaam, achternaam)
    geheel.save("system.txt")
    return redirect(request.referrer)

@app.route('/removeleraar')
def removeleraar():
    if request.cookies.get("type") != encrypt("System Administrator"):
        flash("Access denied")
        return redirect("/login")

    afkorting = request.args.get("naamcode")
    geheel.deleteLeraar(afkorting)
    geheel.save("system.txt")
    return redirect(request.referrer)

@app.route('/klassen')
def klassen():
    if request.cookies.get("type") != encrypt("System Administrator"):
        flash("Access denied")
        return redirect("/login")

    return render_template('klassen.html', klassen=geheel.tabelKlassen())

@app.route('/addklas', methods=['GET'])
def addklas():
    if request.cookies.get("type") != encrypt("System Administrator"):
        flash("Access denied")
        return redirect("/login")

    klas = request.args.get("klas")
    geheel.addKlas(klas)
    geheel.save("system.txt")
    return redirect(request.referrer)

@app.route('/removeklas')
def removeklas():
    if request.cookies.get("type") != encrypt("System Administrator"):
        flash("Access denied")
        return redirect("/login")

    klas = request.args.get("klas")
    geheel.deleteKlas(klas)
    geheel.save("system.txt")
    return redirect(request.referrer)

@app.route('/leerlingen')
def leerlingen():
    if request.cookies.get("type") != encrypt("System Administrator"):
        flash("Access denied")
        return redirect("/login")

    return render_template('leerlingen.html', leerlingen=geheel.tabelLeerlingen())

@app.route('/addleerling', methods=['GET'])
def addleerling():
    if request.cookies.get("type") != encrypt("System Administrator"):
        flash("Access denied")
        return redirect("/login")

    stamboeknr = request.args.get("stamboeknr")
    naam = request.args.get("naam")
    voornaam = naam.split(" ")[0]
    achternaam = naam[len(voornaam)+1:]
    klas = request.args.get("klas")
    klasnummer = request.args.get("klasnr")
    geheel.addLeerling(achternaam, voornaam, klas, klasnummer, stamboeknr)
    geheel.save("system.txt")
    return redirect(request.referrer)

@app.route('/removeleerling')
def removeleerling():
    if request.cookies.get("type") != encrypt("System Administrator"):
        flash("Access denied")
        return redirect("/login")

    stamboeknr = request.args.get("stamboeknr")
    geheel.deleteLeerling(stamboeknr)
    geheel.save("system.txt")
    return redirect(request.referrer)


@app.route('/getrapport', methods=['GET'])
def getrapport():
    if request.cookies.get("type") != encrypt("Leerling") or \
            not geheel.isLeerling(decrypt(request.cookies.get("name"))):

        return redirect("/login")

    zoeksleutel = request.args.get("zoeksleutel")
    studentennr = decrypt(request.cookies.get("name"))
    klas = geheel.retrieveLeerling(studentennr)[1].getKlas()
    print("Building rapport:", zoeksleutel, klas, studentennr)
    rapport = geheel.buildRapport(zoeksleutel, klas, studentennr, buildHTML=False)
    header = rapport[0]
    footer = rapport[len(rapport)-1]
    body = rapport[1:len(rapport)-1]
    login = geheel.retrieveLeerling(studentennr)[1].getVoornaam() + " " + geheel.retrieveLeerling(studentennr)[1].getNaam()
    rapporten = geheel.rapportenMetPuntenVanLeerling(studentennr)
    return render_template("rapport.html", header=header, footer=footer, body=body,
                           login=login, rapporten=rapporten, id=zoeksleutel)


@app.route('/datastructuren')
def datastructuren():
    if request.cookies.get("type") != encrypt("System Administrator"):
        return redirect("/login")

    info = geheel.datastructuresinfo()
    return render_template('datastructuren.html', vakken=info[0], leraars=info[1], punt=info[2], puntenlijst=info[3],
                           leerling=info[4], rapport=info[5], klassen=info[6], undo=info[7], redo=info[8],
                           instructies=info[9], queue=info[10])


@app.route('/view', methods=['GET'])
def view():
    if request.cookies.get("type") != encrypt("System Administrator"):
        flash("Access denied.")
        return redirect("/login")

    structuur = request.args.get("view")
    if structuur == "leraars":
        png = geheel.printLeraar()
    elif structuur == "punt":
        png = geheel.printPunt()
    elif structuur == "puntenlijst":
        png = geheel.printPuntenlijst()
    elif structuur == "leerling":
        png = geheel.printLeerling()
    elif structuur == "rapport":
        png = geheel.printRapport()
    elif structuur == "klassen":
        png = geheel.printKlas()
    elif structuur == "vakken":
        # png = geheel.printVak()
        png = geheel.printToets()
    elif structuur == "undo":
        png = geheel.printUndo()
    elif structuur == "redo":
        png = geheel.printRedo()
    elif structuur == "instructies":
        png = geheel.printInstructies()
    elif structuur == "queue":
        png = geheel.printQueue()
    else:
        flash("Error: Datastructure not found")
        return redirect(request.referrer)

    (graph, ) = pydot.graph_from_dot_file(png)  # Bewust een halve tuple gedaan
    filelocation = "static/" + png + ".png"
    graph.write_png(filelocation)

    return render_template("view.html", png=filelocation)

@app.route('/logout')
def logout():
    resp = make_response(redirect('/login'))
    resp.set_cookie('name', '', expires=0)
    resp.set_cookie('type', '', expires=0)
    return resp


@app.route('/ADTchanges', methods=['GET'])
def ADTchanges():
    if request.cookies.get("type") != encrypt("System Administrator"):
        flash("Access denied.")
        return redirect('/login')

    vakken = (request.args.get("vakkenchange"), request.args.get("datatypevakken"))
    punt = (request.args.get("puntchange"), request.args.get("datatypepunt"))
    leraar = (request.args.get("leraarschange"), request.args.get("datatypeleraar"))
    puntenlijst = (request.args.get("puntenlijstchange"), request.args.get("datatypepuntenlijst"))
    leerlingen = (request.args.get("leerlingchange"), request.args.get("datatypeleerling"))
    rapport = (request.args.get("rapportchange"), request.args.get("datatyperapport"))
    klassen = (request.args.get("klassenchange"), request.args.get("datatypeklassen"))
    if punt[0] == "true" and geheel.punten.type != punt[1]:
        geheel.puntdatatypechange(punt[1])
    if leraar[0] == "true" and geheel.leraars.type != leraar[1]:
        geheel.leraardatatypechange(leraar[1])
    if vakken[0] == "true" and geheel.vakken.type != vakken[1]:
        geheel.vakkendatatypechange(vakken[1])
    if puntenlijst[0] == "true" and geheel.puntenlijst.type != puntenlijst[1]:
        geheel.puntenlijstdatatypechange(puntenlijst[1])
    if leerlingen[0] == "true" and geheel.leerlingen.type != leerlingen[1]:
        geheel.leerlingdatatypechange(leerlingen[1])
    if rapport[0] == "true" and geheel.rapporten.type != rapport[1]:
        geheel.rapportdatatypechange(rapport[1])
    if klassen[0] == "true" and geheel.klassen.type != klassen[1]:
        geheel.klassendatatypechange(klassen[1])
    return redirect(request.referrer)

# Ensure responses aren't cached - fix logout cached in browser history
# source: https://stackoverflow.com/questions/20652784/flask-back-button-returns-to-session-even-after-logout
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response


if __name__ == '__main__':
    geheel = readFile("system.txt", None)
    app.debug = True
    app.run()

    # Server settings, ignore
    # app.debug = False
    # app.run(host='192.168.0.116', ssl_context='adhoc')
