training_data = [
    {"text": "xin chào", "intent": "chào"},
    {"text": "chào shop", "intent": "chào"},
    {"text": "hi bạn", "intent": "chào"},

    {"text": "tạm biệt", "intent": "tạm biệt"},
    {"text": "cảm ơn", "intent": "tạm biệt"},
    {"text": "bye", "intent": "tạm biệt"},

    {"text": "mở lúc mấy giờ?", "intent": "hỏi_giờ_làm_việc"},
    {"text": "làm việc cuối tuần?", "intent": "hỏi_giờ_làm_việc"},
    {"text": "giờ làm việc", "intent": "hỏi_giờ_làm_việc"},

    {"text": "hàng bị lỗi", "intent": "hỏi_chính_sách_đổi_trả"},
    {"text": "trả hàng", "intent": "hỏi_chính_sách_đổi_trả"},
    {"text": "hàng bị rách, nát, vỡ, dập, bung, ẩm, mốc", "intent": "hỏi_chính_sách_đổi_trả"},

    {"text": "thanh toán khi nhận", "intent": "hỏi_thanh_toán"},
    {"text": "trả bằng thẻ", "intent": "hỏi_thanh_toán"},
    {"text": "chuyển tiền trực tiếp", "intent": "hỏi_thanh_toán"},

    {"text": "bao lâu giao hàng", "intent": "hỏi_thời_gian_giao_hàng"},
    {"text": "khi nhận được hàng?", "intent": "hỏi_thời_gian_giao_hàng"},
    {"text": "hàng chưa đến vậy?", "intent": "hỏi_thời_gian_giao_hàng"},

    {"text": "đơn hàng thế nào rồi", "intent": "hỏi_trạng_thái_đơn_hàng"},
    {"text": "trạng thái đơn", "intent": "hỏi_trạng_thái_đơn_hàng"},
    {"text": "đơn hàng chưa đến ", "intent": "hỏi_trạng_thái_đơn_hàng"},

    {"text": "hủy đơn hàng", "intent": "hủy_đơn_hàng"},
    {"text": "đặt nhầm, hủy", "intent": "hủy_đơn_hàng"},
    {"text": "trả hàng", "intent": "hủy_đơn_hàng"},

    {"text": "mã giảm giá", "intent": "hỏi_khuyến_mãi"},
    {"text": "ưu đãi", "intent": "hỏi_khuyến_mãi"},
    {"text": "khuyến mãi hot", "intent": "hỏi_khuyến_mãi"},
    {"text": "chương trình giảm giá", "intent": "hỏi_khuyến_mãi"},
    {"text": "sale", "intent": "hỏi_khuyến_mãi"},

#################################
    {"text": "loại sản phẩm ", "intent": "loại_sản_phẩm"},
    {"text": "loại mặt hàng ", "intent": "loại_sản_phẩm"},
    {"text": "mặt hàng", "intent": "loại_sản_phẩm"},

################################
    {"text": "thể loại sách", "intent": "các_thể_loại_sách"},
    {"text": "bán sách thể loại", "intent": "các_thể_loại_sách"},
    {"text": "sách mấy loại", "intent": "các_thể_loại_sách"},
    {"text": "thể loại sách", "intent": "các_thể_loại_sách"},
    {"text": "loại sách", "intent": "các_thể_loại_sách"},

    {"text": "sách văn học", "intent": "sách_văn_học"},
    {"text": "sách thể loại văn học ", "intent": "sách_văn_học"},
    {"text": "loại sách văn học", "intent": "sách_văn_học"},
    {"text": "sách văn chương", "intent": "sách_văn_học"},
    {"text": "loại sách thuộc văn học", "intent": "sách_văn_học"},

    {"text": "tiểu thuyết", "intent": "thể_loại_tiểu_thuyết"},
    {"text": "đọc tiểu thuyết", "intent": "thể_loại_tiểu_thuyết"},
    {"text": "sách tiểu thuyết", "intent": "thể_loại_tiểu_thuyết"},
    {"text": "tiểu thuyết hay", "intent": "thể_loại_tiểu_thuyết"},
    {"text": "loại tiểu thuyết", "intent": "thể_loại_tiểu_thuyết"},

    {"text": "truyện ngắn", "intent": "thể_loại_truyện_ngắn"},
    {"text": "đọc truyện ngắn", "intent": "thể_loại_truyện_ngắn"},
    {"text": "loại truyện ngắn", "intent": "thể_loại_truyện_ngắn"},
    {"text": "kiểu truyện ngắn", "intent": "thể_loại_truyện_ngắn"},
    {"text": "truyện ngắn được bán", "intent": "thể_loại_truyện_ngắn"},

    {"text": "sách thơ", "intent": "thể_loại_thơ_ca"},
    {"text": "thơ ca", "intent": "thể_loại_thơ_ca"},
    {"text": "cuốn sách thơ", "intent": "thể_loại_thơ_ca"},
    {"text": "loại sách là thơ", "intent": "thể_loại_thơ_ca"},
    {"text": "tập thơ mới ", "intent": "thể_loại_thơ_ca"},

    {"text": "sách hồi ký", "intent": "thể_loại_hồi_kí_tự_truyện"},
    {"text": "tự truyện", "intent": "thể_loại_hồi_kí_tự_truyện"},
    {"text": "hồi ký nổi tiếng ", "intent": "thể_loại_hồi_kí_tự_truyện"},
    {"text": "thể loại tự truyện ", "intent": "thể_loại_hồi_kí_tự_truyện"},
    {"text": "loại sách hồi ký ", "intent": "thể_loại_hồi_kí_tự_truyện"},

    {"text": "sách kỹ năng sống ", "intent": "sách_kỹ_năng"},
    {"text": "sách kỹ năng", "intent": "sách_kỹ_năng"},
    {"text": "bán sách kỹ năng ", "intent": "sách_kỹ_năng"},
    {"text": "loại sách phát triển bản thân ", "intent": "sách_kỹ_năng"},
    {"text": "loại sách kỹ năng ", "intent": "sách_kỹ_năng"},

    {"text": "sách kỹ năng mềm ", "intent": "thể_loại_kỹ_năng_mềm"},
    {"text": "sách phát triển kỹ năng giao tiếp", "intent": "thể_loại_kỹ_năng_mềm"},
    {"text": "sách kỹ năng làm việc nhóm ", "intent": "thể_loại_kỹ_năng_mềm"},
    {"text": "sách rèn luyện kỹ năng mềm ", "intent": "thể_loại_kỹ_năng_mềm"},
    {"text": "học kỹ năng mềm qua sách", "intent": "thể_loại_kỹ_năng_mềm"},

    {"text": "sách tư duy tích cực ", "intent": "thể_loại_tư_duy_tích_cực"},
    {"text": "sách suy nghĩ tích cực", "intent": "thể_loại_tư_duy_tích_cực"},
    {"text": "sách thay đổi tư duy ", "intent": "thể_loại_tư_duy_tích_cực"},
    {"text": "loại sách tư duy tích cực ", "intent": "thể_loại_tư_duy_tích_cực"},
    {"text": "cải thiện suy nghĩ tích cực qua sách", "intent": "thể_loại_tư_duy_tích_cực"},

    {"text": "sách khởi nghiệp ", "intent": "thể_loại_khởi_nghiệp"},
    {"text": "sách khởi nghiệp kinh doanh ", "intent": "thể_loại_khởi_nghiệp"},
    {"text": "sách khởi nghiệp", "intent": "thể_loại_khởi_nghiệp"},
    {"text": "sách hướng dẫn khởi nghiệp", "intent": "thể_loại_khởi_nghiệp"},
    {"text": "loại sách khởi nghiệp ", "intent": "thể_loại_khởi_nghiệp"},


    {"text": "sách kinh tế ", "intent": "sach_kinh_te_tai_chinh"},
    {"text": "sách tài chính doanh nghiệp", "intent": "sach_kinh_te_tai_chinh"},
    {"text": "sách quản lý tài chính ", "intent": "sach_kinh_te_tai_chinh"},    
    {"text": "sách kiến thức kinh tế", "intent": "sach_kinh_te_tai_chinh"},
    {"text": "tựa sách tài chính", "intent": "sach_kinh_te_tai_chinh"},


    {"text": "sách quản trị kinh doanh ", "intent": "sach_quan_tri_kinh_doanh"},
    {"text": "sách quản lý doanh nghiệp", "intent": "sach_quan_tri_kinh_doanh"},
    {"text": "sách quản trị công ty", "intent": "sach_quan_tri_kinh_doanh"},
    {"text": "sách quản trị chiến lược ", "intent": "sach_quan_tri_kinh_doanh"},
    {"text": "loại sách quản trị", "intent": "sach_quan_tri_kinh_doanh"},

    {"text": "sách đầu tư chứng khoán ", "intent": "sach_dau_tu_chung_khoan"},
    {"text": "sách đầu tư tài chính", "intent": "sach_dau_tu_chung_khoan"},
    {"text": "sách cổ phiếu ", "intent": "sach_dau_tu_chung_khoan"},
    {"text": "sách phân tích chứng khoán ", "intent": "sach_dau_tu_chung_khoan"},
    {"text": "đầu tư qua sách", "intent": "sach_dau_tu_chung_khoan"},

    {"text": "sách marketing", "intent": "sach_marketing_ban_hang"},
    {"text": "sách bán hàng ", "intent": "sach_marketing_ban_hang"},
    {"text": "sách chạy quảng cáo ", "intent": "sach_marketing_ban_hang"},
    {"text": "sách PR truyền thông", "intent": "sach_marketing_ban_hang"},
    {"text": "loại sách bán hàng", "intent": "sach_marketing_ban_hang"},

    {"text": "giáo trình đại học", "intent": "sach_hoc_thuat_giao_trinh"},
    {"text": "sách học thuật chuyên ngành", "intent": "sach_hoc_thuat_giao_trinh"},
    {"text": "sách giáo trình ", "intent": "sach_hoc_thuat_giao_trinh"},
    {"text": "giáo trình chính quy ", "intent": "sach_hoc_thuat_giao_trinh"},
    {"text": "loại sách học thuật", "intent": "sach_hoc_thuat_giao_trinh"},

    {"text": "giáo trình toán", "intent": "sach_khoa_hoc_tu_nhien"},
    {"text": "sách học vật lý", "intent": "sach_khoa_hoc_tu_nhien"},
    {"text": "sách hóa học", "intent": "sach_khoa_hoc_tu_nhien"},
    {"text": "sách bài tập toán lý hóa ", "intent": "sach_khoa_hoc_tu_nhien"},
    {"text": "giáo trình khoa học tự nhiên ", "intent": "sach_khoa_hoc_tu_nhien"},

    {"text": "sách học lập trình", "intent": "sach_cntt_lap_trinh"},
    {"text": "Python qua sách", "intent": "sach_cntt_lap_trinh"},
    {"text": "sách trí tuệ nhân tạo", "intent": "sach_cntt_lap_trinh"},
    {"text": "sách tin học ", "intent": "sach_cntt_lap_trinh"},
    {"text": "giáo trình lập trình C++ ", "intent": "sach_cntt_lap_trinh"},

    {"text": "giáo trình y học ", "intent": "sach_y_duoc"},
    {"text": "sách dược học", "intent": "sach_y_duoc"},
    {"text": "sách giải phẫu sinh lý học ", "intent": "sach_y_duoc"},
    {"text": "sách thuốc và điều trị", "intent": "sach_y_duoc"},
    {"text": "sách y khoa chuyên ngành", "intent": "sach_y_duoc"},


    {"text": "sách thiếu nhi", "intent": "sach_thieu_nhi"},
    {"text": "truyện thiếu nhi", "intent": "sach_thieu_nhi"},
    {"text": "sách trẻ em ", "intent": "sach_thieu_nhi"},
    {"text": "truyện tranh thiếu nhi ", "intent": "sach_thieu_nhi"},
    {"text": "sách học chữ", "intent": "sach_thieu_nhi"},


    {"text": "truyện cổ tích", "intent": "truyen_co_tich"},
    {"text": "truyện cổ tích dân gian", "intent": "truyen_co_tich"},
    {"text": "truyện cổ tích", "intent": "truyen_co_tich"},
    {"text": "loại truyện cổ tích ", "intent": "truyen_co_tich"},
    {"text": "truyện cổ tích song ngữ ", "intent": "truyen_co_tich"},

    {"text": "sách tô màu", "intent": "sach_tuong_tac_thieu_nhi"},
    {"text": "sách tương tác", "intent": "sach_tuong_tac_thieu_nhi"},
    {"text": "bộ sách tập tô", "intent": "sach_tuong_tac_thieu_nhi"},
    {"text": "sách vừa đọc vừa chơi", "intent": "sach_tuong_tac_thieu_nhi"},
    {"text": "sách học chữ qua hình ảnh ", "intent": "sach_tuong_tac_thieu_nhi"},

    {"text": "truyện tranh thiếu nhi", "intent": "truyen_tranh_thieu_nhi"},
    {"text": "manga trẻ em", "intent": "truyen_tranh_thieu_nhi"},
    {"text": "truyện tranh màu", "intent": "truyen_tranh_thieu_nhi"},
    {"text": "truyện tranh thiếu nhi", "intent": "truyen_tranh_thieu_nhi"},
    {"text": "truyện tranh cho trẻ", "intent": "truyen_tranh_thieu_nhi"},


    {"text": "sách học ngoại ngữ ", "intent": "sach_ngoai_ngu"},
    {"text": "học ngoại ngữ ", "intent": "sach_ngoai_ngu"},
    {"text": "sách ngoại ngữ  ", "intent": "sach_ngoai_ngu"},
 

    {"text": "sách học tiếng Anh ", "intent": "loai_sach_ngoai_ngu"},
    {"text": "sách tiếng Nhật", "intent": "loai_sach_ngoai_ngu"},
    {"text": "sách tiếng Hàn ", "intent": "loai_sach_ngoai_ngu"},
    {"text": "giáo trình ngoại ngữ ", "intent": "loai_sach_ngoai_ngu"},
    {"text": "học tiếng Pháp qua sách", "intent": "loai_sach_ngoai_ngu"},

    {"text": "từ điển Anh Việt ", "intent": "tu_dien"},
    {"text": "từ điển tiếng Nhật", "intent": "tu_dien"},
    {"text": "từ điển song ngữ ", "intent": "tu_dien"},
    {"text": "từ điển chuyên ngành", "intent": "tu_dien"},
    {"text": "từ điển giấy ", "intent": "tu_dien"},

    {"text": "sách luyện thi TOEIC ", "intent": "ngu_phap_luyen_thi"},
    {"text": "sách học ngữ pháp tiếng Anh ", "intent": "ngu_phap_luyen_thi"},
    {"text": "ôn thi IELTS qua sách", "intent": "ngu_phap_luyen_thi"},
    {"text": "sách luyện ngữ pháp ", "intent": "ngu_phap_luyen_thi"},
    {"text": "sách luyện thi TOPIK", "intent": "ngu_phap_luyen_thi"},

#######################################

    {"text": "thể loại CD ?", "intent": "cac_the_loai_cd"},
    {"text": "loại CD nhạc", "intent": "cac_the_loai_cd"},
    {"text": "CD có nhạc?", "intent": "cac_the_loai_cd"},
    {"text": "danh sách CD", "intent": "cac_the_loai_cd"},
    {"text": "CD dòng nhạc ?", "intent": "cac_the_loai_cd"},


    {"text": "CD nhạc Pop ?", "intent": "CD_Pop_Ballad_Rock_Jazz"},
    {"text": "CD nhạc Ballad", "intent": "CD_Pop_Ballad_Rock_Jazz"},
    {"text": "CD nhạc Rock?", "intent": "CD_Pop_Ballad_Rock_Jazz"},
    {"text": "CD nhạc Jazz?", "intent": "CD_Pop_Ballad_Rock_Jazz"},
    {"text": "CD nhạc Pop/Ballad?", "intent": "CD_Pop_Ballad_Rock_Jazz"},


    {"text": "CD nhạc US-UK?", "intent": "the_loai_USUK_KPOP_VN"},
    {"text": "nhạc K-pop trên CD", "intent": "the_loai_USUK_KPOP_VN"},
    {"text": "CD nhạc Việt Nam ?", "intent": "the_loai_USUK_KPOP_VN"},
    {"text": "nhạc Hàn trên đĩa CD ?", "intent": "the_loai_USUK_KPOP_VN"},
    {"text": "CD nhạc USUK và Việt", "intent": "the_loai_USUK_KPOP_VN"},

    {"text": "CD nhạc Bolero ?", "intent": "the_loai_tru_tinh_vang_bolero"},
    {"text": "CD nhạc vàng ?", "intent": "the_loai_tru_tinh_vang_bolero"},
    {"text": "nhạc trữ tình ?", "intent": "the_loai_tru_tinh_vang_bolero"},
    {"text": "nhạc bolero", "intent": "the_loai_tru_tinh_vang_bolero"},
    {"text": "CD nhạc trữ tình", "intent": "the_loai_tru_tinh_vang_bolero"},

    {"text": "CD nhạc Indie?", "intent": "the_loai_indie_Acoustic"},
    {"text": "nhạc Acoustic CD ?", "intent": "the_loai_indie_Acoustic"},
    {"text": "CD thể loại Indie", "intent": "the_loai_indie_Acoustic"},
    {"text": "CD acoustic?", "intent": "the_loai_indie_Acoustic"},
    {"text": "nhạc indie/acoustic?", "intent": "the_loai_indie_Acoustic"},


    {"text": "CD nhạc thiếu nhi", "intent": "CD_nhac_thieu_nhi"},
    {"text": "nhạc trẻ em trên CD", "intent": "CD_nhac_thieu_nhi"},
    {"text": "CD nhạc bé ?", "intent": "CD_nhac_thieu_nhi"},
    {"text": "CD nhạc thiếu nhi học tiếng Anh", "intent": "CD_nhac_thieu_nhi"},
    {"text": "CD trẻ em ?", "intent": "CD_nhac_thieu_nhi"},

    {"text": "CD nhạc học tập vui nhộn ?", "intent": "the_loai_nhac_vui_hoc_tap"},
    {"text": "CD nhạc vui học bài", "intent": "the_loai_nhac_vui_hoc_tap"},
    {"text": "Nhạc học tập thiếu nhi ?", "intent": "the_loai_nhac_vui_hoc_tap"},
    {"text": "CD nhạc học tập vui tươi ?", "intent": "the_loai_nhac_vui_hoc_tap"},
    {"text": "nhạc hỗ trợ học tập", "intent": "the_loai_nhac_vui_hoc_tap"},


    {"text": "CD bài hát tiếng Anh cho trẻ?", "intent": "the_loai_bai_hat_tieng_anh_cho_tre"},
    {"text": "nhạc tiếng Anh cho bé học hát", "intent": "the_loai_bai_hat_tieng_anh_cho_tre"},
    {"text": "CD nhạc trẻ em tiếng Anh ?", "intent": "the_loai_bai_hat_tieng_anh_cho_tre"},
    {"text": "nhạc tiếng Anh CD ?", "intent": "the_loai_bai_hat_tieng_anh_cho_tre"},
    {"text": "đĩa nhạc tiếng Anh cho trẻ?", "intent": "the_loai_bai_hat_tieng_anh_cho_tre"},


    {"text": "CD luyện nghe tiếng Anh ?", "intent": "CD_hoc_ngoai_ngu"},
    {"text": "CD học ngoại ngữ", "intent": "CD_hoc_ngoai_ngu"},
    {"text": "CD tiếng Nhật hoặc Hàn ?", "intent": "CD_hoc_ngoai_ngu"},
    {"text": "CD học phát âm tiếng Anh ?", "intent": "CD_hoc_ngoai_ngu"},
    {"text": "CD học ngoại ngữ ?", "intent": "CD_hoc_ngoai_ngu"},


    {"text": "CD luyện nghe tiếng Anh ?", "intent": "the_loai_luyen_nghe_tieng_Anh"},
    {"text": "tài liệu nghe tiếng Anh có CD", "intent": "the_loai_luyen_nghe_tieng_Anh"},
    {"text": "đĩa luyện nghe Anh văn ?", "intent": "the_loai_luyen_nghe_tieng_Anh"},
    {"text": "CD giúp luyện nghe tiếng Anh ?", "intent": "the_loai_luyen_nghe_tieng_Anh"},
    {"text": "CD luyện nghe trình độ tiếng Anh ?", "intent": "the_loai_luyen_nghe_tieng_Anh"},


    {"text": "CD phát âm tiếng Anh ?", "intent": "the_loai_CD_phat_am"},
    {"text": "sách học phát âm kèm đĩa", "intent": "the_loai_CD_phat_am"},
    {"text": "phát âm tiếng Anh có CD ?", "intent": "the_loai_CD_phat_am"},
    {"text": "CD phát âm tiếng Anh ?", "intent": "the_loai_CD_phat_am"},
    {"text": "đĩa học phát âm tiếng Anh", "intent": "the_loai_CD_phat_am"},

#######################################

    {"text": "thể loại DVD ?", "intent": "cac_the_loai_dvd"},
    {"text": "các thể loại DVD", "intent": "cac_the_loai_dvd"},
    {"text": "danh sách thể loại DVD", "intent": "cac_the_loai_dvd"},


    {"text": "DVD phim ?", "intent": "dvd_phim_anh"},
    {"text": "DVD phim ảnh", "intent": "dvd_phim_anh"},
    {"text": "DVD phim hành động  shop?", "intent": "dvd_phim_anh"},
    {"text": "DVD phim tình cảm ?", "intent": "dvd_phim_anh"},
    {"text": "DVD phim điện ảnh ?", "intent": "dvd_phim_anh"},


    {"text": "DVD phim hành động kịch tính?", "intent": "the_loai_hanh_dong"},
    {"text": "phim hành động DVD ?", "intent": "the_loai_hanh_dong"},
    {"text": "DVD phim hành động Mỹ", "intent": "the_loai_hanh_dong"},
    {"text": "phim hành động dạng DVD", "intent": "the_loai_hanh_dong"},
    {"text": "DVD thể loại hành động", "intent": "the_loai_hanh_dong"},


    {"text": "DVD phim tình cảm", "intent": "the_loai_tinh_cam"},
    {"text": "phim lãng mạn DVD", "intent": "the_loai_tinh_cam"},
    {"text": "Phim tình cảm DVD?", "intent": "the_loai_tinh_cam"},
    {"text": "DVD thể loại tình cảm ?", "intent": "the_loai_tinh_cam"},
    {"text": "DVD phim tình yêu?", "intent": "the_loai_tinh_cam"},


    {"text": "DVD phim kinh dị hồi hộp?", "intent": "the_loai_kinh_di"},
    {"text": "phim kinh dị", "intent": "the_loai_kinh_di"},
    {"text": "DVD phim kinh dị ?", "intent": "the_loai_kinh_di"},
    {"text": "DVD thể loại kinh dị", "intent": "the_loai_kinh_di"},
    {"text": "Phim hồi hộp, rùng rợn có DVD ?", "intent": "the_loai_kinh_di"},



    {"text": "phim hoạt hình", "intent": "the_loai_phim_hoat_hinh"},
    {"text": "DVD thiếu nhi hoạt hình ?", "intent": "the_loai_phim_hoat_hinh"},
    {"text": "DVD phim hoạt hình?", "intent": "the_loai_phim_hoat_hinh"},
    {"text": "hoạt hình Disney dạng DVD", "intent": "the_loai_phim_hoat_hinh"},
    {"text": "loại DVD phim hoạt hình ?", "intent": "the_loai_phim_hoat_hinh"},


    {"text": "DVD phim tài liệu", "intent": "dvd_phim_tai_lieu"},
    {"text": "tài liệu dạng DVD", "intent": "dvd_phim_tai_lieu"},
    {"text": "DVD tài liệu khoa học?", "intent": "dvd_phim_tai_lieu"},
    {"text": "phim tài liệu dạng đĩa", "intent": "dvd_phim_tai_lieu"},
    {"text": "DVD thể loại phim tài liệu", "intent": "dvd_phim_tai_lieu"},


    {"text": "DVD phim tài liệu lịch sử ?", "intent": "the_loai_khoa_hoc_lich_su"},
    {"text": "tài liệu khoa học dạng đĩa", "intent": "the_loai_khoa_hoc_lich_su"},
    {"text": "DVD  các phát minh khoa học?", "intent": "the_loai_khoa_hoc_lich_su"},
    {"text": "Phim tài liệu chiến tranh, lịch sử có DVD ?", "intent": "the_loai_khoa_hoc_lich_su"},
    {"text": "DVD lịch sử thế giới", "intent": "the_loai_khoa_hoc_lich_su"},


    {"text": "DVD phim tài liệu  thiên nhiên?", "intent": "the_loai_tu_nhien_dong_vat"},
    {"text": "DVD  động vật hoang dã ?", "intent": "the_loai_tu_nhien_dong_vat"},
    {"text": "phim tài liệu thiên nhiên", "intent": "the_loai_tu_nhien_dong_vat"},
    {"text": "DVD thế giới động vật", "intent": "the_loai_tu_nhien_dong_vat"},
    {"text": "DVD tài liệu  rừng, đại dương", "intent": "the_loai_tu_nhien_dong_vat"},


    {"text": "DVD học liệu", "intent": "dvd_hoc_lieu"},
    {"text": "DVD học kỹ năng hoặc ngoại ngữ", "intent": "dvd_hoc_lieu"},
    {"text": "DVD học yoga, kỹ năng mềm", "intent": "dvd_hoc_lieu"},
    {"text": "tài liệu học trên DVD ?", "intent": "dvd_hoc_lieu"},
    {"text": "DVD hướng dẫn học kỹ năng ?", "intent": "dvd_hoc_lieu"},



    {"text": "DVD hướng dẫn kỹ năng mềm", "intent": "the_loai_ki_nang_mem"},
    {"text": "kỹ năng mềm qua DVD", "intent": "the_loai_ki_nang_mem"},
    {"text": "DVD khóa học kỹ năng?", "intent": "the_loai_ki_nang_mem"},
    {"text": "DVD học giao tiếp, thuyết trình", "intent": "the_loai_ki_nang_mem"},
    {"text": "đĩa kỹ năng mềm", "intent": "the_loai_ki_nang_mem"},


    {"text": "DVD dạy tiếng Anh", "intent": "the_loai_day_ngoai_ngu"},
    {"text": "ngoại ngữ qua DVD", "intent": "the_loai_day_ngoai_ngu"},
    {"text": "DVD học tiếng Nhật/Hàn", "intent": "the_loai_day_ngoai_ngu"},
    {"text": "DVD phát âm tiếng Anh", "intent": "the_loai_day_ngoai_ngu"},
    {"text": "DVD học tiếng Anh", "intent": "the_loai_day_ngoai_ngu"},



    {"text": "DVD yoga ?", "intent": "the_loai_the_thao_yoga"},
    {"text": "đĩa DVD học yoga", "intent": "the_loai_the_thao_yoga"},
    {"text": "DVD tập thể dục ?", "intent": "the_loai_the_thao_yoga"},
    {"text": "DVD thể thao?", "intent": "the_loai_the_thao_yoga"},
    {"text": "tập yoga theo DVD", "intent": "the_loai_the_thao_yoga"},


]
