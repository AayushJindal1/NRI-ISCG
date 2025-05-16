# run_all.py
import glob, subprocess, sys

NB_DIR = 'notebooks'
for nb in sorted(glob.glob(f'{NB_DIR}/*.ipynb')):
    print(f'▶️ Executing {nb}')
    subprocess.run([
        sys.executable, '-m', 'nbconvert',
        '--to', 'notebook',
        '--inplace',
        '--execute',
        '--allow-errors',
        '--ExecutePreprocessor.timeout=300',
        nb
    ], check=True)
print('✅ All done.')
