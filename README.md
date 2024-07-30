Document Similarity Matching System
Overview
  This project implements a document similarity matching system for invoices. The system compares an input invoice with a set of existing invoices to identify the most   similar document based on content and structure. The primary objective is to facilitate the automatic categorization of invoices by matching them to existing           templates or previously processed invoices.
Chosen Document Representation Method
  The invoices are represented using text extracted from PDF files. The text content is processed and converted into numerical feature vectors using the Term             Frequency-  Inverse Document Frequency (TF-IDF) method. This method helps emphasize significant words while reducing the weight of commonly occurring words, ensuring   a more accurate representation of the invoice's unique content.
Similarity Metric Used
  The similarity between invoices is calculated using the Cosine Similarity metric. Cosine similarity measures the cosine of the angle between two vectors (in this       case, TF-IDF vectors), with values ranging from 0 to 1. A score of 1 indicates identical documents, while a score closer to 0 indicates dissimilarity. This metric is   effective for comparing text documents, as it considers the direction of the vectors rather than their magnitude, thus focusing on the content similarity.
Instructions on How to Run the Code
1.	Setup and Requirements
o	Python Version: Ensure you have Python 3.x installed.
o	Dependencies: Install the required Python packages using the following command:
pip install PyPDF2 scikit-learn
2.	Directory Structure
o	Place the invoices in the following folder structure:
document_similarity/
├── test/
│   ├── invoice_77098.pdf
│   ├── invoice_102857.pdf
└── train/
    ├── invoice_102856.pdf
    ├── invoice_77073.pdf
    ├── Faller_8.pdf
    ├── 2024.03.15_1145.pdf
    └── 2024.03.15_0954.pdf
o	The test folder contains the input invoices you want to compare.
o	The train folder contains the existing invoices used for matching.
3.	Running the Code
o	Update the paths in the script if necessary to point to your local directories.
o	Execute the script using a Python interpreter:
python document_similarity.py
o	The script will process each input invoice in the test folder, compare it against the invoices in the train folder, and output the most similar invoice along with the similarity score.
4.	Understanding the Output
o	For each input invoice, the script will display:
	The name of the input invoice.
	The name of the most similar invoice from the training set.
	The similarity score, indicating the degree of similarity.
5.	Example Output
Input Invoice: invoice_102857.pdf
Most similar invoice: invoice_102856.pdf
Similarity score: 0.7612220242402062
==================================================
Input Invoice: invoice_77098.pdf
Most similar invoice: invoice_77073.pdf
Similarity score: 0.8101192883834113
Conclusion
This document similarity matching system provides a straightforward and effective solution for identifying similar invoices based on their content. The combination of text extraction, TF-IDF feature representation, and cosine similarity ensures accurate and meaningful comparisons, facilitating efficient document management and categorization.
Notes
•	Ensure the PDF files are properly formatted and accessible.
•	The system currently focuses on text content; however, additional features such as image similarity or structural analysis can be incorporated for improved accuracy.

