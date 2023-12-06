from passgen import generate_password
from passgen_builder import PasswordBuilder

# BEGIN (write your solution here)
class PasswordGeneratorAdapter:
    def generate_password(self, len, options):
        result = {'uppercase': False, 'digits': False, 'symbols': False}
        if 'uppercase' in options:
            result['uppercase'] = True
        if 'digits' in options:
            result['digits'] = True
        if 'symbols' in options:
            result['symbols'] = True
        return generate_password(len, **result)



# END


builder = PasswordBuilder(PasswordGeneratorAdapter())
password_info = builder.build_password(30, ['uppercase', 'digits', 'symbols'])  # noqa: E501
print(password_info)
