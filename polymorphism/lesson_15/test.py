from passgen_adapter import PasswordGeneratorAdapter
from passgen_builder import PasswordBuilder
import re



builder = PasswordBuilder(PasswordGeneratorAdapter())
password_info = builder.build_password(30, ['uppercase', 'digits', 'symbols'])  # noqa: E501
print(password_info)

assert len(password_info['password']) == 30
assert re.search(r'(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).*', password_info['password'])  # noqa: E501
