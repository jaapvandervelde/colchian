# Changelog

## [Unreleased]

No unreleased changes pending

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
[0.0.3]: /../../../tags/0.0.3
[0.0.2]: /../../../tags/0.0.2
[0.0.1]: /../../../tags/0.0.1
