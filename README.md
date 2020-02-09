# Unique stopwords for subcategories

A product falls in the hierarchy of a category, subcategory and a microcategory. This repository has a python script which runs iterative loops for multiple subcategories huge data. The aim is to find the final non-repeating stopwords for each of the subcategories after considering the individual microcategories in which some stop words may repeat. For example, in the category 'Industrial Uniforms & Safety Wear', there is a subcategory 'Industrial Gloves' which has few microcategories as 'Cut Resistant Gloves', 'Chemical Resistant Gloves', 'Cold Resistant Gloves',etc. all of them have the same stop word 'resistant' within the same subcategory.

In computing, stop words are words which are filtered out before processing of natural language data. Stop words are generally the most common words in a language. They are better removed because they do not contribute in improving the SEO and only introduce inaccurate results if not removed.

Two files are input: first, which has the subcategory to microcategory relations in csv columns and second, which has the subcategory wise high frequency stopwords in csv columns.

## Dependencies :
* Pandas

## Usage :
```
python subcatwiseStopwords700.py
```

**Note :** Replace the file names with your file path on your local machine.
