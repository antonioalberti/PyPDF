import fitz  # PyMuPDF
from PIL import Image
import os
import img2pdf
import sys

# Dimensões de uma página A4 em milímetros
A4_WIDTH_MM = 210  # 210 mm (A4 width)
A4_HEIGHT_MM = 297  # 297 mm (A4 height)

def pdf_to_images(pdf_path, output_folder):
    # Abrir o arquivo PDF
    pdf_document = fitz.open(pdf_path)
    # Extrair o nome do arquivo sem extensão para criar a pasta
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_path = os.path.join(output_folder, pdf_name)

    # Criar a pasta se não existir
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    image_files = []

    # Converter cada página do PDF em uma imagem
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # Aumenta a resolução
        img_filename = os.path.join(output_path, f"page_{page_num+1}.jpg")
        pix.save(img_filename)
        image_files.append(img_filename)

    pdf_document.close()
    return image_files, output_path

def images_to_pdf(image_files, output_pdf_path):
    # Converter as imagens de volta para PDF no formato A4
    with open(output_pdf_path, "wb") as f:
        a4_page_size = (img2pdf.mm_to_pt(A4_WIDTH_MM), img2pdf.mm_to_pt(A4_HEIGHT_MM))  # A4 dimensions in points
        layout_fun = img2pdf.get_layout_fun(a4_page_size)
        f.write(img2pdf.convert(image_files, layout_fun=layout_fun))

def main():
    if len(sys.argv) < 2:
        print("Uso: python script.py caminho_para_o_pdf")
        return

    # Usar os.path.normpath para normalizar o caminho
    pdf_path = os.path.normpath(sys.argv[1])
    
    if not os.path.exists(pdf_path):
        print(f"Erro: o arquivo '{pdf_path}' não foi encontrado.")
        return

    # Extrair o diretório do PDF de entrada
    output_folder = os.path.dirname(pdf_path)

    # Converter PDF em imagens e obter o diretório de saída
    image_files, output_path = pdf_to_images(pdf_path, output_folder)

    # Criar PDF a partir das imagens geradas com o mesmo nome do PDF original
    output_pdf_name = os.path.splitext(os.path.basename(pdf_path))[0] + ".pdf"
    output_pdf_path = os.path.join(output_path, output_pdf_name)
    images_to_pdf(image_files, output_pdf_path)

    print(f"Imagens e novo PDF criados em: {output_pdf_path}")

if __name__ == "__main__":
    main()
