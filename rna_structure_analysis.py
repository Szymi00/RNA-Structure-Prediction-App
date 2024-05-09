import re
import tkinter as tk

# Helper function to find bifurcation
def find_bifurcation_score(matrix, start, end, sequence, allow_GU=False, min_loop_length=0):
    max_score = -1
    bifurcation_point = -1
    for k in range(start + 1, end):
        current_score, _ = is_paired(sequence[start], sequence[k], allow_GU)
        current_score += matrix[k + 1][end]
        loop_length = k - start - 1  # Loop length
        if current_score > max_score and loop_length >= min_loop_length:
            max_score = current_score
            bifurcation_point = k
    return max_score, bifurcation_point

# Function to check base pairing
def is_paired(base1, base2, allow_GU=False):
    if (base1 == 'C' and base2 == 'G') or (base1 == 'G' and base2 == 'C'):
        return 1, 'G-C'
    elif (base1 == 'A' and base2 == 'U') or (base1 == 'U' and base2 == 'A'):
        return 1, 'A-U'
    elif allow_GU and ((base1 == 'G' and base2 == 'U') or (base1 == 'U' and base2 == 'G')):
        return 1, 'G-U'
    else:
        return 0, None

# Function to perform traceback
def perform_traceback(matrix, structure, i, j, sequence, canvas, colors, pair_info, allow_GU, min_loop_length=0):
    while i < j:
        paired, pair_type = is_paired(sequence[i], sequence[j], allow_GU)
        left = matrix[i][j - 1]
        down = matrix[i + 1][j]
        diagonal = matrix[i + 1][j - 1] + paired
        bifurcation_score, k = find_bifurcation_score(matrix, i, j, sequence, allow_GU, min_loop_length)

        if matrix[i][j] == diagonal:
            if paired:
                structure[i] = "("
                structure[j] = ")"
                pair_info[pair_type].append((i + 1, j + 1))
            i += 1
            j -= 1
            colors.append((i, j))  # Add pair indices for coloring
        elif matrix[i][j] == down:
            i += 1
        elif matrix[i][j] == left:
            j -= 1
        elif matrix[i][j] == bifurcation_score:
            perform_traceback(matrix, structure, i, k, sequence, canvas, colors, pair_info, allow_GU, min_loop_length)
            perform_traceback(matrix, structure, k + 1, j, sequence, canvas, colors, pair_info, allow_GU,
                              min_loop_length)
            i = k + 1  # Continue from the next point

        # Update canvas during traceback
        visualize_matrix_partial(matrix, canvas, sequence, colors, pair_info, i, j)

