import os
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
    return text

def compute_similarity(input_text, database_texts):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([input_text] + database_texts)
    similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
    return similarities.flatten()

def main(input_folder, database_folder):
    # Process each file in the test folder as an input invoice
    for input_filename in os.listdir(input_folder):
        if input_filename.endswith(".pdf"):
            input_path = os.path.join(input_folder, input_filename)
            input_text = extract_text_from_pdf(input_path)
            
            # Extract text from all database invoices
            database_texts = []
            database_filenames = []
            for filename in os.listdir(database_folder):
                if filename.endswith(".pdf"):
                    file_path = os.path.join(database_folder, filename)
                    database_texts.append(extract_text_from_pdf(file_path))
                    database_filenames.append(filename)
            
            # Compute similarities
            similarities = compute_similarity(input_text, database_texts)
            
            # Find the most similar invoice
            most_similar_index = similarities.argmax()
            most_similar_score = similarities[most_similar_index]
            most_similar_invoice = database_filenames[most_similar_index]
            
            # Print the result
            print(f"Input Invoice: {input_filename}")
            print(f"Most similar invoice: {most_similar_invoice}")
            print(f"Similarity score: {most_similar_score}")
            print("="*50)

# Example usage
input_folder = r'C:\Users\Ravi Kumara C P\OneDrive\Desktop\document similarity\test'
database_folder = r'C:\Users\Ravi Kumara C P\OneDrive\Desktop\document similarity\train'
main(input_folder, database_folder)
