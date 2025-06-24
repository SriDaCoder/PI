import streamlit as st

def calculate_pi_leibniz(num_terms):
    pi_approx = 0
    for i in range(num_terms):
        term = 4 / (2 * i + 1)
        if i % 2 == 0:
            pi_approx += term
        else:
            pi_approx -= term
    return pi_approx

st.title("Leibniz Formula for Pi Approximation")

num_terms = st.number_input("Enter number of terms:", min_value=1, value=1000, step=1)

if st.button("Calculate Pi"):
    pi_value = calculate_pi_leibniz(num_terms)
    st.write(f"Approximation of Pi with {num_terms} terms: **{pi_value}**")
