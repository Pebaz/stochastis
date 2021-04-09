# Stochastis

> ***Convert Python code into music to hear algorithms***

### About

Pronounced "stoʊ-kæst-ɪs" ("stow" + "cast" + "is" like "miss"), Stochastis was a
small experiment in figuring out if it would be possible to hear what a given
algorithm sounds like. However, the goal was accomplished in a much more general
fashion. Instead of only algorithms, Stochastis converts each function
in a Python module to its corresponding bytecode which it then converts to MIDI
notes along a predefined scale. It then generates a MIDI file from them or plays
them upon generation.

### Installation

```python
$ pip install stochastis
$ pip install git+https://github.com/Pebaz/stochastis
```

### Usage

```python
$ stochastis foo.mid                     # Play from file
$ stochastis some_file.py                # Generate and play from file
$ stochastis some_file.py --out foo.mid  # Generate only
```

### Conclusion

What was accomplished in this experiment is just a small inkling of the amount
of potential this has for pleasing music being generated from a given codebase.

Some ideas for extensions include:

* Identifying patterns in bytecode to produce familiar stanzas
* Performing analysis on the bytecode of functions to identify patterns so that
pre-built sequences of notes can be grafted into the output
* Clearer rules for what is generated based on what is actually written in
Python code
* Integration with better sounding synthesizers
* Layered tracks with multiple intstruments playing at once (drums, etc.)
* Converting program control flow into sections of a given song
