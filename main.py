import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch
import re

# Load the Hugging Face model and tokenizer
model_name = "microsoft/DialoGPT-medium"
chatbot = pipeline("text-generation", model=model_name)

# Initialize conversation history
conversation_history = []

# Function to generate chatbot response
def chatbot_response(prompt):
    global conversation_history

    #write your code below
    prompt = prompt.lower() 
    conversation_history.append(prompt)   
    
    if (prompt == 'hello'): 
        response = 'Hi there! How can I help you today?'
        
    elif (prompt == 'bye'):
        response = 'Goodbye! Have a great day!'
        
    elif (prompt.find('calculate') != -1):
        error_message = "`Invalid operator and/or calculation format. Please use 'calculate <num1> <operator> <num2>'."
        operation = prompt.split(' ')
        
        if len(operation) == 4:
            num1 = int(operation[1])
            num2 = int(operation[3])
            
            if operation[2] == '+':
                calc_result = num1 + num2
                response = f'The result is {calc_result}' 
                
            elif operation[2] == '-':
                calc_result = num1 - num2
                response = f'The result is {calc_result}'
                
            elif operation[2] == '*':
                calc_result = num1 * num2
                response = f'The result is {calc_result}'
                
            elif operation[2] == '/': 
                calc_result = num1 / num2
                response = f'The result is {calc_result}'
                
            else: 
                response = error_message   
                  
        else: 
            response = error_message
            
    else :
        outputs = chatbot(prompt, max_length=1000, pad_token_id=50256)
        response = outputs[0]['generated_text'][len(prompt):].strip()

    conversation_history.append(response)

    # Display conversation history (loops and data structures)
    history = "\n".join(conversation_history[-6:])  # Show last 3 interactions
    
    return history

# Create a Gradio interface below