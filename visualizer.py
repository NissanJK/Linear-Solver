import matplotlib.pyplot as plt
import numpy as np

def plot_matrix(A, b, x=None):
    if A.size == 0:
        fig, axs = plt.subplots(1, 2, figsize=(6, 3))
        axs[0].imshow(b.reshape(-1, 1), cmap='viridis'); axs[0].set_title('b')
        if x is not None:
            axs[1].imshow(x.reshape(-1, 1), cmap='viridis'); axs[1].set_title('x')
        plt.tight_layout()
        plt.show()
    else:
        fig, axs = plt.subplots(1, 3, figsize=(9, 3))
        axs[0].imshow(A, cmap='viridis'); axs[0].set_title('A')
        axs[1].imshow(b.reshape(-1, 1), cmap='viridis'); axs[1].set_title('b')
        if x is not None:
            axs[2].imshow(x.reshape(-1, 1), cmap='viridis'); axs[2].set_title('x')
        plt.tight_layout()
        plt.show()

class Visualizer:
    def __init__(self, gui):
        self.gui = gui

    def start(self, steps_data):
        steps, errors = steps_data
        for s in steps:
            if isinstance(s, tuple):
                A, b = s
                plot_matrix(A, b)
            else:
                plot_matrix(np.array([[]]), np.array(s), s)
        if errors:
            plt.figure()
            plt.plot(errors)
            plt.title('Error per Iteration')
            plt.xlabel('Iteration')
            plt.ylabel('Error')
            plt.show()
