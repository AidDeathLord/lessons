class Easy:

    def go(self):
        for col_index, col in enumerate(self):
            for row_index, row in enumerate(col):
                if not row:
                    return col_index, row_index
