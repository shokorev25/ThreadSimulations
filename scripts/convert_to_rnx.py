import os
import gzip
import subprocess
import shutil

def convert_to_rnx(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        if filename.endswith(".crx.gz"):
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, os.path.splitext(filename)[0] + ".rnx")

            with gzip.open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

            crx2rnx_command = f"bin/CRX2RNX.exe {output_file}"
            subprocess.run(crx2rnx_command, shell=True)
            print(f"Converted {input_file} to {output_file}")

if __name__ == "__main__":
    input_dir = "./data/extracted"
    output_dir = "./data/converted"
    convert_to_rnx(input_dir, output_dir)
