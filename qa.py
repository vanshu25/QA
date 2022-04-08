import pandas as pd


from cdqa.utils.converters import pdf_converter
from cdqa.pipeline import QAPipeline
from cdqa.utils.download import download_model   

download_model(model='bert-squad_1.1', dir='./models')

df = pdf_converter(directory_path='./docs/')
pd.set_option('display.max_colwidth',None)
cdqa_pipeline = QAPipeline(reader='./models/bert_qa.joblib')

cdqa_pipeline.fit_retriever(df)
import joblib
joblib.dump(cdqa_pipeline, './models/bert_qa_custom.joblib')