# TEXT-SUMMARIZATION-TOOL

**COMPANY NAME** : CODTECH IT SOLUTIONS PVT.LTD

**INTERN NAME** : SHAIK MUSHARAF

**INTERN ID** : CT08DM690

**DOMAIN** :ARTIFICIAL INTELLIGENCE

**DURATION **: 8 WEEKS

**MENTOR** : NEELA SANTHOSH

**DESCRIPTION:**

The Text Summarization Tool is a Python script developed using the Natural Language Toolkit (NLTK). It implements an extractive summarization method to automatically generate concise summaries of longer articles or documents. The script identifies the most important sentences based on word frequency and outputs a brief, coherent summary that captures the key points of the original content.

**Here's an overview of its core functionality:**

**1.Input Validation:**

The script first checks whether the input text is valid (non-empty and of string type).

If the input is too short (i.e., has fewer sentences than the summary length), it simply returns the original text.

**2.Text Preprocessing:**
   
The input text is tokenized into individual sentences using sent_tokenize().

It is also tokenized into words, and common stopwords (from NLTK's English stopword list) are removed.

Only alphanumeric words are retained to eliminate punctuation and irrelevant tokens.

**3.Word Frequency Calculation:**

The script calculates the frequency of each remaining word after filtering.

These frequencies are normalized by dividing each frequency by the maximum frequency found, producing a relative importance score for each word.

**4.Sentence Scoring:**

Each sentence is assigned a score based on the total normalized frequency of important words it contains.

The higher the combined score, the more "informative" the sentence is considered to be.

**5.Summary Generation:**

Sentences are ranked based on their scores, and the top N highest-scoring sentences are selected (default is 3).

These selected sentences are then reordered based on their original position in the text to maintain logical flow.

This tool is particularly useful for quickly understanding the main points of lengthy content, saving time by providing a condensed version of the original material.

**output:**

![Task1 py - speech_to_text_tool - Visual Studio Code 07-07-2025 07_33_48](https://github.com/user-attachments/assets/925c00c4-9af7-40d7-8700-fe486665a523)

