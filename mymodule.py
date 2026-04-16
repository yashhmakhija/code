import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6Is2_VQlwBXWWSiRiQi155by3OaftIgxN5llKVAvo1J4wz")

model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content("can you give code for edge detection in python using canny?")

print(response.text)
