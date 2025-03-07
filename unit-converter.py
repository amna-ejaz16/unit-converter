import streamlit as st

st.title("🌍🔗ULTIMATE CONVERTER APP")
st.markdown("### Seamless Conversion of Length, Weight, Time & Temperature")
st.write(" Welcome! Convert Anything in Seconds – Just Select, Enter & Get Converted Result in Real-time")


category = st.selectbox("Choose a category", ["Length", "Weight", "Time", "Temperature"])

if category == "Length":
    unit = st.selectbox("📏 Select Conversion", [
        "Kilometers to Miles", "Miles to Kilometers", 
        "Meters to Feet", "Feet to Meters", 
        "Centimeters to Inches", "Inches to Centimeters", 
        "Miles to Yards", "Yards to Miles"
    ])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion", [
        "Kilograms to Pounds", "Pounds to Kilograms", 
        "Grams to Ounces", "Ounces to Grams", 
        "Kilograms to Stones", "Stones to Kilograms"
    ])
elif category == "Time":
    unit = st.selectbox("🕧 Select Conversion", [
        "Hours to Minutes", "Minutes to Hours", 
        "Minutes to Seconds", "Seconds to Minutes", 
        "Hours to Seconds", "Seconds to Hours", 
        "Days to Hours", "Hours to Days"
    ])
elif category == "Temperature":
    unit = st.selectbox("🌡️ Select Conversion", [
        "Celsius to Fahrenheit", "Fahrenheit to Celsius", 
        "Celsius to Kelvin", "Kelvin to Celsius", 
        "Fahrenheit to Kelvin", "Kelvin to Fahrenheit"
    ])


def convert_units(category, value, unit):
    if category == "Length":
        conversions = {
            "Kilometers to Miles": value * 0.621371,
            "Miles to Kilometers": value / 0.621371,
            "Meters to Feet": value * 3.28084,
            "Feet to Meters": value / 3.28084,
            "Centimeters to Inches": value / 2.54,
            "Inches to Centimeters": value * 2.54,
            "Miles to Yards": value * 1760,
            "Yards to Miles": value / 1760
        }
    elif category == "Weight":
        conversions = {
            "Kilograms to Pounds": value * 2.20462,
            "Pounds to Kilograms": value / 2.20462,
            "Grams to Ounces": value / 28.3495,
            "Ounces to Grams": value * 28.3495,
            "Kilograms to Stones": value / 6.35029,
            "Stones to Kilograms": value * 6.35029
        }
    elif category == "Time":
        conversions = {
            "Hours to Minutes": value * 60,
            "Minutes to Hours": value / 60,
            "Minutes to Seconds": value * 60,
            "Seconds to Minutes": value / 60,
            "Hours to Seconds": value * 3600,
            "Seconds to Hours": value / 3600,
            "Days to Hours": value * 24,
            "Hours to Days": value / 24
        }
    elif category == "Temperature":
        conversions = {
            "Celsius to Fahrenheit": (value * 9/5) + 32,
            "Fahrenheit to Celsius": (value - 32) * 5/9,
            "Celsius to Kelvin": value + 273.15,
            "Kelvin to Celsius": value - 273.15,
            "Fahrenheit to Kelvin": (value - 32) * 5/9 + 273.15,
            "Kelvin to Fahrenheit": (value - 273.15) * 9/5 + 32
        }
    else:
        return None

    return conversions.get(unit, "Invalid conversion")

# ✅ Input field for value entry
value = st.number_input("Enter the value to convert", step=0.01)

# ✅ Button to trigger conversion
if st.button("Convert"):
    result = convert_units(category, value, unit)
    if result is not None:
        st.success(f"The result is {result:.2f}")
    else:
        st.error("Invalid conversion selected!")
