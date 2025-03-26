import streamlit as st

def convert_units(value, from_unit, to_unit, category):
    conversions = {
        "Length": {
            "Metre": 1, "Kilometre": 0.001, "Centimetre": 100, "Millimetre": 1000, "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701
        },
        "Weight": {
            "Kilogram": 1, "Gram": 1000, "Milligram": 1000000, "Pound": 2.20462, "Ounce": 35.274
        },
        "Temperature": {
            "Celsius": (lambda x: x, lambda x: x),
            "Fahrenheit": (lambda x: (x * 9/5) + 32, lambda x: (x - 32) * 5/9),
            "Kelvin": (lambda x: x + 273.15, lambda x: x - 273.15)
        }
    }
    
    if category == "Temperature":
        to_base, from_base = conversions[category][from_unit]
        value_in_base = from_base(value)
        to_base, from_base = conversions[category][to_unit]
        return to_base(value_in_base)
    
    base_value = value / conversions[category][from_unit]
    converted_value = base_value * conversions[category][to_unit]
    return converted_value

st.title("Unit Converter")
st.header("Convert between different units")

category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"])

unit_options = {
    "Length": ["Metre", "Kilometre", "Centimetre", "Millimetre", "Mile", "Yard", "Foot", "Inch"],
    "Weight": ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

col1, col2, col3 = st.columns([1, 0.2, 1])

with col1:
    value = st.number_input("Enter value", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From", unit_options[category])

with col3:
    to_unit = st.selectbox("To", unit_options[category])
    
converted_value = convert_units(value, from_unit, to_unit, category)
st.success(f"{value} {from_unit} = {converted_value:.2f} {to_unit}")
