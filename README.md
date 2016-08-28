# Bitcoin price prediction

An implementation of the 'Bayesian regression for latent source model' method for predicting price variation of [Bitcoin](https://bitcoin.org). You can read more about the method at https://arxiv.org/pdf/1410.1231.pdf.

## Requirements

* [Python](https://www.python.org/) 3.5
* [MongoDB](http://www.mongodb.org/) 3.2
* [bigfloat prerequisites](http://bigfloat.readthedocs.org/en/latest/#prerequisites)

## Installation

Make sure you have installed all the requirements and [created an isolated Python environment](https://virtualenv.pypa.io/en/stable/) for this project (optional). Then follow the installation instructions:

```sh
    $ git clone https://github.com/stavros0/bitcoin-price-prediction.git
    $ cd bitcoin-price-prediction
    $ pip install -e .
```

## Usage

- Use the `okcoin.py` script to gather market data from the [OKCoin Spot Price API](https://www.okcoin.com/about/rest_api.do) at the interval of every ten seconds. Bear in mind that you need **at least** 721 data points so that [`m = len(prices) - n > 0`](https://github.com/stavros0/bitcoin-price-prediction/blob/master/bitcoin_price_prediction/bayesian_regression.py#L28).

```sh
$ python okcoin.py
```

- See [bitcoin-price-prediction/examples](https://github.com/stavros0/bitcoin-price-prediction/tree/master/examples) for how to use the [`bayesian_regression.py`](https://github.com/stavros0/bitcoin-price-prediction/blob/master/bitcoin_price_prediction/bayesian_regression.py) module. [`millionare.py`](https://github.com/stavros0/bitcoin-price-prediction/blob/master/examples/millionaire.py) is intended for tinkering and experimenting only and therefore won't display anything on the screen. That is, you should tinker with my script or write your own script instead. In any case, you have to speak Python.


## License

This project is licensed under the terms of the MIT license. See [LICENSE](https://github.com/stavros0/bitcoin-price-prediction/blob/master/LICENSE) for more information.
