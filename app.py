from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record from MARS NEWS from MONGODB
    mars_news_data = mongo.db.scrape_info_news.find_one()
    # Fine one record from SCRAPE_IMAGE collection
    mars_image_data = mongo.db.scrape_image.find_one()
    # Find one record from MARS WEATHER from MONGODB
    mars_data = mongo.db.scrape_info_weather.find_one()
    # Find one record from MARS FACTS from MONGODB
    mars_facts_data = mongo.db.scrape_info_facts.find_one()
    # Find one record from HEMI IMAGES from MONGODB
    mars_hemi_image_data = mongo.db.scrape_hemi_image.find_one()

    # Return template and data
    return render_template("index.html", mars_news_data=mars_news_data, mars_data=mars_data, mars_image_data=mars_image_data, mars_facts_data=mars_facts_data, mars_hemi_image_data=mars_hemi_image_data)



# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function for MARS NEWS
    mars_news_data = scrape_mars.scrape_info_news()
    mongo.db.scrape_info_news.update({}, mars_news_data, upsert=True)

    # Run the scrape for features image MARS FEATURED_IMAGE_URL
    mars_image_data = scrape_mars.scrape_image()
    mongo.db.scrape_image.update({}, mars_image_data, upsert=True)

    # Run the scrape function for MARS TWITTER WEATHER
    mars_data = scrape_mars.scrape_info_weather()
    mongo.db.scrape_info_weather.update({}, mars_data, upsert=True)

    # Run the scrape function for MARS FACTS
    mars_facts_data = scrape_mars.scrape_info_facts()
    mongo.db.scrape_info_facts.update({}, mars_facts_data, upsert=True)

    # Run the scrape function for HEMI IMAGES
    mars_hemi_image_data = scrape_mars.scrape_hemi_image()
    mongo.db.scrape_hemi_image.update({}, mars_hemi_image_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
