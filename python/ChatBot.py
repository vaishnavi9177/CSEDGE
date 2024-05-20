def chatbot(input_text):
    # Predefined rules and responses
    responses = {
        "hi": "Hello!",
        "how are you": "I'm doing well, thank you!",
        "kk bye": "Goodbye! Have a great day!",
        "default": "I'm sorry, I didn't understand that."
    }

    # Convert input to lowercase for case-insensitive matching
    input_text = input_text.lower()

    # Check if input matches any predefined rules
    if input_text in responses:
        return responses[input_text]
    else:
        return responses["default"]

# Main function to interact with the chatbot
def main():
    print("Welcome to the Rule-Based Chatbot!")

    while True:
        user_input = input("You: ")
        response = chatbot(user_input)
        print("AI User:", response)

        # Exit the loop if user says "bye"
        if user_input.lower() == "bye":
            break

if __name__ == "__main__":
    main() # Call the main function
