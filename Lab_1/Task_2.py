# TODO Найдите количество книг, которое можно разместить на дискете

disk_volume_Mb = 1.44
pages_in_book = 100
lines_on_page = 50
symbols_in_line = 25
symbol_weight_b = 4

disk_volume_b = disk_volume_Mb * 1024 ** 2
book_weight_b = pages_in_book * lines_on_page * symbols_in_line * symbol_weight_b

number_of_books = int(disk_volume_b // book_weight_b)

print("Количество книг, помещающихся на дискету:", number_of_books)
