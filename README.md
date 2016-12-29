# RePoE

Repository of Path of Exile resources for tool developers.

Contains information about stat and mod id resolution to supplement the
[unofficial Wiki's API](https://pathofexile.gamepedia.com/api.php). See the `data`
folder for those files.

For the actual GGPK parsing, [PyPoE](https://github.com/OmegaK2/PyPoE) is used.
The code here just converts PyPoE's Python objects to JSON.

Developed to allow [PoESkillTree](https://github.com/EmmittJ/PoESkillTree) full
usage of the Wiki's API, so only information the Wiki's API doesn't contain is extracted
here.

## Files

The `data` folder contains the generated data in Json format. Each file has a nicely
formatted and a compact version. The formatted versions complement the descriptions
in the `docs` folder.
