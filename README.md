# Application for predicting the secondary structure of RNA using Nussinov's Algorithm

## Table of contents
* [Motivation](#motivation)
* [Project assumptions](#project-assumptions)
* [Technologies](#technologies)
* [Application overview](#application-overview)
* [Usage](#usage)
* [Examples of prediction](#examples-of-prediction)
  

  
# Motivation
The objective of this project was to develop a functional desktop application capable of predicting RNA secondary structures based on user-input RNA sequences. My interest in bioinformatics during my engineering studies prompted me to choose this topic for my diploma thesis. I encountered various existing solutions to RNA folding problems, each with its own set of features. To address this, I consolidated these different approaches and integrated them into a comprehensive application. Some of the key functionalities include: support for GU pairs, customizable settings for the minimal number of nucleotides in loops, detailed information on specific loop types, visualization of secondary structures using dot-bracket notation, and the representation of flat graphs.
These features were designed to offer users a versatile tool for RNA structure prediction, catering to a wide range of research and practical applications in bioinformatics

# Project assumptions
- **Graphical User Interface (GUI)**: The application will feature a graphical user interface, facilitating user interaction through intuitive browsing and navigation.
- **Versatile Input Data**: Users will be able to input RNA sequences of varying lengths, enabling flexible prediction of secondary structure for different types of sequences.
- **Specific Loop Information**: The application will provide detailed information regarding specific loops in the RNA secondary structure, enhancing user understanding of prediction results.
- **Configurable Minimum Loop Length Settings**: Users will have the ability to adjust the minimum loop length, allowing for more precise RNA structure prediction according to their preferences or research requirements.
- **Inclusion of GU Pairs**: The application will allow for the inclusion of GU pairs in the RNA secondary structure prediction process, essential for prediction accuracy.
- **Result Visualization in Dot-Bracket Format**: The resulting RNA secondary structure will be presented in dot-bracket format, facilitating user comprehension of the structure.
- **Visualization of Obtained Structure Using Flat Graph**: Additionally, users will be able to visualize the obtained RNA structure using a flat graph, providing an additional layer of understanding and analysis of the results.

# Technologies:
- Python: 3.9
- Tkinter: 8.6.12
- draw_rna: 0.1.0
- re:  2022.7.9

# Application overview:
Here is the list of available features:
- **Graphical User Interface (GUI)**: An intuitive user interface facilitating RNA secondary structure prediction.
- **Versatile Input Data**: Ability to input RNA sequences of varying lengths for flexible structure prediction.
- **Customizable Settings**: Customizable minimum loop length settings allowing for precise RNA structure prediction.
- **Support for GU Pairs**: Support for GU pairs in the RNA structure prediction process for increased accuracy.
- **Detailed Structure Information**: Detailed information regarding individual loops in the RNA secondary structure.
- **Structure Visualization**: Visualization of RNA structure in dot-bracket notation and via a flat graph.

![GUI of the application](https://github.com/Szymi00/RNA-Structure-Prediction-App/blob/main/assets/images/GUI.jpg?raw=true)

# Usage:
1. Launch the application.
2. Enter an RNA sequence in the designated input field.
3. Adjust settings such as allowing GU pairs and setting the minimal loop length according to your requirements.
4. Click the "Predict Structure" button to generate the secondary structure prediction.
5. The predicted structure will be displayed in dot-bracket notation, along with detailed information on hairpin loops, bulge loops, internal loops, and external bases.
6. Optionally, click the "Visualize Structure" button to view a graphical representation of the predicted structure using a flat graph.

   
# Examples of prediction:
All sequences were taken from [Rfam database](https://rfam.org/).

Example 1: Predicting RNA Secondary Structure for Sequence Homo sapiens tRNA RF00005:
- GGUAAGAUGGCUGAGCAAAGCAUUAGACUGUAAAUCUAAAAACUCUCU
  ![Result for tRNA RF0005](https://github.com/Szymi00/RNA-Structure-Prediction-App/blob/main/assets/images/example1.jpg?raw=true)
  
Example 2: Predicting RNA Secondary Structure for Sequence Ciona savignyi 5S ribosomal RNA RF00001:
- GCUUAUCACCAUUCCAGAUUGAAUAUACCCGAUCUCGUCUGAUCUCGGAAGUCAAGCAAUCUCGUUUUACCA
  ![Result for rRNA RF0001](https://github.com/Szymi00/RNA-Structure-Prediction-App/blob/main/assets/images/example2.jpg?raw=true)
  
Example 3: Predicting RNA Secondary Structure for Sequence Homo sapiens (human) Small nucleolar RNA Z39 RF00341:
- GUGCAUGUGAUGAAGCAAAUCAGUAUGAAUGAAUUCAUGAUACUGUAAACGCUUUCUGAUGUA
![Result for snRNA RF00341](https://github.com/Szymi00/RNA-Structure-Prediction-App/blob/main/assets/images/example3.jpg?raw=true)

Example 4: Predicting RNA Secondary Structure for Sequence Homo sapiens (human) microRNA hsa-mir-103b precursor (hsa-mir-103b-2) RF00129:
- UCAUAGCCCUGUACAAUGCUGCUUGACCUGAAUGCUACAAGGCAGCACUGUAAAGAAGCUGA
  ![Result for miRNA RF00129](https://github.com/Szymi00/RNA-Structure-Prediction-App/blob/main/assets/images/example4.jpg?raw=true)
