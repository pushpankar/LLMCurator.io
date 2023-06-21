from flask import Flask, jsonify, request
import random
from bardapi import Bard

app = Flask(__name__)

bard_key = 'XQiBHxTDxkoNXgCzIqnrzZGN9FUXdQazyFHzi-chBF88QNstH6ueApmWZmbhJKNbdrtyIg.'
bard = Bard(token=bard_key)


def generate_lorem_ipsum():
    lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed blandit ullamcorper neque vitae dignissim. Nulla facilisi. Vestibulum sed leo et elit consectetur venenatis sed a nunc. Fusce non fermentum tortor. Aliquam erat volutpat. Quisque sit amet tristique eros, ut vulputate mauris. Praesent sit amet ultricies massa. Cras consectetur est nulla, vel tempor nunc aliquet id. Pellentesque interdum tempor libero, a malesuada risus faucibus a. Sed et sem eget sapien vestibulum laoreet."

    lorem_ipsum_length = random.randint(5, len(lorem_ipsum))  # Random length between 5 and total word count
    generated_text = lorem_ipsum[:lorem_ipsum_length]

    return generated_text


@app.route('/api/infer', methods=['POST'])
def process_data():
    input_string = request.get_json().get('prompt', '')
    processed_data = input_string.upper()  # Perform some processing on the input string
    # response_data = {'responses': [generate_lorem_ipsum() for _ in range(3)]}
    bard_resp = bard.get_answer(input_string)['content']
    response_data = {'response': [bard_resp, bard_resp]}
    print(response_data)
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5056)
