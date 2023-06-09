PREFIX = """
Answer the following questions as best you can, 
You have access to the following tools.  
But every tool has a cost, so be smart and efficient. 
Aim to complete tasks in the least number of steps:
"""

FORMAT_INSTRUCTIONS = """Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, must be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question"""

SUFFIX = """Output the final answer if the latest observation can solve the original input question.

Question: {input}
{agent_scratchpad}"""


APITABLE_GET_SPACES_PROMPT = """
This tool is useful when you need to fetch all spaces the user has access to, 
find out how many spaces there are, or as an intermediary step that involv searching by spaces. 
there is no input to this tool.
"""

APITABLE_GET_NODES_PROMPT = """
This tool uses APITable's node API to help you search for datasheets, mirrors, dashboards, folders, and forms.
These are all types of nodes in APITable.
The input to this tool is a space id.
You should only respond in JSON format like this:
Output a json object that contains the following keys: space_id
"""

APITABLE_GET_FIELD_PROMPT = """
This tool helps you search for fields in a datasheet using APITable's field API.
To use this tool, input a datasheet id.
If the user query includes terms like "latest", "oldest", or a specific field name, 
please use this tool first to get the field name as field key
You should only respond in JSON format like this:
{{"datasheet_id": "dstlRNFl8L2mufwT5t"}}
Do not make up a datasheet_id if you're not sure about it, use the get_nodes tool to retrieve all available datasheet_ids.
"""

APITABLE_CREATE_FIELD_PROMPT = """
This tool helps you create fields in a existing datasheet.
To use this tool, input a space id and a datasheet id.
This tool will output a json object that contains the following keys: space_id, datasheet_id, field_data
The field_data is a json that contains the following keys: name, type, property
Different field types have different properties, the following are all field types and their properties
And if a parameter name includes `(*)`, it indicates that the item is required and must be included in property key:
1.SingleText:
defaultValue | string | Default is empty
2.Text: No field properties are available.
3.SingleSelect:
options | object arrays	| List of all available options, Default is empty
Each object in the `options` key has the following schema:
name | string | option name
4.MultiSelect: The field properties are the same as the SingleSelect.
5.Number:
defaultValue | string | Default is empty.
precision(*) | number(enum) | the precision of the number. 0 (for integers), 1 (to one decimal place), 2 (to two decimal places), 3 (to three decimal places), 4 (to four decimal places)
6.Currency:
symbol | string | Currency symbol
7.Percent:
precision(*) | number(enum) | the precision of the number. 0 (for integers), 1 (to one decimal place), 2 (to two decimal places), 3 (to three decimal places), 4 (to four decimal places)
8.DateTime:
dateFormat | string(enum) | `YYYY-MM-DD` `YYYY-MM` `MM-DD` `YYYY` `MM` `DD` 
includeTime | boolean | Include time or not, default is False
timeFormat | string(enum) | `HH:mm` `hh:mm`
9.Attachment: Don't need properties
10.Member:
isMulti(*) | boolean | Is it possible to select multiple members, default is True
shouldSendMsg | boolean | Whether to send a message to members in time, default is False
11.Checkbox:
icon | string(enum) | Default is white_check_mark
12.Rating:
icon | string(enum) | Default is star
max | number | The maximum value of the rating, from 1-10, default is 5
13.URL: Don't need properties
14.Phone: Don't need properties
15.Email: Don't need properties
16.MagicLink:
foreignDatasheetId | string | Related datasheet id
limitSingleRecord | boolean | Link to multiple records, default is False
17.AutoNumber: Don't need properties
18.CreatedTime: Same as DateTime.
19.LastModifiedTime: Same as DateTime.
20.CreatedBy: Don't need properties
21.LastModifiedBy: Don't need properties
22.Formula:
expression | string | formula expression, default is empty
valueType | string(enum) | Including `String` `Boolean` `Number` `DateTime` `Array`
hasError | boolean | Default is False
"""

APITABLE_GET_RECORDS_PROMPT = """
This tool is a wrapper around APITable's record API, allowing you to retrieve specific data from a datasheet.
To use this tool, provide a datasheet ID as input, which should follow the format "dstXXXXXX".
Here are some examples of how to use this tool:
1.Find all the records in datasheet, output a json object that contains the following keys: datasheet_id
2.Find records with special condition in datasheet, output a json object that contains the following keys: datasheet_id, filter_condition
filter_condition is a json object which key is field name and value is lookup value, for example:
"filter_condition": {{"title": "test"}}
3.Find and sort records in datasheet, output a json object that contains the following keys: datasheet_id, sort_condition
sort_condition is a list of json object, each json object has two keys: field and order, field is the name of field and order has two values desc or asc, for example:
"sort_condition": [{{ "field": "Create Date", "order": "desc" }}]
4.Find records and limit the number of returned values in datasheet, output a json object that contains the following keys: datasheet_id, maxRecords_condition
maxRecords_condition is a number
"""

APITABLE_CREATE_DATASHEET_PROMPT = """
This tool helps you create a datasheet in a space.
To use this tool, input a space id and a name (maximum 10 characters) that you need to generate it automatically
This tool will output a json object that contains the following keys: space_id, datasheet_id, field_data
The field_data is a list that contains field data, each field data contains the following keys: name, type, property
Different field types have different properties, the following are all field types and their properties
And if a parameter name includes `(*)`, it indicates that the item is required and must be included in property key:
1.SingleText:
defaultValue | string | Default is empty
2.Text: No field properties are available.
3.SingleSelect:
options | object arrays	| List of all available options, Default is empty
Each object in the `options` key has the following schema:
name | string | option name
4.MultiSelect: The field properties are the same as the SingleSelect.
5.Number:
defaultValue | string | Default is empty.
precision(*) | number(enum) | the precision of the number. 0 (for integers), 1 (to one decimal place), 2 (to two decimal places), 3 (to three decimal places), 4 (to four decimal places)
6.Currency:
symbol | string | Currency symbol
7.Percent:
precision(*) | number(enum) | the precision of the number. 0 (for integers), 1 (to one decimal place), 2 (to two decimal places), 3 (to three decimal places), 4 (to four decimal places)
8.DateTime:
dateFormat | string(enum) | `YYYY-MM-DD` `YYYY-MM` `MM-DD` `YYYY` `MM` `DD` 
includeTime | boolean | Include time or not, default is False
timeFormat | string(enum) | `HH:mm` `hh:mm`
9.Attachment: Don't need properties
10.Member:
isMulti(*) | boolean | is it possible to select multiple members
shouldSendMsg | boolean | Whether to send a message to members in time, default is False
11.Checkbox:
icon | string(enum) | Default is white_check_mark
12.Rating:
icon | string(enum) | Default is star
max | number | The maximum value of the rating, from 1-10, default is 5
13.URL: Don't need properties
14.Phone: Don't need properties
15.Email: Don't need properties
16.MagicLink:
foreignDatasheetId | string | Related datasheet id
limitSingleRecord | boolean | Link to multiple records, default is False
17.AutoNumber: Don't need properties
18.CreatedTime: Same as DateTime.
19.LastModifiedTime: Same as DateTime.
20.CreatedBy: Don't need properties
21.LastModifiedBy: Don't need properties
22.Formula:
expression | string | formula expression, default is empty
valueType | string(enum) | Including `String` `Boolean` `Number` `DateTime` `Array`
hasError | boolean | Default is False
Creating a datasheet may require multiple fields, so you should put the data into a list named field_data
"""
