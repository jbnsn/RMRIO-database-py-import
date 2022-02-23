# Importing the RMRIO database in Python

This script allows for importing and indexing the RMRIO database files (*.mat-files) in Python as Pandas DataFrames.

> **RMRIO: A highly resolved MRIO database for analyzing environmental footprints and
Green Economy Progress**
>
> Y Cabernard, Livia, and Stephan Pfister. 2021. ‘A Highly Resolved MRIO Database for Analyzing Environmental Footprints and Green Economy Progress’. Science of The Total Environment 755 (February): 142587. https://doi.org/10.1016/j.scitotenv.2020.142587.
>
> Download RMRIO via: https://zenodo.org/record/3993659

Author of this script (not the RMRIO database) is jonas.bunsen@tu-berlin.de

# Instructions

Download the RMRIO database and RMRIO labels for a specific year from
[Zenodo.org](https://zenodo.org/record/3993659):

- Year_YYYY_RMRIO.zip
- Labels_RMRIO.zip
    
Extract the *.zip-files into the folder `rmrio-data` and run `main.py`. The class `rmrio_import` can be loaded with the parameters `rmrio_file_path` and `rmrio_year` specified e.g.

```Python
rmrio_db_importer = rmrio.rmrio_import(   
    rmrio_file_path = "path/to/RMRIO/",
    rmrio_year = 2015
    )
```

# Preview ([in Spyder IDE](https://spyder-ide.org/))
![RMRIO_A_head](/readme-supplementary/RMRIO_A_head.png)