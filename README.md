# Web Scraping Homework - Mission to Mars

We used a Jupyter Notebook to scrape the NASA Mars News Site https://mars.nasa.gov/news/ and collect the latest News Title and Paragraph Text. 

We visited https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars for JPL Featured Space Image.

We used splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

We visited the Mars Facts webpage https://space-facts.com/mars/ and used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

Then we used Pandas to convert the data to a HTML table string.

We visited the USGS Astrogeology site https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars to obtain high resolution images for each of Mar's hemispheres.

We used a Python dictionary to save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. 

We used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

We converted the Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that executed all the scraping code from above and returned one Python dictionary containing all of the scraped data.

We created a root route `/` that queried the Mongo database and passed the mars data into an HTML template to display the data.

We created a template HTML file called `index.html` that took the mars data dictionary and displayed all of the data in HTML elements using Bootstrap. 
