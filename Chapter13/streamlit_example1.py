import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# Selectbox for bins
option = st.selectbox(
    "Select number of bins",
    (10, 20, 30, 40, 50, 60, 70, 80),
)

# Button triggers the histogram generation
if st.button("Show histogram"):
    # Generate random data
    arr = np.random.normal(1, 1, size=100)

    # Plotting
    fig, ax = plt.subplots()
    ax.hist(arr, bins=option)
    st.pyplot(fig)