# Visualization of matrix filling
def visualize_matrix_partial(matrix, canvas, sequence, colors, pair_info, current_i, current_j):
    canvas.delete("all")

    rows = len(matrix)
    cols = len(matrix[0])
    cell_size = 20

    # Draw D(i,j) label
    x = cell_size / 2
    y = cell_size / 2
    canvas.create_text(x, y, text="D(i,j)", anchor=tk.CENTER, fill="black")

    # Draw sequence labels
    for i in range(rows):
        x = (i + 1) * cell_size + cell_size / 100
        y = cell_size / 100
        symbol = structure[i] if current_i == i or current_j == i else "."
        canvas.create_text(x, y, text=symbol, anchor=tk.CENTER, fill="black")
        if structure[i] == "(" or structure[i] == ")":
            canvas.create_text(x, y - cell_size / 2, text=structure[i], anchor=tk.CENTER, fill="red")

    for j in range(cols):
        x = cell_size / 2
        y = (j + 1) * cell_size + cell_size / 2
        symbol = structure[j] if current_i == j or current_j == j else "."
        canvas.create_text(x, y, text=symbol, anchor=tk.CENTER, fill="black")
        if structure[j] == "(" or structure[j] == ")":
            canvas.create_text(x - cell_size / 2, y, text=structure[j], anchor=tk.CENTER, fill="red")

    # Draw matrix cells and nucleotides
    for i in range(rows):
        for j in range(cols):
            x = (j + 1) * cell_size
            y = (i + 1) * cell_size
            canvas.create_rectangle(x, y, x + cell_size, y + cell_size, outline="black", fill="white")
            canvas.create_text(x + cell_size / 2, y + cell_size / 2, text=str(matrix[i][j]), anchor=tk.CENTER)

    # Highlight values in cells
    for i, j in colors:
        x = (j + 1) * cell_size
        y = (i + 1) * cell_size
        canvas.create_rectangle(x, y, x + cell_size, y + cell_size, outline="black", fill="yellow")
        # Draw numbers in the highlighted cells
        canvas.create_text(x + cell_size / 2, y + cell_size / 2, text=str(matrix[i][j]), anchor=tk.CENTER)

    # Create cells for nucleotide sequence above the matrix
    for i in range(rows):
        x = (i + 1) * cell_size
        y = cell_size / 2
        canvas.create_rectangle(x, 0, x + cell_size, cell_size, outline="black", fill="lightgrey")
        canvas.create_text(x + cell_size / 2, y, text=sequence[i], anchor=tk.CENTER, fill="black")

    for j in range(cols):
        x = cell_size / 2
        y = (j + 1) * cell_size
        canvas.create_rectangle(0, y, cell_size, y + cell_size, outline="black", fill="lightgrey")
        canvas.create_text(x, y + cell_size / 2, text=sequence[j], anchor=tk.CENTER, fill="black")

    # Display base pairing information next to the matrix
    pair_text = ""
    for pair_type, pairs in pair_info.items():
        pair_text += f"{pair_type}: {', '.join([f'({pair[0]},{pair[1]})' for pair in pairs])}\n"

    canvas.create_text(
        (cell_size / 2) + cell_size * (cols + 1),
        (cell_size / 2) + cell_size * (rows + 2),
        text=f"Pair Info:\n{pair_text}",
        anchor=tk.W,
        fill="blue"
    )

    canvas.update()

# Function to merge loops
def merge_loops(loops):
    start = min(loop[0] for loop in loops)
    end = max(loop[1] for loop in loops)
    return start, end

# Function to detect loops
def detect_loops(structure):
    hairpin_loops = [(match.start(), match.end()) for match in re.finditer(r'\(\.{3,10}\)', structure)]

    bulge_loops = []
    in_bulge = False
    start = 0
    max_dots = 3  # Maximum dots on one side of the parentheses pair

    for i, char in enumerate(structure):
        if char == ".":
            if not in_bulge:
                in_bulge = True
                start = i
        elif char == "(":
            if in_bulge:
                in_bulge = False
                bulge_end = i - 1
                if bulge_end >= start and i - start <= max_dots:  # Added condition for maximum dots
                    bulge_loops.append((start, bulge_end))
        elif char == ")":
            if in_bulge:
                in_bulge = False
                bulge_end = i - 1
                if bulge_end >= start and i - start <= max_dots:  # Added condition for maximum dots
                    bulge_loops.append((start, bulge_end))

    internal_loops = []
    if len(bulge_loops) == 2:
        # Merge two bulge loops into an internal loop
        merged_internal_loop = merge_loops(bulge_loops)
        internal_loops.append(merged_internal_loop)
    elif len(bulge_loops) == 4:
        # Merge first and last bulge loop into one internal loop
        merged_internal_loop1 = merge_loops([bulge_loops[0], bulge_loops[-1]])
        # Merge second and third bulge loops into another internal loop
        merged_internal_loop2 = merge_loops([bulge_loops[1], bulge_loops[2]])
        internal_loops.extend([merged_internal_loop1, merged_internal_loop2])
    elif len(bulge_loops) == 6:
        merged_internal_loop1 = merge_loops([bulge_loops[0], bulge_loops[-1]])
        merged_internal_loop2 = merge_loops([bulge_loops[1], bulge_loops[2]])
        merged_internal_loop3 = merge_loops([bulge_loops[3], bulge_loops[4]])
        internal_loops.extend(([merged_internal_loop1, merged_internal_loop2, merged_internal_loop3]))
    elif len(bulge_loops) >= 8:
        merged_internal_loop1 = merge_loops([bulge_loops[0], bulge_loops[-1]])
        merged_internal_loop2 = merge_loops([bulge_loops[1], bulge_loops[2]])
        merged_internal_loop3 = merge_loops([bulge_loops[3], bulge_loops[4]])
        merged_internal_loop4 = merge_loops([bulge_loops[5], bulge_loops[6]])
        internal_loops.extend(
            ([merged_internal_loop1, merged_internal_loop2, merged_internal_loop3, merged_internal_loop4]))

    external_base = [(match.start(), match.end()) for match in
                     re.finditer(r'(?<=\()\.(?=\))|(?<=\))\.(?=\()', structure)]

    return hairpin_loops, bulge_loops, internal_loops, external_base

