from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        data = {
            "gengo1": request.form['gengo1'],
            "gengo2": request.form['gengo2'],
            "gengo3": request.form['gengo3'],
            "mokuteki1": request.form["mokuteki1"],
            "mokuteki2": request.form["mokuteki2"],
            "mokuteki3": request.form["mokuteki3"],
            "mokuteki4": request.form["mokuteki4"]
        }
        return render_template("index.html", data=data)
    else:
        return render_template("form.html")

if __name__=="__main__":
    app.run(port=8000, debug=True)