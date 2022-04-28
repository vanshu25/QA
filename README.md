# BERT QUESTION ANSWERING FLASK APP

This is a flask app that performs question-answering on various pdf files. You can use bunch of pdf files and can get contextual answers, either exact or most simillar, to given question. These days pdf files are generating at a very large scale. Using pdf files is really easy and can be useful in many cases. For example, you have a set of pdf files of annual reports of a company or have any other large number of pdf files from which you want to extract data then building a question-answering system can be very beneficial.

![](https://github.com/vanshu25/Flask-App-for-answering-questions/blob/main/images/1.png)

## Project Structure

### Folder for Pdf documents - docs

* When you will upload the pdf file, it will get stored in this folder.


### Folder for visualisation images - Static/Images
* This is the folder where the wordcloud visualisation of uploaded pdf file will be stored.


### Models

* Create a folder named "models" and in this folder we are going to download pre-trained model called 'bert-squad_1.1'. This model is pre-trained model on Stanford Question Answering Dataset (SQuAD). 
 
 To download this pre-trained model, run the following in python : <br>
  
   > from cdqa.utils.download import download_model <br>
   > download_model(model='bert-squad_1.1', dir='./models')


### Templates

* Create a folder named "templates" and here we are gonna add our html files for the app. I have added three files here - home.html, success.html, and after.html


### qa.py

* In this python file, we have used the pre trained model which is present in 'models' folder to fit the pdf files.
* We have imported packages like pandas, cdqa, etc. So, you must download these packages.
* First, we have converted the pdf files to pandas dataframe by using 'pdf_converter' which we have imported from 'cdqa.utils.converters'
* Then, we have used 'QAPipeline' which we have imported from 'cdqa.pipeline'. It will create question-answering pipeline and fit our documents.
* At last, we have used 'joblib' which is a set of tools to provide lightweight pipelining in Python.


### app.py

* This contains python code to run flask app where we have specified routes.
* It is also specified that the maximum file size is 5 MB and allowed extension is .pdf

 We have defined a function in this file: <br>
   > app.config['MAX_CONTENT_LENGTH'] = 5*1024 * 1024
     app.config['UPLOAD_EXTENSIONS'] = ['.pdf']


## Running the Flask App

* Activate your virtual environment and then run 'flask run'
* You can then go to the localhost on which the app is running.

![](https://github.com/vanshu25/Flask-App-for-answering-questions/blob/main/images/1.png)
![](https://github.com/vanshu25/Flask-App-for-answering-questions/blob/main/images/3.png)
![](https://github.com/vanshu25/Flask-App-for-answering-questions/blob/main/images/4.png)
