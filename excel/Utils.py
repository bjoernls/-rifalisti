

def __convert_to_num(col):
    return ord(col.lower()) - 96


def filter_cols_before_start(column, info):
    return ord(column.get_pos()) >= ord(info.get_start_write_row_col()[1])
