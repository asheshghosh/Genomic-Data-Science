# Genomic Data Science

Welcome to the **Genomic Data Science** repository. Here, you'll find algorithms and best practices for genomic data analysis, ranging from basic DNA string manipulation to advanced sequence matching and genome assembly.

---

## Table of Contents

- [Part 1.1: DNA Strings Notebook](#part-11-dna-strings-notebook)
- [Part 1.2: DNA Sequence Notebook](#part-12-dna-sequence-notebook)
- [Part 1.3: DNA Sequence Matching Notebook](#part-13-dna-sequence-matching-notebook)
- [Part 1.4: Lambda Virus Genome Notebook](#part-14-lambda-virus-genome-notebook)
- [Part 2.1: Approx Boyer Moore Notebook](#part-21-approx-boyer-moore-notebook)
- [Part 2.2: DNA Indexing Notebook](#part-22-dna-indexing-notebook)
- [Part 2.3: Approximate Matching Notebook](#part-23-approximate-matching-notebook)
- [Part 2.4: Homo Sapiens Chromosome 1 GRCh38 Notebook](#part-23-homo-sapiens-chromosome-1-GRCh38-notebook)
- [Part 3.1: Dynamic Programming and Distances Notebook](#part-31-dynamic-programming-and-distances-notebook)
- [Paret 3.2: Dynamic Programming Application Notebook](#part-32-dynamic-programming-application-notebook)
- [Part 4.1:]
- [Part 4.2:]

---

## Part 1.1: DNA Strings Notebook

This section covers the basics of DNA strings and fundamental algorithms for their manipulation.

### Topics Covered

- **Basics of DNA Strings**  
  Understand the properties and representation of DNA sequences.

- **Longest Common Sequence**  
  Determine the longest common subsequence between two strings.

- **Exact String Matching**  
  Check if two given strings are identical.

- **Complementary Strand Generation**  
  Obtain the complementary strand of a given DNA sequence.

- **Virus Sequence Retrieval**  
  Extract the sequence of a virus using the `lambda_virus.fa` file.

- **Nucleobase Counting**  
  Count the individual nucleobases (A, T, G, and C) in a genome.

- **Histogram Plotting**  
  Use Python's matplotlib to plot a histogram of base counts for A, T, G, and C.

---

## Part 1.2: DNA Sequence Notebook

Focuses on working with DNA sequence data in FASTQ format and performing quality control.

### Topics Covered

- **Data Acquisition**  
  Download model DNA sequence data in FASTQ format.

- **FASTQ File Parsing**  
  Read FASTQ files to generate sequences along with their associated quality scores.

- **Quality Score Conversion**  
  Convert quality score characters (Phred+33 encoded) to numerical values.

- **Quality Score Visualization**  
  Plot quality scores to assess the sequencing quality.

- **GC Content Analysis**  
  Determine the GC content of the species based on the sequencing data.

---

## Part 1.3: DNA Sequence Matching Notebook

Develop and implement algorithms for DNA sequence matching.

### Topics Covered

- **Phix Genome Retrieval**  
  Obtain the Phix genome file.

- **Genome Reading and Parsing**  
  Read the genome and implement a matching algorithm.

- **Sequence Matching**  
  Download a sequence and apply the matching algorithm.

- **Complementary Strand Matching**  
  Enhance matching by considering the complementary strand of DNA.

- **Histogram of Matching Regions**  
  Plot a histogram showing regions in the genome with matching sequences.

---

## Part 1.4: Lambda Virus Genome Notebook

Apply genomic data science techniques on the Lambda virus genome and extend these methods to the Human genome.

### Topics Covered

- **Lambda Virus Genome Analysis**  
  Implement and test algorithms on the Lambda virus genome.

- **Human Genome Analysis**  
  Extend the concepts and algorithms to analyze the Human genome.

---

## Part 2.1: Approx Boyer Moore Notebook

While exact matching algorithms have been extensively studied, real-world genomic applications often demand approximate matching methods. However, when exact matching is appropriate, the **Boyer-Moore algorithm** stands out due to its exceptional efficiency in scanning massive DNA sequences. By leveraging heuristics like the bad-character and good-suffix rules, Boyer-Moore frequently skips large sections of the text, dramatically reducing the number of comparisons compared to naive methods.

### Advantages of the Boyer-Moore Algorithm in Genomic Data Science

- **Efficiency:**  
  Operates in sublinear time on average by quickly eliminating unlikely match positions, making it ideal for handling vast genomic datasets.

- **Reduced Comparisons:**  
  Employs heuristics that minimize unnecessary character comparisons, significantly speeding up the search process.

- **Effective Preprocessing:**  
  Preprocesses the pattern in linear time, a beneficial feature when the same pattern is used to search across extensive genomic data.

- **Scalability:**  
  Its computational efficiency allows it to scale effectively to large DNA sequences, a critical requirement in genomic research.

- **Adaptability:**  
  The core principles of Boyer-Moore can be extended to support approximate matching, addressing biological variability where perfect matches are rare.

Overall, the Boyer-Moore algorithm is a robust and adaptable tool for efficient and effective pattern matching in genomic research.


### More algorithms

#### Raita Algorithm

The Raita algorithm is a variant of the Boyer-Moore string matching algorithm that improves performance by performing quick pre-checks. Specifically, it first compares the last, first, and middle characters of the pattern against the corresponding characters in the text. Only if these key positions match does it proceed to a full comparison of the entire pattern. This strategy reduces the number of unnecessary character comparisons, making the algorithm more efficient when scanning large texts, such as genomic sequences.

#### Apostolico–Giancarlo Algorithm

The Apostolico–Giancarlo algorithm is an optimized string matching method that refines the Boyer–Moore approach. It introduces a skip mechanism that avoids rechecking characters that have already been matched in previous alignments, thereby reducing redundant comparisons. This makes the algorithm particularly efficient in scenarios with overlapping or repetitive pattern occurrences, offering improved performance in worst-case cases while maintaining the benefits of Boyer–Moore’s heuristics such as the bad-character and good-suffix rules.

#### Knuth–Morris–Pratt Algorithm

The Knuth–Morris–Pratt (KMP) algorithm is an efficient string matching method that preprocesses the pattern to create a "failure function" (or prefix function). This function indicates the longest proper prefix of the pattern that is also a suffix, enabling the algorithm to bypass redundant comparisons when a mismatch occurs. By doing so, KMP achieves a worst-case time complexity of O(n + m), where n is the length of the text and m is the length of the pattern, making it highly effective for searching within large texts.

---

## Part 2.2: DNA Indexing Notebook

---

## Part 2.3: Approximate Matching Notebook

---

## Part 2.4: Homo Sapiens Notebook

---

## Part 3.1: Dynamic Programming and Distances Notebook

---

## Part 3.1: Dynamic Programming Application Notebook

---

This repository is designed to guide you through the core algorithms and methodologies used in Genomic Data Science. Each notebook builds upon previous exercises to help you gain a comprehensive understanding of the field. Enjoy exploring and learning!
