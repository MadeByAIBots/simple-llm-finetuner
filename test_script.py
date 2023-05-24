
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

if __name__ == '__main__':
    main()
