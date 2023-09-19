from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
import pandas as pd
from app.utils import data_processing, data_visualization

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and data_processing.allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        df = data_processing.load_data(filepath)
        return render_template('dashboard.html', df=df)

@app.route('/edit', methods=['GET', 'POST'])
def edit_data():
    if request.method == 'POST':
        # Aqui, você pode processar os dados do formulário e salvar as alterações.
        # Por exemplo, se você tiver um campo de formulário chamado 'grupo', você pode acessá-lo com request.form['grupo']

        grupo = request.form.get('grupo')
        vlr_venda = request.form.get('vlr_venda')
        # ... e assim por diante para outros campos

        # Aqui, você pode adicionar a lógica para salvar esses dados em um banco de dados ou arquivo.

        flash('Dados atualizados com sucesso!', 'success')
        return redirect(url_for('dashboard'))  # Supondo que você tenha uma função de rota chamada 'dashboard'

    return render_template('edit_data.html')
