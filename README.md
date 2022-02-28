# Importing the RMRIO database in Python

This script allows for importing and indexing the RMRIO database files (_*.mat-files_) in Python as Pandas DataFrames. See below for [instructions](#instructions).

> **RMRIO: A highly resolved MRIO database for analyzing environmental footprints and
Green Economy Progress**
>
> Cabernard, Livia, and Stephan Pfister. 2021. ‘A Highly Resolved MRIO Database for Analyzing Environmental Footprints and Green Economy Progress’. Science of The Total Environment 755 (February): 142587. https://doi.org/10.1016/j.scitotenv.2020.142587.
>
> Download RMRIO via: https://zenodo.org/record/3993659

Author of this script (not of the RMRIO database) is jonas.bunsen@tu-berlin.de

**Note:** This module for importing the RMRIO database is not to be mistaken with the package [_pymrio_](https://github.com/konstantinstadler/pymrio) for importing some of the most common MRIO databases and for conducting MRIO-analyses.

# Instructions

Download the RMRIO database and RMRIO labels for a specific year from
[Zenodo.org](https://zenodo.org/record/3993659):

1. Year_YYYY_RMRIO.zip
2. Labels_RMRIO.zip
    
Extract the *.zip-files into the folder `rmrio-data` and run `main.py`. In the example given in the screenshot below, the file `main.py` is located in a folder named `RMRIO`.

![files](/readme-supplementary/filepaths.png)

Alternatively, the class `rmrio_import` can be loaded in `main.py` with the optional parameters `rmrio_file_path` and `rmrio_year` specified e.g.

```Python
rmrio_db_importer = rmrio.rmrio_import(   
    rmrio_file_path = "path/to/RMRIO/",
    rmrio_year = 2015
    )
```

# Preview ([in Spyder IDE](https://spyder-ide.org/))

## Spyder IDE Variable Explorer
![RMRIO_A_head](/readme-supplementary/variable_explorer.png)

## A-Matrix
![RMRIO_A_head](/readme-supplementary/RMRIO_A_head.png)