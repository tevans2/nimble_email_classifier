# Purpose: OpenAI text-davinci-003 text completion classifier
import os
from time import sleep
import openai

# Set up your OpenAI API credentials
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]


def classify_phrase_intent(text: str) -> str:
    # Generate prompt for the GPT-3.5 model
    pwd_prompt = f"Debtors of a debt collection company have to use their account number to open personal documents and often they do not know their account number or don't know that they have to enter it to view their documents. As a result of this our company gets a large number of emails responses to shared documents inquiring about how to open them or what the customers account number is. I want to be able to isolate these types of emails from the rest of incoming emails. Determine whether the following email body falls into this category of people having trouble accesing their documents '{text}'.\nOutput only one of the following options according to your choice: 1 - the email does fall into the given category. 0 - the email body is related to a different subject matter\nDo not explain your choice."
    payment_prompt = f"You are an email classifier working for a debt collections company. Your role is to identify emails in which a debtor is attempting to make a payment/settlement arrangement. Any email in which a debtor is trying to pay must be identified by responding with a 1. Any other category must be labled with a 0. 1 - the email does fall into the given category. 0 - the email body is related to a different subject matter\nDo not explain your choice."

    # Call the OpenAI API to generate the intent
    # TODO: handle timeouts & errors
    for i in range(3):
        # Call the OpenAI API to generate the intent
        try:
            response = openai.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt=payment_prompt,
                max_tokens=256,
                n=1,
                stop=None,
                temperature=0.0,
                top_p=1.0,
                timeout=20,
            )
            # print("API call successful.")
        except Exception as e:
            print(repr(e))
            print(f"Error: OpenAI API call failed. Retrying ({i})...")
            sleep(i * 5)
            continue
        else:
            break

    # Extract the generated intent from the API response
    intent = response.choices[0].text.strip().lower().replace(".", "")  # type: ignore

    if intent not in ["0", "1"]:
        print("text-davinci-003 returned an invalid intent: ", intent)
        intent = "unclear"

    sleep(1)  # rate limiting

    return intent
