import argparse
from huggingface_hub import InferenceClient
import sys

# Models available for selection
# For adding more models, extend this dictionary with the model name coppied from HuggingFace
# E.g., 2: "another-model-name"
# Remember to update the argument parser choices accordingly!
MODEL_OPTIONS = {
    0: "meta-llama/Llama-3.3-70B-Instruct",
    1: "mistralai/Mixtral-8x22B-Instruct-v0.1"
}

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Run LLM inference using a prompt loaded from a file."
    )
    
    parser.add_argument(
        "prompt_file",
        type=str,
        help="Path to the text file containing the prompt."
    )
    
    parser.add_argument(
        "-m", "--model-choice",
        type=int,
        choices=MODEL_OPTIONS.keys(),
        default=0,
        help="Model selection: 0 (Llama-3.3-70B-Instruct) or 1 (Mixtral-8x22B-Instruct-v0.1). Default is 0."
    )

    parser.add_argument(
        "-o", "--output",
        type=str,
        default="output.txt",
        help="Path to the output file where the response will be saved. Default is 'output.txt'."
    )
    
    return parser.parse_args()

def main():
    args = parse_arguments()
    PROMPT_FILE_PATH = args.prompt_file
    OUTPUT_FILE_PATH = args.output
    MODEL_NAME = MODEL_OPTIONS[args.model_choice]
    
    try:
        with open(PROMPT_FILE_PATH, 'r', encoding='utf-8') as file:
            prompt_content = file.read()
    except FileNotFoundError:
        print(f"ERROR: Prompt file not found at: {PROMPT_FILE_PATH}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR reading file: {e}")
        sys.exit(1)
    
    # You can change the provider if needed
    client = InferenceClient(
        provider="together"
    )

    messages = [
        {
            "role": "user",
            "content": prompt_content
        }
    ]
    
    print(f"Starting inference on model: {MODEL_NAME}")
    print(f"Prompt loaded from: {PROMPT_FILE_PATH} (Length: {len(prompt_content)} chars)")
    
    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME, 
            messages=messages, 
        )
        
        response_text = completion.choices[0].message.content

        with open(OUTPUT_FILE_PATH, 'w', encoding='utf-8') as f:
            f.write(response_text)

        print(f"Response written to: {OUTPUT_FILE_PATH}")

    except Exception as e:
        print(f"ERROR during API call or file writing: {e}")
        sys.exit(1)
        
if __name__ == "__main__":
    main()