# It's not SQL, it's pandas but i didn't rename the folder
### How it works
- Inside the belief state you can write python code separated by semicolons
- The code will be evaluated from left to right, so if you have a variable that depends on another make sure the order is correct
- Inside the system reply you can use the variables defined in the belief state
- the variable 'df' will always be the currently selected domain dataframe
    - When a user mentions or queries a domain make sure to set the domain variable again (even if it didn't change in the dialogue)
- The variable 'row' will be the last accessed row. Also make sure to set this whenever a user aks anything so that future queries can use it

### best practice
- Try to use as many different column values as possible so that the model learns what to focus on
- You can also make up columns and domains because the model should learn the structure of the input, not memorize the column values
    - For example "what is the sheeesh of the burr" is a completely reasonable training set question
- if you're out of ideas for training dialogues just copy an existing one and reformulate it and change the order (if possible)

### Reserved names
- df = reserved for the currently selected domain data frame
- row = the row of the last accesed entity (make sure to set this variable every time a user queries for an attribute)
