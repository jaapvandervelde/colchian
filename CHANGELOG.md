# Changelog

## [Unreleased]

No unreleased changes pending

## [0.1.5] - 2023-04-26

### Fixed:
  - pin `jinja2` version in hopes of fixing readthedocs.io deployment issue 

## [0.1.0] - 2023-04-26

Version published for external integration, no changes.

## [0.0.9] - 2023-04-26

### Added:
  - extra documentation for wildcards

### Changed:
  - throw Colchian.ValidationError instead of SyntaxError when validation fails

### Fixed:
  - `.validated()` returns a copy with the keys in the same order as the original

## [0.0.8] - 2023-04-04

### Added:
  - `mkdocs` documentation for readthedocs.io

Note: dismissed the idea of help-text generation. Modules like `conffu` can add this on top of `colchian` as needed. 

## [0.0.7] - 2023-03-15

### Added:
  - allow non-string types as keys in type dictionaries, as long as they are hashable; allowing for casts when not strict
  - allow for keywords `keys` and `strict` to be optional in custom validation functions

### Fixed:
  - include the exact key causing a failure in error messages
  - quote exception text using backticks instead of double quotes or no quotes

## [0.0.6] - 2021-09-02

### Fixed:
  - Formatting keys would fail if an unexpected type was present as a dictionary key, or an empty string was used as a key

## [0.0.5] - 2021-09-02

### Added:
  - The Colchian class now has a class attribute `type_factories`, which is a dictionary of type to factory function for that type. It allows you to set an override function for `.validated()` to use when creating a new instance of a dictionary to return from `.validated()`. This is only required if the constructor requires parameters - the factory function will be called with the original dict and is expected to return a new, empty instance of the same dictionary class.
```python
    class MyDict(dict):
        important = True

    def my_dict_factory(x: MyDict):
        result = type(x)()
        result.important = x.important
        return result

    Colchian.type_factories[MyDict] = my_dict_factory
```
In this example, any dictionaries of type `MyDict`  returned by `Colchian.validated()` would have `.important` set to the same value as their corresponding `MyDict` in the dictionary being validated.

## [0.0.4] - 2021-09-02

### Fixed:
  - an AssertionError was not caught correctly, and has been replaced with the expected Colchian.ValidationError

## [0.0.3] - 2021-09-01

### Added
  - Key validation based on type, callable, callable with parameters in a tuple, and restricted tuples, allowing:
```python
type_dict = {
    int: str,
    is_valid_path: int,
    (contains_substr, 'xxx'): str,
    ('one', 'two', 'three'): (1, 2, 3)  # no matching, just separate restriction for key and value 
}
```

## [0.0.2] - 2021-09-01

### Fixed
  - Link to repository URL in setup
  - Errors in readme

## [0.0.1] - 2021-09-01

### Added
  - Cloned and adapted from python_package_template
  - Implemented main Colchian class
  - Validation and correction of json documents (or rather a `dict` loaded from a .json file) 
  - Unit tests for core functionality

[Unreleased]: /../../../
[0.1.5]: /../../../tags/0.1.5
[0.1.0]: /../../../tags/0.1.0
[0.0.9]: /../../../tags/0.0.9
[0.0.8]: /../../../tags/0.0.8
[0.0.7]: /../../../tags/0.0.7
[0.0.6]: /../../../tags/0.0.6
[0.0.5]: /../../../tags/0.0.5
[0.0.4]: /../../../tags/0.0.4
[0.0.3]: /../../../tags/0.0.3
[0.0.2]: /../../../tags/0.0.2
[0.0.1]: /../../../tags/0.0.1
