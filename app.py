from flask import Flask, render_template, request, redirect, send_file
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model database
class Transaksi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tanggal = db.Column(db.Date, nullable=False)
    kategori = db.Column(db.String(50), nullable=False)
    jumlah = db.Column(db.Float, nullable=False)
    catatan = db.Column(db.String(200))

with app.app_context():
    db.create_all()

# Halaman utama: input & daftar transaksi
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        tanggal = datetime.strptime(request.form['tanggal'], '%Y-%m-%d')
        kategori = request.form['kategori']
        jumlah = float(request.form['jumlah'])
        catatan = request.form['catatan']

        transaksi = Transaksi(tanggal=tanggal, kategori=kategori, jumlah=jumlah, catatan=catatan)
        db.session.add(transaksi)
        db.session.commit()
        return redirect('/')

    transaksi_list = Transaksi.query.order_by(Transaksi.tanggal.desc()).all()
    return render_template('index.html', transaksi_list=transaksi_list)

# Edit transaksi
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    transaksi = Transaksi.query.get_or_404(id)
    if request.method == 'POST':
        transaksi.tanggal = datetime.strptime(request.form['tanggal'], '%Y-%m-%d')
        transaksi.kategori = request.form['kategori']
        transaksi.jumlah = float(request.form['jumlah'])
        transaksi.catatan = request.form['catatan']
        db.session.commit()
        return redirect('/')
    return render_template('edit.html', transaksi=transaksi)

# Hapus transaksi
@app.route('/delete/<int:id>')
def delete(id):
    transaksi = Transaksi.query.get_or_404(id)
    db.session.delete(transaksi)
    db.session.commit()
    return redirect('/laporan')

# Halaman laporan
@app.route('/laporan')
def laporan():
    transaksi_list = Transaksi.query.all()
    total_pemasukan = sum(t.jumlah for t in transaksi_list if t.jumlah > 0)
    total_pengeluaran = sum(abs(t.jumlah) for t in transaksi_list if t.jumlah < 0)
    saldo = total_pemasukan - total_pengeluaran
    return render_template('laporan.html',
                           pemasukan=total_pemasukan,
                           pengeluaran=total_pengeluaran,
                           saldo=saldo,
                           transaksi_list=transaksi_list)

# Cetak PDF
from flask import flash
app.secret_key = "rahasia123"

@app.route('/laporan/pdf')
def laporan_pdf():
    transaksi_list = Transaksi.query.all()

    if not transaksi_list:  # kalau kosong
        flash("Tidak ada data transaksi untuk dicetak PDF!", "error")
        return redirect('/laporan')

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.setFont("Helvetica", 12)
    p.drawString(30, 750, "Laporan Keuangan Anak Kos")
    p.drawString(30, 735, f"Tanggal Cetak: {datetime.now().strftime('%d-%m-%Y')}")

    y = 700
    for t in transaksi_list:
        line = f"{t.tanggal.strftime('%d-%m-%Y')} | {t.kategori} | {rupiah_format(t.jumlah)} | {t.catatan}"
        p.drawString(30, y, line)
        y -= 20
        if y < 50:
            p.showPage()
            y = 750
            
    p.save()
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="laporan_keuangan.pdf", mimetype='application/pdf')

# Fungsi format rupiah
@app.template_filter('rupiah')
def rupiah_format(value):
    try:
        value = float(value)
        return "Rp {:,.0f}".format(value).replace(",", ".")
    except:
        return value

if __name__ == '__main__':
    app.run(debug=True)
