# hw6_lastname_firstname.py
# Solutions for CS1350 Week 6 Homework - Advanced Pattern Matching with Regular Expressions
import re
from collections import Counter

# Problem 1
def problem1():
    """
    Extract information using regex groups.
    """
# a) Extract date components from various date formats
    dates_text = """
    Important dates:
    - Project due: 2024-03-15
    - Meeting on: 12/25/2024
    - Holiday: July 4, 2025
    """
    # Pattern that captures ISO dates YYYY-MM-DD
    pattern_iso = r'(\d{4}-\d{2}-\d{2})'
    iso_dates = re.findall(pattern_iso, dates_text)

# b) Parse email addresses and extract username and domain
    emails_text = "Contact john.doe@example.com or alice_smith@university.edu for info"
    # Named groups for username and domain
    pattern_email = r'(?P<username>[\w\.-]+)@(?P<domain>[\w\.-]+\.[A-Za-z]{2,})'
    email_parts = []
    for m in re.finditer(pattern_email, emails_text):
        email_parts.append({'username': m.group('username'), 'domain': m.group('domain')})

# c) Extract phone numbers with area codes
    phones_text = "Call (555) 123-4567 or 800-555-1234 for support"
    # Capture area code in group 1 and rest in group 2
    # Handles (555) 123-4567 and 800-555-1234 and variants with . or spaces
    pattern_phone = r'\(?(\d{3})\)?[-.\s]?(\d{3}[-.\s]?\d{4})'
    phone_numbers = re.findall(pattern_phone, phones_text)

# d) Find repeated words in text (consecutive repeated words)
    repeated_text = "The the quick brown fox jumped over the the lazy dog"
    pattern_repeated = r'\b([A-Za-z]+)\s+\1\b'
    # Use IGNORECASE to find 'The the' and 'the the'
    repeated_words = [w.lower() for w in re.findall(pattern_repeated, repeated_text, flags=re.IGNORECASE)]

    return {
        'iso_dates': iso_dates,
        'email_parts': email_parts,
        'phone_numbers': phone_numbers,
        'repeated_words': repeated_words
    }

# Problem 2
def problem2():
    """
    Use alternation to create flexible patterns.
    """
# a) Match different image file extensions
    files_text = """
    Documents: report.pdf, notes.txt, presentation.pptx
    Images: photo.jpg, diagram.png, icon.gif, picture.jpeg
    Code: script.py, program.java, style.css
    """
    pattern_images = r'\b[\w\-/]+?\.(?:jpg|jpeg|png|gif)\b'
    image_files = re.findall(pattern_images, files_text, flags=re.IGNORECASE)

# b) Match different date formats
    mixed_dates = "Meeting on 2024-03-15 or 03/15/2024 or March 15, 2024"
    # Match ISO, US (MM/DD/YYYY), and textual (e.g., March 15, 2024)
    pattern_dates = r'\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|[A-Za-z]+ \d{1,2}, \d{4}'
    all_dates = re.findall(pattern_dates, mixed_dates)

# c) Extract prices in different formats
    prices_text = "$19.99, USD 25.00, 30 dollars, €15.50, £12.99"
    # Match $, USD, "dollars", € and £ variations
    pattern_prices = r'(?:\$\d+(?:\.\d+)?|USD\s*\d+(?:\.\d+)?|\d+(?:\.\d+)?\s*dollars|€\d+(?:\.\d+)?|£\d+(?:\.\d+)?)'
    prices = re.findall(pattern_prices, prices_text, flags=re.IGNORECASE)

# d) Match programming language mentions and abbreviations
    code_text = """
    We use Python for data science, Java for enterprise apps,
    JavaScript or JS for web development, and C++ or CPP for systems.
    """
    pattern_langs = r'\b(?:Python|Java(?:Script)?|JS|JavaScript|C\+\+|CPP)\b'
    languages = re.findall(pattern_langs, code_text, flags=re.IGNORECASE)

    return {
        'image_files': image_files,
        'all_dates': all_dates,
        'prices': prices,
        'languages': languages
    }

