from flask import Flask, render_template

app = Flask(__name__)

PLACES = [
    {
        "rank": 1,
        "name": "Vidhana Soudha",
        "category": "landmarks",
        "tags": ["Heritage", "Architecture"],
        "description": "An iconic Bengaluru landmark known for its grand Neo-Dravidian architecture.",
        "image": "https://commons.wikimedia.org/wiki/Special:FilePath/Vidhana%20Soudha%20in%20Bengaluru.jpg?width=1600",
        "map": "https://www.google.com/maps?q=Vidhana+Soudha,+Bengaluru&output=embed",
        "maps_link": "https://www.google.com/maps/search/?api=1&query=Vidhana+Soudha+Bengaluru"
    },
    {
        "rank": 2,
        "name": "Bengaluru Palace",
        "category": "landmarks",
        "tags": ["Heritage", "Palace"],
        "description": "A historic palace surrounded by gardens and known for its distinctive architecture.",
        "image": "https://commons.wikimedia.org/wiki/Special:FilePath/Bengaluru%20Palace.jpg?width=1600",
        "map": "https://www.google.com/maps?q=Bengaluru+Palace&output=embed",
        "maps_link": "https://www.google.com/maps/search/?api=1&query=Bengaluru+Palace"
    },
    {
        "rank": 3,
        "name": "Lalbagh Botanical Garden",
        "category": "nature",
        "tags": ["Nature", "Garden"],
        "description": "A large botanical garden famous for its greenery, glass house and flower shows.",
        "image": "https://commons.wikimedia.org/wiki/Special:FilePath/LalBagh%2CBangalore.jpg?width=1600",
        "map": "https://www.google.com/maps?q=Lalbagh+Botanical+Garden+Bengaluru&output=embed",
        "maps_link": "https://www.google.com/maps/search/?api=1&query=Lalbagh+Botanical+Garden+Bengaluru"
    },
    {
        "rank": 4,
        "name": "Cubbon Park",
        "category": "nature",
        "tags": ["Nature", "Walks"],
        "description": "A green urban retreat in central Bengaluru, ideal for walks and relaxed sightseeing.",
        "image": "https://commons.wikimedia.org/wiki/Special:FilePath/Cubbon%20Park%20Bangalore.jpg?width=1200",
        "map": "https://www.google.com/maps?q=Cubbon+Park+Bengaluru&output=embed",
        "maps_link": "https://www.google.com/maps/search/?api=1&query=Cubbon+Park+Bengaluru"
    },
    {
        "rank": 5,
        "name": "ISKCON Temple",
        "category": "temples",
        "tags": ["Temple", "Spiritual"],
        "description": "A prominent temple complex on Chord Road, combining traditional and modern design.",
        "image": "https://commons.wikimedia.org/wiki/Special:FilePath/ISKCON%20Temple%20Bangalore.jpg?width=1200",
        "map": "https://www.google.com/maps?q=ISKCON+Temple+Bangalore&output=embed",
        "maps_link": "https://www.google.com/maps/search/?api=1&query=ISKCON+Temple+Bangalore"
    },
    {
        "rank": 6,
        "name": "Nandi Hills",
        "category": "hills",
        "tags": ["Hills", "Sunrise"],
        "description": "A popular hill destination near Bengaluru, especially known for sunrise views.",
        "image": "https://commons.wikimedia.org/wiki/Special:FilePath/Nandi%20Hills%2C%20Bengaluru.jpg?width=1600",
        "map": "https://www.google.com/maps?q=Nandi+Hills,+Karnataka&output=embed",
        "maps_link": "https://www.google.com/maps/search/?api=1&query=Nandi+Hills+Karnataka"
    },
    {
    "rank": 7,
    "name": "Commercial Street",
    "category": "shopping",
    "tags": ["Shopping", "Street Food"],
    "description": "One of Bengaluru's well-known shopping streets for fashion, accessories and local finds.",
    "image": "https://commons.wikimedia.org/wiki/Special:FilePath/Commercial%20Street%20Bangalore.jpg?width=1600",
    "map": "https://www.google.com/maps?q=Commercial+Street+Bengaluru&output=embed",
    "maps_link": "https://www.google.com/maps/search/?api=1&query=Commercial+Street+Bengaluru"
},

    {
        "rank": 8,
        "name": "Church Street",
        "category": "party",
        "tags": ["Cafes", "Bookshops", "Walks"],
        "description": "A pedestrian-friendly Central Business District street known for its cafes, restaurants, bookshops and evening buzz. It runs beside Brigade Road, making it easy to explore both on foot.",
        "image": "https://commons.wikimedia.org/wiki/Special:FilePath/Bangalore_Church_street_trees_1.jpg?width=1600",
        "photo_credit": "Photo: T. R. Shankar Raman (CC BY-SA 4.0)",
        "photo_source": "https://commons.wikimedia.org/wiki/File:Bangalore_Church_street_trees_1.jpg",
        "research_source": "https://site.bbmp.gov.in/departmentwebsites/Eng/pdf/Road%20Infrastructure/INFRASTRUCTURE%20ASSESSMENT%20OF%20CHURCH%20STREET%20AND%20SCOPE%20FOR%20PEDESTRIANIZATION_FINAL.pdf",
        "research_credit": "BBMP Church Street infrastructure assessment",
        "map": "https://www.google.com/maps?q=Church+Street+Bengaluru&output=embed",
        "maps_link": "https://www.google.com/maps/search/?api=1&query=Church+Street+Bengaluru"
    },
    {
        "rank": 9,
        "name": "MG Road",
        "category": "food",
        "tags": ["Food", "Shopping"],
        "description": "A central Bengaluru destination surrounded by restaurants, cafes, shops and city attractions.",
        "image": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=1400&q=85",
        "map": "https://www.google.com/maps?q=MG+Road+Bengaluru&output=embed",
        "maps_link": "https://www.google.com/maps/search/?api=1&query=MG+Road+Bengaluru"
    },
    {
        "rank": 10,
        "name": "UB City",
        "category": "shopping",
        "tags": ["Luxury Shopping", "Dining", "Architecture"],
        "description": "A mixed-use luxury destination in Bengaluru's central business district on Vittal Mallya Road. The Collection brings designer boutiques together with restaurants and cafes, making it a good stop for shopping or an evening meal.",
        "image": "https://commons.wikimedia.org/wiki/Special:FilePath/UB_City%2C_Bangalore.JPG?width=1600",
        "photo_credit": "Photo: Prateek Karandikar (CC BY-SA)",
        "photo_source": "https://commons.wikimedia.org/wiki/File:UB_City,_Bangalore.JPG",
        "research_source": "https://ubcitybangalore.in/about/",
        "research_credit": "UB City official website",
        "map": "https://www.google.com/maps?q=UB+City+Bengaluru&output=embed",
        "maps_link": "https://www.google.com/maps/search/?api=1&query=UB+City+Bengaluru"
    },
]

