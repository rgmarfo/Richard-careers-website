from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        "id":1,
        "title":"Data Analyst",
        "location": "Kofordua, Ghana",
        "salary":"GHc 4,000"
        
        
    },
    {
        "id":2,
        "title":"Data Scientist",
        "location": "Oyoko, Ghana",
        "salary":"GHc 2,000"
        
        
    },
    {
        "id":3,
        "title":"Frontend Engineer",
        "location": "SaintJames, Ghana",
        "salary":"GHc 5,000"
        
        
    },
    {
        "id":4,
        "title":"Mathematician",
        "location": "Kofordua, Ghana",
        "salary":"GHc 15,000"
        
        
    },
]


@app.route("/")
def hello_world():
    return render_template('home.html',jobs=JOBS,company_name = "Richard")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
    