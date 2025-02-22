import os 
import subprocess

filess = None

# Function to open file dialog and select files
def select_files():
    global filess
    file_paths = filedialog.askopenfilenames(title="Select Python Files", filetypes=[("Python Files", "*.py")])
    filess = list(file_paths)
    show_selected_files()

def show_selected_files():
    selected_files_text.delete(1.0, tk.END)
    if filess:
        for file in filess:
            selected_files_text.insert(tk.END, file + "\n")
    else:
        selected_files_text.insert(tk.END, "No files selected.")

def run_pylint_analysis():
    if not filess:
        print("No files selected. Exiting.")
        return

    python_files = filess
    
pyright_log_file = "pyright_log.txt"
with open(pyright_log_file, 'w', encoding='utf-8') as f:
        for python_file in python_files:
            result = subprocess.run(["pyright", python_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
            f.write(result.stdout)
            f.write(result.stderr)