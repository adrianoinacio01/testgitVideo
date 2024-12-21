import os
import openai
# from openai import openAI

def read_text_chunks(input_folder):
    """Read pre-processed text files from a folder."""
    chunks = []
    try:
        for file_name in sorted(os.listdir(input_folder)):
            file_path = os.path.join(input_folder, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                chunks.append(file.read())
    except Exception as e:
        print(f"Error reading files: {e}")
    return chunks

def summarize_chunk(chunk, model="gpt-4", max_tokens=1000):
    """Summarize a single chunk using OpenAI GPT API."""
    openai.api_key = os.getenv("OPENAI_API_KEY")  # Ensure API key is set

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an expert summarizer. Summarize the text below by paraphrasing and reorganizing while retaining core ideas."},
                {"role": "user", "content": chunk}
            ],
            max_tokens=max_tokens,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except openai.error.InvalidRequestError as e:
        print(f"Invalid request: {e}")
        return ""
    except openai.error.AuthenticationError as e:
        print(f"Authentication error: {e}")
        return ""
    except openai.error.OpenAIError as e:
        print(f"OpenAI API error: {e}")
        return ""
    except Exception as e:
        print(f"Unexpected error: {e}")
        return ""

def generate_summaries(input_folder, output_file, model="gpt-4", max_tokens=1000):
    """Generate summaries for all text chunks and combine them into a single file."""
    chunks = read_text_chunks(input_folder)
    full_summary = []

    for idx, chunk in enumerate(chunks):
        print(f"Summarizing chunk {idx + 1}/{len(chunks)}...")
        summary = summarize_chunk(chunk, model, max_tokens)
        if summary:  # Only append non-empty summaries
            full_summary.append(summary)

    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write("\n\n".join(full_summary))
        print(f"Summary saved to {output_file}")
    except Exception as e:
        print(f"Error saving summary: {e}")

if __name__ == "__main__":
    input_folder = r"C:\\Users\\adria\\Workspace\\programas\\resumirTexto\\solutions_neetcode\\output_chunks"  # Folder containing your text chunks
    output_file = r"C:\\Users\\adria\\Workspace\\programas\\resumirTexto\\solutions_neetcode\\final_summary.txt"  # Desired output file
    
    generate_summaries(input_folder, output_file)
