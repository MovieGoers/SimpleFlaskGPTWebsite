#testing for github commit
import openai

from flask import Flask, render_template, request

app = Flask(__name__)

openai.api_key = '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'

model_id = 'gpt-3.5-turbo'

def ChatGPT_conversation(conversation):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/output', methods=['POST'])
def output():
    conversation = []
    user_text = request.form['input_text']
    # user_text에서 사용자가 입력한 정보가 들어간다.

    conversation.append({'role': 'system', 'content': user_text})
    conversation = ChatGPT_conversation(conversation)

    return render_template('index.html', output_text=conversation[-1]['content'].strip())

if __name__ == '__main__':
    app.run(debug=True)