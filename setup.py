from setuptools import setup


setup(
    name="cvx",
    version="0.1.1",
    description="OpenCV 'extension' with routinely used methods",
    url="https://github.com/erikperillo/cvx",
    author="Erik Perillo",
    author_email="erik.perillo@gmail.com",
    license="GPL3",
    packages=["cvx"],
    classifiers=["Programming Language :: Python :: 2.7"],
    zip_safe=False,
    install_requires=["numpy"]
) 
