import json
import random

def get_recent_messages():

    # Define a file name and learn instructions
    file_name = "stored_data.json"
    learn_instruction = {
        "role": "system",
        "content": "You are interviewing the user for a job as a retail assistant. Ask short questions that are relevant to the junior position. Your name is Rachel. The user is called Eitan. Keep your answers to under 30 words."
    }

    # Initialize messages
    messages = []

    # Add a random element (humor etc)
    x = random.uniform(0, 1)
    instruction = learn_instruction["content"]
    if x < 0.5:
        instruction = instruction + " Your response will include some dry humour."
    else:
        instruction = instruction + " Your response will include a rather challenging question."

    # Append instruction to message
    messages.append(learn_instruction)

    # Get last messages
    try:
        with open(file_name) as user_file:
            data = json.load(user_file)

            # Append 5 last items of data
            for item in data[-5:]:
                messages.append(item)
            # if data:
            #     if len(data) < 5:
            #         for item in data:
            #             messages.append(item)
            #     else:
            #         for item in data[-5:]:
            #             messages.append(item)

    except Exception as e:
        print(e)
        pass

    return messages