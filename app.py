# app.py (Computer Guesses)

import streamlit as st

# Set page title and icon
st.set_page_config(page_title="🤖 Computer Guesses Your Number", page_icon="🖥️")

# Add a colorful title
st.markdown(
    """
    <style>
    .title {
        font-size: 35px;
        font-weight: bold;
        color: white;
        background-color: #33A8FF;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
    }
    </style>
    <div class="title">🤖 Computer Guesses Your Number 🖥️</div>
    """,
    unsafe_allow_html=True
)

# Add a colorful header
st.markdown(
    """
    <style>
    .header {
        font-size: 30px;
        font-weight: bold;
        color: #FF5733;
        text-align: center;
    }
    </style>
    <div class="header">✨ Think of a Number Between 1 and 100 ✨</div>
    """,
    unsafe_allow_html=True
)

# Initialize variables in session state
if "low" not in st.session_state:
    st.session_state.low = 1
if "high" not in st.session_state:
    st.session_state.high = 100
if "guess" not in st.session_state:
    st.session_state.guess = 50
if "feedback" not in st.session_state:
    st.session_state.feedback = ""

# Function to reset the game
def reset_game():
    st.session_state.low = 1
    st.session_state.high = 100
    st.session_state.guess = 50
    st.session_state.feedback = ""

# Add instructions
st.markdown(
    """
    <style>
    .instructions {
        font-size: 20px;
        color: #33FF57;
        text-align: center;
    }
    </style>
    <div class="instructions">🎯 Think of a number between 1 and 100. The computer will try to guess it!</div>
    """,
    unsafe_allow_html=True
)

# Display the computer's guess
st.markdown(
    f"""
    <style>
    .guess {{
        font-size: 25px;
        font-weight: bold;
        color: #FFA500;
        text-align: center;
    }}
    </style>
    <div class="guess">🤖 Computer's Guess: {st.session_state.guess}</div>
    """,
    unsafe_allow_html=True
)

# Add buttons for user feedback
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⬆️ Too Low"):
        st.session_state.low = st.session_state.guess + 1
        st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
with col2:
    if st.button("🎉 Correct"):
        st.session_state.feedback = "correct"
with col3:
    if st.button("⬇️ Too High"):
        st.session_state.high = st.session_state.guess - 1
        st.session_state.guess = (st.session_state.low + st.session_state.high) // 2

# Display feedback
if st.session_state.feedback == "correct":
    st.markdown(
        f"""
        <style>
        .success {{
            font-size: 30px;
            font-weight: bold;
            color: #33FF57;
            text-align: center;
        }}
        </style>
        <div class="success">🎉 The computer guessed your number! It's {st.session_state.guess}.</div>
        """,
        unsafe_allow_html=True
    )
    if st.button("🔄 Play Again"):
        reset_game()

# Add a colorful footer
st.markdown(
    """
    <style>
    .footer {
        font-size: 20px;
        color: #33C1FF;
        text-align: center;
        margin-top: 50px;
    }
    </style>
    <div class="footer">🚀 Thanks for playing with the computer! 🚀</div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <h5 style="color: red; font-weight: bold; text-align: center; margin-top: 20px;">
        ✏️📚 Author: Azmat Ali 📚✏️
    </h5>
    """,
    unsafe_allow_html=True
)