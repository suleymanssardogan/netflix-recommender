
import pandas as pd
import streamlit as st

df = pd.read_csv("Data/netflix_cleaned.csv")


page_bg_img = '''
<style>
.stApp {
  background-image: url("images/cinema.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: fixed;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("🎬 Netflix Movie and Series Recommender Systems")
st.header("Welcome Let's Enjoy Time")
#Category
genres = df["listed_in"].str.split(", ").explode().unique()

selected_genres = st.selectbox("What kind of movie do you want to watch? ",sorted(genres))

filtered_df = df[df["listed_in"].str.contains(selected_genres,case=False,na=False)]
st.subheader(f"Have Founded {len(filtered_df)} about {selected_genres}")
st.dataframe(filtered_df[["title","type","listed_in","description"]].reset_index(drop=True))
