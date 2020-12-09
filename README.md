# Video

https://youtu.be/mYrQq4w8k6k

# Overview of the project

This project is a flask application meant to be run locally on your machine.
It allows the user to explore statistical distributions, discrete and continuous.

You can pick any distribution from Wikipedia, access its facts quickly, sample from it, and compute expectancy of functions of r.v. using LOTUS.

# Running the application

Open a terminal in the /project/ main folder, type ~~~flask run~~~, and click on the link.

If you encounter any problems while doing this, you might not have installed one of the required Python packages.
For instance, the CS50 IDE lacks scipy.
Type ~~~pip install -r requirements.txt~~~ to solve this.

# Adding distributions you need and setting favorites

This application supports any of the dozens of discrete and continuous distributions that are listed on Wikipedia.
It already ships with some of the most popular ones saved into distributions50.db, but you are encouraged to add your own through the main page.

The main page displays a brief intro to the project, a list of all the distributions you have added, and at the bottom a form to add new ones.

The form for a new distribution requires the Wikipedia link, and optionally the name of the scipy module for it to support sampling/computing expectancies.

To change which distributions are your "favorite" that appear in the top navbar, click on the appropriate link on the rightmost column in the table.

Here you can navigate to the pages for each distribution by clicking on its name, plus its wiki page and its scipy docs.

# Reading pages for each individual distribution

Each distribution page holds various information that is fetched from Wikipedia about that particular distribution.

In the first section you can find a brief summary, although the math sometimes doesn't render correctly.

In the second section you can find pictures of its CDF/PDF and facts about mean, variance, and more.

If your selected distribution is supported by scipy, you will have two more sections available outlined below.

# scipy features

In the third section you can set parameters of your choice for the distribution family you are seeing.
You can then sample any number of points you desire from that distribution, and view the results in a new page.
Of course the sampling is random, so you will have new numbers each time.

In the last section you can compute the expectancy of arbitrary functions of your random variable.
For instance if X is a Normally distributed random variable, you might want to know E[X^2], E[sin X], E[e^-X], or more generally E[f(X)] for any function.
This done in stat 110 using LOTUS, and here you can verify your results for any function f you can think of.