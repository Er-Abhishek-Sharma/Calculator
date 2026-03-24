import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮")

# Title
st.title("🧮 Calculator")
st.caption("Real-time • Instant Results")
st.divider()

# Inputs
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Value A", value=0.0)

with col2:
    num2 = st.number_input("Value B", value=0.0)

# Operation
operation = st.radio(
    "Select Operation",
    ["Add", "Subtract", "Multiply", "Divide"],
    horizontal=True
)

st.divider()

# Calculation
result = None

if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 == 0:
        st.error("⚠️ Division by Zero!")
    else:
        result = num1 / num2

# Result
if result is not None:
    st.success(f"Result: {round(result, 6)}")

# History
if "history" not in st.session_state:
    st.session_state.history = []

if result is not None:
    if st.button("Save to History"):
        entry = f"{num1} {operation} {num2} = {round(result, 6)}"
        if entry not in st.session_state.history:
            st.session_state.history.insert(0, entry)

# Show history
if st.session_state.history:
    st.divider()
    st.subheader("History")

    if st.button("Clear History"):
        st.session_state.history = []
        st.rerun()

    for item in st.session_state.history[:10]:
        st.text(item)
