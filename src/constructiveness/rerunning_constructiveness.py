#!/usr/bin/env python
__author__ = 'VasundharaGautam'

import csv
import os
import sys

import pandas as pd

from bs4 import BeautifulSoup
sys.path.append(os.environ['HOME'] + 'src/models/')
from constructiveness_predictor import ConstructivenessPredictor

DATA_DIR = os.environ['HOME'] + 'data/'
CONVERSATION_FILE = os.path.join(DATA_DIR, 'the_conversation.csv')
CONVERSATION_OUTFILE = 'conversation_constructiveness_results.csv'

TYEE_FILE = os.path.join(DATA_DIR, 'the_tyee_posts_preprocessed.csv')
TYEE_OUTFILE = 'tyee_constructiveness_results.csv'

SOCC_FILE = os.path.join(DATA_DIR, 'gnm_comments.csv')
SOCC_OUTFILE = 'socc_constructiveness_results.csv'

def getCleanText(row):
    return BeautifulSoup(row, features='lxml').text

def main():
    predictor = ConstructivenessPredictor()
    
     df = pd.read_csv(CONVERSATION_FILE, low_memory=False).dropna()
     df['cleaned'] = df['Comment body'].apply(getCleanText)
     df = df[df['cleaned'] != ''][['cleaned', 'Article ID', 'Comment ID']]
    
     with open(CONVERSATION_OUTFILE, 'w') as fo:
         writer = csv.writer(fo)
         writer.writerow(['article_id', 'comment_id', 'bilstm_prediction', 'cnn_prediction', 'comment_text'])
        
         for i,row in df.iterrows():
             bilstm_prediction = predictor.predict_bilstm(row['cleaned'])[-5:-1]
             cnn_prediction = predictor.predict_cnn(row['cleaned'])[-5:-1]

             writer.writerow([row['Article ID'],
                              row['Comment ID'],
                              bilstm_prediction,
                              cnn_prediction,
                              row['cleaned']])
            
    df = pd.read_csv(TYEE_FILE, low_memory=False).dropna(axis=0, subset=['message_preprocessed'])
    df['cleaned'] = df['message_preprocessed'].apply(getCleanText)
    df = df[df['cleaned'] != ''][['cleaned', 'post_id', 'thread_id']]
    
    print(len(df))
    
    with open(TYEE_OUTFILE, 'w') as fo:
        writer = csv.writer(fo)
        writer.writerow(['post_id', 'thread_id', 'bilstm_prediction', 'cnn_prediction', 'comment_text'])
        
        for i,row in df.iterrows():
            bilstm_prediction = predictor.predict_bilstm(row['cleaned'])[-5:-1]
            cnn_prediction = predictor.predict_cnn(row['cleaned'])[-5:-1]

            writer.writerow([row['post_id'],
                             row['thread_id'],
                             bilstm_prediction,
                             cnn_prediction,
                             row['cleaned']])
            
     df = pd.read_csv(SOCC_FILE, low_memory=False) 
     df['cleaned'] = df['comment_text'].apply(getCleanText)
     df = df[df['cleaned'] != ''][['cleaned', 'article_id', 'comment_id']]
    
     with open(SOCC_OUTFILE, 'w') as fo:
         writer = csv.writer(fo)
         writer.writerow(['article_id', 'comment_id', 'bilstm_prediction', 'cnn_prediction', 'comment_text'])
        
         for i,row in df.iterrows():
             bilstm_prediction = predictor.predict_bilstm(row['cleaned'])[-5:-1]
             cnn_prediction = predictor.predict_cnn(row['cleaned'])[-5:-1]

             writer.writerow([row['article_id'],
                              row['comment_id'],
                              bilstm_prediction,
                              cnn_prediction,
                              row['cleaned']])

if __name__== '__main__':
    main()