HEROES = [
    {
        "name": "Vidhana Soudha",
        "eyebrow": "01 / ICONIC BENGALURU",
        "text": "Start with the city’s most recognisable landmark.",
        "image": "https://commons.wikimedia.org/wiki/Special:FilePath/Vidhana%20Soudha%20in%20Bengaluru.jpg?width=2000",
    },
    {
        "name": "Bengaluru Palace",
        "eyebrow": "02 / ROYAL HERITAGE",
        "text": "Step into Bengaluru’s historic palace atmosphere.",
        "image": "https://commons.wikimedia.org/wiki/Special:FilePath/Bengaluru%20Palace.jpg?width=2000",
    },
    {
        "name": "Lalbagh",
        "eyebrow": "03 / GREEN BENGALURU",
        "text": "Slow down among gardens, trees and botanical beauty.",
        "image": "https://commons.wikimedia.org/wiki/Special:FilePath/LalBagh%2CBangalore.jpg?width=2000",
    },
    {
        "name": "Cubbon Park",
        "eyebrow": "04 / CITY ESCAPE",
        "text": "Find a calm green space in the heart of the city.",
        "image": "https://commons.wikimedia.org/wiki/Special:FilePath/Cubbon%20Park.jpg?width=1600",
    },
    {
        "name": "Nandi Hills",
        "eyebrow": "05 / HILLS & SUNRISE",
        "text": "Chase cool air, clouds and sunrise views outside the city.",
        "image": "https://commons.wikimedia.org/wiki/Special:FilePath/Nandi%20Hills%2C%20Bengaluru.jpg?width=2000",
    },
]

@app.route("/")
def home():
    return render_template("index.html", places=PLACES, heroes=HEROES)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
