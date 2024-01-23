from Sanitizer import Sanitizer
from SanitizerStripTagsDecorator import SanitizerStripTagsDecorator
from Application import Application


sanitizer = Sanitizer()
print(sanitizer.sanitize('sdafsdf  '))

decorated = SanitizerStripTagsDecorator(sanitizer)
print(decorated.sanitize('<p>  dfasdfadf </p>'))
app = Application(decorated)
assert app.run('<p>text<p>') == 'text'
assert app.run('  <hr>   another text ') == 'another text'

