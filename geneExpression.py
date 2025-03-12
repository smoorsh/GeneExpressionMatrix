### import necessary libraries ###
import sys
import numpy as np
import pandas as pd
import os
import glob

### open and read files, create output file ###
outfile = sys.argv[1]
directory = sys.argv[2]
columns = ['gene_id', 'gene_name', 'gene_type', 'unstranded', 'stranded_first', 'stranded_second', 'tpm_unstranded', 'fpkm_unstranded', 'fpkm_uq_unstranded']

### locate each subdirectory ###
subdirs = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d)) and not d.startswith('.')]
total_dirs = len(subdirs)

# Dictionary to store gene expression data
gene_dict = {}

# Keep track of all sample IDs for creating the matrix later
all_samples = []

# Process each subdirectory
for subdir in subdirs:
    dir_path = os.path.join(directory, subdir)
    sample_id = subdir  # Using directory name as sample ID
    all_samples.append(sample_id)
    
    # Find .tsv files in the directory
    tsv_files = glob.glob(os.path.join(dir_path, "*.tsv"))
    
    for tsv_file in tsv_files:
    
        # Read the TSV file
        whole_df = pd.read_csv(tsv_file, sep='\t', comment='#', dtype="string", names=columns)
            
        # Remove the first five rows from each file
        new_df = whole_df.drop(range(5))
            
        # Extract gene_name and stranded_second columns
        for _, row in new_df.iterrows():
            gene_name = row['gene_name']
            expression = row['stranded_second']
                
            # Initialize the gene entry if it doesn't exist
            if gene_name not in gene_dict:
                gene_dict[gene_name] = {}
                
            # Store the expression value for this gene and sample
            gene_dict[gene_name][sample_id] = expression
                

# Create a DataFrame from the dictionary
expression_matrix = pd.DataFrame.from_dict(gene_dict, orient='index')

# Fill NaN values (genes not found in some samples)
expression_matrix = expression_matrix.fillna('0')

# Ensure all samples are included (even if some genes weren't found in them)
for sample in all_samples:
    if sample not in expression_matrix.columns:
        expression_matrix[sample] = '0'

# Save the expression matrix
expression_matrix.to_csv(outfile, sep='\t')
