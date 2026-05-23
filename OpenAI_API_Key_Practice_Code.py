import os
from openai import OpenAI

# This looks at the OS environment, this code from line 5 - 10 isn't necessary actually to make this program run as expected u just need openai py library
key = os.environ.get('OPENAI_API_KEY')

# if key is None:
#     print("The terminal doesn't know the key!")
# else:
#     print("Key found! Ready to work.")

Resume = True
while Resume:
    print("\n******************Hi There******************\n")
    print("How Can I help u ?")
    Prompt = input("Enter yr Question (User):")
    client = OpenAI()
    response = client.responses.create(
        model="gpt-5-nano",
        input=Prompt
    )
    print(f"\n{response.output_text}\n")

    while True:
            nums = [0,1] 
            try:
                check = int(input("Wanna Continue? (0 or 1) : "))
                if check not in nums:
                    raise Exception("Enter only these 2 nums: either 0 or 1 ok!\n")
            except ValueError:
                print("\nEnter the Correct option (Either 0 or 1)!\n")
            except Exception as e:
                print(e)
            else:
                if check == 0:
                    Resume = False
            break



# import requests
# api_key = key

# # End point for chat completions
# url="https://api.openai.com/v1/chat/completions"

# # Headers include yrs API key for authentication
# headers ={
#     "Authorization":f"Bearer {api_key}",
#     "Content_Type":"application/json"
# }

# # Request body (JSON)
# data = {
#     "model":"gpt-5-nano",
#     "messages":[
#         {"role":"system", "content":"U are a hepful Assistant."},
#         {"role":"user", "content":"What's AI/ML/DL ?"},
#         ],
#         "max_completion_tokens":100
# }

# # Send POST request
# response = requests.post(url, headers=headers, json=data)

# #Print the response from LLM
# print(response.json())

















# To request the openai server using openai API key w/o downloading 3rd part library like openai
# import os
# import requests
# import json

# # 1. First Principles: Define your endpoint and credentials
# API_KEY = os.getenv("OPENAI_API_KEY")
# URL = "https://api.openai.com/v1/responses"

# Resume = True
# while Resume:
#     Prompt = input("\n******************Enter yrs qstn?******************\nUser:")
#     # 2. Structure the payload for the Responses API
#     payload = {
#         "model": "gpt-5-nano",
#         "input": "Write a one-sentence bedtime story about a unicorn.",
#         "instructions": "Be brief and magical."
#     }

#     # 3. Set the headers (Your digital passport)
#     headers = {
#         "Authorization": f"Bearer {API_KEY}",
#         "Content-Type": "application/json"
#     }

#     # 4. Make the raw POST request
#     response = requests.post(URL, headers=headers, data=json.dumps(payload))

#     # 5. Extract the output
#     if response.status_code == 200:
#         data = response.json()
#         # In the 2026 Responses API, the text is in 'output_text'
#         print(f"\nAI(ChatGPT): {data}")
#     else:
#         print(f"Error {response.status_code}: {response.text}")

#     while True:
#         nums = [0,1] 
#         try:
#             check = int(input("Wanna Continue? (0 or 1) : "))
#             if check not in nums:
#                 raise Exception("Enter only these 2 nums: either 0 or 1 ok!")
#         except ValueError:
#             print("Enter the Correct option (Either 0 or 1)!")
#         except Exception as e:
#             print(e)
#         else:
#             if check == 0:
#                 Resume = False
#             break





