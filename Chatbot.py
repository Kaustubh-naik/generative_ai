import openai
import time

openai.api_key  = 'Secret key'
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def chatbot():
    print("Welcome!, I can recommend you the best books for any topic")
    context = [{'role':'system','content':"""You are a chatbot which recommend books.You are supposed to analyze user's request and give specific responce.If user ask any responce which is other than book recommendation you must say 'I don't know' """},]
    # responce = get_completion_from_messages(context)
    # print(f"{responce}")
    try:
        text = input("[You]:")
        context += [{'role':'user','content':f'{text}'}]
        responce = get_completion_from_messages(context)
        count = 1
        while "Bye".lower() not in text.lower() or count < 10:
            print(f"{responce}")
            context += [{'role':'system','content':f'{responce}'}] 
            text = input("[You]:")
            context += [{'role':'user','content':f'{text}'}] 
            responce = get_completion_from_messages(context)
            count = count+1
        print("Thank you for visiting")
    except openai.error.RateLimitError:
        print("Rate limit exceeded. Please wait for a minute.")
        time.sleep(60)
        return get_completion_from_messages(context)

chatbot()

