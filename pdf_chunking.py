import fitz  # PyMuPDF
import tiktoken
import math

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text

def count_tokens(text, model="gpt-4"):
    """Count the number of tokens in a text using the tiktoken library."""
    try:
        encoding = tiktoken.encoding_for_model(model)
        tokens = encoding.encode(text)
        return len(tokens), tokens
    except Exception as e:
        print(f"Error counting tokens: {e}")
        return 0, []

def chunk_text_by_tokens(text, token_limit, model="gpt-4"):
    """Split text into chunks that fit within the token limit."""
    _, tokens = count_tokens(text, model)
    encoding = tiktoken.encoding_for_model(model)

    chunks = []
    for i in range(0, len(tokens), token_limit):
        chunk_tokens = tokens[i:i + token_limit]
        chunks.append(encoding.decode(chunk_tokens))

    return chunks

def save_chunks_to_files(chunks, output_folder):
    """Save each chunk to a separate text file."""
    try:
        for idx, chunk in enumerate(chunks):
            file_path = f"{output_folder}/chunk_{idx + 1}.txt"
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(chunk)
    except Exception as e:
        print(f"Error saving chunks: {e}")

if __name__ == "__main__":
    pdf_path = "Animal Farm by George Orwell.pdf"  # Replace with the path to your PDF
    output_folder = "output_chunks"  # Replace with your desired output folder
    token_limit = 4096  # Adjust based on your model's token limit

    # Step 1: Extract text from PDF
    text = extract_text_from_pdf(pdf_path)

    # Step 2: Count tokens in the extracted text
    total_tokens, _ = count_tokens(text)
    print(f"Total tokens in the PDF: {total_tokens}")

    # Step 3: Split text into chunks
    chunks = chunk_text_by_tokens(text, token_limit)
    print(f"Total chunks created: {len(chunks)}")

    # Step 4: Save chunks to separate files
    save_chunks_to_files(chunks, output_folder)
    print(f"Chunks saved to folder: {output_folder}")
