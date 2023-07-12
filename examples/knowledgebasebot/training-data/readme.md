# Stuttbard

## Training Data
There are two methods of creating training data. Either with a json file or a python file.
### With python File
- create a python file with any name under `./data`
```python
def main(domain_sampler, parametrize):
    # The values inside the %(col_name)s will be replaced by a sample from the options['col_name'] sampler
    templates = [
        {
        "user": "I want to eat %(cuisine)s food",
        "belief": "df = domains['restaurant'].query('cuisine == \"%(cuisine)s\"') ; names = df['name'].tolist()",
        "system": "Here are some %(cuisine)s restaurants {templates.list(names)}"
        }
    ]
    options = {
        # The first index is the domain name, the second index is the column name
        "cuisine": domain_sampler['restaurant']['cuisine']
    }
    # To beef up the training data size you can generate multiple training samples from one template
    # For example this way we will populate each template with different values twice
    number_of_repetitions = 2
    return parametrize(number_of_repetitions, options, templates)
```

## Variables
The following are variables which you can use inside of the belief states
### domains
- The `domains` is a dicttionary which holds the dataframes for the domains.
- When you change the domain make sure to set the df variable
```python
# get df of domain
df = domains['moped']

# get all domains the model can talk about
domain_keys = domains.keys()
```
### df
- The `df` variable holds the dataframe that was recently talked about
```python
# Get a row from the current dataframe by name
# Make sure to escape the " quotation marks
row = df.query('name == \"Hatori\"').iloc[0]

# Get the nth item from the current dataframe (-n for n last)
row = df.iloc[n]

# Get all unique column values
cuisines = df['cuisine'].unique()

# Get a "recommendation" aka random row
row = df.sample().iloc[0]
```
### row
- The `row` variable is the df row that was recently mentioned or accessed
- Everytime a user mentions a single row make sure to set this variable
```python
address = row['address']
```
### actions
- This is an object which has action methods that you can call
- Only ever use one action per belief state
- Make sure to call the action from the last code block in the belief state
```python
url = row['website']
actions.open_website(url)
```

# Templates
With templates you can render a variable in a specific way. Only use templates in the response string
```python
# Render as a list
system = "Sure here are some options {templates.list(res)}"
```
- templates : Render something in a specific way