# Problem 3
def problem3():
    """
    Practice with findall() and finditer() methods.
    """
    log_text = """
    [2024-03-15 10:30:45] INFO: Server started on port 8080
    [2024-03-15 10:31:02] ERROR: Connection failed to database
    [2024-03-15 10:31:15] WARNING: High memory usage detected (85%)
    [2024-03-15 10:32:00] INFO: User admin logged in from 192.168.1.100
    [2024-03-15 10:32:30] ERROR: File not found: config.yml
    """
# a) Extract timestamps using findall()
    pattern_timestamp = r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]'
    timestamps = re.findall(pattern_timestamp, log_text)

# b) Use findall() with groups to extract log levels and messages
    pattern_log = r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]\s+(\w+):\s+(.+)'
    log_entries = re.findall(pattern_log, log_text)

# c) Use finditer() to get positions of all IP addresses
    pattern_ip = r'(\d{1,3}(?:\.\d{1,3}){3})'
    ip_addresses = []
    for m in re.finditer(pattern_ip, log_text):
        ip_addresses.append({'ip': m.group(1), 'start': m.start(1), 'end': m.end(1)})

# d) Use finditer() to create a highlighted version of errors
    def highlight_errors(text):
        """
        Surround entire lines that contain ERROR with ** markers.
        """
        # Capture entire line (multiline)
        return re.sub(r'(^.*ERROR.*$)', r'**\1**', text, flags=re.MULTILINE)

    highlighted_log = highlight_errors(log_text)

    return {
        'timestamps': timestamps,
        'log_entries': log_entries,
        'ip_addresses': ip_addresses,
        'highlighted_log': highlighted_log
    }

# Problem 4
def problem4():
    """
    Practice text transformation using re.sub().
    """
# a) Clean and format phone numbers
    messy_phones = """
    Contact list:
    - John: 555.123.4567
    - Jane: (555) 234-5678
    - Bob: 555 345 6789
    - Alice: 5554567890
    """
    def standardize_phones(text):
        """
        Convert all phone number formats to (XXX) XXX-XXXX.
        """
        pattern = r'\(?(\d{3})\)?[\s\.-]?(\d{3})[\s\.-]?(\d{4})'
        replacement = r'(\1) \2-\3'
        return re.sub(pattern, replacement, text)

    cleaned_phones = standardize_phones(messy_phones)

# b) Redact sensitive information
    sensitive_text = """
    Customer: John Doe
    SSN: 123-45-6789
    Credit Card: 4532-1234-5678-9012
    Email: john.doe@email.com
    Phone: (555) 123-4567
    """
    def redact_sensitive(text):
        # Replace SSN
        text = re.sub(r'\b\d{3}-\d{2}-\d{4}\b', 'XXX-XX-XXXX', text)
        # Replace credit card numbers in typical 4-4-4-4 formats with dashes or spaces or none
        text = re.sub(r'\b(?:\d{4}[-\s]?){3}\d{4}\b', 'XXXX-XXXX-XXXX-XXXX', text)
        return text

    redacted_text = redact_sensitive(sensitive_text)

# c) Convert markdown links to HTML
    markdown_text = """
    Check out [Google](https://google.com) for search.
    Visit [GitHub](https://github.com) for code.
    Read documentation at [Python Docs](https://docs.python.org).
    """
    def markdown_to_html(text):
        pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        return re.sub(pattern, r'<a href="\2">\1</a>', text)

    html_text = markdown_to_html(markdown_text)

