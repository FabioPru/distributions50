from flask import render_template

WIKI_STUB = 'wikipedia.org/wiki/'
END_STUB = '_distribution'

PARAMS_TO_INT = ['size', 'n', 'm', 'k']


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def get_missing_args(dst):
    try:
        # Attempt calling the function to sample
        dst.rvs()
        return []
    except Exception as e:
        # Parse the error message and turn it into a list of arguments that were missing
        return str(e).split('\'')[1::2]


def parse_parameters(d):
    print(d)
    params = {k: float(val) for k, val in d.items() if k != 'scipy' and k != 'lam'}
    # Convert parameters to integer, if necessary
    for p in PARAMS_TO_INT:
        if p in params:
            params[p] = int(params[p])
    return params


def get_side_short(soup):
    '''Returns the side bar as a soup component and the short description as text'''
    text = []
    body = soup.find("div", class_="mw-parser-output")
    short = []
    side = None

    for x in body:
        # This loops over elements fetching the side table
        if side is not None:
            try:
                if 'toc' in x['class']:
                    break
            except:
                short.append(x)
        try:
            if 'infobox' in x['class']:
                side = x
        except:
            pass

    for s in short:
        # Convert text paragraphs into str
        try:
            text.append(s.text)
        except:
            pass

    return side, text


def fetch_images(side):
    # These are the things we are looking for to put in our parameters
    LOOK_FOR_DIV = ['Probability density', 'Probability mass', 'Cumulative distribution']
    LOOK_FOR_TH = ['Mean', 'Variance', 'PDF', 'CDF']
    images = []

    table = side.find('tbody')

    # Look for images in the RHS table
    for rw in table.find_all('tr'):
        try:
            for st in LOOK_FOR_TH:
                if rw.find('th').text.startswith(st):
                    images.append((st, rw.find('img')['src']))
        except:
            pass

        try:
            for st in LOOK_FOR_DIV:
                if rw.find('div').text.startswith(st):
                    images.append((st, 'https://' + rw.find('img')['src'][2:]))
        except:
            pass
    return images