# Importing the RMRIO database in Python

This script allows for importing the indexed RMRIO database (*.mat-files) in Python (Pandas).

*"A highly resolved MRIO database for analyzing environmental footprints and
Green Economy Progress"*

Cabernard, Livia, and Stephan Pfister. 2021. ‘A Highly Resolved MRIO Database
for Analyzing Environmental Footprints and Green Economy Progress’.
Science of The Total Environment 755 (February): 142587.
https://doi.org/10.1016/j.scitotenv.2020.142587.

Download the RMRIO database via: https://zenodo.org/record/3993659

Author of this script is jonas.bunsen@tu-berlin.de

If you use this script in your work I'd appreciate a reference to this repository.

# Instructions

Download the RMRIO database and RMRIO labels for a specific year from
[Zenodo.org](https://zenodo.org/record/3993659):

- Year_YYYY_RMRIO.zip
- Labels_RMRIO.zip
    
Extract the *.zip-files into the folder `rmrio-data` and you're good to go. Alternatively, load the class `rmrio_import` with the parameter `rmrio_file_path` and `rmrio_year` specified:

```Python
rmrio_db_importer = rmrio.rmrio_import(   
    rmrio_file_path = "path/to/RMRIO/",
    rmrio_year = 2015
    )
```

# Preview ([in Spyder IDE](https://spyder-ide.org/))
![RMRIO_A_head](/readme/RMRIO_A_head.png)