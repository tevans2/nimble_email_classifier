# Purpose: OpenAI GPT-3.5-turbo ChatCompletion classifier
import os
from time import sleep
import openai

# Set up your OpenAI API credentials
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]


def classify_phrase_intent(text: str) -> str:
    # Generate a conversation with the GPT-3.5-turbo model
    conversation = [
        {
            "role": "system",
            "content": "Debtors of a debt collection company have to use their account number to open personal documents and often they do not know their account number or don't know that they have to enter it to view their documents. As a result of this our company gets a large number of emails responses to shared documents inquiring about how to open them or what the customers account number is. I want to be able to isolate these types of emails from the rest of incoming emails. Determine whether the following email body falls into this category of people having trouble accesing their documents '{text}'.\nOutput only one of the following options according to your choice: 1 - the email does fall into the given category. 0 - the email body is related to a different subject matter\nDo not explain your choice.",
        },
        {
            "role": "user",
            "content": f"Decide if the following is an account number/password request (1) or if it is unrelated (0): '{text}'.\nOutput only one of the following options exactly as written in the set and do not explain your choice: [1, 0]",
        },
    ]

    # Call the OpenAI API to generate the intent
    # Retry loop to handle timeouts & errors
    for i in range(3):
        # Call the OpenAI API to generate the intent
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=conversation,
                max_tokens=256,
                n=1,
                stop=None,
                temperature=0.0,
                top_p=1.0,
                timeout=20,
            )
        except Exception as e:
            print(repr(e))
            print("Error: OpenAI API call failed. Retrying ({i})...")
            sleep(i * 5)
            continue
        else:
            break

    # Extract the generated intent from the API response
    intent = response.choices[0].message.content.strip().lower().replace(".", "")  # type: ignore

    if intent not in ["1", "0"]:
        print("GPT-3.5-turbo returned an invalid intent: ", intent)
        intent = "unclear"

    sleep(1)  # rate limiting

    return intent
