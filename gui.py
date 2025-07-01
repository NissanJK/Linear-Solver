import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
from methods import gaussian_elimination, matrix_inversion, jacobi, gauss_seidel
from visualizer import Visualizer
from validator import validate_solution

class LinearSolverGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Linear System Solver')
        self._build_widgets()
        self.steps = None
        self.visualizer = Visualizer(self)

    def _build_widgets(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.pack(fill=tk.BOTH, expand=True)

        size_label = ttk.Label(frame, text='Matrix Size:')
        size_label.grid(row=0, column=0)
        self.size_var = tk.IntVar(value=2)
        size_menu = ttk.Combobox(frame, textvariable=self.size_var, values=[2,3,4,5], width=3)
        size_menu.grid(row=0, column=1)
        size_menu.bind('<<ComboboxSelected>>', lambda e: self._build_matrix_inputs())

        methods = ['Gaussian Elimination', 'Matrix Inversion', 'Jacobi', 'Gauss-Seidel']
        ttk.Label(frame, text='Method:').grid(row=0, column=2)
        self.method_var = tk.StringVar(value=methods[0])
        method_menu = ttk.Combobox(frame, textvariable=self.method_var, values=methods)
        method_menu.grid(row=0, column=3)

        ttk.Button(frame, text='Solve', command=self.solve).grid(row=0, column=4)
        ttk.Button(frame, text='Visualize Steps', command=self.visualize).grid(row=0, column=5)
        ttk.Button(frame, text='Reset', command=self.reset).grid(row=0, column=6)

        # Matrix entries
        self.matrix_frame = ttk.Frame(frame)
        self.matrix_frame.grid(row=1, column=0, columnspan=7, pady=10)
        self._build_matrix_inputs()

        # Output
        self.output = tk.Text(frame, height=10, width=80)
        self.output.grid(row=2, column=0, columnspan=7)

    def _build_matrix_inputs(self):
        for widget in self.matrix_frame.winfo_children():
            widget.destroy()
        n = self.size_var.get()
        self.A_entries = []
        self.b_entries = []
        for i in range(n):
            row_entries = []
            for j in range(n):
                e = ttk.Entry(self.matrix_frame, width=5)
                e.grid(row=i, column=j)
                e.insert(0, '0')
                row_entries.append(e)
            self.A_entries.append(row_entries)
            be = ttk.Entry(self.matrix_frame, width=5)
            be.grid(row=i, column=n+1)
            be.insert(0, '0')
            self.b_entries.append(be)

    def _read_system(self):
        n = self.size_var.get()
        A = np.zeros((n,n), float)
        b = np.zeros(n, float)
        try:
            for i in range(n):
                for j in range(n):
                    A[i,j] = float(self.A_entries[i][j].get())
                b[i] = float(self.b_entries[i].get())
        except ValueError:
            messagebox.showerror('Input Error', 'Please enter valid numbers')
            return None, None
        return A, b

    def solve(self):
        A, b = self._read_system()
        if A is None: return
        method = self.method_var.get()
        if method == 'Gaussian Elimination':
            x, steps = gaussian_elimination.solve(A, b)
            errors = None
        elif method == 'Matrix Inversion':
            x, steps = matrix_inversion.solve(A, b)
            errors = None
        elif method == 'Jacobi':
            x, steps, errors = jacobi.solve(A, b, tol=1e-6, max_iter=100)
        else:
            x, steps, errors = gauss_seidel.solve(A, b, tol=1e-6, max_iter=100)

        self.steps = (steps, errors)
        valid = validate_solution(A, x, b)
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, f'Solution x = {x}\n')
        self.output.insert(tk.END, f'Validation: {valid}\n')

    def visualize(self):
        if not self.steps:
            messagebox.showinfo('Info', 'Solve first to visualize')
            return
        self.visualizer.start(self.steps)

    def reset(self):
        self.output.delete(1.0, tk.END)
        self.steps = None

    def run(self):
        self.root.mainloop()
