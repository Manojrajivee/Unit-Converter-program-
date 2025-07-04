def convert_length(value, from_unit, to_unit):
    conversions = {
        "m": 1,
        "cm": 100,
        "mm": 1000,
        "km": 0.001,
        "in": 39.3701,
        "ft": 3.28084,
        "yd": 1.09361,
        "mi": 0.000621371
    }

    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError("Unsupported length unit.")
    
    value_in_meters = value / conversions[from_unit]
    return value_in_meters * conversions[to_unit]


def convert_weight(value, from_unit, to_unit):
    conversions = {
        "kg": 1,
        "g": 1000,
        "mg": 1e6,
        "lb": 2.20462,
        "oz": 35.274
    }

    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError("Unsupported weight unit.")
    
    value_in_kg = value / conversions[from_unit]
    return value_in_kg * conversions[to_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    
    if from_unit == "C":
        if to_unit == "F":
            return (value * 9/5) + 32
        elif to_unit == "K":
            return value + 273.15
    elif from_unit == "F":
        if to_unit == "C":
            return (value - 32) * 5/9
        elif to_unit == "K":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "K":
        if to_unit == "C":
            return value - 273.15
        elif to_unit == "F":
            return (value - 273.15) * 9/5 + 32

    raise ValueError("Unsupported temperature unit.")


if __name__ == "__main__":
    # Example usage
    print("Length:", convert_length(1, "km", "m"))       # 1000.0
    print("Weight:", convert_weight(1, "kg", "g"))       # 1000.0
    print("Temp:", convert_temperature(100, "C", "F"))   # 212.0
