from json import load
from example_configuration_type import example_configuration_type, MyColchian

with open('example_configuration.json') as f:
    try:
        data = load(f)
        v_data = MyColchian.validated(data, example_configuration_type)
        print(v_data)
    except SyntaxError as e:
        print(e)
