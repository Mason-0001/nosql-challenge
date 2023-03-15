from nbconvert import PythonExporter
import nbformat

def scrape(notebook_file, output_file):
    # Read the notebook file
    with open(notebook_file) as f:
        nb = nbformat.read(f, as_version=4)

    # Configure the exporter
    exporter = PythonExporter()

    # Export the notebook to a Python script
    (script, _) = exporter.from_notebook_node(nb)

    # Write the script to the output file
    with open(output_file, 'w') as f:
        f.write(script)


notebook_file = '/Users/Mason/Desktop/Personal-Repo/nosql-challenge/Missions_to_Mars/mission_to_mars.ipynb'

output_file = '/Users/Mason/Desktop/Personal-Repo/nosql-challenge/Missions_to_Mars/scrape_mars.py'

scrape(notebook_file, output_file)