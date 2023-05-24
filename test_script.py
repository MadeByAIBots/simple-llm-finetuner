
import os
from trainer import Trainer

def main():
    # Instantiate the Trainer class
    trainer = Trainer()

    # Load the model
    model_name = 'gpt2'
    trainer.load_model(model_name)

    # Prepare the training text
    with open('data.txt', 'r') as f:
        training_text = f.read()

    # Train the model on the training text
    trainer.train(training_text)

    # Prepare the test prompt
    with open('test-prompt.txt', 'r') as f:
        test_prompt = f.read()

    # Generate a response from the model
    response = trainer.generate_response(test_prompt)
    print('Generated response:', response)

    # Prepare the expected response
    with open('test-response.txt', 'r') as f:
        expected_response = f.read()

    # Assert that the response contains the expected response
    assert expected_response in response, f'Expected "{expected_response}" to be in "{response}"'

    print('Test passed.')

if __name__ == '__main__':
    main()
