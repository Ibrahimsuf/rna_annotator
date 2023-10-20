# rna_annotator

Python script to get rna annotations from MCAnnotate, 3DNA, and RNAVIEW.
Uses RNApdbee ("http://rnapdbee.cs.put.poznan.pl/") webserver to get MCAnnotate, 3DNA, and RNAVIEW annotations. Then puts all of the annotations into csv.

```bash
pip3 install -r requirements.txt
python main.py <pdb id> <output_file.csv>
```
