import re

def filter_snake_case(camel_case_string):
  name = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', camel_case_string)
  return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', camel_case_string).lower()

class FilterModule(object):
    def filters(self):
      return {'snake_case': filter_snake_case}