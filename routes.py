from flask import Blueprint, render_template, request
from forms import AddSearchForm
from func import Maxlength
from Key import Key
import requests, json

routes = Blueprint("routes", __name__, static_folder= "static", template_folder="template")

url = "https://jikan1.p.rapidapi.com/search/"
host = "jikan1.p.rapidapi.com"

headers = {'x-rapidapi-host': host,'x-rapidapi-key': Key}

@routes.route('/', methods = ["GET", "POST"])
def home():
    form = AddSearchForm()
    if form.validate_on_submit():
        name = form.searchinput.data
        return redirect("/search")
    else:
        
        return render_template("home.html")

@routes.route('/search', methods = ["GET", "POST"])
def search():
    form = AddSearchForm()
    if form.validate_on_submit():
        return redirect("/search")
    else:
        param1 =request.args["cat"]
        param2 = request.args["Search"]
        test = requests.get(url + param1, headers=headers, params = {'q': param2})
        response = test.json()
        response = response["results"]
        length = Maxlength(response)
        return render_template("search.html",param1=param1, param2=param2,test=test, response=response, length=length)