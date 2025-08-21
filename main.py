import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")