# Interactive Polyscope

This integrates a custom GUI event loop to be able to run [polyscope](https://github.com/nmwsharp/polyscope) asynchronously in a jupyter notebook.

## Installation

```bash
pip install git+https://github.com/ugogon/interactive_polyscope.git
```

## Usage

```python
import polyscope as ps
import interactive_polyscope

%gui polyscope

ps.show()

#other commands
```

The important thing is the `%gui polyscope` magic command. It runs a custom event loop that handles the jupyter kernel REPL and the polyscope event loop.
