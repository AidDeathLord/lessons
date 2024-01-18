class HTMLElement:
    def __init__(self):
        self.body = None

    def set_text_context(self, body):
        self.body = body

    # BEGIN (write your solution here)

    def __str__(self):
        params = type(self)._params
        if params['pair']:
            return f"<{params['name']}>{self.body}</{params['name']}>"
        return f"<{params['name']}>"
    # END

