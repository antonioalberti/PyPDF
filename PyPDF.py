import fitz  # PyMuPDF
from PIL import Image
import os
import img2pdf
import sys

# Dimensions of an A4 page in millimeters
A4_WIDTH_MM = 210  # 210 mm (A4 width)
A4_HEIGHT_MM = 297  # 297 mm (A4 height)

def pdf_to_images(pdf_path, output_folder):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    # Extract the file name without extension to create the folder
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_path = os.path.join(output_folder, pdf_name)

    # Create the folder if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    image_files = []

    # Convert each page of the PDF into an image
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # Increase resolution
        img_filename = os.path.join(output_path, f"page_{page_num+1}.jpg")
        pix.save(img_filename)
        image_files.append(img_filename)

    pdf_document.close()
    return image_files, output_path

def images_to_pdf(image_files, output_pdf_path):
    # Convert the images back to PDF in A4 format
    with open(output_pdf_path, "wb") as f:
        a4_page_size = (img2pdf.mm_to_pt(A4_WIDTH_MM), img2pdf.mm_to_pt(A4_HEIGHT_MM))  # A4 dimensions in points
        layout_fun = img2pdf.get_layout_fun(a4_page_size)
        f.write(img2pdf.convert(image_files, layout_fun=layout_fun))

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py path_to_pdf")
        return

    # Use os.path.normpath to normalize the path
    pdf_path = os.path.normpath(sys.argv[1])
    
    if not os.path.exists(pdf_path):
        print(f"Error: the file '{pdf_path}' was not found.")
        return

    # Extract the directory of the input PDF
    output_folder = os.path.dirname(pdf_path)

    # Convert PDF to images and get the output directory
    image_files, output_path = pdf_to_images(pdf_path, output_folder)

    # Create PDF from the generated images with the same name as the original PDF
    output_pdf_name = os.path.splitext(os.path.basename(pdf_path))[0] + ".pdf"
    output_pdf_path = os.path.join(output_path, output_pdf_name)
    images_to_pdf(image_files, output_pdf_path)

    print(f"Images and new PDF created at: {output_pdf_path}")

if __name__ == "__main__":
    main()
