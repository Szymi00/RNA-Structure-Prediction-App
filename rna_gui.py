import tkinter as tk
from tkinter import ttk, scrolledtext

from draw_rna import ipynb_draw

from rna_structure_analysis import predict_RNA_structure, detect_loops, format_structure_info


# Class handling the application
class RNAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RNA Structure Predictor")

        self.sequence_label = ttk.Label(self.root, text="RNA Sequence:")
        self.sequence_label.grid(column=0, row=0, padx=10, pady=10)

        self.sequence_entry = ttk.Entry(self.root, width=50)
        self.sequence_entry.grid(column=1, row=0, padx=10, pady=10)

        self.allow_GU_var = tk.BooleanVar()
        self.allow_GU_checkbox = ttk.Checkbutton(self.root, text="Allow GU pairs", variable=self.allow_GU_var)
        self.allow_GU_checkbox.grid(column=2, row=0, padx=10, pady=10)

        self.min_loop_length_label = ttk.Label(self.root, text="Minimal Loop Length:")
        self.min_loop_length_label.grid(column=0, row=3, padx=10, pady=10)

        self.min_loop_length_combobox = ttk.Combobox(self.root, values=[0, 1, 2, 3, 4, 5, ], state="readonly")
        self.min_loop_length_combobox.set(0)
        self.min_loop_length_combobox.grid(column=1, row=3, columnspan=2, padx=10, pady=10)

        self.predict_button = ttk.Button(self.root, text="Predict Structure", command=self.predict_structure)
        self.predict_button.grid(column=3, row=0, padx=10, pady=10)

        self.visualize_button = ttk.Button(self.root, text="Visualize Structure", command=self.visualize_structure)
        self.visualize_button.grid(column=4, row=0, padx=10, pady=10)

        self.result_text = scrolledtext.ScrolledText(self.root, width=70, height=10, wrap=tk.WORD)
        self.result_text.grid(column=0, row=1, columnspan=5, padx=10, pady=10)

        self.matrix_image_label = ttk.Label(self.root, text="Matrix Visualization:")
        self.matrix_image_label.grid(column=0, row=2, padx=10, pady=10)

        self.matrix_image_canvas = tk.Canvas(self.root, width=800, height=400)
        self.matrix_image_canvas.grid(column=1, row=2, columnspan=4, padx=10, pady=10, sticky="w")

        self.scroll_x = ttk.Scrollbar(self.root, orient="horizontal", command=self.matrix_image_canvas.xview)
        self.scroll_x.grid(column=1, row=4, columnspan=4, sticky="ew")  # Adjusted row to avoid overlapping
        self.matrix_image_canvas.configure(xscrollcommand=self.scroll_x.set)

        self.scroll_y = ttk.Scrollbar(self.root, orient="vertical", command=self.matrix_image_canvas.yview)
        self.scroll_y.grid(column=5, row=2, sticky="ns")
        self.matrix_image_canvas.configure(yscrollcommand=self.scroll_y.set)

    def predict_structure(self):
        global sequence, allow_GU
        sequence = self.sequence_entry.get().upper()
        allow_GU = self.allow_GU_var.get()
        min_loop_length = int(self.min_loop_length_combobox.get())

        if sequence:
            matrix, structure = predict_RNA_structure(sequence, self.matrix_image_canvas, allow_GU, min_loop_length)

            # Detect hairpin loops, bulge loops, and internal loops
            hairpin_loops, bulge_loops, internal_loops, external_base = detect_loops(structure)

            # Update pair_info
            pair_info = {'Hairpin Loops': hairpin_loops,
                         'Bulge Loops': bulge_loops,
                         'Internal Loops': internal_loops,
                         'External base': external_base}

            # Update result text
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Structure: {structure} \n")
            self.result_text.insert(tk.END, format_structure_info(pair_info))

    def visualize_structure(self):
        global structure, sequence
        ipynb_draw.draw_struct(sequence, structure)
