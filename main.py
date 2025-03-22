from flask import Flask, render_template

app = Flask(__name__)


def home():
    return render_template('home.html')

def community():
    return render_template("community.html")

def news():
    return render_template("news.html")

def sales():
    return render_template("sales.html")

def valheim():
    return render_template("valheim.html")

def reddeadredemption2():
    return render_template("reddeadredemption2.html")

def deeprockgalactic():
    return render_template("deeprockgalactic.html")

def factorio():
    return render_template("factorio.html")

def kingdomcomedeliverance2():
    return render_template("kingdomcomedeliverance2.html")

app.add_url_rule("/kingdomcomedeliverance2","kingdomcomedeliverance2", kingdomcomedeliverance2, methods=["GET","POST"])
app.add_url_rule("/factorio","factorio", factorio, methods=["GET","POST"])
app.add_url_rule("/deeprockgalactic","deeprockgalactic", deeprockgalactic, methods=["GET","POST"])
app.add_url_rule("/reddeadredemption2","reddeadredemption2", reddeadredemption2, methods=["GET","POST"])
app.add_url_rule("/valheim","valheim", valheim, methods=["GET","POST"])
app.add_url_rule("/","home", home, methods=["GET","POST"])
app.add_url_rule("/community","community", community, methods=["GET","POST"])
app.add_url_rule("/news","news", news, methods=["GET","POST"])
app.add_url_rule("/sales","sales", sales , methods=["GET","POST"])

app.run(debug=True)
