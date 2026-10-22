# Báo Cáo Đề Tài Bài Tập Lớn Học Máy: Online Purchase Intention Prediction

## 1. Tổng Quan Bài Toán & Bộ Dữ Liệu
* **Bài toán:** Phân loại nhị phân (Binary Classification) dự đoán hành vi mua hàng của người dùng trực tuyến (`Revenue`: True/False).
* **Nguồn dữ liệu:** UCI Machine Learning Repository / Kaggle (`Online Shoppers Purchasing Intention Dataset`).
* **Kích thước:** 12.330 phiên truy cập (sau khi lọc 125 dòng trùng còn 12.205 dòng), 17 thuộc tính đầu vào.
* **Đặc tính dữ liệu:**
  * Mất cân bằng nhãn: ~84.5% không mua (`False`), ~15.5% có mua (`True`).
  * 10 biến số liên tục (Thời lượng xem trang, `BounceRates`, `ExitRates`, `PageValues`,...).
  * 7 biến phân loại (`Month`, `VisitorType`, `Weekend`, `OperatingSystems`, `Browser`, `Region`, `TrafficType`).

---

## 2. Tiền Xử Lý Dữ Liệu
1. **Làm sạch:** Khử 125 mẫu trùng lặp, kiểm tra không có giá trị khuyết thiếu (missing values).
2. **Chuẩn hóa & Mã hóa:** Dùng `ColumnTransformer`:
   * Biến số: `StandardScaler` (Z-score normalization).
   * Biến phân loại: `OneHotEncoder(handle_unknown='ignore')`.
3. **Chiến lược xử lý mất cân bằng nhãn:** Sử dụng tham số `class_weight='balanced'` trực tiếp trong hàm mất mát cho các thuật toán hỗ trợ, kết hợp phân tầng (Stratified K-Fold) để giữ nguyên tỷ lệ nhãn khi chia tập train/test (80/20).

---

## 3. Bảng Kết Quả Đánh Giá 5 Mô Hình (Test Set)

| Mô hình | Test Accuracy | Test Precision | Test Recall | Test F1-Score | Test ROC-AUC | Test PR-AUC |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Logistic Regression** | 84.60% | 0.5050 | 0.7958 | **0.6179** | 0.9097 | 0.6627 |
| **KNN (k=7)** | 87.67% | 0.6901 | 0.3848 | **0.4941** | 0.8270 | 0.5717 |
| **Decision Tree (depth=6)** | 83.78% | 0.4892 | 0.8272 | **0.6148** | 0.9119 | 0.6673 |
| **Random Forest (150 trees)** | **87.96%** | **0.5894** | **0.7592** | **0.6636** | **0.9258** | **0.7096** |
| **SVM (RBF kernel)** | 86.89% | 0.5589 | 0.7696 | **0.6476** | 0.9095 | 0.6695 |

---

## 4. Phân Tích & Kết Luận: Mô Hình Nào Phù Hợp Nhất?

### 1. Mô hình tốt nhất: **Random Forest**
* **Điểm F1-Score cao nhất (0.6636)** và **ROC-AUC vượt trội (0.9258)**, PR-AUC đạt **0.7096**.
* Cân bằng tốt nhất giữa **Precision (58.9%)** và **Recall (75.9%)**. Giúp doanh nghiệp không bỏ sót khách hàng tiềm năng mà vẫn hạn chế tối đa báo động giả (False Positives).
* Chống overfitting tốt nhờ cơ chế Bagging (Ensemble).

### 2. Đánh giá chi tiết các mô hình còn lại:
* **SVM (RBF):** Xếp thứ hai (F1: 0.6476, ROC-AUC: 0.9095). Ranh giới quyết định phi tuyến mạnh, nhưng chi phí tính toán cao và khó giải thích (black-box).
* **Logistic Regression:** Hiệu năng baseline tốt đáng ngạc nhiên (F1: 0.6179, ROC-AUC: 0.9097). Rất dễ giải thích trọng số và triển khai nhanh.
* **Decision Tree:** Recall cao nhất (82.72%) nhưng Precision thấp nhất (48.92%) do cây quyết định đơn lẻ dễ bị nhạy cảm với nhiễu.
* **KNN:** Kém nhất (F1: 0.4941). Bị ảnh hưởng nặng bởi lời nguyền số chiều (Curse of Dimensionality) sau khi One-Hot Encoding tạo ra nhiều đặc trưng thưa, đồng thời nhạy cảm với mất cân bằng nhãn.

### 3. Đóng góp của đặc trưng (Feature Importance):
* Thuộc tính quan trọng nhất: **`PageValues`** (giá trị trang web do Google Analytics tính toán) chiếm tỷ trọng vượt trội trong việc quyết định người dùng có thanh toán hay không.
* Nhóm đặc trưng tiếp theo là **`ExitRates`**, **`ProductRelated_Duration`**, và các tháng cao điểm cuối năm (`Month_Nov`).

---

## 5. Cấu Trúc Thư Mục Dự Án
```text
online-purchase-intention/
├── data/
│   └── online_shoppers_intention.csv
├── notebooks/
│   └── purchase_intention_analysis.ipynb
├── outputs/
│   ├── benchmark_results.csv
│   ├── correlation_matrix.png
│   ├── eda_overview.png
│   ├── model_comparison_bar.png
│   ├── roc_curves.png
│   ├── pr_curves.png
│   ├── confusion_matrices.png
│   └── rf_feature_importance.png
├── download_data.py
├── run_pipeline.py
├── requirements.txt
└── README.md
```
