#download the following packages para muggana
#pip install pylint
#pip install pandas
#pip install matplotlib
#pip install customtkinter
#pip install pillow
#pip install pyright

import os
import subprocess
import re
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import customtkinter as ctk
from tkinter import filedialog
from tkinter import ttk
from matplotlib.ticker import PercentFormatter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import time

filess = None
pyright_path = "pyright"
pylint_path = "pylint"

def error():
    print("Error function executed")
    # Define refactor error codes
    error_error_codes = [ "reportGeneralTypeIssues", "reportFunctionMemberAccess",
    "reportMissingImports", "reportInvalidTypeForm", "reportAbstractUsage",
    "reportArgumentType", "reportAssertTypeFailure", "reportAssignmentType",
    "reportAttributeAccessIssue", "reportCallIssue", "reportInconsistentOverload",
    "reportIndexIssue", "reportInvalidTypeArguments", "reportNoOverloadImplementation",
    "reportOperatorIssue", "reportOptionalSubscript", "reportOptionalMemberAccess",
    "reportOptionalCall", "reportOptionalIterable", "reportOptionalContextManager",
    "reportOptionalOperand", "reportRedeclaration", "reportReturnType",
    "reportTypedDictNotRequiredAccess", "reportPrivateImportUsage", "reportIncompatibleMethodOverride",
    "reportIncompatibleVariableOverride", "reportOverlappingOverload", "reportPossiblyUnboundVariable",
    "reportUndefinedVariable", "reportUnboundVariable", "reportUnhashable",
    "reportUnusedCoroutine", "reportUnusedExcept",
    ]
    feedbacks_by_module = {}

    hello_log_file = "all_log.txt"
    current_file_name = "Unknown Module"  

    feedbacks_by_module = {}

    with open(hello_log_file, 'r', encoding='utf-8') as f:
        log_content = f.readlines()
        for line in log_content:
            
            file_match = re.match(r'\(([\w.]+\.py)\)', line)
            if file_match:
                current_file_name = file_match.group(1)  
                if current_file_name not in feedbacks_by_module:
                    feedbacks_by_module[current_file_name] = {}

    
            for error_code in error_error_codes:
                if error_code in line:
                    match = re.search(r'Line : (\d+) \[(\w+)\] - (.+)', line)
                    if match:
                        line_number = match.group(1)
                        error_code = match.group(2)
                        error_message = match.group(3)
                        if current_file_name not in feedbacks_by_module:
                            feedbacks_by_module[current_file_name] = {}
                        feedbacks_by_module[current_file_name].update(
                            {f"Line : {line_number} [{error_code}] - {error_message}": int(line_number)}
                        )

    for module_name in feedbacks_by_module:
        sorted_feedbacks = sorted(feedbacks_by_module[module_name].items(), key=lambda x: x[1])
        feedbacks_by_module[module_name] = sorted_feedbacks

    feedback_text = ""
    for module_name, feedbacks in feedbacks_by_module.items():
        feedback_text += f"\n({module_name})\n"
        if feedbacks:  
            for feedback in feedbacks:
                feedback_text += feedback[0] + "\n\n"
        else:  
            feedback_text += "There are no errors found for this file.\n\n"

    if not feedback_text.strip():  
        feedback_text = "No files were analyzed or no errors were found."

    print(feedback_text)
    update_gui(feedback_text)

