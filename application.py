import os
import requests
import numpy as np

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from bs4 import BeautifulSoup
from scipy import stats

from helpers import *


# Flask starter code adapted from finance pset
# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///distributions50.db")


@app.route("/")
def index():
    '''Shows the landing page with the distribution list read from db'''

    dist = db.execute("SELECT name, wiki, scipy, favorite FROM distributions ORDER BY name")
    fav = db.execute("SELECT name FROM distributions WHERE favorite=1 ORDER BY name")
    return render_template("index.html", fav=fav, dist=dist)


@app.route("/distribution", methods=["GET"])
def distribution():
    '''Renders all elements in the page for a specific distribution'''

    if not request.args.get('name'):
        return apology("must provide a distribution name", 400)
    name = request.args.get('name')
    entry = db.execute("SELECT * FROM distributions WHERE name = ?", name)[0]
    wiki = entry['wiki']
    scipy = entry['scipy']

    # Scraping code adapted from BeautifulSoup docs and
    # https://riptutorial.com/beautifulsoup

    try:
        req = requests.get(wiki)
        soup = BeautifulSoup(req.text, "html.parser")
    except:
        return apology("scraping failed", 400)

    side, short = get_side_short(soup)
    images = fetch_images(side)

    scrape = {'title': soup.find('h1').text,
              'short': short,
              'images': images
              }

    # scipy.stats functionalities
    # https://docs.scipy.org/doc/scipy/reference/stats.html
    if scipy != '':
        # Figure out what parameters the distribution needs by trying
        dst = stats.__getattribute__(scipy)
        missing_args = get_missing_args(dst)
    else:
        missing_args = 0

    fav = db.execute("SELECT name FROM distributions WHERE favorite=1 ORDER BY name")
    return render_template("distribution.html", fav=fav, name=name, scrape=scrape, scipy=scipy, missing_args=missing_args)


@app.route("/sample", methods=["GET"])
def sample():
    """Sample points from a distribution"""

    try:
        dst = stats.__getattribute__(request.args.get('scipy'))
        params = parse_parameters(dict(request.args))
        print(params)
        # scipy function for sampling from a distribution
        samples = dst.rvs(**params)
    except:
        return apology("one of the arguments you passed wasn't accepted by scipy", 400)

    fav = db.execute("SELECT name FROM distributions WHERE favorite=1 ORDER BY name")
    return render_template("sample.html", fav=fav, samples=samples)


@app.route("/expect", methods=["POST"])
def expect():
    """Find expectancy of a function"""

    try:
        dst = stats.__getattribute__(request.form.get('scipy'))
        params = parse_parameters(dict(request.form))

        # Figure out required parameters
        missing_args = get_missing_args(dst)
        args = tuple([params[arg] for arg in missing_args])

        # I know this is literally the worst code security-wise you have seen in your life
        # and it allows any malicious agent to run arbitrary code on the server's machine
        # and it's well-advertised and easy to spot
        # BUT
        # there's literally no way to make it secure as the functionality itself requires
        # running arbitrary code and this code is not hosted anywhere so... deal with it?
        val = dst.expect(eval(request.form.get('lam')), args=args)
    except:
        return apology("one of the arguments you passed wasn't accepted by scipy", 400)

    fav = db.execute("SELECT name FROM distributions WHERE favorite=1 ORDER BY name")
    return render_template("expect.html", fav=fav, val=val, lam=request.form.get('lam'))


@app.route("/create", methods=["POST"])
def create():
    """Create a new distribution adding it to the database"""

    if not request.form.get('wiki'):
        return apology("must provide a wikipedia link", 400)

    url = request.form.get('wiki')

    # Ensure start and end of the link match what we're looking for
    s_i = url.find(WIKI_STUB)
    e_i = url.find(END_STUB)
    if s_i == -1 or e_i == -1:
        return apology("url does not appear to be a valid wiki page", 400)

    # Generate name from the url
    name = url[s_i+len(WIKI_STUB):e_i].replace(" ", "_")

    # Ensure distribution does not already exist
    rows = db.execute("SELECT * FROM distributions WHERE name = ?", name)
    if len(rows) > 0:
        return apology("distribution already exists", 400)

    if request.form.get('scipy') is not None:
        db.execute("INSERT INTO distributions (name, wiki, scipy) VALUES (?, ?, ?);",
                   name, url, request.form.get('scipy').strip().lower())
    else:
        db.execute("INSERT INTO distributions (name, wiki) VALUES (?, ?);", name, url)

    return redirect("/")


@app.route("/changefav", methods=["GET"])
def changefav():
    """Change favorite status of a distribution"""

    # Check post url has not been tampered
    if not request.args.get('name'):
        return apology("must provide a distribution name", 400)
    if not request.args.get('new') or not request.args.get('new') in ["0", "1"]:
        return apology("not a valid value to change to", 400)

    # Ensure distribution exists
    rows = db.execute("SELECT * FROM distributions WHERE name = ?", request.args.get('name'))
    if len(rows) == 0:
        return apology("distribution name does not exist", 400)

    db.execute("UPDATE distributions SET favorite = ? WHERE name = ?",
               request.args.get('new'), request.args.get('name'))

    return redirect("/")


@app.route("/design", methods=["GET", "POST"])
def design():
    fav = db.execute("SELECT name FROM distributions WHERE favorite=1 ORDER BY name")
    return render_template("design.html", fav=fav)


@app.route("/readme", methods=["GET", "POST"])
def readme():
    fav = db.execute("SELECT name FROM distributions WHERE favorite=1 ORDER BY name")
    return render_template("readme.html", fav=fav)


@app.route("/credits", methods=["GET", "POST"])
def credits():
    fav = db.execute("SELECT name FROM distributions WHERE favorite=1 ORDER BY name")
    return render_template("credits.html", fav=fav)