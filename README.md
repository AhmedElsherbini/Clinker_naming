# Clinker_naming
**Kindly if you find this repo useful for your work, cite & star this repo**

**What is this script?**

[Clinker](https://github.com/gamcil/clinker) is a my favorite tool for synteny visualization and gnemic data showing. However, for gene annotation, it is a bit complicated in comparison Easyfig. This is a script that is a workaround to overcome this.


**What do you need?**

This script is working on Python 3.9

You shall have many GenBank files

For many genebank files
```bash
for d in *.gbk ; do  f=$(echo $d | sed -E "s/\.gbk*//") ; python clinker_naming.py -i ${f}.gbk -o ${f}_named.gbk  ; done
```
Let's do the simple Clinker command line

```bash
clinker *_named.gbk -p file.html
```

**Well, what is the heck here?**

Any GenBank file has a conserved sentence among all bacterial GenBank files, which is (transl_table=11), which is related to the translation table of [codon](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi).

Well, we simply substitute the trans_table with *, and then all genes will have a conserved value of * at the transl_table in the HTML file.

Then, you have to open the HTML file 




