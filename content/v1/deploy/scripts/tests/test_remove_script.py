import subprocess
import nbformat as nbf

path_old = 'base_notebook.ipynb'
path_new = 'new_notebook.ipynb'
cmd = 'python ../remove_okpy_server_code.py {} {} --overwrite'.format(path_old, path_new)
subprocess.check_output(cmd.split())

new = nbf.read(path_new, nbf.NO_CONVERT)
assert all(ii not in new['cells'][1]['source'] for ii in ('ok.auth', 'ok.submit'))
