import os,glob
from flask import Flask, render_template, request, redirect, url_for, abort
from werkzeug.utils import secure_filename
import PyPDF2
from PIL import Image
import joblib
from wordcloud import WordCloud, STOPWORDS



app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 5*1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.pdf']
app.config['UPLOAD_PATH'] = 'docs'

@app.route('/')
def main():
    return render_template('home.html')


@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']
        filename = secure_filename(f.filename)

        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                abort(400)  
        f.save(os.path.join(app.config['UPLOAD_PATH'],f.filename))

           
    
        
    # creating a pdf file object
    pdfFileObj = open("docs/"+f.filename, 'rb')
        
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
        
    # printing number of pages in pdf file
    num = pdfReader.numPages
    
    all_text = ""
    # creating a page object
    for i in range(0,num):
        pageObj = pdfReader.getPage(i)
        all_text += pageObj.extractText()
        
    

    # closing the pdf file object
    pdfFileObj.close()
    

    stopwords = set(STOPWORDS)
    wc = WordCloud(background_color="white",
                  stopwords = stopwords)
    wc.generate(all_text)
    wc.to_file("static/images/wordcloud.png")

    return render_template("success.html", name = f.filename)  




@app.route('/Answer', methods=['POST'])
def home():
    cdqa_pipeline= joblib.load('./models/bert_qa_custom.joblib')
    query = request.form['a']
    pred = cdqa_pipeline.predict(query=query)
    return render_template('after.html', data=pred)



# @app.route('/home',methods=['POST'])
# def again():
#     dir = '/files/'
#     filelist = glob.glob(os.path.join(dir, "*"))
#     for f in filelist:
#         os.remove(f)
    
#     return render_template('home.html')



if __name__ == "__main__":
    app.run(debug=True)