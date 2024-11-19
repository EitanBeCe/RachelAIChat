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
    if x < 0.5:
        learn_instruction["content"] = learn_instruction["content"] + " Your response will include some dry humour."
    else:
        learn_instruction["content"] = learn_instruction["content"] + " Your response will include a rather challenging question."

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


def store_messages(request_message, response_message):

    file_name = "stored_data.json"

    messages = get_recent_messages()[1:]

    # Add messages to data
    user_message = {"role": "user", "content": request_message}
    assistant_message = {"role": "assistant", "content": response_message}
    messages.append(user_message)
    messages.append(assistant_message)

    # Save the updated file
    with open(file_name, "w") as f:
        json.dump(messages, f)


def reset_messages():

    # Overwrite file with nothing
    open("stored_data.json", "w")