import re


# 2: Extract email addresses
def extract_emails(txt):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(pattern, txt)
    unique_emails = set(emails)
    return unique_emails, len(unique_emails)


# 3: Extract phone numbers
def extract_phone_numbers(txt):
    pattern = r'\(\d{3}\) \d{3}-\d{4}'
    phone_numbers = re.findall(pattern, txt)
    return phone_numbers


# 4: Extract hashtags
def extract_hashtags(txt):
    pattern = r'#\w+'
    hashtags = re.findall(pattern, txt)
    hashtags = [hashtag.lower() for hashtag in hashtags if len(hashtag) > 4]
    unique_hashtags = set(hashtags)
    return unique_hashtags


# 5: Find URLs
def find_urls(txt):
    pattern = r'https?://[^\s/$.?#].[^\s]*'
    urls = re.findall(pattern, txt)
    return urls


# 6: Validate IPv4 address
def validate_ip(ip_address):
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return bool(re.match(pattern, ip_address))


# Example usage
if __name__ == "__main__":
    para = """
    Contact us at support@example.com or john.doe@subdomain.example.com.
    Also, reach out to admin@example.com or info@example.com.
    Call me at (123) 456-7890 or (987) 654-3210.
    You can also reach me at (555) 123-4567.
    Here are some hashtags: #Python #python #AI #Programming #Tech
    Visit our website at https://www.example.com for more information.
    Also check out http://blog.example.com/2024/09/latest-news.
    """

    # 2
    unique_emails, email_count = extract_emails(para)
    print("Unique Emails:", unique_emails)
    print("Num of Unique Emails:", email_count)

    # 3
    phone_numbers = extract_phone_numbers(para)
    print("Phone Numbers:", phone_numbers)

    # 4
    hashtags = extract_hashtags(para)
    print("Unique Hashtags:", hashtags)

    # 5
    urls = find_urls(para)
    print("URLs:", urls)

    # 6
    ip_addresses = ["192.168.0.1", "127.0.0.1", "256.100.50.0", "192.168.0"]
    ip_results = {ip: validate_ip(ip) for ip in ip_addresses}
    print("IP Address Validity:", ip_results)
