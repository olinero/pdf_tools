import os
from PyPDF2 import PdfMerger
from tkinter import Tk, filedialog

def combine_pdfs_in_folder():
    # Open a dialog to select the folder
    Tk().withdraw()  # We don't want a full GUI, so keep the root window from appearing
    folder_path = filedialog.askdirectory(title="Select Folder Containing PDFs")

    if not folder_path:
        print("No folder selected. Exiting...")
        return

    # Initialize a PDF merger object
    pdf_merger = PdfMerger()

    # Track if we added any PDFs
    pdfs_added = False

    # Loop through the files in the selected folder
    for item in sorted(os.listdir(folder_path)):
        if item.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, item)
            print(f"Adding {pdf_path} to merger")
            try:
                pdf_merger.append(pdf_path)
                pdfs_added = True
            except Exception as e:
                print(f"Error adding {pdf_path}: {e}")

    # Check if any PDFs were added
    if not pdfs_added:
        print("No PDFs were added to the merger. Exiting...")
        return

    # Save the merged PDF to the same folder
    output_pdf_path = os.path.join(folder_path, "merged_document.pdf")
    try:
        pdf_merger.write(output_pdf_path)
        pdf_merger.close()
        print(f"All PDFs combined into {output_pdf_path}")
    except Exception as e:
        print(f"Error saving merged PDF: {e}")

if __name__ == "__main__":
    combine_pdfs_in_folder()
