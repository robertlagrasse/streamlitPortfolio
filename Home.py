import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.jpeg', use_column_width=True)
with col2:
    st.title('Grandmaster Groove')
    content = '''
    Ladies and gentlemen, allow me to introduce you to Grandmaster Groove, the funky fly python programmer extraordinaire. With his infectious energy and unparalleled programming skills, Grandmaster Groove has become a legend in the tech world.

But Grandmaster Groove's legendary mojo is not just a result of his technical prowess. No, his secret lies in the funk stone, a rare and mystical gem that he discovered on a trip to the Congo. Legend has it that the funk stone has the power to imbue its bearer with an irresistible groove, and Grandmaster Groove has certainly felt its effects.

With the funk stone by his side, Grandmaster Groove has become the go-to programmer for clients looking for not just great code, but a truly funky experience. His programs aren't just functional; they're a feast for the senses, with beats that make you want to dance and visuals that dazzle the eye. So if you're looking for a programmer who can bring the funk, look no further than Grandmaster Groove.
    '''
    st.write(content)

content = '''
According to chatGPT:
If you're a jive turkey who wants to stay relevant in the tech world, you better bow down before Grandmaster Groove. He's the baddest dude around, and he's not afraid to show it.
'''
st.write(content)

df = pandas.read_csv('data/data.csv',sep=',')

midpoint = int(len(df)/2)
col3, empty, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:midpoint].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'], use_column_width=True)
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[midpoint:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'], use_column_width=True)
        st.write(f"[Source Code]({row['url']})")