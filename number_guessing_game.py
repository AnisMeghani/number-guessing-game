import streamlit as st
import random

def main():
    st.set_page_config(page_title="🎯 Number Guessing Game", layout="centered")
    st.title('🎯 Number Guessing Game By "Muhammad Anis Meghani" ')
    
    # Difficulty selection
    difficulty = st.radio("Select Difficulty:", ("Easy (1-20)", "Medium (1-50)", "Hard (1-100)"))
    
    # Set range and max attempts based on difficulty
    if difficulty == "Easy (1-20)":
        max_number = 20
        max_attempts = 5
    elif difficulty == "Medium (1-50)":
        max_number = 50
        max_attempts = 10
    else:
        max_number = 100
        max_attempts = 15
    
    # Session State to store the random number and attempts
    if 'random_number' not in st.session_state or 'max_number' not in st.session_state or st.session_state.max_number != max_number:
        st.session_state.random_number = random.randint(1, max_number)
        st.session_state.attempts = 0
        st.session_state.max_number = max_number
    
    st.write(f"Guess a number between 1 and {max_number}")
    
    user_guess = st.number_input("Enter your guess:", min_value=1, max_value=max_number, step=1)
    
    if st.button("Check Guess"):
        if st.session_state.attempts < max_attempts:
            st.session_state.attempts += 1
            if user_guess < st.session_state.random_number:
                st.warning(f"Too Low! Try Again. Attempts left: {max_attempts - st.session_state.attempts}")
            elif user_guess > st.session_state.random_number:
                st.warning(f"Too High! Try Again. Attempts left: {max_attempts - st.session_state.attempts}")
            else:
                st.success(f"🎉 Correct! You guessed it in {st.session_state.attempts} attempts!")
                st.session_state.random_number = random.randint(1, max_number)  # Reset game
                st.session_state.attempts = 0
        else:
            st.error(f"❌ Game Over! The correct number was {st.session_state.random_number}. Try Again!")
            st.session_state.random_number = random.randint(1, max_number)  # Reset game
            st.session_state.attempts = 0
    

