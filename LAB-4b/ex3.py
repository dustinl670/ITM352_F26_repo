# Get a URL from the user, clean it, and extract the domain name and...
# Name: Dustin Lopera
# Date: September 18th, 2026

url = input("Enter a URL: ")

cleaned_url = url.replace("https://", "")
cleaned_url = cleaned_url.replace("/", "")
print("Cleaned URL: ", cleaned_url)

parts = cleaned_url.split(".")
print("The parts are: ", parts)

domain_name = parts[1]
tld = parts[2]
print("Domain name: ", domain_name)
print("TLD: ", tld)