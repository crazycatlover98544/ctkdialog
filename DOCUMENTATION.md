# Documentation
## `yesno`
Shows a yes/no dialog.

Example: `ctkdialog.yesno('Should I Come','Should I come into this game?')`

|Options|Default Value|Keyword Argument|What It Does|
|---|---|---|---|
|title|N/A|False|Value of title for the dialog, must be a string|
|contents|N/A|False|Content of the dialog, must be a string|
|theme|`'System'`|True|Change the default CTk theme, valid options are `'System'`,`'Dark'`,`'Light'`|
|values|`['Yes','No']`/`['Yes','No','Cancel']` (add_cancel=True)|True|Change the values the buttons have, must be a length of 2 (for standard yes/no dialogs) or 3 (for yes/no/cancel dialogs); can be a list or tuple|
|add_cancel|False|True|Adds a "Cancel" button which returns none; does the same thing as _yesnocancel_.|

## `yesnocancel`
Shows a yes/no/cancel dialog. This is the same thing as passing `add_cancel=True` to yesno.

Example: `ctkdialog.yesnocancel('Save','Do you want to save this important work?')`

|Options|Default Value|Keyword Argument|What It Does|
|---|---|---|---|
|title|N/A|False|Value of title for the dialog, must be a string|
|contents|N/A|False|Content of the dialog, must be a string|
|theme|`'System'`|True|Change the default CTk theme, valid options are `'System'`,`'Dark'`,`'Light'`|
|values|`['Yes','No','Cancel']`|True|Change the values the buttons have, must be a length of 3; can be a list or tuple|

## `okay`
Shows an information dialog.

Example: `ctkdialog.okay('Alert','The danger is here!')`

|Options|Default Value|Keyword Argument|What It Does|
|---|---|---|---|
|title|N/A|False|Value of title for the dialog, must be a string|
|contents|N/A|False|Content of the dialog, must be a string|
|theme|`'System'`|True|Change the default CTk theme, valid options are `'System'`,`'Dark'`,`'Light'`|
|value|`'OK'`|True|Change the values the button has; must be a string|

## `textinput`
Shows a text input, where the user can enter a single line of text.

Example: `ctkdialog.textinput('Enter Code','Enter the 4-digit code from the game card.')`

|Options|Default Value|Keyword Argument|What It Does|
|---|---|---|---|
|title|N/A|False|Value of title for the dialog, must be a string|
|contents|N/A|False|Content of the dialog, must be a string|
|theme|`'System'`|True|Change the default CTk theme, valid options are `'System'`,`'Dark'`,`'Light'`|
|oldtext|N/A|True|Specify the text that fills the box by default|
