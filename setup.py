from setuptools import setup, find_packages

setup(
    name="actividades", # Cambié el nombre a algo más general
    version="0.0.1",
    author="wilmer arce",
    author_email="",
    description="",
    py_modules=["actividad_2", "actividad_3"],
    install_requires=[
        "pandas",
        "openpyxl",
        "requests", # Paquete separado
        "matplotlib",  # Paquete separado
        "numpy",  # Paquete separado
        "seaborn"  # Paquete separado

    ]   
)