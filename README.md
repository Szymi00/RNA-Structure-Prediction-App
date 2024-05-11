# Application for predicting the secondary structure of RNA using Nussinov's Algorithm

## Table of contents
* [Motivation](#motivation)
* [Project assumptions](#project-assumptions)
* [Technologies](#technologies)
  

  
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