# d) Implement a simple template system
    template = """
    Dear {name},
    Your order #{order_id} for {product} has been shipped.
    Tracking number: {tracking}
    """
    values = {
        'name': 'John Smith',
        'order_id': '12345',
        'product': 'Python Book',
        'tracking': 'TRK789XYZ'
    }
    def fill_template(template, values):
        """
        Replace all {key} placeholders with values from dictionary.
        If key missing, leave placeholder unchanged.
        """
        def repl(m):
            key = m.group(1)
            return str(values.get(key, m.group(0)))
        return re.sub(r'\{(\w+)\}', repl, template)

    filled_template = fill_template(template, values)

    return {
        'cleaned_phones': cleaned_phones,
        'redacted_text': redacted_text,
        'html_text': html_text,
        'filled_template': filled_template
    }

# Problem 5
def problem5():
    """
    Use compiled patterns for efficiency and clarity.
    """
    class PatternLibrary:
        """
        Library of compiled regex patterns for common use cases.
        """
# a) Email validation pattern (case insensitive)
        EMAIL = re.compile(r'^[\w\.-]+@[\w\.-]+\.[A-Za-z]{2,}$', re.IGNORECASE)
# b) URL pattern (with optional protocol)
        URL = re.compile(r'^(?:https?://)?(?:www\.)?[\w\.-]+\.[A-Za-z]{2,}(?:/[\w\-\./?&=#%+]*)?$', re.IGNORECASE)

# c) US ZIP code (5 digits or 5+4 format)
        ZIP_CODE = re.compile(r'^\d{5}(?:-\d{4})?$')

# d) Strong password (verbose pattern with comments)
        PASSWORD = re.compile(r'''
            ^               # start
            (?=.{8,}$)      # at least 8 characters
            (?=.*[A-Z])     # at least one uppercase
            (?=.*[a-z])     # at least one lowercase
            (?=.*\d)        # at least one digit
            (?=.*[^A-Za-z0-9]) # at least one special char
            .+              # rest of the password
            $               # end
        ''', re.VERBOSE)

# e) Credit card number (with spaces or dashes optional)
        CREDIT_CARD = re.compile(r'^(?:\d{4}[-\s]?){3}\d{4}$')

    test_data = {
        'emails': ['valid@email.com', 'invalid.email', 'user@domain.co.uk'],
        'urls': ['https://example.com', 'www.test.org', 'invalid://url'],
        'zips': ['12345', '12345-6789', '1234', '123456'],
        'passwords': ['Weak', 'Strong1!Pass', 'nouppercas3!', 'NoDigits!'],
        'cards': ['1234 5678 9012 3456', '1234-5678-9012-3456', '1234567890123456']
    }

    validation_results = {
        'emails': [bool(PatternLibrary.EMAIL.match(e)) for e in test_data['emails']],
        'urls': [bool(PatternLibrary.URL.match(u)) for u in test_data['urls']],
        'zips': [bool(PatternLibrary.ZIP_CODE.match(z)) for z in test_data['zips']],
        'passwords': [bool(PatternLibrary.PASSWORD.match(p)) for p in test_data['passwords']],
        'cards': [bool(PatternLibrary.CREDIT_CARD.match(c)) for c in test_data['cards']]
    }

    return validation_results

# Problem 6
def problem6():
    """
    Create a log file analyzer using regex.
    """
    log_data = """
    192.168.1.1 - - [15/Mar/2024:10:30:45 +0000] "GET /index.html HTTP/1.1" 200
    5234
    192.168.1.2 - - [15/Mar/2024:10:30:46 +0000] "POST /api/login HTTP/1.1" 401
    234
    192.168.1.1 - - [15/Mar/2024:10:30:47 +0000] "GET /images/logo.png HTTP/1.1" 304 0
    192.168.1.3 - - [15/Mar/2024:10:30:48 +0000] "GET /admin/dashboard HTTP/1.1" 403 0
    192.168.1.2 - - [15/Mar/2024:10:30:49 +0000] "POST /api/login HTTP/1.1" 200
    1234
    192.168.1.4 - - [15/Mar/2024:10:30:50 +0000] "GET /products HTTP/1.1" 200
    15234
    192.168.1.1 - - [15/Mar/2024:10:30:51 +0000] "GET /contact HTTP/1.1" 404 0
    """
