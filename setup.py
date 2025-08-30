from setuptools import setup, find_packages

setup(
    name='word-detector',
    version='2.0.0',
    description='Word Detector with Scale Space Technique',
    author='Harald Scheidl',
    packages=find_packages(),
    url="https://github.com/githubharald/WordDetector",
    install_requires=[
        'numpy>=1.24.0',
        'scikit-learn>=1.3.0',
        'opencv-python>=4.8.0'
    ],
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)