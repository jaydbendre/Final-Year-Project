import preprocessor as p
import numpy as np 
import pandas as pd 
import emoji
import keras
from sklearn.model_selection import train_test_split
import tensorflow as tf
from keras.models import Sequential
from keras.layers.recurrent import LSTM, GRU,SimpleRNN
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.embeddings import Embedding
from keras.layers.normalization import BatchNormalization
from keras.utils import np_utils
from sklearn import preprocessing, decomposition, model_selection, metrics, pipeline
from keras.layers import GlobalMaxPooling1D, Conv1D, MaxPooling1D, Flatten, Bidirectional, SpatialDropout1D
from keras.preprocessing import sequence, text
from keras.callbacks import EarlyStopping
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
import plotly.graph_objects as go
import plotly.express as px
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import ModelCheckpoint
import transformers
from transformers import TFAutoModel, AutoTokenizer
from tqdm.notebook import tqdm
from tokenizers import Tokenizer, models, pre_tokenizers, decoders, processors
from tqdm import tqdm
import pickle

class SentimentAnalyzer():
    
    sent_to_id  = {"empty":0, "sadness":1,"enthusiasm":2,"neutral":3,"worry":4,
                            "surprise":5,"love":6,"fun":7,"hate":8,"happiness":9,"boredom":10,"relief":11,"anger":12}

    misspell_data = pd.read_csv("Soulage/Extras/aspell.txt",sep=":",names=["correction","misspell"])
    misspell_data.misspell = misspell_data.misspell.str.strip()
    misspell_data.misspell = misspell_data.misspell.str.split(" ")
    misspell_data = misspell_data.explode("misspell").reset_index(drop=True)
    misspell_data.drop_duplicates("misspell",inplace=True)
    miss_corr = dict(zip(misspell_data.misspell, misspell_data.correction))

    contractions = pd.read_csv("Soulage/Extras/contractions.csv")
    cont_dic = dict(zip(contractions.Contraction,contractions.Meaning))

    p.set_options(p.OPT.MENTION,p.OPT.URL)
    max_len = 160
    text = ""
    
    def __init__(self,text):
        with open("Soulage/Extras/tokenizer.pickle","rb") as f:
            token = pickle.load(f)
        self.text = self.clean_text(text)
        self.text = token.texts_to_sequences([self.text])
        self.text = sequence.pad_sequences(self.text, maxlen=self.max_len, dtype='int32')
        
    def misspelled_correction(self,val):
        for x in val.split(): 
            if x in self.miss_corr.keys(): 
                val = val.replace(x, self.miss_corr[x]) 
        return val

    def cont_to_meaning(self,val):
        for x in val.split():
            if x in self.cont_dic.keys():
                val = val.replace(x,self.cont_dic[x])
        return val

    def punctuation(self,val):
        punctuations = '''()-[]{};:'"\,<>./@#$%^&_~'''
    # val = str(val)
        for x in val.lower():
            if x in punctuations:
                val = val.replace(x," ")
        return val

    def clean_text(self,val):
        val = self.misspelled_correction(val)
        val = self.cont_to_meaning(val)
        val = p.clean(val)
        val = ' '.join(self.punctuation(emoji.demojize(val)).split())

        return val

    # @tf.function
    # def get_sentiment(self,text):
    #     text = self.clean_text(text)
    #     # print(text)
    #     model = tf.keras.models.load_model("Soulage/Emotional_analysis_v1")
    #     #tokenize
    #     with open("Soulage/Extras/tokenizer.pickle","rb") as f:
    #         token = pickle.load(f)
    #     twt = token.texts_to_sequences([text])
    #     twt = sequence.pad_sequences(twt, maxlen=self.max_len, dtype='int32')
    #     sentiment = model.predict(twt,batch_size=1,verbose = 2)
    #     sent = np.round(np.dot(sentiment,100).tolist(),0)[0]
    #     result = pd.DataFrame([self.sent_to_id.keys(),sent]).T
    #     result.columns = ["sentiment","percentage"]
    #     result=result[result.percentage !=0]
    #     return result