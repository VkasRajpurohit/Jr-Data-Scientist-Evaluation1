import boto3
import pandas as pd

from flask import Flask, render_template, request
from flask_cors import cross_origin
from werkzeug.utils import secure_filename


# Self written module
from Logging import logger
from data_preprocessing.text_preprocessor import Text_Preprocessor
from data_preprocessing.sentiment_checker import SentimentAnalyzer


BUCKET_NAME = 'review-ratings'
s3 = boto3.resource(service_name='s3',
                    region_name='us-east-1',
                    aws_access_key_id='AKIAWEUQWUKRPX2PJLFY',
                    aws_secret_access_key='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')

app = Flask(__name__)  # app as object created
logger.lg.info('app start- working fine')  # from Logging import logger
ALLOWED_EXTENSIONS = {'csv'}


@app.route('/', methods=['GET', 'POST'])  # To render Home_Page
@cross_origin()
def home_page():
    """landing to home_page"""
    logger.lg.info('landing on home page- working fine')
    return render_template('index.html')


@app.route('/about')  # To render about page
@cross_origin()
def about():
    """about the app information"""
    logger.lg.info('about page- working fine')
    return render_template('about.html')


@app.route('/contact')  # To render contact page
@cross_origin()
def contact():
    """contact information"""
    logger.lg.info('contact page- working fine')
    return render_template('contact.html')


@app.route('/Process_file', methods=['GET', 'POST'])  # To render result page
@cross_origin()
def Process_file():
    """It will process the file uploaded by user & display result.
       Written by : Vikram Singh
       Date: 05/02/2022"""

    if request.method == 'POST':
        logger.lg.info('Request = POST.')
        try:
            try:
                uploaded_file = request.files['uploaded_file']
                if uploaded_file:
                    filepath = secure_filename(uploaded_file.filename)
                    # for security : secure_filename(uploaded_file.filename)
                    uploaded_file.save(filepath)
                    s3.Bucket(BUCKET_NAME).upload_file(Filename=filepath, Key=filepath)   # Upload files to S3 bucket
                    logger.lg.info('File uploaded successfully.')
            except Exception as e:
                logger.lg.warning('unable to complete request: {}'.format(e))

            logger.lg.info('Process started.')
            try:
                # Load csv file directly from S3 bucket
                obj = s3.Bucket(BUCKET_NAME).Object(filepath).get()
                csv_file = pd.read_csv(obj['Body'], index_col=0)
                logger.lg.info('Reading uploaded CSV file.')
            except Exception as e:
                logger.lg.warning('unable to complete request: {}'.format(e))

            try:
                data = csv_file[['Text', 'Star']]
                logger.lg.info('Selected only Text & Star Columns.')
            except Exception as e:
                logger.lg.warning('unable to complete request: {}'.format(e))

            logger.lg.info('Text Preprocessing Started.')
            # from data_preprocessing.text_preprocessor import Text_Preprocessor
            run = Text_Preprocessor()
            try:
                data = data.dropna(axis=0)
                logger.lg.info('Removed all the rows having null values.')
                data["Text"] = data["Text"].apply(lambda x: run.remove_html_tags(x))
                logger.lg.info('Removed html tags.')
                data["Text"] = data["Text"].apply(lambda x: run.remove_unwanted_bracs(x))
                logger.lg.info('Removed all the unwanted brackets.')
                data["Text"] = data["Text"].apply(lambda x: run.remove_links(x))
                logger.lg.info('Removed all the links present.')
                data_text_cleaner = data["Text"].apply(lambda x: run.text_cleaner(x))
                logger.lg.info('Performed all the basic text cleaning steps & removed all the stopwords present.')
                logger.lg.info('Text Preprocessing Completed successfully.')
            except Exception as e:
                logger.lg.warning('unable to complete request: {}'.format(e))

            # from data_preprocessing.sentiment_checker import SentimentAnalyzer
            logger.lg.info('checking sentiments.')
            sa = SentimentAnalyzer()
            try:
                sentiment_polarity, compound = sa.sentiments(data_text_cleaner)
                data['Sentiments'] = compound.apply(lambda c: 'Positive' if c > 0.4 else ('Negative' if c < 0 else 'Neutral'))
                logger.lg.info('checking sentiments analysis completed.')
            except Exception as e:
                logger.lg.warning('unable to complete request: {}'.format(e))

            check_attention = data[(data["Sentiments"] == "Positive") & (data["Star"] < 2)]
            logger.lg.info('Process completed successfully.')
            return render_template('result.html', data=check_attention.to_html())
        except Exception as e:
            logger.lg.warning('unable to complete request: {}'.format(e))


if __name__ == '__main__':  # on running python main.py
    app.run(debug=True)
