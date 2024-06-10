## Documentation
Each module should contain a manifest file, with the following structure:

- `name`:   
  - data_type: String  
  - description: Unique and concise name for the module  
- `author`:  
  - data_type: String  
  - description: The name of the individual or company that developed the module  
- `version`:  
  - data_type: String  
  - description: Version of the module following the standard convention (major.minor.maintenance)  
- `category`:  
  - data_type: String  
  - description: Appropriate category designation for the module such as 'Sales', 'Stock'  
- `website`:  
  - data_type: String  
  - description: The website link of the author or the module homepage  
- `depends`:  
  - data_type: List of strings  
  - description: Each string is the technical name of another module this module depends on  
- `data`:  
  - data_type: List of strings  
  - description: Specifies path to the data files of the module containing definitions of model data, views, actions, workflows, demos etc.  
- `_documentation`:  
  - data_type: Dictionary  
  - keys:  
    - `banner`:  
      - data_type: String  
      - description: The path of the banner image file  
    - `icon`:  
      - data_type: String  
      - description: The path of the icon image file  
    - `excerpt`:  
      - data_type: String  
      - description: Brief overview of the problem the module aims to solve  
    - `summary`:  
      - data_type: String  
      - description: High level summary of the functionality provided  
    - `issue`:  
      - data_type: String  
      - description: Specifies the issue addressed by the module  
    - `solution`:  
      - data_type: String  
      - description: Details how the issue is solved using the module  
    - `manual`:  
      - data_type: List of dictionaries  
      - description: Each dictionary represents steps to use the module with keys 'title', 'description', 'images'  
    - `features`:  
      - data_type: Dictionary  
      - description: Each dictionary represents a feature provided by the module  
- `license`:  
  - data_type: String  
  - description: Specifies the type of license applied - 'GPL-3', 'AGPL-3', 'LGPL-3', 'OPL-1', 'Other proprietary'  
- `installable`:  
  - data_type: Boolean  
  - description: Specifies if the module is installable, should always be 'True'  
- `images`:  
  - data_type: List of strings  
  - description: List of filepaths or URLs providing screenshots of the module’s functionality  

### Rewriting documentation with GPT-4
Here is how you can generate documentation with GPT-4 following the structure above.
1. Create a new session using the :gpt-new command, send message
2. Provide the default prompt for documentation using the :gpt-prompt-autodocs (may need to refresh if you do not see it yet), send message
3. Copy paste the content of your current manifest.py file, send message
4. GPT should send you back the proper format

For reference, this is the prompt I designed to do this:
```
I will provide you a structured data used in a manifest.py file describing an odoo module.
I need you to rephrase this data, using the instructions below and send back as a python dictionary code block we can copy paste.
I will send you the actual code to rework on my next message.

We plan to use this as base for documentation for end users who may not have much experience in the system. 
The documentation should be clear, avoid acronyms and abbreviations, and of course feel interesting.
The English level should be professional.
Make sure to replace "PO" by "Purchase Order" , "MO" by "Manufacturing Order", "SO" by "Sale Order", etc...
The output should follow the structure below, but with more user-friendly text (descriptions, explanations etc.).
You must generate the "summary" property, which is a 300 paragraph summarizing the content of the documentation, without being redundant. I will not provide this property to you.
In general, add any missing properties as per the structure below.

There are some properties for which you can absolutely NOT modify the values which are: depends, version, data.
Also, you cannot add pictures path, but you can suggest it if they are missing, as comments after your code block.

The correct structure of the manifest file is defined by the python dictionary below, all properties are mandatory, your response must respect this syntax: 
{  \n"name": "", #(str): The name of the Odoo module.  \n"author": "", #(str): The author of the module.  \n"version": "", #(str): The version number of the module.  \n"category": "", #(str): The category of the module.  \n"website": "", #(str): The website of the author or the module itself.  \n"depends": [], #(list of str): The module dependencies, i.e., other modules required for this module to work.  \n"data": [], #(list of str): List of xml, csv files to be loaded when installing/updating the module.  \n"_documentation": { # An object that contains documentation for this module.  \n"banner": "banner.jpg", #(str): The path to the banner image for this module.  \n"icon": "icon.png", #(str): The path to the icon image for this module.  \n"excerpt": "", #(str): A brief introduction or summary of the module.  \n"summary": "", #(str): A more detailed description about the module, 300 words paragraph, to be generated by GPT bot.  \n"issue": "", #(str): A description of a problem or issue that this module tries to solve.  \n"solution": "", #(str): How module solves the stated problem.  \n"manual": [ #(list of dict): An array of manual steps in dict format.  \n{  \n"title": "", #(str): The title for this manual step.  \n"description": "", #(str): The description for this manual step.  \n"images": [] #(list of str): List of images for this manual step.  \n},  \n],  \n"features": [ # Array of dicts detailing features of this module.  \n{  \n"title": "", #(str): The title for this feature.  \n"description": "", #(str): The description for this feature.  \n},  \n],  \n},  \n"license": "", # (str): The license for the module.  \n"installable": True, # (bool): True if the module can be installed.  \n"images": [], # (list of str): List of paths to images associated with this module.  \n}  \n

Are you ready ? 
```
