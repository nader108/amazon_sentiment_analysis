import helper
import streamlit as st
import pickle


dt = pickle.load(open("dt.pkl" , "rb"))
SVM = pickle.load(open("svc.pkl" , "rb"))
lr = pickle.load(open("lr.pkl" , "rb"))

text_dt = st.text_input("Enter your review for dt model ")
text_dt = helper.text_preprocessing(text_dt)
pred_dt = dt.predict(text_dt)
if st.button("Predict_dt") :
    pred_dt


text_svm = st.text_input("Enter your review for svm model")
text_svm = helper.text_preprocessing(text_svm)
pred_SVM = SVM.predict(text_svm)
if st.button("Predict_SVM"):
    pred_SVM



text_lr = st.text_input("Enter your review for lr model")
text_lr = helper.text_preprocessing(text_lr)
pred_lr = lr.predict(text_lr)
if st.button("Predict_lr"):
    pred_lr



