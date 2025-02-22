#download the following packages
#pip install pylint
#pip install pandas
#pip install matplotlib

import os
import subprocess
import re
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from matplotlib.ticker import PercentFormatter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading

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
            
    # Run pylint on the selected python files and write the output to a log file
    log_file = "pylint_log.txt"
    with open(log_file, 'w', encoding='utf-8') as f:
        for python_file in python_files:
            result = subprocess.run(["pylint", "--exit-zero", "--output-format=text", python_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
            f.write(result.stdout)
            f.write(result.stderr)

    # Error codes (to be edited later)
    error_codes = {
        'Fatal': ['F0001'],
        'Error': ['E00139', 'E130711', 'E1507', 'E1201', 'E1301', 'E11426', 'E011612', 'E0104', 'E0001', 'E1700', 'E010510', 'E02032', 'E02373', 'E0242', 'E0245', 'E0238', 'E0236', 'E0202', 'E110110', 'E1136', 'E11114', 'E11285', 'E07018', 'E011110', 'E0712', 'E1141', 'E0240', 'E0239', 'E030412', 'E030812', 'E0243', 'E0244', 'E0311', 'E0313', 'E0312', 'E0309', 'E0305', 'E0310', 'E0303', 'E1139', 'E0306', 'E1127', 'E0307', 'E113010', 'E0301', 'E1134', 'E1133', 'E110210', 'E0702', 'E1519', 'E1520', 'E113110', 'E1135', 'E2501', 'E0611', 'E0603', 'E0602', 'E0601', 'E0118'],
        'Warning': ['W0101', 'W0102', 'W0104', 'W0105', 'W0106', 'W0107', 'W0108', 'W0109', 'W0110', 'W0111', 'W0112', 'W0113', 'W0114', 'W0115', 'W0116', 'W0117', 'W0118', 'W0119', 'W0120', 'W0121', 'W0122', 'W0123', 'W0124', 'W0125', 'W0126', 'W0127', 'W0128', 'W0129', 'W0130', 'W0131', 'W0132', 'W0133', 'W0134', 'W0135', 'W0136', 'W0137', 'W0138', 'W0139', 'W0140', 'W0141', 'W0142', 'W0143', 'W0144', 'W0145', 'W0146', 'W0147', 'W0148', 'W0149', 'W0150', 'W0151', 'W0152', 'W0153', 'W0154', 'W0155', 'W0156', 'W0157', 'W0158', 'W0159', 'W0160', 'W0161', 'W0162', 'W0163', 'W0164', 'W0165', 'W0166', 'W0167', 'W0168', 'W0169', 'W0170', 'W0171', 'W0172', 'W0173', 'W0174', 'W0175', 'W0176', 'W0177', 'W0178', 'W0179', 'W0180', 'W0181', 'W0182', 'W0183', 'W0184', 'W0185', 'W0186', 'W0187', 'W0188', 'W0189', 'W0190', 'W0191', 'W0192', 'W0193', 'W0194', 'W0195', 'W0196', 'W0197', 'W0198', 'W0199'],
        'Convention': ['C0101', 'C0102', 'C0103', 'C0104', 'C0105', 'C0106', 'C0107', 'C0108', 'C0109', 'C0110', 'C0111', 'C0112', 'C0113', 'C0114', 'C0115', 'C0116', 'C0117', 'C0118', 'C0119', 'C0120', 'C0121', 'C0122', 'C0123', 'C0124', 'C0125', 'C0126', 'C0127', 'C0128', 'C0129', 'C0130', 'C0131', 'C0132', 'C0133', 'C0134', 'C0135', 'C0136', 'C0137', 'C0138', 'C0139', 'C0140', 'C0141', 'C0142', 'C0143', 'C0144', 'C0145', 'C0146', 'C0147', 'C0148', 'C0149', 'C0150', 'C0151', 'C0152', 'C0153', 'C0154', 'C0155', 'C0156', 'C0157', 'C0158', 'C0159', 'C0160', 'C0161', 'C0162', 'C0163', 'C0164', 'C0165', 'C0166', 'C0167', 'C0168', 'C0169', 'C0170', 'C0171', 'C0172', 'C0173', 'C0174', 'C0175', 'C0176', 'C0177', 'C0178', 'C0179', 'C0180', 'C0181', 'C0182', 'C0183', 'C0184', 'C0185', 'C0186', 'C0187', 'C0188', 'C0189', 'C0190', 'C0191', 'C0192', 'C0193', 'C0194', 'C0195', 'C0196', 'C0197', 'C0198', 'C0199'],
        'Refactor': ['R0101', 'R0102', 'R0103', 'R0104', 'R0105', 'R0106', 'R0107', 'R0108', 'R0109', 'R0110', 'R0111', 'R0112', 'R0113', 'R0114', 'R0115', 'R0116', 'R0117', 'R0118', 'R0119', 'R0120', 'R0121', 'R0122', 'R0123', 'R0124', 'R0125', 'R0126', 'R0127', 'R0128', 'R0129', 'R0130', 'R0131', 'R0132', 'R0133', 'R0134', 'R0135', 'R0136', 'R0137', 'R0138', 'R0139', 'R0140', 'R0141', 'R0142', 'R0143', 'R0144', 'R0145', 'R0146', 'R0147', 'R0148', 'R0149', 'R0150', 'R0151', 'R0152', 'R0153', 'R0154', 'R0155', 'R0156', 'R0157', 'R0158', 'R0159', 'R0160', 'R0161', 'R0162', 'R0163', 'R0164', 'R0165', 'R0166', 'R0167', 'R0168', 'R0169', 'R0170', 'R0171', 'R0172', 'R0173', 'R0174', 'R0175', 'R0176', 'R0177', 'R0178', 'R0179', 'R0180', 'R0181', 'R0182', 'R0183', 'R0184', 'R0185', 'R0186', 'R0187', 'R0188', 'R0189', 'R0190', 'R0191', 'R0192', 'R0193', 'R0194', 'R0195', 'R0196', 'R0197', 'R0198', 'R0199']
    }

    # Count the number of errors in each category
    error_counts = {code: 0 for codes in error_codes.values() for code in codes}
    category_counts = {category: 0 for category in error_codes.keys()}

    # Count the number of errors in each category by finding the error codes in the log file
    with open(log_file, 'r', encoding='utf-8') as f:
        log_content = f.read()
        for code in error_counts:
            count = len(re.findall(r'\b' + re.escape(code) + r'\b', log_content))
            error_counts[code] = count
            for category, codes in error_codes.items():
                if code in codes:
                    category_counts[category] += count

    # Display the number of errors in each category
    print("Accumulated counts:")
    for category, count in category_counts.items():
        print(f"{category}: {count}")

    # Dataframe of the error categories for the pareto chart
    df = pd.DataFrame({'Analysis': [category_counts['Fatal'], category_counts['Error'], category_counts['Warning'],  category_counts['Convention'], category_counts['Refactor']]})
    df.index = ['Fatal', 'Error', 'Warning', 'Convention', 'Refactor']
    df = df.sort_values(by='Analysis', ascending=False)
    df["cumpercentage"] = df["Analysis"].cumsum()/df["Analysis"].sum()* 100

    # Show the pareto chart
    fig, ax1 = plt.subplots()
    fig.patch.set_facecolor('#333333')  # Set the background color of the figure
    ax1.set_facecolor('#444444')  # Set the background color of the axes
    ax1.bar(df.index, df["Analysis"], color="C0")
    ax1.set_ylabel("Number of Errors", color="C0")
    ax1.tick_params(axis="y", colors="C0")
    ax1.set_xlabel("Error Category")
    ax1.set_xticklabels(df.index, rotation=45)
    ax1.set_title("Pareto Chart of Error Categories")
    ax2 = ax1.twinx()
    ax2.plot(df.index, df["cumpercentage"], color="C1", marker="D", ms=7)
    ax2.yaxis.set_major_formatter(PercentFormatter())
    ax2.tick_params(axis="y", colors="C1")
    #plt.show()

    # Find the top errors contributing to 80% of the issues
    df_pareto = df[df["cumpercentage"] <= 80]

    # If the dataframe is empty, use the first row
    if df_pareto.empty:
        df_pareto = df.iloc[:1]

    # Display the top errors contributing to 80% of the issues
    df_pareto_category = df_pareto.index.tolist()
    final_analysis = [category[0] for category in df_pareto_category]
    print("\nTop Errors Contributing to 80% of Issues:")
    print(final_analysis)

    # Display the feedback for the errors causing 80% of the issues
    relevant_errors = df_pareto.index.tolist()
    print("\nFeedbacks for errors causing 80% of the issues:")
    feedbacks_by_module = {}

    # Find the error codes in the log file and display the feedback
    for error in relevant_errors:
        with open(log_file, 'r', encoding='utf-8') as f:
            log_content = f.readlines()
            for line in log_content:
                if any(code in line for code in error_codes[error]):
                    match = re.search(r'(\w+\.py):(\d+):\d+: (\w\d+): (.+)', line)
                    if match:
                        module_name = match.group(1)
                        line_number = match.group(2)
                        error_code = match.group(3)
                        error_message = match.group(4)
                        if module_name not in feedbacks_by_module:
                            feedbacks_by_module[module_name] = []
                        feedbacks_by_module[module_name].append(f"Line {line_number} : {error_code}: {error_message}")

    # Display the feedbacks by module
    feedback_text = ""
    for module_name, feedbacks in feedbacks_by_module.items():
        feedback_text += f"\n({module_name})\n"
        for feedback in feedbacks:
            feedback_text += feedback + "\n\n"

    # Update the GUI with the chart and feedbacks
    update_gui(fig, feedback_text)

def update_gui(fig, feedback_text):
    # Clear previous content
    for widget in chart_frame.winfo_children():
        widget.destroy()
    for widget in feedback_frame.winfo_children():
        widget.destroy()

    # Add the chart to the chart frame
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Add the feedbacks to the feedback frame
    feedback_label = tk.Label(feedback_frame, text="Feedbacks", font=("Arial", 20), bg='#333333', fg='#FFFFFF')
    feedback_label.pack(pady=10)
    feedback_text_widget = ScrolledText(feedback_frame, wrap=tk.WORD, font=("Arial", 12), bg='#333333', fg='#FFFFFF')
    feedback_text_widget.pack(fill=tk.BOTH, expand=True)
    feedback_text_widget.insert(tk.END, feedback_text)

# Create the main window
root = tk.Tk()
root.title("Pylint Analysis")
root.geometry("1200x800")
root.configure(bg='#333333')

# Create a title label
title_label = tk.Label(root, text="Pylint Analysis Tool", font=("Arial", 24), bg='#333333', fg='#FF3399')
title_label.pack(pady=20)

# Create a frame for the buttons and selected files
control_frame = tk.Frame(root, bg='#333333')
control_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

# Create a button to select files
select_files_button = tk.Button(control_frame, text="Select Files", font=("Arial", 16), command=select_files, bg='#FF3399', fg='#FFFFFF')
select_files_button.pack(side=tk.LEFT, padx=10)

# Create a button to run the Pareto analysis
run_analysis_button = tk.Button(control_frame, text="Run Pareto Analysis", font=("Arial", 16), command=lambda: threading.Thread(target=run_pylint_analysis).start(), bg='#FF3399', fg='#FFFFFF')
run_analysis_button.pack(side=tk.LEFT, padx=10)

# Create a ScrolledText widget to display selected files
selected_files_text = ScrolledText(control_frame, wrap=tk.WORD, font=("Arial", 12), height=5, bg='#333333', fg='#FFFFFF')
selected_files_text.pack(fill=tk.X, pady=10)

# Create a frame for the chart
chart_frame = tk.Frame(root, bg='#333333')
chart_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a frame for the feedbacks
feedback_frame = tk.Frame(root, bg='#333333')
feedback_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Start the Tkinter main loop
root.mainloop()