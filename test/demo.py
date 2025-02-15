import os
import subprocess
import re

directory = r"C:\Users\emman\OneDrive\Documents\GitHub\erroranalysisparetoprinciple\test"
log_file = os.path.join(directory, "pylint_log.txt")

python_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.py')]

with open(log_file, 'w', encoding='utf-8') as f:
    for python_file in python_files:
        result = subprocess.run(["pylint", "--exit-zero", "--output-format=text", python_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
        f.write(result.stdout)
        f.write(result.stderr)

error_codes = {
    'Value Error': ['E00139', 'E130711', 'E1507', 'E1201', 'E1301'],
    'Syntax Error': ['E11426', 'E011612', 'E0104', 'E0001', 'E1700', 'E010510'],
    'Attribute Error': ['E02032', 'E02373', 'E0242', 'E0245', 'E0238', 'E0236', 'E0202', 'E110110', 'E1136'],
    'Type Error': ['E11114', 'E11285', 'E07018', 'E011110', 'E0712', 'E1141', 'E0240', 'E0239', 'E030412', 'E030812', 'E0243', 'E0244', 'E0311', 'E0313', 'E0312', 'E0309', 'E0305', 'E0310', 'E0303', 'E1139', 'E0306', 'E1127', 'E0307', 'E113010', 'E0301', 'E1134', 'E1133', 'E110210', 'E0702', 'E1519', 'E1520', 'E113110', 'E1135', 'E2501'],
    'Name Error': ['E0611', 'E0603', 'E0602', 'E0601', 'E0118']
}

error_counts = {code: 0 for codes in error_codes.values() for code in codes}

with open(log_file, 'r', encoding='utf-8') as f:
    log_content = f.read()
    for code in error_counts:
        error_counts[code] = len(re.findall(r'\b' + re.escape(code) + r'\b', log_content))

for error_type, codes in error_codes.items():
    print(f"{error_type}:")
    for code in codes:
        print(f"  {code}: {error_counts[code]}")
    print()