def refactor():
    print("Refactor function executed")

    # Define refactor error codes
    refactor_error_codes = [
        "R0201", "R0401", "R0801", "R0901", "R0902", "R0903", "R0904", "R0911",
        "R0912", "R0913", "R0914", "R0915", "R0921", "R0922", "R0923",
    ]
    feedbacks_by_module = {}

    hello_log_file = "all_log.txt"
    current_file_name = "Unknown Module"  

    feedbacks_by_module = {}

    with open(hello_log_file, 'r', encoding='utf-8') as f:
        log_content = f.readlines()
        for line in log_content:
            
            file_match = re.match(r'\(([\w.]+\.py)\)', line)
            if file_match:
                current_file_name = file_match.group(1)  
                if current_file_name not in feedbacks_by_module:
                    feedbacks_by_module[current_file_name] = {}

    
            for error_code in refactor_error_codes:
                if error_code in line:
                    match = re.search(r'Line : (\d+) \[(\w\d+)\] - (.+)', line)
                    if match:
                        line_number = match.group(1)
                        error_code = match.group(2)
                        error_message = match.group(3)
                        if current_file_name not in feedbacks_by_module:
                            feedbacks_by_module[current_file_name] = {}
                        feedbacks_by_module[current_file_name].update(
                            {f"Line : {line_number} [{error_code}] - {error_message}": int(line_number)}
                        )
    for module_name in feedbacks_by_module:
        sorted_feedbacks = sorted(feedbacks_by_module[module_name].items(), key=lambda x: x[1])
        feedbacks_by_module[module_name] = sorted_feedbacks

    feedback_text = ""
    for module_name, feedbacks in feedbacks_by_module.items():
        feedback_text += f"\n({module_name})\n"
        if feedbacks:  
            for feedback in feedbacks:
                feedback_text += feedback[0] + "\n\n"
        else:  
            feedback_text += "There are no errors found for this file.\n\n"

    if not feedback_text.strip():  
        feedback_text = "No files were analyzed or no errors were found."

    print(feedback_text)
    update_gui(feedback_text)

def warning():

    print("Warning function executed")
    # Define refactor error codes
    warning_error_codes = [
    "W0101", "W0102", "W0104", "W0105", "W0106", "W0107", "W0108", "W0109",
    "W0110", "W0120", "W0121", "W0122", "W0141", "W0142", "W0150", "W0199",
    "W0201", "W0211", "W0212", "W0221", "W0222", "W0223", "W0231", "W0232",
    "W0233", "W0234", "W0301", "W0311", "W0312", "W0331", "W0332", "W0333",
    "W0401", "W0402", "W0403", "W0404", "W0406", "W0410", "W0511", "W0512",
    "W0601", "W0602", "W0603", "W0604", "W0611", "W0612", "W0613", "W0614",
    "W0621", "W0622", "W0623", "W0631", "W0632", "W0633", "W0701", "W0702",
    "W0703", "W0704", "W0710", "W0711", "W0712", "W1001", "W1111", "W1201",
    "W1300", "W1301", "W1401", "W1402", "W1501",
    ]
    feedbacks_by_module = {}

    hello_log_file = "all_log.txt"
    current_file_name = "Unknown Module"  

    feedbacks_by_module = {}

    with open(hello_log_file, 'r', encoding='utf-8') as f:
        log_content = f.readlines()
        for line in log_content:
            
            file_match = re.match(r'\(([\w.]+\.py)\)', line)
            if file_match:
                current_file_name = file_match.group(1)  
                if current_file_name not in feedbacks_by_module:
                    feedbacks_by_module[current_file_name] = {}

    
            for error_code in warning_error_codes:
                if error_code in line:
                    match = re.search(r'Line : (\d+) \[(\w\d+)\] - (.+)', line)
                    if match:
                        line_number = match.group(1)
                        error_code = match.group(2)
                        error_message = match.group(3)
                        if current_file_name not in feedbacks_by_module:
                            feedbacks_by_module[current_file_name] = {}
                        feedbacks_by_module[current_file_name].update(
                            {f"Line : {line_number} [{error_code}] - {error_message}": int(line_number)}
                        )

    for module_name in feedbacks_by_module:
        sorted_feedbacks = sorted(feedbacks_by_module[module_name].items(), key=lambda x: x[1])
        feedbacks_by_module[module_name] = sorted_feedbacks

    feedback_text = ""
    for module_name, feedbacks in feedbacks_by_module.items():
        feedback_text += f"\n({module_name})\n"
        if feedbacks:  
            for feedback in feedbacks:
                feedback_text += feedback[0] + "\n\n"
        else:  
            feedback_text += "There are no errors found for this file.\n\n"

    if not feedback_text.strip():  
        feedback_text = "No files were analyzed or no errors were found."

    print(feedback_text)
    update_gui(feedback_text)

