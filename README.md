# Linear System Solver

A Python desktop application to solve systems of linear equations using various numerical methods.

## Features
- Solve using **Gaussian Elimination**, **Matrix Inversion**, **Jacobi**, and **Gauss-Seidel** methods.
- Visualize intermediate steps and error convergence with Matplotlib.
- Validate solutions automatically.
- Export results and error plots to CSV or PDF.
- Supports matrix sizes from 2x2 up to 5x5.
- User-friendly Tkinter GUI.
- Step-by-step visualization and error tracking for iterative methods.
- Modular design for easy extension.

## Installation

1. Clone or download this repository.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the application:
```bash
python main.py
```

## How to Use

1. **Select Matrix Size:** Choose the size (2x2 to 5x5) from the dropdown.
2. **Enter Coefficients:** Fill in the matrix **A** and vector **b** in the input fields.
3. **Choose Method:** Select a solution method from the dropdown.
4. **Solve:** Click **Solve** to compute the solution.
5. **Visualize:** Click **Visualize Steps** to see the step-by-step process and error convergence (for iterative methods).
6. **Export:** Use the export feature to save results as CSV or PDF.
7. **Reset:** Click **Reset** to clear all fields and outputs.

## Example

**Input:**
- Matrix Size: 4

- A:
    [ 10.0, -1.0,  2.0,  0.0],
    [ -1.0, 11.0, -1.0,  3.0],
    [  2.0, -1.0, 10.0, -1.0],
    [  0.0,  3.0, -1.0,  8.0]

- b:
    [6.0, 25.0, -11.0, 15.0]

**Output:**
```
Solution x = [ 1.  2. -1.  1.]
Validation: True
```

## Extending

Add new methods under the `methods/` folder following the existing interface:
```python
def solve(A, b, **kwargs):
    # Your implementation
    return x, steps  # or x, steps, errors for iterative methods
```

## Dependencies

- numpy
- matplotlib
- fpdf
- tkinter (built-in)

## Troubleshooting

- If you encounter issues with the GUI, ensure you are running Python 3.x and all dependencies are installed.
- For PDF export, make sure the `fpdf` package is installed.

## License

This project is for educational and research purposes.
