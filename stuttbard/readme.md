# Stuttbard

## Generating training Data
To generate the training data run `python3 -m scripts.create_data` in the root folder.

# Beliefstate
## Special Keywords
A beliefstate is a String of key value pairs.
There are a few reserved keywords which are not allowed to be column names
```
#domain: Select a domain
belief = "domain = restaurant"

#sortby: Sort the dataframe by a column
belief = "sortby = rating"

#entity_name: Select an entity from the current dataframe by name
belief = "entity_name = Hatori"

#entity_index: Select an entity from the current dataframe by index
belief = "entity_index = 0"

#head: Select only the first n entries from the df
belief = "head = 2"
```
## System Response
In the System response you can either reference columns of the currently selected dataframe or attributes from the currently selected entity
- Use `slot_entity_xxx` to select attribute `xxx` from the active entity
- Use `slot_df_xxx` to list all values of column `xxx` from the active dataframe
```bash
# Select an Address
system = "The address of the slot_entity_name is slot_entity_address"

# Show all names in df
system = "Here are some places that fit your description slot_df_name"
```