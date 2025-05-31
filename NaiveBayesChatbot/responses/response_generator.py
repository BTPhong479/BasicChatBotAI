

def generate_response(intent):
    if intent == "chào":
        return "Chào bạn! Tôi có thể giúp gì?"
    elif intent == "unknown":
        return "Tôi không hiểu bạn đang nói gì cả 😭"
    elif intent == "tạm biệt":
        return "Không có gì, rất vui khi được giúp đỡ bạn 😊"
    elif intent == "hỏi_giờ_làm_việc":
        return "Shop mình làm việc cả tuần, thời gian từ 6 giờ 30 phút đến 22 giờ."
    elif intent == "hỏi_chính_sách_đổi_trả":
        return "Dạ, nếu sản phẩm bị lỗi do nhà sản xuất hoặc hư hỏng trong quá trình vận chuyển, bạn hoàn toàn có thể đổi/trả hàng trong vòng 7 ngày kể từ khi nhận. Vui lòng liên hệ với shop để được hỗ trợ nhanh nhất ạ!"
    elif intent == "hỏi_thanh_toán":
        return "Dạ, shop hỗ trợ nhiều hình thức thanh toán như: thanh toán khi nhận hàng (COD), chuyển khoản ngân hàng, hoặc quẹt thẻ/thanh toán online tuỳ theo khu vực."
    elif intent == "hỏi_thời_gian_giao_hàng":
        return "Dạ, thời gian giao hàng thông thường từ 2-5 ngày làm việc, tuỳ địa chỉ của bạn. Trong nội thành thường giao nhanh hơn ạ."
    elif intent == "hỏi_trạng_thái_đơn_hàng":
        return "Dạ, để kiểm tra trạng thái đơn hàng, bạn vui lòng gửi giúp shop mã đơn hàng hoặc số điện thoại đặt hàng, mình sẽ kiểm tra và phản hồi ngay cho bạn ạ!"
    elif intent == "hủy_đơn_hàng":
        return "Dạ, bạn vui lòng cung cấp mã đơn hàng hoặc tên/số điện thoại đã đặt, shop sẽ hỗ trợ hủy đơn hoặc xử lý hoàn/trả hàng theo yêu cầu của bạn nhé!"
    elif intent == "hỏi_khuyến_mãi":
        return "Dạ, hiện tại shop đang có nhiều chương trình khuyến mãi hấp dẫn! Bạn có thể theo dõi ở mục Khuyến mãi/Ưu đãi trên website hoặc nhắn tin để mình tư vấn chi tiết từng chương trình nhé!"
    #######################
    elif intent == "loại_sản_phẩm":
        return "Hiện tại shop có các loại sản phẩm như sách, CD và DVD, bạn muốn biết thông tin nhiều hơn về loại nào?"
    elif intent == "các_thể_loại_sách":
        return "Hiện tại shop có các thể loại sách tiêu biểu như văn hoc, kỹ năng, kinh tế chính trị, học thuật, thiếu nhi và ngoại ngữ bạn muốn biết chi tiết hơn về loại sách nào?"
    elif intent == "sách_văn_học":
        return "Sách văn học có các thể loại chính sau: tiểu thuyết, truyện ngắn, thơ ca và hồi kí tự truyện, bạn muốn xem chi tiết thể loại nào?"
    elif intent == "thể_loại_tiểu_thuyết":
        return "Thể loại tiểu thuyết có các cuốn nổi bật như là: Nỗi buồn chiến tranh, Số đỏ, Tuổi thơ dữ dội, Cánh đồng bất tận, Nhà giả kim, để có thể xem nhiều hơn bạn hãy truy cập vào website nhé."
    elif intent == "thể_loại_truyện_ngắn":
        return "Thể loại truyện ngắn có các cuốn nổi bật như là: Chiếc thuyền ngoài xa, Lão Hạc, Vợ nhặt, Hai đứa trẻ, Con mèo dạy hải âu bay, để có thể xem nhiều hơn bạn hãy truy cập vào website nhé."
    elif intent == "thể_loại_thơ_ca":
        return "Thể loại thơ ca có các cuốn nổi bật như là: Truyện Kiều, Nhật ký trong tù, Sóng, Việt Bắc, Bếp lửa, để có thể xem nhiều hơn bạn hãy truy cập vào website nhé."
    elif intent == "thể_loại_hồi_kí_tự_truyện":
        return "Thể loại hồi kí tự truyện có các cuốn nổi bật như là: Nhật ký Đặng Thùy Trâm, Tự truyện Lê Vân - Yêu và sống, Bên thắng cuộc (Huy Đức), Đường xa nghĩ về địa cầu (Nguyên Ngọc), Hồi ký Nguyễn Hiến Lê, để có thể xem nhiều hơn bạn hãy truy cập vào website nhé."
    elif intent == "sách_kỹ_năng":
        return "Sách kỹ năng có các thể loại chính sau: kỹ năng mềm, tư duy tích cực, khởi nghiệp, bạn muốn biết chi tiết hơn về thể loại sách nào?"
    elif intent == "thể_loại_kỹ_năng_mềm":
        return "Thể loại ký năng mềm có các cuốn nổi bật như là: Đắc nhân tâm, Tôi tài giỏi bạn cũng thế, 7 thói quen để thành đạt, Khéo ăn nói sẽ có được thiên hạ, Nghệ thuật giao tiếp để thành công, để có thể xem nhiều hơn bạn hãy truy cập vào website nhé."
    elif intent == "thể_loại_tư_duy_tích_cực":
        return "Thể loại tư duy tích cưc có các cuốn nổi bật như là: Bạn đắt giá bao nhiêu?, Quẳng gánh lo đi và vui sống, Hạt giống tâm hồn, Tôi quyết định sống tích cực, Điều kỳ diệu của thái độ sống tích cực, để có thể xem nhiều hơn bạn hãy truy cập vào website nhé."
    elif intent == "thể_loại_khởi_nghiệp":
        return "Thể loại khởi nghiệp có các cuốn nổi bật như là: Khởi nghiệp tinh gọn, Quốc gia khởi nghiệp, Dạy con làm giàu tập 1, Bí mật tư duy triệu phú, Không bao giờ là thất bại! Tất cả là thử thách, để có thể xem nhiều hơn bạn hãy truy cập vào website nhé."
    elif intent == "sach_kinh_te_tai_chinh":
        return "Sách kinh tế, tài chính có các thể loại chính sau: quản trị doanh nghiệp, đầu tư chứng khoán, marketing bán hàng, bạn muốn biết chi tiết hơn về thể loại sách nào?"
    elif intent == "sach_quan_tri_kinh_doanh":
        return "Thể loại quản trị kinh doanh có các cuốn nổi bật như là: Từ tốt đến vĩ đại, Nhà lãnh đạo không chức danh, Nghĩ giàu làm giàu, Quản trị học - Harold Koontz, 21 nguyên tắc vàng của nghệ thuật lãnh đạo, để có thể xem nhiều hơn bạn hãy truy cập vào website nhé."
    elif intent == "sach_dau_tu_chung_khoan":
        return "Thể loại đầu tư chứng khoán có các cuốn nổi bật như là: Cổ phiếu thường là gì? - Philip Fisher, Nhà đầu tư thông minh - Benjamin Graham, Cha giàu cha nghèo - Robert Kiyosaki, Phân tích kỹ thuật chứng khoán - John Murphy, Đầu tư chứng khoán theo trường phái giá trị - Bruce Greenwald, để có thể xem nhiều hơn bạn hãy truy cập vào website nhé."
    elif intent == "sach_marketing_ban_hang":
        return "Thể loại marketing bán hàng có các cuốn nổi bật như là: Marketing căn bản - Philip Kotler, Chiến lược marketing - Philip Kotler, Bán hàng đỉnh cao - Brian Tracy, Nghệ thuật bán hàng chuyên nghiệp - Zig Ziglar, Marketing online hiệu quả - Dave Chaffey, để có thể xem nhiều hơn bạn hãy truy cập vào website nhé."
    elif intent == "sach_hoc_thuat_giao_trinh":
        return "Sách học thuật, giáo trình có các thể loại chính sau: khoa học tự nhiên, cntt lập trình, y dược, bạn muốn biết chi tiết hơn về thể loại sách nào?"
    elif intent == "sach_khoa_hoc_tu_nhien":
        return "Thể loại khoa học tự nhiên có các cuốn nổi bật như là: Vũ trụ học căn bản - Neil deGrasse Tyson, Đời sống và Sinh học - Carl Sagan, Khám phá thiên nhiên hoang dã - David Attenborough, Bí mật thế giới tự nhiên - Jane Goodall, Sinh học cho người mới bắt đầu - Bill Bryson, để có thể xem nhiều hơn bạn hãy truy cập vào website nhé."
    elif intent == "sach_cntt_lap_trinh":
        return "Thể loại cntt lập trình có các cuốn nổi bật như là: Lập trình Python căn bản - Lê Minh Hoàng, Học lập trình C++ - Nguyễn Văn A, Hướng dẫn Java cho người mới bắt đầu - Trần Thị Bích, Thuật toán và cấu trúc dữ liệu - Phạm Văn Cường, Lập trình web với JavaScript - Nguyễn Thị Dung, để có thể xem nhiều hơn bạn hãy truy cập vào website nhé."
    elif intent == "sach_y_duoc":
        return "Thể loại y dược có các cuốn nổi bật như là: Giáo trình Y học Đại cương - Bộ Y tế, Dược học cơ sở - Nguyễn Thị Hòa, Hướng dẫn sử dụng thuốc - Nguyễn Văn Bình, Bệnh học nội khoa - Trần Văn Tuấn, Dược lý học cơ bản - Lê Thị Hồng, để có thể xem nhiều hơn bạn hãy truy cập vào website nhé."
    elif intent == "sach_thieu_nhi":
        return "Sách thiếu nhi có các thể loại chính sau: truyện cổ tích, sách tương tác tô màu, truyện tranh thiếu nhi, bạn muốn biết chi tiết hơn về loại sách nào?"
    elif intent == "truyen_co_tich":
        return "Thể loại truyện cổ tích có các cuốn nổi bật như là: Truyện cổ tích Việt Nam (Nhiều tác giả), Tấm Cám - Nguyễn Đổng Chi, Sơn Tinh - Thủy Tinh, Sọ Dừa - Nhiều tác giả, Cây tre trăm đốt - Nhiều tác giả, để có thể xem nhiều hơn bạn hãy truy cập vào website nhé."
    elif intent == "sach_tuong_tac_thieu_nhi":
        return "Thể loại sách tương tác cho trẻ có các cuốn nổi bật như là: Sách tô màu cho bé, Sách pop-up, Sách cảm ứng (Interactive books), Sách lật mở (Lift-the-flap books), Sách học chữ qua hình ảnh, để có thể xem nhiều hơn bạn hãy truy cập vào website nhé."
    elif intent == "truyen_tranh_thieu_nhi":
        return "Thể loại truyện tranh thiếu nhi có các cuốn nổi bật như là: Doraemon, Thám tử Conan, Naruto, One Piece, Bảy Viên Ngọc Rồng (Dragon Ball), để có thể xem nhiều hơn bạn hãy truy cập vào website nhé."
    elif intent == "sach_ngoai_ngu":
        return "Sách ngoại ngữ có thể loại chính sau: sách ngôn ngữ, từ điển, sách ngữ pháp luyện thi, bạn muốn biết thêm về loại sách nào?"
    elif intent == "loai_sach_ngoai_ngu":
        return "Thể loại sách ngoại ngữ có các cuốn nổi bật như là: Sách học tiếng Anh, Sách học tiếng Nhật, Sách học tiếng Hàn, Sách học tiếng Pháp, để có thể xem nhiều hơn bạn hãy truy cập vào website nhé."
    elif intent == "tu_dien":
        return "Thể loại từ điển có các cuốn nổi bật như là: Oxford Dictionary, Cambridge Dictionary, Longman Dictionary, Collins Dictionary, Macmillan Dictionary, để có thể xem nhiều hơn bạn hãy truy cập vào website nhé."
    elif intent == "ngu_phap_luyen_thi":
        return "Thể loại ngữ pháp luyện thi có các cuốn nổi bật như là: Luyện thi TOEFL,Luyện thi IELTS,Luyện thi TOPIK, để có thể xem nhiều hơn bạn hãy truy cập vào website nhé."
    ####################################
    elif intent == "cac_the_loai_cd":
        return "Hiện tại shop có các thể loại CD tiêu biểu như: Pop-balad-rock, thiếu nhi, CD học ngoại ngữ, bạn muốn biết rõ hơn về loại nào?"
    elif intent == "CD_Pop_Ballad_Rock_Jazz":
        return "CD Pop-Ballad-Rock_Jazz có các thể loại chính như: USUK-KPOP-VN, trữ tình - bolero, Acoustic, bạn muốn biết chi tiết hơn về loiaj nào?"
    elif intent == "the_loai_USUK_KPOP_VN":
        return "Về thể loại trên shop có các CD bán chạy nhất như là: The Best of US-UK Hits, BTS - Love Yourself, BLACKPINK - The Album, Mỹ Tâm - Tâm 9, Đen Vâu - Show của Đen Live CD, để có thể xem nhiều hơn bạn hãy truy cập website nhé!"
    elif intent == "the_loai_tru_tinh_vang_bolero":
        return "Về thể loại trên shop có các CD bán chạy nhất như là: Giọng Ca Để Đời - Chế Linh, Bolero Hay Nhất - Lệ Quyên, Tình Khúc Vàng - Tuấn Vũ, Duyên Phận - Như Quỳnh, Nhạc Vàng Xưa - Hương Lan, để có thể xem nhiều hơn bạn hãy truy cập website nhé!"
    elif intent == "the_loai_indie_Acoustic":
        return "Về thể loại trên shop có các CD bán chạy nhất như là: Chân Ái - Orange & Khói, Lặng Lẽ - Thái Đinh, Vẽ - Trinh x Freaky, Có Một Ngày Buồn Như Thế - Vũ., Tình Yêu Xanh Lá - Nguyên Hà, để có thể xem nhiều hơn bạn hãy truy cập website nhé!"
    elif intent == "CD_nhac_thieu_nhi":
        return "CD nhạc thiếu nhi có các thể loại chính như: nhạc vui học tập cho bé, bài hát tiếng anh cho bé, bạn muôns biết rõ hơn về thể loại nào?"
    elif intent == "the_loai_nhac_vui_hoc_tap":
        return "Về thể loại nhạc học này shop có các CD nổi bật như: Bé Vui Đến Trường, Bảng Chữ Cái Vui Nhộn, Học Toán Cùng Âm Nhạc, Vui Học Tiếng Việt, ABC Song & Những Bài Hát Học Tập, để có thêm thông tin cho các CD trên bạn vui lòng truy cập website để tìm hiểu nhé."
    elif intent == "the_loai_bai_hat_tieng_anh_cho_tre":
        return "Về thể lọai nhạc tiếng Anh cho trẻ shop có các CD nổi bật như: Twinkle Twinkle Little Star, ABC Song, Old MacDonald Had a Farm, If You're Happy and You Know It, The Wheels on the Bus, để có thêm thông tin cho các CD trên và hơn thê thế nữa bạn vui lòng truy cập website nhé."
    elif intent == "CD_hoc_ngoai_ngu":
        return "CD về học ngoại ngữ có 2 loại chính sau: thể loại luyện nghe Tiếng Anh, và CD luyện phát âm, bạn muốn biết thêm về thê loại nào?"
    elif intent == "the_loai_luyen_nghe_tieng_Anh":
        return "Về thể loại CD luyện nghe Tiếng anh shop có các CD nổi bật như: English Listening Practice, Real English Conversations, Spotlight English, VOA Learning English, BBC Learning English Audio, để biết thêm thông tin chi tiết bạn vui lòng truy cập website nhé. "
    elif intent == "the_loai_CD_phat_am":
        return "Về thể loại CD để luyện phát âm, shop có các CD như sau: English Pronunciation in Use, Ship or Sheep, Pronunciation Workshop, Mastering the American Accent, Oxford English Pronunciation Course, để biết thêm thông tin chi tiết bạn vui lòng truy cập website nhé. "
    ############################################
    elif intent == "cac_the_loai_dvd":
        return "Hiện tại shop có các thể loại DVD chính như: phim ảnh, phim tài liệu, học liệu, bạn muốn biết rõ hơn về thể loại nào?"
    elif intent == "dvd_phim_anh":
        return "Về DVD phim ảnh có các thể loại sau: phim hành động, phim tình cảm, phim kinh dị, phim hoạt hình bạn muốn biết rõ hơn về thể loại nào?"
    elif intent == "the_loai_hanh_dong":
        return "Thể loại hành động này có các DVD được săn đón nhiều nhất như: Bẫy Rồng, Lửa Phật, Hai Phượng, Avengers: Endgame, John Wick, để có thể biết thêm chi tiết hoặc tìm các phim khác bạn vui lòng truy cập website nhé."
    elif intent == "the_loai_tinh_cam":
        return "Thể loại tình cảm này có các DVD được săn đón nhiều nhất như: Mắt Biếc, Thương Nhớ Ở Ai, Chuyện Tình Mùa Thu, The Notebook, Titanic, để có thể biết thêm chi tiết hoặc tìm các phim khác bạn vui lòng truy cập website nhé."
    elif intent == "the_loai_kinh_di":
        return "Thể loại kinh dị này có các DVD được săn đón nhiều nhất như: Conjuring, Ám Ảnh Kinh Hoàng, The Ring, Ma Trận Kinh Hoàng, The Exorcist, để có thể biết thêm chi tiết hoặc tìm các phim khác bạn vui lòng truy cập website nhé."
    elif intent == "the_loai_phim_hoat_hinh":
        return "Thể loại phim hoạt hình này có các DVD được săn đón nhiều nhất như: Frozen, Spirited Away, How to Train Your Dragon, Coco, Zootopia, để có thể biết thêm chi tiết hoặc tìm các phim khác bạn vui lòng truy cập website nhé."
    elif intent == "dvd_phim_tai_lieu":
        return "Về DVD phim tài liệu có các thể loại chính như: khoa học - lịch sử, thế giới tự nhiên - động vật bạn muốn biết thêm thông tin về laoij nào?"
    elif intent == "the_loai_khoa_hoc_lich_su":
        return "Thể loại khoa học, lịch sử này có các DVD được săn đón nhiều nhất như: The Vietnam War Documentary, The History of Ancient Egypt, World War II in Color, The Civil Rights Movement, The Story of the Roman Empire, để có thể biết thêm chi tiết hoặc tìm các phim khác bạn vui lòng truy cập website nhé."
    elif intent == "the_loai_tu_nhien_dong_vat":
        return "Thể loại về tự nhiên, động vật này có các DVD được săn đón nhiều nhất như: Planet Earth, Blue Planet, The Life of Mammals, Wild China, Ocean Wonders, để có thể biết thêm chi tiết hoặc tìm các phim khác bạn vui lòng truy cập website nhé."
    elif intent == "dvd_hoc_lieu":
        return "Về DVD học hiệu có các thể loại chính là: về kỹ năng mềm, dạy ngoại ngữ và về thể thao - yoga bạn muốn tìm hiêủ thêm về thể loại nào?"
    elif intent == "the_loai_ki_nang_mem":
        return "Thể loại kĩ năng mềm này có các DVD được bán chạy nhất như: Giao Tiếp Hiệu Quả, Kỹ Năng Lãnh Đạo, Quản Lý Thời Gian, Giải Quyết Xung Đột, Kỹ Năng Thuyết Trình, để có thể biết thêm chi tiết hoặc tìm các phim khác bạn vui lòng truy cập website nhé."
    elif intent == "the_loai_day_ngoai_ngu":
        return "Thể loại dạy học ngoại ngữ này có các DVD được bán chạy nhất như: Tiếng Anh Giao Tiếp Cơ Bản, Luyện Phát Âm Tiếng Anh, Tiếng Nhật Sơ Cấp, Tiếng Hàn Căn Bản, Tiếng Trung Thực Hành, để có thể biết thêm chi tiết hoặc tìm các phim khác bạn vui lòng truy cập website nhé."
    elif intent == "the_loai_the_thao_yoga":
        return "Thể loại thể thao này có các DVD được bán chạy nhất như: Tập gym cho người mới, Hướng dẫn bóng đá cơ bản, Kỹ thuật bơi lội nâng cao,Yoga thư giãn, Tập luyện thể thao tại nhà, để có thể biết thêm chi tiết hoặc tìm các phim khác bạn vui lòng truy cập website nhé."   
    else:
        return "HuHu, hiện tại câu hỏi về phạm trù của bạn tôi chưa được huấn luyện rất xin lỗi bạn 😊"
    

    