# Pattern that attempts to capture:
# ip, timestamp, method, path, status, and an optional size (which probably will be on next line)
    log_pattern = re.compile(
        r'(?m)(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - - \[(?P<timestamp>[^\]]+)\] "\s*(?P<method>[A-Z]+)\s+(?P<path>[^"\s]+)[^"]*"\s+(?P<status>\d{3})\s*(?P<size>\d+)?',
        flags=re.DOTALL
    )

    parsed_logs = []
    for m in log_pattern.finditer(log_data):
        size_str = m.group('size')
        size = int(size_str) if size_str and size_str.isdigit() else 0
        entry = {
            'ip': m.group('ip'),
            'timestamp': m.group('timestamp'),
            'method': m.group('method'),
            'path': m.group('path'),
            'status': int(m.group('status')),
            'size': size
        }
        parsed_logs.append(entry)

# Analysis
    total_requests = len(parsed_logs)
    unique_ips = sorted({e['ip'] for e in parsed_logs})
    error_count = sum(1 for e in parsed_logs if 400 <= e['status'] < 600)
    total_bytes = sum(e['size'] for e in parsed_logs)
# Most requested path: 
    paths = [e['path'] for e in parsed_logs]
    most_requested_path = Counter(paths).most_common(1)[0][0] if paths else ''
    methods_used = sorted({e['method'] for e in parsed_logs})

    analysis = {
        'total_requests': total_requests,
        'unique_ips': unique_ips,
        'error_count': error_count,
        'total_bytes': total_bytes,
        'most_requested_path': most_requested_path,
        'methods_used': methods_used
    }

    return {
        'parsed_logs': parsed_logs,
        'analysis': analysis
    }

# Bonus Challenge (optional)
def bonus_challenge():
    """
    Convert markdown formatting to HTML.
    Support: **bold**, *italic*, [links](url), # headers
    """
    markdown = """
    # Main Header
    This is a **bold** word and this is *italic*.
    Check out [this link](https://example.com).
    ## Subheader
    Another paragraph with **multiple** *formatting* options.
    """
    html = markdown

# Headers: handling from h6 down to h1 by examining leading # count
    def header_repl(m):
        hashes = m.group(1)
        level = len(hashes)
        content = m.group(2).strip()
        return f'<h{level}>{content}</h{level}>'
    html = re.sub(r'^\s*(#{1,6})\s*(.+)$', header_repl, html, flags=re.MULTILINE)
    
# Links
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html)

# Bold (**) then italic (*)
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)

# Wrapping paragraphs: naive split on blank lines
    parts = [p.strip() for p in re.split(r'\n\s*\n', html) if p.strip()]
    final_html = '\n'.join(
        p if p.startswith('<h') else f'<p>{p}</p>' for p in parts
    )
    return final_html

# Run tests when executed
if __name__ == "__main__":
    print("Problem 1 Results:")
    print(problem1())
    print("\nProblem 2 Results:")
    print(problem2())
    print("\nProblem 3 Results:")
    res3 = problem3()
    print("Timestamps:", res3['timestamps'])
    print("Log entries (level, message):", res3['log_entries'])
    print("IP addresses with positions:", res3['ip_addresses'])
    print("Highlighted log:\n", res3['highlighted_log'])
    print("\nProblem 4 Results:")
    res4 = problem4()
    print("Cleaned phones:\n", res4['cleaned_phones'])
    print("Redacted text:\n", res4['redacted_text'])
    print("HTML text:\n", res4['html_text'])
    print("Filled template:\n", res4['filled_template'])
    print("\nProblem 5 Results:")
    print(problem5())
    print("\nProblem 6 Results:")
    res6 = problem6()
    print("Parsed logs:")
    for entry in res6['parsed_logs']:
        print(entry)
    print("Analysis:")
    print(res6['analysis'])
    print("\nBonus Challenge Result (HTML):")
    print(bonus_challenge())
