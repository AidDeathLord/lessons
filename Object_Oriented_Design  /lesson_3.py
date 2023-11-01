class PasswordValidator():
    OPTIONS = {
        'min_len': 8,
        'contain_numbers': False,
    }

    # BEGIN (write your solution here)
    def __init__(self, password='', **options):
        self.options = PasswordValidator.OPTIONS | options
        self.password = password
        print(self.options)

    def validate(self, password):
        result = {}
        if self.options['contain_numbers']:
            if not PasswordValidator._has_number(self, password):
                result['contain_numbers'] = 'should contain at least one number'
        if self.options['min_len'] > len(password):
            result['min_len'] = 'too small'
        return result
    # END

    def _has_number(self, password):
        return any(char.isdigit() for char in password)


options = {'contain_numbers': True}
validator = PasswordValidator(**options)
errors1 = validator.validate('qwertya3sdf')
print(errors1)  # => {'min_len': 'too small'}

