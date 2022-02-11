import pathlib
import subprocess

"""
dot -Tps input.dot > output.eps
dot -Tpng input.dot > output.png
dot -Tsvg input.dot > output.svg
"""

cmd = 'dot {source}.dot -Tsvg -o ../output/{output}.svg'
cmd_png = 'dot {source}.dot -Tpng -o ../output/{output}.png'
here = pathlib.Path(__file__).parent.parent.joinpath('dot').absolute()

dot_files = here.glob('*.dot')

for f in dot_files:
    print(f"Processing {f}...")
    subprocess.call(cmd.format(source=f.stem, output=f.stem), shell=True, cwd=str(here))
    subprocess.call(cmd_png.format(source=f.stem, output=f.stem), shell=True, cwd=str(here))
