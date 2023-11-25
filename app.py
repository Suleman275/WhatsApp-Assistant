from dotenv import load_dotenv
import google.generativeai as palm
import os

load_dotenv()

palm.configure(api_key=os.environ['palmkey'])

# Create a new conversation
response = palm.chat(messages='Hello')
print (response.last)

prompt = input("Enter yoru reply")

print(prompt)
while prompt != "end":
   response = response.reply(prompt)
   print(response.last)
   #print(response.messages)
   prompt = input("Enter yoru reply")