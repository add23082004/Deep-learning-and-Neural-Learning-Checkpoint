from flask import Flask, request, render_template
from main import CustomChatGPT

app = Flask(__name__)

messages = [{"role": "system", "content": "You are a financial expert that specializes in real estate investment and negotiation"}]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    if request.method == 'POST':
        user_input = request.form['user_input']

        # Use your chatbot function here for generating response
        bot_response = CustomChatGPT(user_input)

        return render_template('index.html', user_input=user_input, bot_response=bot_response)


if __name__ == '__main__':
    app.run(debug=True)
