# Proposal

## What will (likely) be the title of your project?

Distributions50

## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")

An interactive website to learn and visualize statistical distributions, and perform computation on them.

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

Web application with separate pages for each statistical distribution.

Will pull facts about it from Wikipedia dynamically, and render them nicely including pictures.

There will be a html template using Bootstrap CSS, and values will be scraped and rendered by Python code.

User can submit a form on the website to sample values from those distributions, change parameters and more.

This will call through a Flask application the corresponding functions in the Python library scipy.stats

## If planning to combine CS50's final project with another course's final project, with which other course? And which aspect(s) of your proposed project would relate to CS50, and which aspect(s) would relate to the other course?

No

## If planning to collaborate with 1 or 2 classmates for the final project, list their names, email addresses, and the names of their assigned TFs below.

No

## In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?

Web application using Flask

At least the very main continuous distributions (uniform, exponential, normal, ...)

User can sample from those distributions dynamically

Facts about them pulled from Wikipedia, including PDF, CDF, pictures

### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

More continuous distributions

User can set parameters for those distributions, and pictures of pdf/cdf dynamically update

Support for discrete distributions as well

Nicer website styled using Bootstrap

### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

Interactive plots

Compute arbitrary functions of those distributions using LOTUS, e.g. compute E(X^2), using underlying library in scipy.stats

Users can add "fun facts" about distributions to the website, which are then shown to other users

LaTeX rendering

## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?

Learn about scipy.stats, only have very basic knowledge of it. How to instantiate a distribution object, how to set parameters, how to sample from it.

Learn how to render matplotlib plots directly into web page. Only know how to do so by saving the file on the server, would like to avoid that.

Start writing Flask application:

Code to scrape from Wikipedia text and images. Using BeautifulSoup which I've used before.

Experiment with layout/CSS to make it nice on all devices. Bootstrap. Start with something basic

Button for sampling from selected distribution. Flask route like /sample?dist=expo&no_values=1.