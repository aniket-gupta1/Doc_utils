import os
import sys

def convert(filename_doc, filename_pdf):
	os.system(f"lowriter --convert-to pdf:writer_pdf_Export {filename_doc} --outdir {filename_pdf}")

if __name__=="__main__":
	if len(sys.argv)==1:
		print("Error: No file given")
		print("Usage: convert_docx_to_pdf.py filename.docx output_dir")
		exit()

	if 2>=len(sys.argv):
		print("No output path given")
		convert(sys.argv[1], ".")
		exit()
	else:
		convert(sys.argv[1], sys.argv[2])

