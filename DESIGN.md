# Structure of the project

The project is a flask application and therefore follows all the flask conventions we learned
while coding CS50 Finance for the last pset.
The ~~~application.py~~~ is deliberately left very clean and easy to understand.
Messy code and arcane tricks that magically work are put in ~~~helpers.py~~~.

# Template files

All pages extend the layout template which contains the top navigation bar and a footer.
As the list of favorite distributions to be displayed can change over the course of time,
it is necessary to pass it as an argument (fav) to render_template every time.
The rest of the files are quite self-explanatory, altough they sometimes contain
lots of boilerplate to deal with edge cases such as the scipy module not existing for that distribution,
or parameters that need to be integers instead of reals, etc.

# HTML styling and bootstrap

The styling is done using bootstrap and a custom .css file adapted from the one used in CS50 Finance.
It has a nice light-blue and white theme, and is generally intutive to use and pleasing to look at.
Some notable design elements are the collapsing cards in the distributions' pages,
the different fonts in the forms within, and the look of the table's entries in the main page.

# Adding distributions and favoriting

The list of available distributions and their Wiki page is maintained in a sqlite database.
The name of each distribution is automatically generated from the Wiki page for a better user experience.
Information about distributions and favorites is shared among all website users;
this is okay if this is run locally but should be changed with a login system if this is hosted on a server.
Various checks are made to verify the user's provided Wikipedia link is valid,
and similarly for other user input in the app.

# Fetching information from Wikipedia

Scraping from Wikipedia pages is done using the BeautifulSoup Python library.
This is by far the worst part of code and has several issues with rendering LaTeX formulas and images.
It tries to figure out which paragraphs come before the table of contents,
but ignoring clarifications about the article that sometimes appear at the top,
tries to convert the content into text, and shows it in the first card.
The second card tries to fetch information from the RHS table and link to its images

# scipy functionalities

The sampling and expectation computing parts are done using the built-in functionalities in scipy.
A distribution object is instantiated after fetching the name from the database.
To figure out the parameters of that distribution, we try a sampling call
and analyze the exception which lists the missing required parameters.
This is how we construct the form the user has to fill.




