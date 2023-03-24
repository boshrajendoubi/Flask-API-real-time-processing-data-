from flask import Flask , render_template , url_for, request, redirect
from forms import FileForm
import os
from werkzeug.utils import secure_filename
import pandas as pd
from flask import send_from_directory

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'flaskapp'
app.config['UPLOAD_FOLDER'] = 'files'

@app.route('/upload')
def index():
    # Lire le fichier Excel
    # Renvoyer les données sous forme de page HTML
        return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])

def FileUpload():
    # initialiser le nom du fichier 
    FileName= "not yet"
    # récupérer le fichier à partir du formulaire 
    if request.method == 'POST':
        file = request.files['file']
        file_path = 'files/' + file.filename
        FileName=file.filename
        basedir = os.path.abspath(os.path.dirname(__file__))
        file.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], file.filename))
        #Append the files
        df = pd.read_excel(file_path)
        df1 = pd.read_excel('E:/Sauvgarde Dell Bochra/Document/Isg L3/INITBDC/Test/test.xlsx')
        # si les fichiers ont la meme structure de colonnes ---> Append the files 
        if set(df1.columns) == set(df.columns):
            dataframes=[df1,df]
            df_combined = pd.concat(dataframes, axis=0, ignore_index=True)
            #df2 = pd.read_excel('E:/Sauvgarde Dell Bochra/Document/Isg L3/INITBDC/Test/test.xlsx')
            return render_template('forms.html', data= { df.to_html(), df1.to_html(),df_combined.to_html(),FileName })
        else: # si les fichiers n'ont pas la meme structure des colonnes 
            return render_template('forms.html', data = "Les fichiers n'ont pas les mêmes colonnes. Impossible de les joindre.")
    
       
    return render_template('forms.html') 
 


    
    
    
    

if __name__=="__main__":
    app.run(debug=True)