def convention():
    print("convention function executed")

    # Define refactor error codes
    convention_error_codes = [
    "C0102", "C0103", "C0111", "C0112", "C0121", "C0202", "C0203", "C0204",
    "C0301", "C0302", "C0303", "C0304", "C0321", "C0322", "C0323", "C0324",
    "C0325", "C0326", "C1001",
    ]

    feedbacks_by_module = {}

    hello_log_file = "all_log.txt"
    current_file_name = "Unknown Module"  

    feedbacks_by_module = {}

    with open(hello_log_file, 'r', encoding='utf-8') as f:
        log_content = f.readlines()
        for line in log_content:
            
            file_match = re.match(r'\(([\w.]+\.py)\)', line)
            if file_match:
                current_file_name = file_match.group(1)  
                if current_file_name not in feedbacks_by_module:
                    feedbacks_by_module[current_file_name] = {}

    
            for error_code in convention_error_codes:
                if error_code in line:
                    match = re.search(r'Line : (\d+) \[(\w\d+)\] - (.+)', line)
                    if match:
                        line_number = match.group(1)
                        error_code = match.group(2)
                        error_message = match.group(3)
                        if current_file_name not in feedbacks_by_module:
                            feedbacks_by_module[current_file_name] = {}
                        feedbacks_by_module[current_file_name].update(
                            {f"Line : {line_number} [{error_code}] - {error_message}": int(line_number)}
                        )

# Sort feedbacks by line number
    for module_name in feedbacks_by_module:
        sorted_feedbacks = sorted(feedbacks_by_module[module_name].items(), key=lambda x: x[1])
        feedbacks_by_module[module_name] = sorted_feedbacks

# Generate feedback text
    feedback_text = ""
    for module_name, feedbacks in feedbacks_by_module.items():
        feedback_text += f"\n({module_name})\n"
        for feedback in feedbacks:
            feedback_text += feedback[0] + "\n\n"

    if not feedback_text.strip():
        feedback_text = "There are no convention errors found."

    print(feedback_text)
    update_gui(feedback_text)

def fatal():
    print("Fatal function executed")
    # Define refactor error codes
    fatal_error_codes = [
    "F0001", "F0002", "F0003", "F0004", "F0010", "F0202", "F0220", "F0321",
    "F0401",
    ]
    feedbacks_by_module = {}

    hello_log_file = "all_log.txt"
    current_file_name = "Unknown Module"  

    feedbacks_by_module = {}

    with open(hello_log_file, 'r', encoding='utf-8') as f:
        log_content = f.readlines()
        for line in log_content:
            
            file_match = re.match(r'\(([\w.]+\.py)\)', line)
            if file_match:
                current_file_name = file_match.group(1)  
                if current_file_name not in feedbacks_by_module:
                    feedbacks_by_module[current_file_name] = {}

    
            for error_code in fatal_error_codes:
                if error_code in line:
                    match = re.search(r'Line : (\d+) \[(\w\d+)\] - (.+)', line)
                    if match:
                        line_number = match.group(1)
                        error_code = match.group(2)
                        error_message = match.group(3)
                        if current_file_name not in feedbacks_by_module:
                            feedbacks_by_module[current_file_name] = {}
                        feedbacks_by_module[current_file_name].update(
                            {f"Line : {line_number} [{error_code}] - {error_message}": int(line_number)}
                        )

    for module_name in feedbacks_by_module:
        sorted_feedbacks = sorted(feedbacks_by_module[module_name].items(), key=lambda x: x[1])
        feedbacks_by_module[module_name] = sorted_feedbacks

    feedback_text = ""
    for module_name, feedbacks in feedbacks_by_module.items():
        feedback_text += f"\n({module_name})\n"
        if feedbacks:  
            for feedback in feedbacks:
                feedback_text += feedback[0] + "\n\n"
        else:  
            feedback_text += "There are no errors found for this file.\n\n"

    if not feedback_text.strip():  
        feedback_text = "No files were analyzed or no errors were found."

    print(feedback_text)
    update_gui(feedback_text)
    
