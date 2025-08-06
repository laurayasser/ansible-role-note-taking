from flask import Flask, request, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__, template_folder='templates')

def init_db():
    conn = sqlite3.connect('notes.db')
    conn.execute('CREATE TABLE IF NOT EXISTS notes (timestamp TEXT, content TEXT)')
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    init_db()
    if request.method == 'POST':
        note = request.form['note']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        conn = sqlite3.connect('notes.db')
        conn.execute('INSERT INTO notes (timestamp, content) VALUES (?, ?)', (timestamp, note))
        conn.commit()
        conn.close()
    conn = sqlite3.connect('notes.db')
    notes = conn.execute('SELECT * FROM notes ORDER BY rowid DESC').fetchall()
    conn.close()
    return render_template('index.html', notes=notes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
