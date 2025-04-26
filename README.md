# PyPDF

This Python script converts a PDF file into images (one image per page) and then recreates a new PDF from those images, formatted to A4 page size.

## Features

- Converts each page of a PDF into a high-resolution JPEG image.
- Saves the images in a folder named after the original PDF file.
- Recreates a PDF from the generated images, ensuring the pages are formatted to A4 size.

## Requirements

- Python 3.x
- PyMuPDF (`fitz`)
- Pillow (`PIL`)
- img2pdf

You can install the required packages using pip:

```bash
pip install pymupdf pillow img2pdf
```

## Usage

Run the script from the command line, passing the path to the PDF file as an argument:

```bash
python PyPDF.py path/to/your/file.pdf
```

The script will create a folder with the same name as the PDF file in the same directory, containing the images of each page. It will also generate a new PDF from these images inside that folder.

## Example

```bash
python PyPDF.py example.pdf
```

Output:

- A folder named `example` containing `page_1.jpg`, `page_2.jpg`, etc.
- A new PDF file named `example.pdf` inside the `example` folder, with pages formatted to A4 size.

## Notes

- The script increases the resolution of the images extracted from the PDF for better quality.
- The new PDF is created using the images and formatted to standard A4 dimensions.

## License

This project is provided as-is without any warranty.
