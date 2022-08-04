from flask import Flask
from restaurant.logger import logging

app=Flask(__name__)

@app.route('/') # never give space after this line
def index():
    logging.info("we are testing logging module")
    return "HEY I'm STARTING NEW PROJECT on MACHINE LEARNING"

if __name__=='__main__':
    app.run(debug=True)