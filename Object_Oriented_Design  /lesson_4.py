class Truncater:
    OPTIONS = {
        'separator': '...',
        'length': 200,
    }

    def __init__(self, length=200, separator='...'):
        self.options = Truncater.OPTIONS
        self.options['separator'] = separator
        self.options['length'] = length

    def truncate(self, text, **options):
        options = Truncater.OPTIONS | options
        result = ''

        if len(text) > options['length']:
            result = result + text[:options['length']] + options['separator']
        else:
            result = text
        return result


truncater = Truncater()
print(truncater.truncate('one two'))  # 'one two'
print(truncater.truncate('one two', length=6))  # 'one tw...'
print(truncater.truncate('one two', separator='.'))  # 'one two'
print(truncater.truncate('one two', length=3))  # 'one...'

truncater = Truncater(length=3)
print(truncater.truncate('one two'))  # 'one...'
print(truncater.truncate('one two', separator='!'))  # 'one!'
print(truncater.truncate('one two'))  # 'one...'
print(truncater.truncate('one two', length=7))  # 'one two'
