# RePoE

Repository of Path of Exile resources for tool developers.

Contains data about stats, mods and gems at the moment. See the `data`
folder for those files and the `docs` folder for their documentation.

For the actual GGPK parsing, [PyPoE](https://github.com/OmegaK2/PyPoE) is used.
The code here just converts PyPoE's Python objects to JSON.

Developed to supply [PoESkillTree](https://github.com/EmmittJ/PoESkillTree) with the
game data information it requires. If you need other files converted, feel free to
open an Issue or Pull Request for that.

## Files

The `data` folder contains the generated data in Json format. Each file has a
formatted and a compact version. The formatted versions complement their descriptions
in the `docs` folder.

Note that the file formats are not yet final, they may change at any time. Once
they are more stable, I'll probably make releases every time the game has updates
that changes these files.

The following data is currently available:

- `stat_translations.json`: Maps stat ids together with their values to human-readable
  text. This is the text that appears on items in-game.
- `stats.json`: Describes stat ids. Defines whether they are local and whether they
  are aliased depending on main-hand or off-hand.
- `mods.json`: Describes mod ids. Defines which items they can appear on and what
  stats with what values they have.
- `crafting_bench_options.json`: Describes master craftable mods. Defines which
  masters can craft them at which level on which items.
- `npc_master.json`: Describes the master's signature mods and on which items they
  can appear.
- `gems.json`: Describes skill gems and skill gem effects only provided by mods.
- `gem_tags.json`: Simple object that contains all gem tags with their internal id as
  keys and their translation as value.
- `gem_tooltips.json`: Describes tooltips for skill gems and skill gem effects only
  provided by mods.
  
## Running RePoE

- Install Python 3.4 or 3.5 and Git
- Install [PyPoE](https://github.com/OmegaK2/PyPoE):
  * Clone PyPoE and go into its folder
  * Minimal install: `pip install -e .`
  * Full install: `pip install -e .[full]` (not required for RePoE, requires Python
    3.4)
- Clone RePoE and go into its folder
- Run `python RePoE.py`  
  (`python RePoE.py -h` to see arguments)

## Credits

- [Grinding Gear Games](http://www.grindinggear.com/) for 
  [Path of Exile](https://www.pathofexile.com/). The contents of all `data` files
  obviously belong to them.
- [OmegaK2](https://github.com/OmegaK2/) for [PyPoE](https://github.com/OmegaK2/PyPoE).
