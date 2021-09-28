from flask import Flask, render_template
import urllib.request, json
import os


app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

@app.route("/")
def get_movies():
    url = "https://api.themoviedb.org/3/movie/popular?api_key=a43bd6b6eb4030a589bf0e0a8cdf215d".format(os.environ.get("a43bd6b6eb4030a589bf0e0a8cdf215d"))
    print(os.environ.get("a43bd6b6eb4030a589bf0e0a8cdf215d"))
    response = urllib.request.urlopen(url)
    data = response.read()
    jsondata = json.loads(data)

    return render_template ("movie.html", movies=jsondata["results"])

@app.route("/movies")
def get_movies_list():
    url = "https://api.themoviedb.org/3/movie/popular?api_key=a43bd6b6eb4030a589bf0e0a8cdf215d"

    response = urllib.request.urlopen(url)
    data = response.read()
    jsondata = json.loads(data)

    movie_json = []

    for movie in jsondata["results"]:
        movie = {
            "title": movie["title"],
            "overview": movie["overview"],
        }

        movie_json.append(movie)
    print(movie_json)
    return {"movie title": movie_json}


if __name__ == '__main__':
    app.run(debug=True)
