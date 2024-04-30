Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> !pip install transformers
... 
... from transformers import GPTJTokenizer, GPTJForCausalLM
... 
... # Load pre-trained model and tokenizer
... tokenizer = GPTJTokenizer.from_pretrained("EleutherAI/gpt-j-6B")
... model = GPTJForCausalLM.from_pretrained("EleutherAI/gpt-j-6B")
... 
... # Dictionary to store user feedback for each question
... feedback = {}
... 
... def chatbot(question):
...     if question in feedback:
...         response = feedback[question]['response']
...     else:
...         # Tokenize input text
...         input_ids = tokenizer.encode(question, return_tensors='pt')
... 
...         # Generate response
...         output = model.generate(input_ids, max_length=200, num_return_sequences=1, early_stopping=True, do_sample=True, top_k=50, top_p=0.95, num_beams=1)
...         response = tokenizer.decode(output[0], skip_special_tokens=True)
... 
...     print("Bot:", response)
...     rating = input("Please rate my response out of 5: ")
...     try:
...         rating = float(rating)
...         if question in feedback:
...             feedback[question]['total'] += rating
...             feedback[question]['count'] += 1
...         else:
...             feedback[question] = {'total': rating, 'count': 1, 'response': response}
...     except ValueError:
...         print("Invalid input! Please enter a number.")
... 
... # Sample conversation loop
... while True:
...     user_input = input("You: ")
...     if user_input.lower() == 'exit':
...         break
...     chatbot(user_input)
