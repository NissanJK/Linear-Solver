import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import messagebox, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Visualizer:
    def __init__(self, gui):
        self.gui = gui
        self.steps = []
        self.errors = None
        self.current_index = 0
        self.window = None
        self.fig = None
        self.canvas = None
        self.image_frames = []

    def start(self, steps_data):
        self.steps, self.errors = steps_data
        self.current_index = 0
        self.image_frames = []
        self._init_window()

    def _init_window(self):
        self.window = tk.Toplevel(self.gui.root)
        self.window.title("Visualization Steps")
        self.window.geometry("700x400")

        self.fig, _ = plt.subplots(1, 2, figsize=(7, 3))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        btn_frame = tk.Frame(self.window)
        btn_frame.pack(pady=10)

        next_btn = tk.Button(btn_frame, text="Next", command=self.show_next_step)
        next_btn.grid(row=0, column=0, padx=5)

        save_btn = tk.Button(btn_frame, text="Save as GIF", command=self.save_as_gif)
        save_btn.grid(row=0, column=1, padx=5)

        self.show_next_step()

    def show_next_step(self):
        if self.current_index >= len(self.steps):
            self._plot_error()
            return

        s = self.steps[self.current_index]
        self.fig.clf()

        if isinstance(s, tuple) and len(s) == 2:
            A, b = s
            axs = self.fig.subplots(1, 2)
            axs[0].imshow(np.array(b).reshape(-1, 1), cmap='viridis')
            axs[0].set_title('b')
            axs[1].imshow(np.array(A), cmap='viridis')
            axs[1].set_title('A')
        else:
            axs = self.fig.subplots(1, 2)
            axs[0].imshow(np.array(s).reshape(-1, 1), cmap='viridis')
            axs[0].set_title('b')
            axs[1].imshow(np.array(s).reshape(-1, 1), cmap='viridis')
            axs[1].set_title('x')

        self.fig.tight_layout()
        self.canvas.draw()
        self.canvas.flush_events()
        self.canvas.get_tk_widget().update()

        # Capture frame for GIF
        self.fig.canvas.draw()
        image = np.frombuffer(self.fig.canvas.tostring_rgb(), dtype='uint8')
        image = image.reshape(self.fig.canvas.get_width_height()[::-1] + (3,))
        self.image_frames.append(image)

        self.current_index += 1

    def _plot_error(self):
        if self.errors is None:
            messagebox.showinfo("Info", "No error data to plot.")
            return

        self.fig.clf()
        ax = self.fig.add_subplot(111)
        ax.plot(self.errors, marker='o')
        ax.set_title("Error per Iteration")
        ax.set_xlabel("Iteration")
        ax.set_ylabel("Error")
        self.fig.tight_layout()
        self.canvas.draw()

    def save_as_gif(self):
        import imageio

        if not self.image_frames:
            messagebox.showerror("Error", "No frames to save.")
            return

        path = filedialog.asksaveasfilename(defaultextension=".gif",
                                            filetypes=[("GIF files", "*.gif")])
        if not path:
            return

        try:
            imageio.mimsave(path, self.image_frames, fps=1)
            messagebox.showinfo("Saved", f"GIF saved to:\n{path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save GIF:\n{e}")
