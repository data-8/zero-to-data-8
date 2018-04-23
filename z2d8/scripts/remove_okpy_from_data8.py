"""Remove all OKpy server dependencies from a folder with Data 8 materials."""

from subprocess import check_call
from glob import glob
import os
import shutil as sh
import argparse
from tqdm import tqdm

DESCRIPTION = ("Find all Jupyter Notebook files in a folder, and remove all references to the OKpy server."
               "This simply calls the `remove_okpy_server_code.py` script on each notebook we find.")

parser = argparse.ArgumentParser(description=DESCRIPTION)
parser.add_argument("path_in", help="Path to the folder we'll modify.")
parser.add_argument("path_out", help="Path for the output folder")
parser.add_argument("--overwrite", dest='overwrite', action='store_true', help="Overwrite the output file if it exists.")
parser.set_defaults(overwrite=False)


def main():
    # Parse args
    args = parser.parse_args()
    in_path = args.path_in
    out_path = args.path_out
    overwrite = args.overwrite
    
    # Make a copy of the repository
    if os.path.exists(out_path):
        if overwrite is False:
            raise ValueError("Output path exists and overwrite is False")
        else:
            sh.rmtree(out_path)
    sh.copytree(in_path, out_path)
    
    # Now loop through the new one and update the jupyter notebooks
    all_files = glob(os.path.join(out_path, '**', '*.ipynb'), recursive=True)
    for ifile in tqdm(all_files):
        if ' ' in ifile:
            ifile = '"%s"' % ifile
        cmd = ['python', 'remove_okpy_server_code.py', ifile, ifile, '--overwrite']
        check_call(cmd)

if __name__ == '__main__':
    main()