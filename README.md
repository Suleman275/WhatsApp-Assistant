# WhatsApp-Assistant
A Whatsapp chatbot powered by Google's new PaLM API

To try it out for yourself:
1. Clone the Project
2. Create a Twilio Account at https://www.twilio.com/
3. Install ngrok(https://ngrok.com/download) (you can use whatever you want to deploy the application. This is just what I used)
4. Get the PaLM API key from https://developers.generativeai.google/products/palm or https://makersuite.google.com/app/apikey
5. Create a file named ".env"  in the project folder and paste in the following palmkey="Your-API-Key"
6. Run the following command in your terminal "pip install flask twilio dotenv google.generativeai pyngrok"
7. Run the Python file
8. Open another terminal and run the command "ngrok http 5000" This will give you a link
9. Navigate to your Twilio WhatsApp sandbox settings and paste in the link from ngrok where it says "When a message comes in". Leave the method as POST
10. Add "/bot" to the end of the link and save
11. Your bot is now active! Just join your chat room by sending it the code that Twilio gives you and you can chat with Google PaLM
