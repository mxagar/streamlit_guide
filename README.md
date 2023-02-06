# Streamlit Guide

This is a [Streamlit](https://streamlit.io/) guide in which 12 data science web apps as built. The original repository is from [Chanin Nantasenamat, Ph.D.](https://github.com/dataprofessor): [streamlit_freecodecamp](https://github.com/dataprofessor/streamlit_freecodecamp). I extended the repository with my notes: [`Streamlit_Guide.md`](Streamlit_Guide.md). The repository has also a [FreeCodeCamp](https://www.freecodecamp.org/) course by Dr. Nantasenamat: [Build 12 Data Science Apps with Python and Streamlit - Full Course](https://youtu.be/JwSS70SZdyM).

If you're looking for a written tutorial, just open [`Streamlit_Guide.md`](Streamlit_Guide.md) and follow it by checking the code in the app folders. In addition to that, the file [`streamlit_summary_app.py`](streamlit_summary_app.py) is a summary app file, which doesn't run, but which is a compilation of the most important commands.

To use the apps, you should install the requirements in a python environment; for instance, you can do it with [conda](https://docs.conda.io/en/latest/) using the provided YAML file:

```bash
# Create environment with YAML, incl. packages
conda env create -f conda.yaml
conda activate streamlit-guide
```

Note that the `requirements.txt` file is used in the deployment examples, i.e., it's not enough for running the complete repository.

Mikel Sagardia, 2023.  
No guarantees.