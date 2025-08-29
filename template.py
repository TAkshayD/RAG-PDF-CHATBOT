import os

structure = {
    "app": ["__init__.py", "main.py"],
    "app/models": ["__init__.py", "predictor.py", "model.pkl"],
    "app/api": ["__init__.py", "routes.py"],
    "app/core": ["config.py", "utils.py"],
    "app/schemas": ["__init__.py", "insurance.py"],
    "data": ["raw.csv", "processed.csv"],
    "notebooks": ["EDA.ipynb", "model_training.ipynb"],
    "tests": ["test_api.py", "test_model.py"],
}

# Create directories and files
for folder, files in structure.items():
    os.makedirs(folder, exist_ok=True)
    for file in files:
        open(os.path.join(folder, file), "a").close()

# Create root-level files
root_files = ["requirements.txt", "Dockerfile", ".gitignore", "README.md", "LICENSE"]
for file in root_files:
    open(file, "a").close()


