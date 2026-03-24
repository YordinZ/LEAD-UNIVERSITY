text = "Hello, World!"

 # Encode into bytes
encoded_text = text.encode("utf-8")
print(encoded_text)

 # Decode back to a string
decoded_text = encoded_text.decode("utf-8")
print(decoded_text)