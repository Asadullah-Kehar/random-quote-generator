import streamlit as st
import requests
import random

st.set_page_config(page_title="Random Quote Generator", page_icon="💡")

# App title
st.title("💡 Random Quote Generator")

# Option to choose source
source = st.radio("Choose quote source:", ["Static List", "Online API"])

# Static list of quotes
quotes = [
    "The best way to get started is to quit talking and begin doing. – Walt Disney",
    "Don’t let yesterday take up too much of today. – Will Rogers",
    "It’s not whether you get knocked down, it’s whether you get up. – Vince Lombardi",
    "If you are working on something exciting, it will keep you motivated. – Steve Jobs",
    "Success is not in what you have, but who you are. – Bo Bennett",
    "Happiness is not something ready-made. It comes from your own actions. – Dalai Lama",
    "In the middle of every difficulty lies opportunity. – Albert Einstein"
]

# Generate button
if st.button("✨ Generate Quote"):
    if source == "Static List":
        quote = random.choice(quotes)
        st.success(quote)
    else:
        try:
            response = requests.get("https://api.quotable.io/random")
            if response.status_code == 200:
                data = response.json()
                st.success(f"{data['content']} – {data['author']}")
            else:
                st.error("⚠️ Could not fetch quote. Try again!")
        except:
            st.error("⚠️ Error connecting to the API.")

# Footer
st.caption("Made with ❤️ using Streamlit on Hugging Face")
