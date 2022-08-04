import sys
from flask import Flask
from restaurant.logger import logging
from restaurant.exception import RestaurantException

app=Flask(__name__)

@app.route('/') # never give space after this line
def index():
    try:
        raise Exception("We are testing Exception module in our project")
    except Exception as e:
        restaurant=RestaurantException(e,sys)
        logging.info(restaurant.error_message)
    logging.info("we are testing logging module")
    return "HEY I'm STARTING NEW PROJECT on MACHINE LEARNING"

if __name__=='__main__':
    app.run(debug=True)