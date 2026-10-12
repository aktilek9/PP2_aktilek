import re

# text = "My phone is 87771234567"
text = "I have 12 apples, 5 bananas and 123 oranges."

result = re.search(r"@", text)

print(result.group())