from json.decoder import JSONDecodeError
from flask import Flask, request, jsonify
import secrets
import random
import json

facts = [
    "You can tell the temperature by counting a cricket’s chirps!",
    "Sandstorms can swallow up entire cities",
    "Dirt mixed with wind can make dust storms called black blizzards.",
    "A mudslide can carry rocks, trees, vehicles and entire buildings!",
    "The coldest temperature ever officially recorded was -89.2°C. Brrrr!",
    "Mild autumn weather often means bigger spiders in our homes.",
    "A heatwave can make train tracks bend!",
    "About 2,000 thunderstorms rain down on Earth every minute.",
    "A 2003 heatwave turned grapes to raisins before they were picked from the vine!",
    "Lightning often follows a volcanic eruption.",
    "Raindrops can be the size of a housefly and fall at more than 30kmph.",
    "Cape Farewell in Greenland is the windiest place on the planet.",
    "Hurricanes can push more than 6m of water ashore.",
    "In July 2001 the rainfall in Kerala, India, was blood red!",
    "Blizzards can make snowflakes feel like pellets hitting your face.",
    "A hurricane in Florida, USA, caused 900 captive pythons to escape.",
    "Worms wriggle up from underground when a flood is coming.",
    "A thunderstorm can produce 160kmph winds!",
    "In Antarctica, snow can fall so hard you can’t see your hand in front of your face.",
    "A whiteout or heavy snowfall that makes it difficult to see, can make you feel sick.",
    "Wildfires sometimes create tornadoes made of fire called fire whirls.",
    "Some tornadoes can be faster than formula one racing cars!",
    "Black ice, a transparent coating of ice on a surface, can make pavements super-slippery.",
    "Some frogs get noisier just before it rains.",
    "Waterspouts, or rotating columns of air over water, can make sea creatures rain down from the sky.",
    "The most damage ever caused by a thunderstorm was in 1995, when hailstones bigger than cricket balls fell in Texas, USA.",
    "In 1684, it was so cold that the River Thames froze solid for two months.",
    "Cats and dogs have been known to sense when a tornado is approaching.",
    "Mawsynram, India, receives an average of 467 inches of rain per year, making it the wettest place on Earth.",
    "Around 100 lightning strikes hit Earth every second.",
    "Thunder is the sound caused by the rapid expansion of air due to the heat from lightning, which can reach up to 54,000°F — hotter than the surface of the sun!",
    "Tornadoes can spin at speeds up to 300 mph (480 km/h), which is faster than the top speed of a commercial airplane.",
    "The coldest temperature ever recorded on Earth was -128.6°F (-89.2°C) in Antarctica on July 21, 1983.",
    "A full circle rainbow can often be seen from the air or on high mountains, but we usually see only a half-circle because the ground blocks the rest of the arc.",
    "The highest cloud recorded was at about 85,000 feet (25,900 meters) above the Earth’s surface, higher than some commercial jets fly!",
    "Hailstones can grow to the size of softballs, but typically they range from pea-size to golf ball size.",
    "The fastest wind speed ever recorded was 253 mph (407 km/h) in Australia during Cyclone Olivia in 1996.",
    "No two snowflakes are exactly alike, but they all have six sides, due to the molecular structure of ice.",
    "Heat lightning is just lightning that occurs too far away for the thunder to be heard. It can be seen on the horizon during warm, humid nights.",
    "Fog is made up of tiny water droplets suspended in the air, and it can reduce visibility to as little as 10 feet (3 meters) or even less.",
    "Deserts can sometimes receive rain only once every few years, but when it does rain, the landscape can change almost overnight into a colorful floral display.",
    "The Coriolis Effect is responsible for the rotation direction of large weather systems: it causes storms in the Northern Hemisphere to rotate counterclockwise and clockwise in the Southern Hemisphere.",
    "There are four main cloud types: cirrus, cumulus, stratus, and nimbus. Each one has distinct characteristics and weather implications.",
    "The Northern and Southern Lights (Auroras Borealis and Australis) are caused by particles from the Sun interacting with the Earth's magnetic field, creating colorful light displays.",
    "Some hurricanes can be over 500 miles (800 km) wide, with their winds reaching speeds of over 200 mph (320 km/h)."
]

app = Flask(__name__)
save_file = 'favorites.json'


def read_favorites():
    try:
        with open(save_file, "r") as f:
            return json.load(f)
    except (FileNotFoundError, JSONDecodeError) as e:
        print("error", e)
        return {}


def write_favorites(data):
    with open(save_file, "w") as f:
        json.dump(data, f)


@app.route('/fact', methods=['GET'])
def get_random_fact():
    random_fact = random.choice(facts)
    return jsonify({ "fact": random_fact }), 200


@app.route('/favorites', methods=['GET'])
def get_favorites():
    try:
        favorites = read_favorites()
        return jsonify({ "favorites": favorites }), 200
    except OSError as e:
        print("error", e)
        return jsonify({ "error": "Internal Server Error" }), 500


@app.route('/favorites', methods=['POST'])
def post_favorite():
    data = request.get_json(force=True, silent=True)
    if not data or "fact" not in data:
        return jsonify({ "error": "Missing 'fact' property in body" }), 400

    try:
        favorites = read_favorites()
        fact = data.get('fact')
        id = next((k for k, v in favorites.items() if v == fact), None)

        if id == None:
            id = secrets.token_hex(8)
            favorites[id] = fact
            write_favorites(favorites)

        return jsonify({ "id": id }), 200
    except (OSError, JSONDecodeError) as e:
        print("error", e)
        return jsonify({ "error": "Internal Server Error" }), 500


@app.route('/favorites/<string:id>', methods=['DELETE'])
def delete_favorite(id):
    try:
        favorites = read_favorites()
        n = favorites.pop(id, None)
        write_favorites(favorites)
        return jsonify({ 'n': 0 if n == None else 1 }), 200
    except (OSError, JSONDecodeError) as e:
        print("error", e)
        return jsonify({ "error": "Internal Server Error" }), 500


if __name__ == '__main__':
    app.run(debug=True)

