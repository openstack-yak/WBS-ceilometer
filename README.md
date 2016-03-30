## WBS-ceilometer

### Workspace for developing Work Breakdown Structions

Outline a card's work in yaml format.

You can download a trello board by exporting it as json.
You can convert the json board to yaml with the json2yaml.py script in the tools section here.
You can preview the python instance of your yaml task expansion with yaml2py.py.

You can get the URL to a specific card, or export the json for a single card from the ''share and more'' menu on the right side of the card.
However, trello gives you the json form of the transactional data for your board.
For task expansion, we are using a different form.

The cards we are currently interested in

  - [CFGDFT -- Centralize configuration defaults](https://trello.com/c/TSIPTycQ)
  - [GNOBEN -- Benchmark Gnocchi](https://trello.com/c/dFqhW3am)
  - [CEIDOC -- Review and update or expand administrators and operators guides for Ceilometer](https://trello.com/c/w8rAJ0u8)
  

TODO:
  - retrieve and update card data by trello-api;
  - filter out trello info not useful to developing work structure;
  - the complete json for the [OSIC - Ceilometer/Horizon/Fleetmgt](https://trello.com/b/Rd79MAR2/osic-ceilometer-horizon-fleetmgt) board (and its yaml version) is probably not needed here, but for now it might be useful as a reference;  delete at some point

Some potentially useful references:

  - https://pythonhosted.org/trello/trello.html
  - https://trello.com/app-key
