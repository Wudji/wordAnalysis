## Word Analysis

This repository uses the Python library ***spaCy*** to analyze and compare the ***mean dependency distance*** (MDD) between magazine texts and academic papers as part of a research for the ***Academic English Writing*** course.

### How to Use

1. **Install dependencies**

    First, make sure you have Python installed. Then, install all required libraries using the following command:

   ```
   pip install -r requirements.txt
   ```

   Additionally, download the English language model for spaCy (if not already installed):

   ```
   python -m spacy download en_core_web_lg
   ```

2. **Prepare your text files**

   - One text file should contain magazine writing.
   - The other should contain academic paper writing.

3. **Run the script**

    Use the following command to run the analysis script:

   ```
   python release.py --magazine path/to/magazine.txt --paper path/to/paper.txt
   ```

   Example:

   ```
   python release.py --magazine data/magazine_sample.txt --paper data/paper_sample.txt
   ```