def select_files():
    global filess
    file_paths = filedialog.askopenfilenames(title="Select Python Files", filetypes=[("Python Files", "*.py")])
    file_names = [os.path.basename(path) for path in file_paths]  
    selected_files_text.delete("1.0", "end")  
    selected_files_text.insert("end", "\n".join(file_names))
    filess = list(file_paths)
    show_selected_files()

def show_selected_files():
    selected_files_text.delete(1.0, ctk.END)
    if filess:
        for file in filess:
            selected_files_text.insert(ctk.END, file + "\n")
    else:
        selected_files_text.insert(ctk.END, "No files selected.")

def smooth_increment(progress_bar, target_value, step=1, delay=0.01):
    """
    Smoothly increment the progress bar to the target value.
    :param progress_bar: The progress bar widget.
    :param target_value: The value to increment the progress bar to.
    :param step: The step size for each increment.
    :param delay: The delay (in seconds) between each increment.
    """
    current_value = progress_bar["value"]
    while current_value < target_value:
        current_value += step
        if current_value > target_value:
            current_value = target_value
        progress_bar["value"] = current_value
        root.update_idletasks()
        time.sleep(delay)

def run_analysis():

    progress_bar = ttk.Progressbar(control_frame, orient="horizontal", length=1000, mode="determinate")
    progress_bar.grid(pady=5, padx=200, sticky='nsew', row=1, columnspan=3)
    progress_bar["maximum"] = 100  
    progress_bar["value"] = 0  
    
    if not filess:
        print("No files selected. Exiting.")
        progress_bar.destroy()
        return

    python_files = filess

    pyright_log_file = "pyright_log.txt"
    with open(pyright_log_file, 'w', encoding='utf-8') as f:
        for python_file in python_files:
            result = subprocess.run([pyright_path, python_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
            f.write(result.stdout)
            f.write(result.stderr)
            smooth_increment(progress_bar, progress_bar["value"] + 12.5 / len(python_files))
   
    pylint_log_file = "pylint_log.txt"
    with open(pylint_log_file, 'w', encoding='utf-8') as f:
        for python_file in python_files:
            result = subprocess.run([pylint_path, "--exit-zero", "--output-format=text", python_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
            f.write(result.stdout)
            f.write(result.stderr)
            progress_bar["value"] += (25 / len(python_files))  
            smooth_increment(progress_bar, progress_bar["value"] + (25 / len(python_files)))

    # Error codes for Pylint and Pyright
    pylint_error_codes = [
    "C0102", "C0103", "C0111", "C0112", "C0121", "C0202", "C0203", "C0204",
    "C0301", "C0302", "C0303", "C0304", "C0321", "C0322", "C0323", "C0324",
    "C0325", "C0326", "C1001",

    "F0001", "F0002", "F0003", "F0004", "F0010", "F0202", "F0220", "F0321",
    "F0401",

    "R0201", "R0401", "R0801", "R0901", "R0902", "R0903", "R0904", "R0911",
    "R0912", "R0913", "R0914", "R0915", "R0921", "R0922", "R0923",

    "W0101", "W0102", "W0104", "W0105", "W0106", "W0107", "W0108", "W0109",
    "W0110", "W0120", "W0121", "W0122", "W0141", "W0142", "W0150", "W0199",
    "W0201", "W0211", "W0212", "W0221", "W0222", "W0223", "W0231", "W0232",
    "W0233", "W0234", "W0301", "W0311", "W0312", "W0331", "W0332", "W0333",
    "W0401", "W0402", "W0403", "W0404", "W0406", "W0410", "W0511", "W0512",
    "W0601", "W0602", "W0603", "W0604", "W0611", "W0612", "W0613", "W0614",
    "W0621", "W0622", "W0623", "W0631", "W0632", "W0633", "W0701", "W0702",
    "W0703", "W0704", "W0710", "W0711", "W0712", "W1001", "W1111", "W1201",
    "W1300", "W1301", "W1401", "W1402", "W1501",
    ]

    pyright_error_codes = [ "reportGeneralTypeIssues", "reportFunctionMemberAccess",
    "reportMissingImports", "reportInvalidTypeForm", "reportAbstractUsage",
    "reportArgumentType", "reportAssertTypeFailure", "reportAssignmentType",
    "reportAttributeAccessIssue", "reportCallIssue", "reportInconsistentOverload",
    "reportIndexIssue", "reportInvalidTypeArguments", "reportNoOverloadImplementation",
    "reportOperatorIssue", "reportOptionalSubscript", "reportOptionalMemberAccess",
    "reportOptionalCall", "reportOptionalIterable", "reportOptionalContextManager",
    "reportOptionalOperand", "reportRedeclaration", "reportReturnType",
    "reportTypedDictNotRequiredAccess", "reportPrivateImportUsage", "reportIncompatibleMethodOverride",
    "reportIncompatibleVariableOverride", "reportOverlappingOverload", "reportPossiblyUnboundVariable",
    "reportUndefinedVariable", "reportUnboundVariable", "reportUnhashable",
    "reportUnusedCoroutine", "reportUnusedExcept",
    ]

    pylint_error_counts = {code: 0 for code in pylint_error_codes}
    pyright_error_counts = {code: 0 for code in pyright_error_codes}

    # Count the number of errors in each category by finding the error codes in the Pyright log file
    with open(pyright_log_file, 'r', encoding='utf-8') as f:
        log_content = f.read()
        for code in pyright_error_codes:
            count = len(re.findall(r'\b' + re.escape(code) + r'\b', log_content))
            pyright_error_counts[code] += count

    with open(pylint_log_file, 'r', encoding='utf-8') as f:
        log_content = f.read()
        for code in pylint_error_codes:
            count = len(re.findall(r'\b' + re.escape(code) + r'\b', log_content))
            pylint_error_counts[code] += count

    print("Pylint Error Counts:")
    for code, count in pylint_error_counts.items():                                #FOR DEBUGGIN PURPOSES
        print(f"{code}: {count}")

    print("\nPyright Error Counts:")
    for code, count in pyright_error_counts.items():
        print(f"{code}: {count}") 
    
    # Filter the error counts to only 1 or higher
    filtered_pylint_error_counts = {code: count for code, count in pylint_error_counts.items() if count >= 1}
    filtered_pyright_error_counts = {code: count for code, count in pyright_error_counts.items() if count >= 1}


    combined_error_counts = {**filtered_pylint_error_counts, **filtered_pyright_error_counts}

    #dataframe for the pareto chart
    df = pd.DataFrame(list(combined_error_counts.items()), columns=['Error Code', 'Count'])
    df = df.sort_values(by='Count', ascending=False)
    df["cumpercentage"] = df["Count"].cumsum() / df["Count"].sum() * 100
    print(df)

    #pareto Chart
    def show_chart():
        fig, ax1 = plt.subplots(figsize=(6, 25))  # Adjust the size of the plot
        fig.patch.set_facecolor('#212121')  # Set the background color of the figure
        ax1.set_facecolor('#444444')  # Set the background color of the axes

        ax1.bar(df['Error Code'], df["Count"], color="C0")
        ax1.set_ylabel("Number of Errors", color="C0")
        ax1.tick_params(axis="y", colors="C0")
        ax1.set_xlabel("Error Code")

        # Ensure proper tick setting before modifying labels
        ax1.set_xticks(range(len(df['Error Code'])))
        ax1.set_xticklabels(df['Error Code'], rotation=90, fontsize=10, color="white")

        ax1.set_title("Pareto Chart of Error Codes", color="white")

        ax2 = ax1.twinx()
        ax2.plot(range(len(df['Error Code'])), df["cumpercentage"], color="C1", marker="D", ms=7)
        ax2.yaxis.set_major_formatter(PercentFormatter())
        ax2.tick_params(axis="y", colors="C1")

        plt.subplots_adjust(bottom=0.4)  # Adjust layout to prevent cutoffs

        # Add the chart to the chart frame
        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=ctk.TOP, fill=ctk.BOTH, expand=True)
        
    # Find the top errors contributing to 80% of the issues
    df_pareto = df[df["cumpercentage"] <= 100]

    # If the dataframe is empty, use the first row
    if df_pareto.empty:
        df_pareto = df.iloc[:1]
    smooth_increment(progress_bar, progress_bar["value"] + (50 / len(python_files)))

    df_pareto_category = df_pareto['Error Code'].tolist()
    final_analysis = [category for category in df_pareto_category]
    print("\nTop Errors Contributing to 80% of Issues:")
    print(final_analysis)

    # Display the feedback for the errors causing 80% of the issues
    relevant_errors = df_pareto['Error Code'].tolist()
    print("\nFeedbacks for errors causing 80% of the issues:")
    feedbacks_by_module = {}

    # Find the error codes in the log file and display the feedback
    for error in relevant_errors:
        if error.startswith('report'):
            with open(pyright_log_file, 'r', encoding='utf-8') as f:
                log_content = f.readlines()
                for line in log_content:
                    if error in line:
                        match = re.search(r'([\w.]+\.py):(\d+):\d+ - error: (.+) \((\w+)\)', line)
                        print(match)
                        if match:
                            module_name = match.group(1)
                            line_number = match.group(2)
                            error_code = match.group(4)
                            error_message = match.group(3)
                            if module_name not in feedbacks_by_module:
                                feedbacks_by_module[module_name] = {}
                            feedbacks_by_module[module_name].update({f"Line : {line_number} [{error_code}] - {error_message}":int(line_number)})
        else:
            with open(pylint_log_file, 'r', encoding='utf-8') as f:
                log_content = f.readlines()
                for line in log_content:
                    if error in line:
                        match = re.search(r'(\w+\.py):(\d+):\d+: (\w\d+): (.+)', line)
                    
                        if match:
                            module_name = match.group(1)
                            line_number = match.group(2)
                            error_code = match.group(3)
                            error_message = match.group(4)
                            if module_name not in feedbacks_by_module:
                                feedbacks_by_module[module_name] = {}
                            feedbacks_by_module[module_name].update({f"Line : {line_number} [{error_code}] - {error_message}":int(line_number)})

    sorted_feedbacks = sorted(feedbacks_by_module[module_name].items(), key=lambda x: x[1])
    feedbacks_by_module[module_name] = sorted_feedbacks
    smooth_increment(progress_bar, progress_bar["value"] + (75 / len(python_files)))


    feedback_text = ""
    for module_name, feedbacks in feedbacks_by_module.items():
        feedback_text += f"\n({module_name})\n"
        for feedback in feedbacks:
            if isinstance(feedback, str):
                feedback_text += feedback + "\n\n"
            else:
                feedback_text += str(feedback[0]) + "\n\n"
    hello_log_file = "all_log.txt"
    with open(hello_log_file, 'w', encoding='utf-8') as f:
        for python_file in python_files:
            f.write(feedback_text)
    smooth_increment(progress_bar, 100)
    progress_bar.destroy()
    update_gui(feedback_text)
    show_chart()
        
    


def all():
    hello_log_file = "all_log.txt"
    with open(hello_log_file, 'r', encoding='utf-8') as f:
        log_content = f.read()

    update_gui(log_content)
    

def update_gui(feedback_text):
    for widget in feedback_frame.winfo_children():
        widget.destroy()

    button_functions = {"All": all, "Error": error, "Refactor": refactor, "Warning": warning, "Convention": convention, "Fatal": fatal}


    error_frame = ctk.CTkFrame(feedback_frame, border_color='#FFFFFF', fg_color='#212121', border_width= 2)
    error_frame.pack(pady=5, padx=5, fill= 'x')

    for label, func in button_functions.items():
        button = ctk.CTkButton(error_frame, border_width= 2, border_color="#FFFFFF",font=("Arial", 14), text=label, corner_radius=0, fg_color='#e0569c', height=45 , width=115, command=func)
        button.pack(expand = 'True', padx=5, pady= 5,  fill= 'x', side = 'left')

    feedback_text_frame = ctk.CTkFrame(feedback_frame, fg_color="transparent", border_color="#FFFFFF", border_width=3,)
    feedback_text_frame.pack(fill=ctk.BOTH, expand=True)

    feedback_image = ctk.CTkImage(light_image = Image.open("Feedback.png"), dark_image= Image.open("Feedback.png"), size= (200, 25))    
    feedback_label = ctk.CTkLabel(feedback_text_frame, text="", image = feedback_image)
    feedback_label.pack(pady=10)

    feedback_text_widget = ctk.CTkTextbox(master=feedback_text_frame, font=("Segoe UI", 12), fg_color="#212121", text_color="white", wrap="word", border_color="#FFFFFF", border_width=3)
    feedback_text_widget.pack(side="left", fill="both", expand=True)
    feedback_text_widget.insert(ctk.END, feedback_text)

    


root = ctk.CTk()
root.geometry("1200x800")
root.configure(fg_color='#212121')
#sa title 
title_image = ctk.CTkImage(light_image = Image.open("Title.png"), dark_image= Image.open("Title.png"), size= (1200, 50))
title_label = ctk.CTkLabel(root, text="", image= title_image)

title_label.pack(pady=20)
# 3box under title
control_frame = ctk.CTkFrame(root, border_color='#212121', fg_color='#212121', height= 75)
control_frame.pack(anchor="n", padx=15, pady=5)
# select files box
select_files_button = ctk.CTkButton(master=control_frame, text="SELECT FILES", fg_color='#c11c84', hover_color= '#86335d', font=("Arial bold", 16),text_color='#FFFFFF', hover=True, command=select_files, height=75, width=175, border_width=3, border_color='#FFFFFF', corner_radius=1)
select_files_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
# run box
player_image = ctk.CTkImage(light_image=Image.open("player.png"), dark_image=Image.open("player.png"), size=(125, 40))
run_analysis_button = ctk.CTkButton(master=control_frame, border_width=3, text="", image=player_image,fg_color='#e0569c', hover_color= '#86335d', border_color='#FFFFFF', height=75, width=175, command=lambda: threading.Thread(target=run_analysis).start(), corner_radius=1)
run_analysis_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")



# text frame sa abox under title
text_frame = ctk.CTkFrame(control_frame, fg_color="transparent", corner_radius=1)
text_frame.grid(row=0, column=1,padx=5, pady=5, sticky="nsew")
text_frame.grid_propagate(False)  # Prevent auto-resizing to children

# text sa box udner title
selected_files_text = ctk.CTkTextbox(master=text_frame, font=("Arial", 12), height=75, width=1000,fg_color="#212121", text_color="white", border_color="#FFFFFF", border_width=3, wrap="word", corner_radius=1)
selected_files_text.pack(side="left", expand= "True", fill="x")

control_frame.grid_columnconfigure(1, weight=50)
control_frame.grid_columnconfigure(2, weight=50)
control_frame.grid_columnconfigure(0, weight=50)
control_frame.grid_rowconfigure(0, weight=50)
control_frame.grid_rowconfigure(1, weight=1)


# Create and pack buttons


chart_frame = ctk.CTkFrame(root, fg_color='#212121', corner_radius=1)
chart_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=False)

feedback_frame = ctk.CTkFrame(root, fg_color='#212121', border_color="#FFFFFF", corner_radius=1)
feedback_frame.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=True, padx = 30, pady= 20)




root.mainloop()