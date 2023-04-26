In Greek mythology, the Colchian Dragon guarded the Golden Fleece. Jason was sent on a quest to obtain the Golden Fleece, to prove himself worthy as king - but the Colchian Dragon was the final obstacle (after many others) stopping Jason from obtaining the fleece.

The `colchian` package contains the `Colchian` class, which can be used to validate .json documents, or rather the Python `dict` resulting from loading a .json file with `json.load()`.

Colchian was developed with validation of .json configurations in mind, specifically those provided by the Conffu (https://pypi.org/project/conffu/) package, but will work for any reasonably sized .json or .yaml file (no testing was performed for large documents, nor has the code been optimised for performance).

However, Colchian can be used to validate or correct any dictionary with mostly json-like structure and content. 

- define validation rules in Python code, using a simple dictionary format
- validate and correct a dictionary, returning a new dictionary with the corrections applied
- raise exceptions if the dictionary cannot be corrected, with clear information on what the error is and where it occurs
- validate keys as well as values
