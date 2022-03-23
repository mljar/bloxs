<p align="center">
<img src="https://raw.githubusercontent.com/mljar/visual-identity/main/bloxs/blox%20line%20white.png" />
</p>

# Bloxs

Bloxs is a simple python package that helps you display information in an attractive way (formed in blocks).

It works with: Jupyter Notebook, Google Colab, Deepnote, Kaggle Notebook, [Mercury](https://github.com/mljar/mercury).

## Get started

Install bloxs:

```
pip install bloxs
```

Import and create a bloxs
```
from bloxs import B
B(1234, "Bloxs in notebook!")
```

![](docs/media/test_bloxs.png)

## Exmaples

| Bloxs | Code |
| --- | --- |
| ![](docs/media/number.png) | `B(1234, "Bloxs in notebook!")` |
| ![](docs/media/percent.png) | `B(1999, "Percent change!", percent_change=10)` |
| ![](docs/media/emojis.png) | `B("🎉🎉🎉", "Works with emojis")` |


