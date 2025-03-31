# GeneExpressionMatrix
A python script that takes GDC gene expression data and creates a gene expression matrix.

### Obtain gene expression data
Using the Genome Data Commons website, https://portal.gdc.cancer.gov/, search for RNA-Seq data for your cancer of interest.
Search for "TCGA" under "Project". Use the four letter code for your cancer of interest to find the TCGA project you are looking for. For example, to find breast cancer data, search for "TCGA-BRCA" under "Project".
Select "RNA-Seq" under "Experimental Strategy".
Select "Transcriptome Profiling" under "Data Category".
Select "Open" under "Access" (unless you have permission to use controlled files).
Download the manifest file for these files.
Upload the manifest file to your working directory. 

### Using the GDC data transfer tool
Download the Ubuntu GDC data transfer tool, gdc-client, from the GDC's website, https://gdc.cancer.gov/access-data/gdc-data-transfer-tool.
Upload the compressed file to your working directory and decompress it.
Move "gdc-client" to your $PATH using the command line below, or another method compatible with your computer.
```
cp gdc-client ~/bin
```
Use GDC client to download all of the files from the manifest file using the following command line. Be sure to replace "manifest.txt" with your manifest file's name.
```
gdc-client download -m manifest.txt
```
You should now have a directory for each gene expression file containing that file's gene expression data.

## Installation
Clone the repository
```
git clone https://github.com/smoorsh/GeneExpressionMatrix.git
```

## Run the program
Change to the GeneExpressionPython directory
Replace 'outfileNameHere.tsv' with your desired matrix name and 'pathToDirectory' with the path to the directory of your gene expression files.
```
cd GeneExpressionPython
python geneExpression.py outfileNameHere.tsv pathToDirectory
```
