import streamlit as st
import poetrytools
import matplotlib
from string import ascii_lowercase


lyrics = """When I find myself in times of trouble
Mother Mary comes to me
Speaking words of wisdom
Let it be
And in my hour of darkness
She is standing right in front of me
Speaking words of wisdom
Let it be
Let is be, let it be
Let it be, let it be
Whisper words of wisdom
Let it be
And when the brokenhearted people
Living in the world agree
There will be an answer
Let it be
For though they may be parted
There is still a chance that they will see
There will be an answer
Let it be
Let is be, let it be
Let it be, let it be
Yeah, there will be an answer
Let it be
Let is be, let it be
Let it be, let it be
Whisper words of wisdom
Let it be
Let is be, let it be
Let it be, yeah, let it be
Whisper words of wisdom
Let it be
And when the night is cloudy
There is still a light that shines on me
Shine on 'til tomorrow
Let it beI wake up to the sound of music
Mother Mary comes to me
Speaking words of wisdom
Let it be, yeah
Let it be, let it be
Let it be, yeah, let it be
Oh, there will be an answer
Let it be
Let it be, let it be
Let it be, yeah, let it be
Whisper words of wisdom
Let it be
"""

scheme_colors = [v for v in matplotlib.colors.TABLEAU_COLORS.values()]

st.title("Rhyme Schemegi")
st.subheader("Input")
text = st.text_area("Words", value=lyrics, height=400)

try:
    lines = poetrytools.tokenize(text)
    schemes = poetrytools.rhyme_scheme(lines)
except:
    st.error("Error")

st.subheader("Result")
for tokens, scheme in zip(lines, schemes):
    if scheme == "X":
        line = ' '.join(tokens)
    else:
        i = ascii_lowercase.index(scheme.lower())
        color = scheme_colors[i]        
        if scheme.isupper(): # 1行まるまる一緒
            line = f"<span style='color: {color};'>{' '.join(tokens)}</span>"
        else: # 文末の韻
            tokens[-1] = f"<span style='color: {color};'>{tokens[-1]}</span>"
            line = ' '.join(tokens)
    st.markdown(line, unsafe_allow_html=True)