import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
        }


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random():
    cafe = random.choice(Cafe.query.all())
    # Option 3 convert to dict then jsonify
    return jsonify(cafe=cafe.to_dict())

    # # OPTION 1 - Flat response of all data
    # return jsonify(
    #     cafe={
    #         "can_take_calls": cafe.can_take_calls,
    #         "coffee_price": cafe.coffee_price,
    #         "has_sockets": cafe.has_sockets,
    #         "has_toilet": cafe.has_toilet,
    #         "has_wifi": cafe.has_wifi,
    #         "id": cafe.id,
    #         "img_url": cafe.img_url,
    #         "location": cafe.location,
    #         "map_url": cafe.map_url,
    #         "name": cafe.name,
    #         "seats": cafe.seats,
    #     }
    # )

    # # OPTION 2 - Grouped responses, ommiting some data
    # return jsonify(
    #     cafe={
    #         # Omit the id from the response
    #         # "id": cafe.id,
    #         "name": cafe.name,
    #         "map_url": cafe.map_url,
    #         "img_url": cafe.img_url,
    #         "location": cafe.location,
    #         # Put some properties in a sub-category
    #         "amenities": {
    #             "seats": cafe.seats,
    #             "has_toilet": cafe.has_toilet,
    #             "has_wifi": cafe.has_wifi,
    #             "has_sockets": cafe.has_sockets,
    #             "can_take_calls": cafe.can_take_calls,
    #             "coffee_price": cafe.coffee_price,
    #         },
    #     }
    # )


@app.route("/all")
def get_all():
    cafes = Cafe.query.all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route("/search")
def search():
    location = request.args.get("loc")
    cafe = Cafe.query.filter_by(location=location).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(
            error={
                "Not Found": "Sorry, we don't have a ccafe at that location"
            }
        )


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Sucessfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
# Put = replace entire record
# patch = update specified fields in record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        new_price = request.args.get("new_price")
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(success="Sucessfully updated the price")
    else:
        return jsonify(error={"Not Found": "No cafe found with that id"}), 404


# HTTP DELETE - Delete Record
@app.route("/delete/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = request.args.get("api_key")
    if api_key != "TopSecretKey":
        return jsonify(error={"Invalid Key": "Invalid API Key"}), 401

    cafe = Cafe.query.get(cafe_id)
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(success="Sucessfully deleted cafe")
    else:
        return jsonify(error={"Not Found": "No cafe found with that id"}), 404


if __name__ == "__main__":
    app.run(debug=True)
