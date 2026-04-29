import streamlit as st

st.title("DoorDash E-Bike Helper 🚲")

distance = st.number_input("Distance (miles)", value=3.0)
pay = st.number_input("Pay ($)", value=8.0)
battery = st.slider("Battery %", 0, 100, 70)
if distance > 6:
    st.info("Long Distance Order")
ratio = pay / distance
if battery < 20:
    st.error("❌ SKIP - Battery low")
elif ratio >= 2:
    st.success("✅ TAKE - Good order")
elif ratio >= 1.5:
    st.warning("⚠️ MAYBE")
else:
    st.error("❌ SKIP - Bad pay")

st.write(f"$ per mile: {round(ratio,2)}")