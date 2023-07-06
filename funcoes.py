import time

def print_files_main():
    print()
    print('+-------------------------------------------+');
    print('|             ARQUIVOS CRIADOS              |');
    print('+-------------------------------------------+');
    time.sleep(0.5) 

def print_file(csv_filename):
    print(f"| {csv_filename:<23} | \033[94mSuccessful\033[0m      |")
    print("+-------------------------+-----------------+")
    time.sleep(0.3) 