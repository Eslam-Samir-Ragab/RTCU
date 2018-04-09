# Reverse Translator by Codon Usage (RTCU)
 The program uses the codon usage preference of your choice to reverse translate a protein or DNA sequence

## How to use:
1.	you need to install [python 2.7](https://www.python.org/downloads/) or [python 3](https://www.python.org/downloads/) on your machine.
2. you need to install [Numpy](https://pypi.python.org/pypi/numpy) and [Biopython](http://biopython.org/wiki/Download)
3. you need to install future module by [pip command](https://docs.python.org/3/installing/)
4.	Click “Clone or download” > “Download ZIP” > extract the downloaded file.
5.	Open the file “**rtcu.py**” with (python.exe).
  * [Windows](http://stackoverflow.com/a/1527012/7414020)
  * U/Linux : use the command `chmod u+x rtcu.py`
  * Mac : use the command `python rtcu.py`
6.	State your variables and press Enter.

## Example

If you want to reverse translate a protein sequence do the following:
1. copy the file "original_codon_usage.txt" to a new file with your preferred name, for example "mycodons.txt".
2. modify the codons for each amino acid in your newly copied file based on your organism / preference.
3. use this file as a guide for the program by applying this command:  
`python rtcu.py -in (input_file) -out (output_file) -codon_usage mycodons.txt`

### **The full RTCU Cheat sheet and notes are [here](https://github.com/Eslam-Samir-Ragab/RTCU/blob/master/additional/RTCU%20Cheat%20sheet.pdf)**


### Any errors please send me an email to <eslam_samir_ragab.ibrahim@stud-mail.uni-wuerzburg.de> or <eslam.ebrahim@pharma.cu.edu.eg>
## Visit [my website](https://sites.google.com/pharma.cu.edu.eg/eslam-ibrahim/) for more details, other publications, and contact
