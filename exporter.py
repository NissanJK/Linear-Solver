import csv
from fpdf import FPDF
import matplotlib.pyplot as plt
import os

def export_csv(filename, x, steps=None, errors=None):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Variable', 'Value'])
        for i, xi in enumerate(x):
            writer.writerow([f'x{i}', xi])
        if errors:
            writer.writerow([])
            writer.writerow(['Iteration', 'Error'])
            for i, e in enumerate(errors):
                writer.writerow([i, e])

class Exporter:
    def __init__(self, x, steps=None, errors=None):
        self.x = x
        self.steps = steps
        self.errors = errors

    def to_pdf(self, filename):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(0, 10, 'Solution', ln=True)
        for i, xi in enumerate(self.x):
            pdf.cell(0, 8, f'x{i} = {xi}', ln=True)
        if self.errors:
            pdf.add_page()
            pdf.set_font('Arial', 'B', 16)
            pdf.cell(0, 10, 'Error Convergence', ln=True)
            plt.figure()
            plt.plot(self.errors)
            plt.xlabel('Iteration')
            plt.ylabel('Error')
            plt.tight_layout()
            plot_path = 'error_plot.png'
            plt.savefig(plot_path)
            plt.close()
            pdf.image(plot_path, x=10, y=30, w=180)
            try:
                os.remove(plot_path)
            except Exception:
                pass
        pdf.output(filename)
