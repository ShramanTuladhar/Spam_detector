import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer

model_path= r"C:\Users\shram\OneDrive\Desktop\spam_detector\model\spam_detector.pickle"
with open (model_path,"rb") as f:
    model= pickle.load(f)

def predict_spam(text):
   
    prediction= model.predict([text])

    return prediction

st.title('Email Spam Detection App')

# Getting input text from the user
email_text = st.text_area("Enter the email text you want to analyze:")

# Initialize predicted to None
predicted = None

# When 'Analyze' is clicked, make the prediction and display it
if st.button('Analyze'):
    predicted = predict_spam(email_text)

# Display the result
if predicted is not None:
    if predicted[0] == 0:
        st.write("This email is likely **Spam**.")
    else:
        st.write("This email is probably **Not Spam**. Relax!")