# Function to format structure information
def format_structure_info(pair_info):
    formatted_info = "\nStructure Info:\n"

    if pair_info.get('Hairpin Loops'):
        formatted_info += f"Hairpin Loops: {', '.join([f'[{start},{end}]' for start, end in pair_info['Hairpin Loops']])}\n"

    if pair_info.get('Bulge Loops'):
        formatted_info += f"Bulge Loops: {', '.join([f'({start},{end})' for start, end in pair_info['Bulge Loops']])}\n"

    if pair_info.get('Internal Loops'):
        formatted_info += f"Internal Loops: {', '.join([f'({start},{end})' for start, end in pair_info['Internal Loops']])}\n"

    if pair_info.get('External base'):
        formatted_info += f"External base: {', '.join([f'({start},{end})' for start, end in pair_info['External base']])}\n"

    return formatted_info

# Function to predict RNA structure
def predict_RNA_structure(sequence, canvas, allow_GU=False, min_loop_length=0):
    length = len(sequence)
    global structure
    structure = ["." for _ in range(length)]
    pair_info = {'A-U': [], 'G-C': [], 'G-U': []}
    matrix = [[0 for _ in range(length)] for _ in range(length)]
    colors = []

    if min_loop_length == 0:
        # Version for min_loop_length == 0
        for x in range(1, length):
            i = 0
            j = x
            while i < (length - x) and j < length:
                score, pair_type = is_paired(sequence[i], sequence[j], allow_GU)
                bifurcation_score, k = find_bifurcation_score(matrix, i, j, sequence, allow_GU, min_loop_length)
                matrix[i][j] = max(
                    matrix[i][j - 1],
                    matrix[i + 1][j],
                    matrix[i + 1][j - 1] + score,
                    bifurcation_score
                )
                i += 1
                j += 1

                # Update matrix filling
                visualize_matrix_partial(matrix, canvas, sequence, colors, pair_info, i, j)
    else:
        # Version for min_loop_length > 0
        for x in range(min_loop_length, length):
            i = 0
            j = x
            while i < (length - x) and j < length:
                score, pair_type = is_paired(sequence[i], sequence[j], allow_GU)
                bifurcation_score, k = find_bifurcation_score(matrix, i, j, sequence, allow_GU, min_loop_length)
                matrix[i][j] = max(
                    matrix[i][j - 1],
                    matrix[i + 1][j],
                    matrix[i + 1][j - 1] + score,
                    bifurcation_score
                )
                i += 1
                j += 1

                # Update matrix filling
                visualize_matrix_partial(matrix, canvas, sequence, colors, pair_info, i, j)

    perform_traceback(matrix, structure, 0, length - 1, sequence, canvas, colors, pair_info, allow_GU, min_loop_length)
    structure = ''.join(char for char in structure)
    return matrix, structure
