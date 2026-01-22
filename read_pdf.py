"""
Simple PDF Text Extractor
This script demonstrates 'Document Reading' by extracting text 
from the Japanese Housing Report PDF.
"""

from pypdf import PdfReader
import os

# Path to the PDF file (Assuming it's in the neighboring folder on Desktop)
pdf_path = os.path.expanduser("~/Desktop/japanese_housing/Japanese_Housing_Report.pdf")

def read_pdf_content(file_path):
    print(f"📄 file: {file_path}")
    print("-" * 50)
    
    try:
        # Create a PDF reader object
        reader = PdfReader(file_path)
        
        # Get the number of pages
        print(f"📚 Number of Pages: {len(reader.pages)}")
        
        # --- Read Page 1 (The Summary) ---
        print("\n🔍 Reading Page 1 Content:\n")
        page = reader.pages[0]
        text = page.extract_text()
        
        # Print the extracted text
        print(text)
        print("-" * 50)
        print("✅ Document read successfully!")
        
    except FileNotFoundError:
        print("❌ Error: Could not find the PDF file.")
        print("Please check if 'Japanese_Housing_Report.pdf' exists in '~/Desktop/japanese_housing/'.")
    except Exception as e:
        print(f"❌ Error reading PDF: {e}")

if __name__ == "__main__":
    read_pdf_content(pdf_path)
