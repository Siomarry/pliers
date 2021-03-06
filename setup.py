from setuptools import setup, find_packages
import os

extra_setuptools_args = dict(
    tests_require=['pytest']
)

thispath, _ = os.path.split(__file__)

ver_file = os.path.join(thispath, 'pliers', 'version.py')

with open(ver_file) as fp:
    exec(fp.read(), globals(), locals())

setup(
    name="pliers",
    version=locals()['__version__'],
    description="Multimodal feature extraction in Python",
    maintainer='Tal Yarkoni',
    maintainer_email='tyarkoni@gmail.com',
    url='http://github.com/tyarkoni/pliers',
    install_requires=['numpy', 'scipy', 'moviepy', 'pandas',
                      'pillow', 'python-magic', 'requests', 'nltk'],
    packages=find_packages(exclude=['pliers/tests']),
    license='MIT',
    package_data={'pliers': ['datasets/*'],
                  'pliers.tests': ['data/*/*']
                  },
    zip_safe=False,
    download_url='https://github.com/tyarkoni/pliers/archive/%s.tar.gz' %
    __version__,
    **extra_setuptools_args,
    extras_require={
        'all':  ['clarifai', 'duecredit', 'face_recognition', 'python-twitter',
                 'gensim', 'google-api-python-client', 'google-compute-engine',
                 'librosa>=0.6.3' 'numba<=0.48', 'matplotlib', 'opencv-python',
                 'pathos', 'pygraphviz', 'pysrt', 'pytesseract',
                 'python-twitter', 'scikit-learn', 'seaborn', 'soundfile',
                 'spacy', 'SpeechRecognition>=3.6.0', 'tensorflow>=1.0.0',
                 'torch', 'transformers', 'xlrd', 'rev_ai']
    },
    python_requires='>=3.5',
)
