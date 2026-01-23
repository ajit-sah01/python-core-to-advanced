import html

user_input = "<script>"
safe_input = html.escape(user_input)
print(safe_input)
