import os
import sys
import getopt
import PyPDF2


def merge_pdfs(input_dir, output_file):
    print('Reading PDFs from', input_dir)

    pdfs_to_merge = []
    for filename in os.listdir(input_dir):
        if filename.endswith('.pdf'):
            pdfs_to_merge.append(os.path.join(input_dir, filename))
            print(filename)

    if len(pdfs_to_merge) > 0:
        pdfWriter = PyPDF2.PdfFileWriter()
        for filename in pdfs_to_merge:
            pdfFileObj = open(filename, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            # Opening each page of the PDF
            for pageNum in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)

        outfile = output_file + '.pdf'
        print()
        print('Writing the merged PDF to', outfile)
        # Save PDF to file
        pdfOutput = open(outfile, 'wb')
        # Outputting the PDF
        pdfWriter.write(pdfOutput)
        # Closing the PDF writer
        pdfOutput.close()
    else:
        print('No files to merge')


def main(opts):
    for opt, arg in opts:
        if opt == '-h':
            print('python3 merge_pdfs.py -i <input_dir> -o <output_file>')
            sys.exit()
        elif opt in ['-i', '--input_dir']:
            input_dir = arg
        elif opt in ['-o', '--output_file']:
            output_file = arg
    
    merge_pdfs(input_dir, output_file)


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["input_dir=", "output_file="])
    except:
        print('Usage: python3 merge_pdfs.py -i <input_dir> -o <output_file>')
        sys.exit(2)
    
    main(opts)
