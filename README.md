# Bitcoin price prediction

An implementation of the 'Bayesian regression for latent source model' method for predicting price variation of [Bitcoin](https://bitcoin.org). You can read more about the method at https://arxiv.org/pdf/1410.1231.pdf.

## Requirements

* [Python](https://www.python.org/) 3.5
* [MongoDB](http://www.mongodb.org/) 3.2
* [bigfloat prerequisites](http://bigfloat.readthedocs.org/en/latest/#prerequisites)

## Installation

```sh
    $ git clone https://github.com/stavros0/bitcoin-price-prediction.git
    $ cd bitcoin-price-prediction
    $ pip install -e .
```

## Usage

- Gather market data from the [OKCoin Spot Price API](https://www.okcoin.com/about/rest_api.do) at the interval of every ten seconds:

```sh
$ python okcoin.py
```

- See [bitcoin-price-prediction/examples](https://github.com/stavros0/bitcoin-price-prediction/tree/master/examples) for how to use the `bayesian_regression.py` module.

## License

This project is licensed under the terms of the MIT license. See LICENSE for more information.
