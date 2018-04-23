"""Remove all lines from notebooks that depend on the OKpy server to exist.

Note that `ok.grade` works locally and only needs the package installed, so
we do not remove these lines. We only remove lines that depend on the *server*.
This includes `ok.auth` and `ok.submit`.

To see an example of how the script works, look at the script in `tests/`.
"""

import nbformat

import os
import sys
import argparse

DESCRIPTION = ("Remove all lines from notebooks that depend on the OKpy server to exist."
               "Note that `ok.grade` works locally and only needs the package installed, so"
               "we do not remove these lines. We only remove lines that depend on the *server*."
               "This includes `ok.auth` and `ok.submit`.")

parser = argparse.ArgumentParser(description=DESCRIPTION)
parser.add_argument("path_in", help="Path to the notebook we'll modify.")
parser.add_argument("path_out", help="Path for the output notebook")
parser.add_argument("--overwrite", dest='overwrite', action='store_true', help="Overwrite the output file if it exists.")
parser.set_defaults(overwrite=False)

NB_VERSION = 4

REMOVE_LINES_TEXT = ['ok.auth(', 'ok.submit(']

def remove_okpy_server(inpath, outpath, overwrite=False):
    """Remove all references to the OKpy server."""
    assert overwrite or not os.path.exists(outpath), 'Already exists: ' + outpath
    nb = nbformat.read(inpath, NB_VERSION)
    for cell in nb['cells']:
        new_contents = '\n'.join(
            [line for line in cell['source'].split('\n')
             if not any(ii in line for ii in REMOVE_LINES_TEXT)])
        cell['source'] = new_contents

    with open(outpath, 'w') as f:
        nbformat.write(nb, f, NB_VERSION)

def main():
    # Parse args
    args = parser.parse_args()
    in_path = args.path_in.strip('\'"')
    out_path = args.path_out.strip('\'"')
    overwrite = args.overwrite
    
    # Do the OKpy scraping
    assert in_path.endswith('.ipynb'), 'In path not a notebook: ' + in_path
    assert os.path.exists(in_path), 'File not found: ' + in_path
    assert out_path.endswith('.ipynb'), 'Out path not a notebook: ' + out_path
    remove_okpy_server(in_path, out_path, overwrite=overwrite)

if __name__ == '__main__':
    main()