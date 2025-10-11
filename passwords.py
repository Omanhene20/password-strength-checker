def password_strength(password):
# Check for non-string input
if not isinstance(password, str):
raise TypeError("Input must be a string")

# Return "weak" for empty password
if password == "":
    return "weak"

# Define allowed symbols
allowed_symbols = set("!@#$%^&*()-_=+[]{};:,.?")

# Check for the presence of letters, digits, and symbols
has_letter = any(ch.isalpha() for ch in password)
has_digit = any(ch.isdigit() for ch in password)
has_symbol = any(ch in allowed_symbols for ch in password)
length = len(password)

# Rule: weak if length < 8 or only letters or only digits
if length < 8 or (has_letter and not has_digit and not has_symbol) or (has_digit and not has_letter and not has_symbol):
    return "weak"

# Rule: strong if length >= 12, contains letters, digits, and at least one symbol
if length >= 12 and has_letter and has_digit and has_symbol:
    return "strong"

# Rule: medium if length >= 8 and contains both letters and digits
if length >= 8 and has_letter and has_digit:
    return "medium"

# Fallback
return "weak"
