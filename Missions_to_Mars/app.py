from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
# import json

app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route('/')
def scrape():
     # Find one record of data from the mongo database
    mars_info = mongo.db.mars_info.find_one()
    ## pass that listing to render_template
    return render_template("index.html", mars_info=mars_info)

# set our path to /scrape
@app.route("/scrape")
def scraper():
    # create a mars database
    # mars_info = mongo.db.mars_info
    # call the scrape function in our scrape_mars file. This will scrape and save to mongo.
    mars_data = scrape_mars.scrape()
    print(mars_data)
    #mars_data_dict = json.loads(json.dumps(mars_data))
   
    # update our mars_info with the data that is being scraped.
    mongo.db.mars_info.replace_one({}, mars_data, upsert=True)
    # return a message to our page so we know it was successful.
    return redirect("/", code=302)

if __name__ == '__main__':
    app.run(debug=True)