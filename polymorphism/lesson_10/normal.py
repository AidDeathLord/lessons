class Normal:
    def go(self):
        col_index = 2
        for col in self[-1::-1]:
            for row_index, row in enumerate(col):
                if not row:
                    return col_index, row_index
            col_index -= 1
