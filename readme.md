# AI-nything
N-ything problem is a modified n-Queens problem. The difference is the considered chesspiece is not onlu the Queen, but also including Knight, Bishoop, and Rook. Just like the n-Queens problem, N-ything problem is to find the combination of chesspiece positiion on 8x8 chessboard with minimum number of attacking chesspieces.
Formally, find the combination of chesspiece so the tuple *(p, q)* where p __attacks_ q is minimum. Note that if p attacks q, it doesn't mean that p attacks p. Note that (p, q) and (q, p) is a completely different tuple
The attacking system on this problem follows the conventional chess rules.

## Prerequisites
1. This app only compatible with Unix based system

## Getting Started

First, put the configuration file in the project directory. 

ex: `input.txt`
```
WHITE KNIGHT <number of white knight>
WHITE BISHOP <number of white bishop>
WHITE ROOK <number of white rook>
WHITE QUEEN <number of white queen>
BLACK KNIGHT <number of black knight>
BLACK BISHOP <number of black bishop>
BLACK ROOK <number of black rook>
BLACK QUEEN <number of black queen>
```


## Running the game

To run the game, simply

```
$ python main.py
```

and just follow the instructions.

## Authors

* **Abram Perdanaputra Situmorang** - *Initial work* - [abrampers](https://github.com/abrampers)
* **Ilham Firdausi Putra** - *Initial work* - [ilhamfp31](https://github.com/ilhamfp31)
* **Nicholas Rianto Putra** - *Initial work* - [Nicholaz99](https://github.com/Nicholaz99)
* **M. Sulthan Adhipradhana** - *Initial work* - [adhipradhana](https://github.com/adhipradhana)
* **Yusuf Rahmat Pratama** - *Initial work* - [yusufrahmatp](https://github.com/yusufrahmatp)

## Report
https://docs.google.com/document/d/1fzwXxGnTdkkiVfkSqpB-gZqZC-Bhnql6hr_OPB0134A/edit?usp=sharing

## Acknowledgments
* Mrs. Masayu Leylia Khodra (Lecturer)
* Magnus Carlsen
