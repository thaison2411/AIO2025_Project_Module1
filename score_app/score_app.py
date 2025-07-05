import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
from PIL import Image

def calculate_average(scores):
    return sum(scores) / len(scores) 

def percentage_distribution(scores):
    bins = {'80-100': 0, '60-79': 0, '<60': 0}
    for score in scores:
        if score >= 80:
            bins['80-100'] += 1
        elif score >= 60:
            bins['60-79'] += 1
        else:
            bins['<60'] += 1
    return bins  

def main():
    st.title("Phân tích điểm số học sinh")
    uploaded_file = st.file_uploader("Chon file excel", type=["xlsx"])
    if uploaded_file:
        #read file
        df = pd.read_excel(uploaded_file)
        scores = df["Điểm số"].astype(float).tolist()

        #avarage score
        average_score  = calculate_average(scores)
        st.write(average_score )

        #distribution
        dist = percentage_distribution(scores)
        labels = list(dist.keys())
        values = list(dist.values())
        st.write(dist)

        #show distribution 
        fig, ax = plt.subplots(figsize = (1,1))
        ax.pie(
            values,
            labels=labels,
            autopct='%1.1f%%',
            textprops={'fontsize': 3.5}
        )
        ax.axis('equal')
        plt.tight_layout(pad=0.1)
        buf = io.BytesIO()
        fig.savefig(buf, format='png', dpi=500)
        img = Image.open(buf)
        st.write("Phân bố điểm số")
        st.image(img)



if __name__ == "__main__":
    main()

