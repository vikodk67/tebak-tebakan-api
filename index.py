import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

books = [
    {'id': 0,
     'soal': 'Pintu apa yang didorong nggak bakalan pernah bisa terbuka?',
     'jwab': 'Pintu yang ada tulisannya geser.',
     'author': 'V I K O'},
     {'id': 1,
     'soal': 'Kebo apa yang bikin kita lelah?',
     'jwab': 'Kebogor jalan kaki.',
     'author': 'V I K O'},
     {'id': 2,
     'soal': 'Sandal apa yang paling enak di dunia?',
     'jwab': 'Sandal terasi',
     'author': 'V I K O'},
     {'id': 3,
     'soal': 'Mengapa burung terbang ke selatan saat musim dingin?',
     'jwab': ' Karena jika harus berjalan terlalu jauh.',
     'author': 'V I K O'},
     {'id': 4,
     'soal': 'Rambut putih namanya uban, rambut merah namanya pirang, kalo rambut hijau namanya apa?',
     'jwab': 'Rambutan belum mateng.',
     'author': 'V I K O'},
     {'id': 5,
     'soal': ' Apa bedanya sarung dan kotak?',
     'jwab': 'Kalau sarung itu bisa kotak-kotak kalau kotak tidak bisa sarung-sarung.',
     'author': 'V I K O'},
     {'id': 6,
     'soal': 'Ayam, ayam apa yang nggak bisa makan dan nggak bisa jalan?',
     'jwab': 'Ayam-ayaman.',
     'author': 'V I K O'},
     {'id': 7,
     'soal': 'Sepatu, sepatu apa yang bisa di pakai masak?',
     'jwab': 'Sepatula (Spatula).',
     'author': 'V I K O'},
     {'id': 8,
     'soal': 'Telor, telor apa yang diinjak nggak pecah?',
     'jwab': 'Telortoar.',
     'author': 'V I K O'},
     {'id': 9,
     'soal': 'Jam, jam apa yang jarumnya muter ke kiri?',
     'jwab': 'Jam Kidal.',
     'author': 'V I K O'},
     {'id': 10,
     'soal': 'Buah apa yang bisa menampung banyak barang?',
     'jwab': 'Leci meja.',
     'author': 'V I K O'},
     {'id': 11,
     'soal': 'Buah apa yang pernah menjajah Indonesia?',
     'jwab': 'Terong Belanda.',
     'author': 'V I K O'},
     {'id': 12,
     'soal': 'Buah apa yang lucu suka bikin ketawa?',
     'jwab': 'Buahahahaha.',
     'author': 'V I K O'},
     {'id': 13,
     'soal': 'Penyanyi luar negeri yang suka bersepeda?',
     'jwab': 'Selena Gowes.',
     'author': 'V I K O'},
     {'id': 14,
     'soal': 'Penyanyi luar negeri yang susah menelan?',
     'jwab': 'Ed Sered.',
     'author': 'V I K O'},
     {'id': 15,
     'soal': 'Sayur apa yang pintar nyanyi?',
     'jwab': 'Kolplay.',
     'author': 'V I K O'},
     {'id': 16,
     'soal': 'Sayur apa yang sukanya nunjuk orang lain?',
     'jwab': 'Sayur lo deh.',
     'author': 'V I K O'},
     {'id': 17,
     'soal': 'Saya ada jeruk lima kamu minta minta satu, sisanya berapa?',
     'jwab': 'Ya tetap lima soalnya kamu nggak dikasih.',
     'author': 'V I K O'},
     {'id': 18,
     'soal': 'Minyak, minyak apa yang disukai laki-laki?',
     'jwab': 'Minyaksikan pertandingan sepak bola.',
     'author': 'V I K O'},
     {'id': 19,
     'soal': 'Siapa yang biasanya adzan di TV?',
     'jwab': 'Saat. (ingat tulisan saat adzan maghrib untuk daerah jakarta dan sekitarnya).',
     'author': 'V I K O'},
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>TEBAK TEBAKAN GAJE API</h1>
<p>Status: ONLINE</p><br><a href="/api/books/all">OPEN DOCS</a>'''


@app.route('/api/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/api/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: Tidak ada bidang id yang disediakan Harap tentukan id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()