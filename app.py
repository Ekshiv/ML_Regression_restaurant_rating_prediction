from flask import Flask

app=Flask(__name__)

@app.route('/') # never give space after this line
def index():
    return "HEY I'm STARTING NEW PROJECT on MACHINE LEARNING"

if __name__=='__main__':
    app.run(debug=True)