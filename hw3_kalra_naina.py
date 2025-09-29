
# CS1350 Week 5 Homework
# Name: _Naina Kalra_
# Date: ___9/28/25____
# This file contains my solutions for all 4 parts of the homework.
# I tried to keep the code simple and added comments to explain what I was doing.

import re

# -------------------------
# Part 1: Advanced String Methods
# -------------------------

# 1a. Receipt formatting
def format_receipt(items):
    """
    Takes a list of (item, price) and prints a formatted receipt.
    """
    print("=== RECEIPT ===")
    total = 0
    for item, price in items:
        total += price
        # left align item name, right align price with 2 decimals
        print(f"{item:<20} ${price:>7.2f}")
    print("================")
    print(f"{'TOTAL':<20} ${total:>7.2f}")


# 1b. Cleaning user data
def clean_user_data(user_str):
    """
    Takes a string with messy user data and returns a cleaned version.
    Removes extra spaces, makes consistent casing.
    Example: "  john  DOE " -> "John Doe"
    """
    # remove leading/trailing spaces
    s = user_str.strip()
    # make sure only one space between words
    s = " ".join(s.split())
    # title case (first letter capitalized)
    s = s.title()
    return s


# 1c. Text analysis
def text_analysis(text):
    """
    Analyzes text: count words, find longest line, detect sentences.
    """
    lines = text.splitlines()
    words = text.split()
    num_words = len(words)
    longest_line = max(lines, key=len) if lines else ""
    # count sentences (ending with ., ?, or !)
    sentences = re.split(r"[.!?]", text)
    num_sentences = sum(1 for s in sentences if s.strip() != "")
    return {"words": num_words, "longest_line": longest_line, "sentences": num_sentences}


# -------------------------
# Part 2: Regular Expressions
# -------------------------

# 2a. Pattern finding
def find_patterns(text):
    """
    Finds different patterns in the text.
    """
    results = {}
    results["integers"] = re.findall(r"\b\d+\b", text)
    results["decimals"] = re.findall(r"\b\d+\.\d+\b", text)
    results["capitals"] = re.findall(r"\b[A-Z][a-z]*\b", text)
    results["3letters"] = re.findall(r"\b\w{3}\b", text)
    results["2words"] = re.findall(r"\b\w+\s+\w+\b", text)
    return results


# 2b. Format validation
def validate_format(pattern, string):
    """
    Validates if a string matches a given regex pattern fully.
    """
    return bool(re.fullmatch(pattern, string))


# Predefined patterns
phone_pattern = r"\(\d{3}\)\s?\d{3}-\d{4}"
date_pattern = r"\d{2}/\d{2}/\d{4}"
time_pattern = r"\d{1,2}:\d{2}(am|pm|AM|PM)"
email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
url_pattern = r"https?://[A-Za-z0-9./-]+"
ssn_pattern = r"\d{3}-\d{2}-\d{4}"


# 2c. Search and extract
def search_extract(text):
    """
    Extracts prices, percentages, years, sentences, questions, and quotes.
    """
    results = {}
    results["prices"] = re.findall(r"\$\d+(?:\.\d{2})?", text)
    results["percentages"] = re.findall(r"\d+%", text)
    results["years"] = re.findall(r"\b\d{4}\b", text)
    results["sentences"] = re.findall(r"[^.!?]+[.!?]", text)
    results["questions"] = re.findall(r"[^.!?]+\?", text)
    results["quotes"] = re.findall(r"\".*?\"", text)
    return results


# -------------------------
# Part 3: Combining Strings and Regex
# -------------------------

# 3a. Cleaning pipeline
def cleaning_pipeline(text):
    """
    Cleans text by removing extra spaces and fixing case.
    """
    text = text.strip()
    text = " ".join(text.split())
    text = text.capitalize()
    return text


# 3b. Smart replacements
def smart_replacements(text):
    """
    Expands contractions and censors bad words.
    """
    # expand simple contractions
    text = re.sub(r"\bcan't\b", "cannot", text, flags=re.IGNORECASE)
    text = re.sub(r"\bwon't\b", "will not", text, flags=re.IGNORECASE)
    # censor "badword" (example)
    text = re.sub(r"badword", "*****", text, flags=re.IGNORECASE)
    return text


# -------------------------
# Part 4: Application – Log File Analyzer
# -------------------------

def log_file_analyzer(log_text):
    """
    Analyzes a log file string.
    Extracts timestamps, error levels, and messages.
    """
    entries = []
    # Example log format: [2023-01-01 12:00:00] ERROR: Something went wrong
    pattern = r"\[(.*?)\]\s+(INFO|ERROR|WARNING):\s+(.*)"
    matches = re.findall(pattern, log_text)
    for ts, level, msg in matches:
        entries.append({"timestamp": ts, "level": level, "message": msg})
    return entries


# -------------------------
# Testing Function
# -------------------------

def run_tests():
    print("=== Testing Part 1 ===")
    format_receipt([("Apple", 1.5), ("Banana", 0.75), ("Milk", 2.99)])
    print(clean_user_data("  john  DOE "))
    print(text_analysis("Hello world.\nThis is a test!\nLongest line here..."))

    print("\n=== Testing Part 2 ===")
    txt = "John bought 3 apples for $5.50 in 2021. He paid 10% tax."
    print(find_patterns(txt))
    print(validate_format(phone_pattern, "(123) 456-7890"))
    print(search_extract(txt))

    print("\n=== Testing Part 3 ===")
    print(cleaning_pipeline("   hello   WORLD  "))
    print(smart_replacements("I can't believe this badword!"))

    print("\n=== Testing Part 4 ===")
    log_sample = """[2023-01-01 12:00:00] INFO: System started
    [2023-01-01 12:01:00] ERROR: Failed to connect
    [2023-01-01 12:02:00] WARNING: Low memory"""
    print(log_file_analyzer(log_sample))


# -------------------------
# Main Guard
# -------------------------

if __name__ == "__main__":
    run_tests()

