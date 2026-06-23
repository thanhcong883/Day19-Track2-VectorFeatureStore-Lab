# Reflection — Lab 19

**Tên:** _Giang Thanh Công_
**Cohort:** _A20_
**Path đã chạy:** _lite_

---

## Câu hỏi (≤ 200 chữ)

- **exact**: BM25 và Hybrid đồng hạng nhất (96.7%) nhờ chứa từ khóa kỹ thuật chính xác xuất hiện verbatim trong tài liệu.
- **paraphrase**: BM25 nhỉnh hơn (33.3% vs 24.0% Semantic) do mô hình `bge-small-en-v1.5` (tiếng Anh) hiểu ngữ nghĩa tiếng Việt kém. RRF kéo Hybrid lên 32.0%. 
- **mixed**: Hybrid thắng tuyệt đối (100.0% vs 97.0% BM25 & 98.5% Semantic) nhờ dung hợp tín hiệu ngữ nghĩa và từ khóa tốt nhất.

**Khi nào KHÔNG dùng hybrid:**
- **Dùng pure BM25:** Khi tài nguyên tính toán/bộ nhớ hạn chế, yêu cầu siêu độ trễ (<5ms), hoặc tìm kiếm mã lỗi, ID, tên riêng cần chính xác 100%.
- **Dùng pure Vector:** Khi tìm kiếm ngữ nghĩa phi văn bản (ảnh, âm thanh), tìm kiếm đa ngôn ngữ (Cross-lingual), hoặc khi truy vấn hoàn toàn là văn phong tự nhiên không trùng từ khóa.

---

## Điều ngạc nhiên nhất khi làm lab này

Sự kết hợp RRF (Reciprocal Rank Fusion) cực kỳ đơn giản (chỉ vài dòng tính toán thứ hạng nghịch đảo) nhưng mang lại hiệu quả vượt trội trong việc dung hợp hai loại tín hiệu tìm kiếm khác nhau, và việc đổi sang IP `127.0.0.1` đã giải quyết triệt để lỗi kết nối IPv6 trên Windows.

---

## Bonus challenge

- [ ] Đã làm bonus (xem `bonus/`)
- [ ] Pair work với: _N/A_
