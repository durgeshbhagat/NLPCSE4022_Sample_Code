# python-chardet-example


## Installation

Clone this repository, then `cd` into the directory.

I suggest creating a virtual environment using (Miniconda/Anaconda) and installing cchardet. Something like the following should work:

```console
conda create -n characterEncoding python=3.7
. conda activate characterEncoding
. pip install chardet
. pip install chcardet

```

If new to virtual environments, feel free to [read my article on the subject](https://dev.to/bowmanjd/python-tools-for-managing-virtual-environments-3bko).

## Usage

```console
python detect.py sample-latin1.csv
```

The code assumes Python 3. You may need to use `python3` in place of `python` above.

Feel free to use your own text files, and analyze and adapt the code.

## Contributing

Please feel free to submit pull requests and/or open issues.

## License

Copyright 2020 Jonathan Bowman. All documentation and code contained in this repository may be freely shared in compliance with [the Apache License, Version 2.0][apache 2.0], and is provided “AS IS” without warranties or conditions of any kind.

[apache 2.0]: http://www.apache.org/licenses/LICENSE-2.0
