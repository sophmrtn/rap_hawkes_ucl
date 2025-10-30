import argparse

def print_message(text):
    print(f"Your messsage is: {text}")

#%% Parse information 
parser = argparse.ArgumentParser()
parser.add_argument('--message', dest='text_message', help='A simple text message to print', required=True)
args = parser.parse_args()

# call function to do correction
print_message(args.text_message)
