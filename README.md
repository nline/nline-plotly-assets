# Assets for nLine's Visualizations

This repository contains a collection of assets for nLine's visualizations. Currently it only contains the Plotly `layout`` and `config` parameters for our generic style.

They can be loaded either in Python automatically:

```py
from pwdata.utils import plotly_style
```

or by accessing the `plotly_style.yml` file.

```py
import plotly_assets
import importlib.resources
import yaml
import plotly.graph_objects as go


style = yaml.safe_load(importlib.resources.open_text("plotly_assets", "plotly_style.yml"))
fig.update_layout(style['layout'])

# Adding data or custom layout parameters

fig.show(config=style['config'])
```

The file is also sourced and used in our Grafana dashboard's from [this link to the raw file](https://raw.githubusercontent.com/nline/nline-plotly-assets/main/plotly_assets/plotly_style.yml).
