from fuzzywuzzy import fuzz

# Danh sách các bệnh viện lớn ở thành phố Hồ Chí Minh
hospitals = [
    {
        'name': 'Bệnh viện Chợ Rẫy',
        'address': '201B Nguyễn Chí Thanh, Phường 12, Quận 5, TP. Hồ Chí Minh',
        'coordinates': (10.754152, 106.665789)
    },
    {
        'name': 'Bệnh viện 115',
        'address': '527 Sư Vạn Hạnh, Phường 12, Quận 10, TP. Hồ Chí Minh',
        'coordinates': (10.762545, 106.662477)
    },
    {
        'name': 'Bệnh viện Đại học Y Dược TP. Hồ Chí Minh',
        'address': '215 Hồng Bàng, Phường 11, Quận 5, TP. Hồ Chí Minh',
        'coordinates': (10.761917, 106.661805)
    },
    {
        'name': 'Bệnh viện Nhân Dân 115',
        'address': '92 Nguyễn Tri Phương, Phường 12, Quận 10, TP. Hồ Chí Minh',
        'coordinates': (10.762285, 106.664328)
    },
    {
        'name': 'Bệnh viện Quân y 175',
        'address': '786 Nguyễn Kiệm, Phường 3, Quận Gò Vấp, TP. Hồ Chí Minh',
        'coordinates': (10.806094, 106.669748)
    },
    {
        'name': 'Bệnh viện Từ Dũ',
        'address': '284 Cống Quỳnh, Phường Phạm Ngũ Lão, Quận 1, TP. Hồ Chí Minh',
        'coordinates': (10.761236, 106.690605)
    },
    {
        'name': 'Bệnh viện FV',
        'address': '6 Nguyễn Lương Bằng, Phường Tân Phú, Quận 7, TP. Hồ Chí Minh',
        'coordinates': (10.731945, 106.742895)
    },
    {
        'name': 'Bệnh viện Răng Hàm Mặt Trung ương TP. Hồ Chí Minh',
        'address': '201 Nguyễn Chí Thanh, Phường 12, Quận 5, TP. Hồ Chí Minh',
        'coordinates': (10.753781, 106.666297)
    },
        {
        'name': 'Bệnh viện Đa khoa Sài Gòn',
        'address': '86-88 Thành Thái, Phường 12, Quận 10, TP. Hồ Chí Minh',
        'coordinates': (10.762693, 106.655073)
    },
    {
        'name': 'Bệnh viện Quốc tế Hạnh Phúc',
        'address': '18A-18B Đường số 1, Khu dân cư Vạn Phúc, TP. Hồ Chí Minh',
        'coordinates': (10.831688, 106.623947)
    },
    {
        'name': 'Bệnh viện Thống Nhất',
        'address': '1 Lý Thường Kiệt, Phường 7, Quận Tân Bình, TP. Hồ Chí Minh',
        'coordinates': (10.790386, 106.65333)
    },
    {
        'name': 'Bệnh viện Phạm Ngọc Thạch',
        'address': '120 Hồng Bàng, Phường 12, Quận 5, TP. Hồ Chí Minh',
        'coordinates': (10.758860, 106.660166)
    },
    {
        'name': 'Bệnh viện Nguyễn Tri Phương',
        'address': '468 Nguyễn Trãi, Phường 8, Quận 5, TP. Hồ Chí Minh',
        'coordinates': (10.761490, 106.661684)
    },
    {
        'name': 'Bệnh viện Đa khoa Tân Hưng',
        'address': '333 Đường 3/2, Phường 12, Quận 10, TP. Hồ Chí Minh',
        'coordinates': (10.758332, 106.664768)
    },
    {
        'name': 'Bệnh viện Đa khoa Quốc tế Vinmec Central Park',
        'address': '208 Nguyễn Hữu Cảnh, Phường 22, Quận Bình Thạnh, TP. Hồ Chí Minh',
        'coordinates': (10.788942, 106.706269)
    },
    {
        'name': 'Bệnh viện Đa khoa Sài Gòn - SGH',
        'address': '19A Đường Cộng Hòa, Phường 12, Quận Tân Bình, TP. Hồ Chí Minh',
        'coordinates': (10.802302, 106.645825)
    },
    {
        'name': 'Bệnh viện Đa khoa Mỹ Đức',
        'address': '78 Đường 3/2, Phường 12, Quận 10, TP. Hồ Chí Minh',
        'coordinates': (10.764553, 106.655526)
    },
    {
        'name': 'Bệnh viện Đa khoa Thành phố Thủ Đức',
        'address': '325 Tô Ngọc Vân, Phường Linh Đông, TP. Thủ Đức, TP. Hồ Chí Minh',
        'coordinates': (10.832911, 106.749537)
    },
        {
        'name': 'Bệnh viện Đa khoa Bình Dân',
        'address': '371 Điện Biên Phủ, Phường 4, Quận 3, TP. Hồ Chí Minh',
        'coordinates': (10.776673, 106.688981)
    },
    {
        'name': 'Bệnh viện Đa khoa Nam Sài Gòn',
        'address': '91 Nguyễn Hữu Cảnh, Phường 22, Quận Bình Thạnh, TP. Hồ Chí Minh',
        'coordinates': (10.790174, 106.704043)
    },
    {
        'name': 'Bệnh viện Đa khoa Gia Định',
        'address': '1 Nơ Trang Long, Phường 7, Quận Bình Thạnh, TP. Hồ Chí Minh',
        'coordinates': (10.796488, 106.693572)
    },
    {
        'name': 'Bệnh viện Chấn thương Chỉnh hình TP. Hồ Chí Minh',
        'address': '29 Ngô Quyền, Phường 6, Quận 10, TP. Hồ Chí Minh',
        'coordinates': (10.764921, 106.660932)
    },
    {
        'name': 'Bệnh viện Đa khoa Cần Giuộc',
        'address': '101/2A Đường 3/2, Phường 12, Quận 10, TP. Hồ Chí Minh',
        'coordinates': (10.759328, 106.666424)
    },
    {
        'name': 'Bệnh viện Y học Cổ truyền TP. Hồ Chí Minh',
        'address': '179 Cống Quỳnh, Phường Phạm Ngũ Lão, Quận 1, TP. Hồ Chí Minh',
        'coordinates': (10.760745, 106.691298)
    },
    {
        'name': 'Bệnh viện Đa khoa An Sinh',
        'address': '10 Nguyễn Gia Trí, Phường 25, Quận Bình Thạnh, TP. Hồ Chí Minh',
        'coordinates': (10.782568, 106.709122)
    },
    {
        'name': 'Bệnh viện Đa khoa Hòa Hảo',
        'address': '254 Hòa Hảo, Phường 4, Quận 10, TP. Hồ Chí Minh',
        'coordinates': (10.762034, 106.661971)
    },
    {
        'name': 'Bệnh viện Quốc tế City',
        'address': '324 Đường 15, Phường An Phú, Quận 2, TP. Hồ Chí Minh',
        'coordinates': (10.769890, 106.774342)
    },
    {
        'name': 'Bệnh viện Đa khoa Tân Tạo',
        'address': '306/7A Tân Tạo, Phường Tân Tạo A, Quận Bình Tân, TP. Hồ Chí Minh',
        'coordinates': (10.750118, 106.609928)
    },
    {
        'name': 'Bệnh viện Đa khoa Việt Đức',
        'address': '81 Lê Thánh Tôn, Phường Bến Nghé, Quận 1, TP. Hồ Chí Minh',
        'coordinates': (10.772519, 106.695376)
    }
]

def find_best_match(query):
    best_match = None
    highest_score = 0
    
    for hospital in hospitals:
        score = fuzz.ratio(query.lower(), hospital['name'].lower())
        if score > highest_score:
            highest_score = score
            best_match = hospital
            
    return best_match

