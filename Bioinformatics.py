import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

image = Image.open('DNA.png')

st.image(image, use_column_width=True)

st.write("""
         # Bio-Informatics DNA Count Web App
        This App counts the Nucleotide composition of the query DNA
        ***
        """)

st.header('Enter the DNA Sequence : ')
sequence_input = ">DNA Query \n GAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence Input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] #Skips the sequence name in the first line
sequence = ''.join(sequence) # Concatenates list to string

st.write("""
         ***
         """)

## Prints the input DNA sequence
st.header('INPUT(DNA Query)')
sequence


## DNA nucleotide count
st.header('OUTPUT(DNA Nucleotide Count)')

### 1. Print dictionary
st.subheader('1.Print Dictionary')
def DNA_nucleotide_count(seq):
    d=dict([
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('G',seq.count('G')),
        ('C',seq.count('C'))
    ])
    return d

X=DNA_nucleotide_count(sequence)

X_label=list(X)
x_values=list(X.values())

X

### 2. Print text
st.subheader('2.Print Text')
st.write('There are  ' + str(X['A']) + ' adenine (A)')
st.write('There are  ' + str(X['T']) + ' thymine (T)')
st.write('There are  ' + str(X['G']) + ' guanine (G)')
st.write('There are  ' + str(X['C']) + ' cytosine (C)')

### 3. Display DataFrame
st.subheader('3.Display DataFrame')
df=pd.DataFrame.from_dict(X,orient='index')
df=df.rename({0:'count'},axis='columns')
df.reset_index(inplace=True)
df=df.rename(columns={'index':'nucleotide'})
st.write(df)

### 4. Display Bar Chart using Altair
st.subheader('4.Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)

p=p.properties(
    width=alt.Step(80) # controls width of bar.
)

st.write(p)
