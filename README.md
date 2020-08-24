# PDF Tools

Some pdf utilities like merging different pdfs into one.

## Usage

1. Install PyPDF2 package from pip

```bash
pip3 install PyPDF2
```

2. To merge pdfs, place them in a folder and run the `merge_pdfs.py` script. The script merges all the pdfs in the specified folder in alphabetical order of their names I think.

```bash
python3 merge_pdfs.py -i <input_dir> -o <output_file>
```
