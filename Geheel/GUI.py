# Voor het maken van deze GUI werd volgende bron meermaals gebruikt: http://flask.pocoo.org/docs/0.12/

from System import *
from flask import Flask, redirect, request, url_for, render_template, make_response, flash
app = Flask(__name__)
app.secret_key = "9j3faDq"


geheel = None
messages = []

@app.route('/')
def index():
    print("Showing the homepage")
    return render_template('index.html')

@app.route('/login')
def login():
    print("Showint the login page")
    return render_template('login.html')


# type kan leerling of leerkracht zijn
@app.route('/verifylogin', methods=['POST'])
# @app.route('/verifylogin')
def verifylogin():
    name = request.form['name']
    print("Verifying login:", name)

    if geheel.isLeerkracht(name):
        resp = make_response(redirect('/home'))
        resp.set_cookie('name', name)
        resp.set_cookie('type', "Leerkracht")
        print("Cookie created")
        return resp
    elif geheel.isLeerling(name):
        resp = make_response(redirect('/home'))
        resp.set_cookie('name', name)
        resp.set_cookie('type', "Leerling")
        print("Cookie created")
        return resp
    elif name == "admin":
        resp = make_response(redirect('/home'))
        resp.set_cookie('type', "admin")
        resp.set_cookie('name', name)
        print("Cookie created")
        return resp
    else:
        flash("Login not found.")
        return redirect('/login')


@app.route('/home')
def home():
    print("Showing homepage")
    name = request.cookies.get('name') # bv. HOFKT
    if request.cookies.get('type') == "Leerkracht":
        leerkracht = geheel.retrieveLeeraar(name)[1]
        naam = leerkracht.getNaam() + " " + leerkracht.getAchternaam()
        return render_template('teacher.html', name=naam, puntenlijsten=geheel.puntenLijstenVanLeerkracht(name))
    elif request.cookies.get("type") == "admin":
        return render_template('admin.html')
    else:
        leerling = geheel.retrieveLeerling(name)[1]
        naam = leerling.getVoornaam() + " " + leerling.getNaam()
        return render_template('student.html', name=naam)


# @app.route('/puntenlijst?ID=<ID>')
@app.route('/puntenlijst')
def puntenlijst():
    ID = request.args.get("ID")
    titel = str(geheel.retrievePuntenlijst(ID)[1])
    toetsen = geheel.toetsenVanPuntenlijst(ID)

    resp = make_response(render_template('puntenlijst.html', title=titel, toetsen=toetsen))
    resp.set_cookie('puntenlijstID', ID)

    return resp


@app.route('/toets')
def toets():
    naam = request.args.get("naam")
    punten = geheel.puntenVanToets(naam)

    resp = make_response(render_template('toets.html', title=naam, punten=punten))
    resp.set_cookie('toetsNaam', naam)

    return resp


@app.route('/removepunt')
def removepunt():
    ID = request.args.get("ID")
    geheel.deletePunt(ID)
    geheel.save("system.txt")
    return redirect(request.referrer)

@app.route('/removetoets')
def removetoets():
    naam = request.args.get("naam")
    geheel.deleteToets(naam)
    geheel.save("system.txt")
    return redirect(request.referrer)

@app.route('/removepuntenlijst')
def removepuntenlijst():
    ID = request.args.get("ID")
    geheel.deletePunt(ID)
    geheel.save("system.txt")
    return redirect(request.referrer)

@app.route('/addpuntenlijst', methods=['GET', 'POST'])
def addpuntenlijst():
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
    naam = request.args.get("naam")
    maximum = request.args.get("maximum")
    puntenlijst = request.cookies.get("puntenlijstID")
    for message in geheel.addToets(puntenlijst, naam, maximum):
        flash(message)
    geheel.save("system.txt")
    return redirect(request.referrer)

@app.route('/addpunt', methods=['GET', 'POST'])
def addpunt():
    stamboeknr = request.args.get("stamboeknr")
    waarde = request.args.get("waarde")
    toets = request.cookies.get("toetsNaam")
    leerkracht = request.cookies.get("name")
    geheel.addPunt(stamboeknr, toets, waarde, leerkracht)
    geheel.save("system.txt")
    return redirect(request.referrer)

@app.route('/vakken')
def vakken():
    return render_template('vakken.html', vakken=geheel.tabelVakken())

@app.route('/addvak', methods=['GET'])
def addvak():
    afkorting = request.args.get("afkorting")
    vak = request.args.get("vak")
    geheel.addVak(afkorting, vak)
    geheel.save("system.txt")
    return redirect(request.referrer)

@app.route('/removevak')
def removevak():
    afkorting = request.args.get("afkorting")
    geheel.deleteVak(afkorting)
    geheel.save("system.txt")
    return redirect(request.referrer)


@app.route('/leraars')
def leraars():
    return render_template('leraars.html', leraars=geheel.tabelLeraars())

@app.route('/addleraar', methods=['GET'])
def addleraar():
    afkorting = request.args.get("naamcode")
    naam = request.args.get("naam")
    voornaam = naam.split(" ")[0]
    achternaam = naam[len(voornaam)+1:]
    geheel.addLeraar(afkorting, voornaam, achternaam)
    geheel.save("system.txt")
    return redirect(request.referrer)

@app.route('/removeleraar')
def removeleraar():
    afkorting = request.args.get("naamcode")
    geheel.deleteLeraar(afkorting)
    geheel.save("system.txt")
    return redirect(request.referrer)

@app.route('/klassen')
def klassen():
    return render_template('klassen.html', klassen=geheel.tabelKlassen())

@app.route('/addklas', methods=['GET'])
def addklas():
    klas = request.args.get("klas")
    geheel.addKlas(klas)
    geheel.save("system.txt")
    return redirect(request.referrer)

@app.route('/removeklas')
def removeklas():
    klas = request.args.get("klas")
    geheel.deleteKlas(klas)
    geheel.save("system.txt")
    return redirect(request.referrer)

@app.route('/leerlingen')
def leerlingen():
    return render_template('leerlingen.html', leerlingen=geheel.tabelLeerlingen())

@app.route('/addleerling', methods=['GET'])
def addleerling():
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
    stamboeknr = request.args.get("stamboeknr")
    geheel.deleteLeerling(stamboeknr)
    geheel.save("system.txt")
    return redirect(request.referrer)


@app.route('/getrapport', methods=['GET'])
def getrapport():
    zoeksleutel = request.args.get("zoeksleutel")
    studentennr = request.cookies.get("name")
    klas = geheel.retrieveLeerling(studentennr)[1].getKlas()
    print("Building rapport:", zoeksleutel, klas, studentennr)
    rapport = geheel.buildRapport(zoeksleutel, klas, studentennr)
    return rapport


@app.route('/datastructuren')
def datastructuren():
    info = geheel.datastructuresinfo()
    return render_template('datastructuren.html', vakken=info[0], leraars=info[1], punt=info[2])


@app.route('/view', methods=['GET'])
def view():
    data = request.args.get("view")
    if data == "vakken":
        geheel.printVak()
    return redirect(request.referrer)

if __name__ == '__main__':
    geheel = readFile("system.txt", None)
    app.debug = True
    app.run()

    # vul hier je local ip in om vanaf een ander toestel op je LAN netwerk de site te bereiken
    # app.run(host='192.168.0.135')