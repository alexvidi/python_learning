# python_learning
First steps in python

### Steps reproduced
1. Clone this repo:
```bash
git clone https://github.com/alexvidi/python_learning.git
````

2. Get Jupyter Lab
```bash
pip install --user jupyterlab
```

3. Create a virtual environment:
```bash
python -m venv venv
````

4. Access your virtual environment:
```bash
source venv/bin/activate
````

5. Register the kernel of your venv:
```bash
pip install ipykernel
python -m ipykernel install --user --name venvname --display-name "Python (venvname)"
````

6. Start working with Jupyter Notebooks on Jupyter Lab:
```bash
jupyter lab
````

7. After your modifications, add files and commit changes:
```bash
git add hello_world.py
git add hello_world.ipynb
git commit -m "Add first python code"
````

8. Push local changes into the remote master branch:
```bash
git push
````
