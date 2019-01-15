from flask import Flask, redirect, request, url_for, render_template, make_response, flash

app = Flask(__name__)
app.secret_key = "krGcQlz" # Een random string (

# Moest flask nog niet geinstalleerd zijn:
#   klik op r.1 van dit bestand op flask (dat een error geeft omdat het nog niet geinstalleerd is)
#   en klik dan op da rood lampje of alt+insert > install package

# Flask roept per webpagina een scriptje op

# Dit is de webpagina voor http://127.0.0.1:5000/
# hetgene tussen de haakjes bij @app.route('/blablabla') is de site waarbij deze functie wordt opgeroepen
#   bv. http://127.0.0.1:5000/blablabla
@app.route('/')
def home_page():
    # Elke functie moet een html-pagina returnen
    # Via render template kunnen we een pagina in de folder "templates" laten "invullen" door jinja,
    # neem gerust een kijkje in home_page.html
    tekst = "Plopperdeplopperdeplop"
    return render_template('home_page.html', naam=tekst)


# Tussen <> betekent een parameter
# @app.route("/page<number>") zou bijvoorbeeld aangeroepen worden bij /page1, /page2, ...
# def(number): Je moet je parameter dan ook mee bij je functie zetten, en kan daar bewerkingen mee doen

# Data op die manier doorgeven is niet zo handig. Het is veel handiger om het te laten invullen door een form
#   (GET vult een url aan). Als we dit doen, moet er niets speciaal bijkomen bij het url.
# Bekijk maar het voorbeeld hieronder


# Dit url kan GET requests opvangen. Je url gaat er dus waarschijnlijk van volgende vorm uitzien:
# /page2?tekstDieJeHebtIngegeven=<text> # Hierbij is <text> de waarde van de variabele tekstDieJeHebtIngegeven
# maar het volstaat om in python te zeggen dat het url van de vorm "/page2" is en gebruik maakt van GET
# Merk op: Bij GET mogen de waarden NIET als parameter bij de functie.
@app.route("/page2", methods=["GET"])
def page2():
    print("Redirected to page2") # je kan hier de gewone run console output gebruiken
    # eigenlijk kan je alles in python gebruiken dat je gewoon bent

    tekst = request.args.get("tekstDieJeHebtIngegeven")
    # De parameter bij get is de naam die je in je html hebt gegeven aan je form

    # Je kan hier bv. if statements zetten om afhankelijk van de input doorverwezen te worden naar een andere pagina

    # We vullen de nieuwe html pagina nu in met de tekst die we hebben ingegeven
    # Bekijk eventueel ook nog eens page2.html
    return render_template('page2.html', tekst=tekst)

@app.route("/page3", methods=["POST"])
def page3():
    print("Redirected to page3")

    # Data opvragen uit een post form:
    num = request.form["nummer"]

    # We kunnen ook in een html file zelf eenvoudige code gebruiken (ook een functie van flask)
    # Bekijk dus zeker eens de html files
    return render_template("page3.html", num=int(num))

@app.route("/page3_setcookie", methods=["POST"])
def setcookie():
    message = request.form["message"]

    # Op een request kan je als antwoord een redirect of een render_template geven
    # make_response(render_template('/page4')) zou dus ook kunnen,
    #   moest page3 geen extra parameters nodige hebben die er nog niet zijn
    resp = make_response(redirect('/page4'))
    # De ccokie met als variabelenaam "bericht" wordt gelijkgesteld aan message
    resp.set_cookie("bericht", message)

    # Stel er is ergens een error gebeurd, dan "flashen" we die om die te laten zien.
    # Eens je een flash-melding hebt laten zien in je html, wordt de lijst met flash messages leeggemaakt.
    flash("Dit is een vooebeeld van een error")

    return resp  # resp betekent een redirect, dus je wordt naar pagina 4 doorverwezen

@app.route("/page4")
def page4():
    # Vraag de cookie terug op (kan ook vanop andere pagina's gebeuren)
    cookie = request.cookies.get("bericht")

    # We kunnen ook loopen over een tabel, een dictionary, een matrix, ... in jinja
    # (jinja is een html plugin die de htmlfiles dus voor deze naar de client te verzenden,
    #  eerst gaat invullen. oa {{ naam }} en {% if ... %} is van jinja. De klant kan via inspect
    #  element dus niet zien wat er hier oorspronkelijk stond, want enkel de ingevulde versie wordt doorgestuurd)
    # Als voorbeeld zullen we dus loopen over deze tabel met rechtsboven de cookie uit die we hebben opgeslagen.
    dictionary = {"Cookie": cookie, "een": 1, "twee": 2}

    # Het vorige url kunnen we opvragen mbv request.referrer
    # zo kunnen we bv. return redirect(request.referrer) gebruiken om naar de vorige pagina te gaan
    url = request.referrer
    return render_template("page4.html", dict=dictionary, url=url)


if __name__ == '__main__':
    # Gebruik altijd debug mode. Zo moet je je site niet de hele tijd herstarten.
    # Flask herkent vanzelf wanneer er aanpassingen zijn geweest in de code en
    # door je pagina dus (soms 2x) te refreshen, krijg je dus vanzelf de pagina gemaakt mbv de aangepaste code.
    app.debug = True
    app.run()
