---
marp: true
theme: default
size: 16:9
paginate: true
header: "Dự Đoán Ý Định Mua Hàng Trực Tuyến | Bài Tập Lớn Học Máy"
footer: "Khoa Khoa học Máy tính • Trường Đại học Phenikaa"
style: |
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');
  section {
    font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
    padding: 40px 60px;
    background: #fafaf9;
    color: #1c1917;
    font-size: 18px;
    line-height: 1.5;
  }
  h1 {
    font-size: 36px;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -0.02em;
    margin-bottom: 8px;
  }
  h2 {
    font-size: 28px;
    font-weight: 700;
    color: #1e293b;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 8px;
    margin-bottom: 18px;
  }
  h3 {
    font-size: 20px;
    font-weight: 600;
    color: #0369a1;
    margin-bottom: 6px;
  }
  .tag {
    display: inline-block;
    padding: 3px 10px;
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-radius: 999px;
    background: #e0f2fe;
    color: #0369a1;
    margin-bottom: 12px;
  }
  .split {
    display: grid;
    grid-template-columns: 1fr 1.25fr;
    gap: 36px;
    align-items: start;
  }
  .split-even {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 28px;
    align-items: start;
  }
  .stat-hero {
    border-left: 4px solid #0284c7;
    padding-left: 16px;
    margin: 14px 0;
  }
  .stat-num {
    font-size: 38px;
    font-weight: 800;
    color: #0369a1;
    line-height: 1;
  }
  .stat-desc {
    font-size: 14px;
    color: #64748b;
    margin-top: 4px;
  }
  .step-row {
    display: flex;
    gap: 14px;
    align-items: flex-start;
    margin-bottom: 14px;
  }
  .step-badge {
    min-width: 28px;
    height: 28px;
    border-radius: 50%;
    background: #0284c7;
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 13px;
    margin-top: 2px;
  }
  .step-content strong {
    color: #0f172a;
    display: block;
    font-size: 16px;
  }
  .step-content p {
    font-size: 14px;
    color: #475569;
    margin: 2px 0 0 0;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 15px;
    margin-top: 10px;
    background: #ffffff;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
  }
  th {
    background: #0f172a;
    color: #ffffff;
    padding: 10px 14px;
    text-align: left;
    font-weight: 600;
  }
  td {
    padding: 9px 14px;
    border-bottom: 1px solid #e2e8f0;
    color: #334155;
  }
  tr:last-child td {
    border-bottom: none;
  }
  .highlight-row {
    background: #f0f9ff;
    font-weight: 700;
    color: #0369a1;
  }
  .footer-clean {
    font-size: 14px;
    color: #64748b;
    border-top: 1px solid #e2e8f0;
    padding-top: 10px;
    margin-top: 14px;
  }
---

<!-- Slide 1: Trang Tiêu Đề -->
<!-- _header: "" -->
<!-- _footer: "" -->

<span class="tag">Báo Cáo Đề Tài Bài Tập Lớn Học Máy</span>

# Dự Đoán Ý Định Mua Hàng Trực Tuyến
### Đánh Giá Thực Nghiệm 5 Thuật Toán Phân Loại Có Giám Sát

<div class="stat-hero">
  <div style="font-size: 16px; color: #334155; line-height: 1.6;">
    Khai thác hành vi duyệt web, chỉ số Google Analytics và kỹ thuật cân bằng dữ liệu nhằm nhận diện khách hàng tiềm năng trước khi rời trang.
  </div>
</div>

<div style="margin-top: 44px; border-top: 1px solid #e2e8f0; padding-top: 18px; display: flex; gap: 48px;">
  <div>
    <div style="font-size: 13px; text-transform: uppercase; color: #94a3b8; font-weight: 600;">Sinh Viên Thực Hiện</div>
    <div style="font-weight: 700; color: #0f172a;">Hoàng Văn Đô (24107948)</div>
    <div style="font-weight: 700; color: #0f172a;">Phan Hoàng Nhật (24100092)</div>
  </div>
  <div>
    <div style="font-size: 13px; text-transform: uppercase; color: #94a3b8; font-weight: 600;">Đơn Vị</div>
    <div style="color: #334155;">Khoa Khoa học Máy tính</div>
    <div style="color: #64748b; font-size: 14px;">Trường Đại học Phenikaa, Hà Nội</div>
  </div>
  <div>
    <div style="font-size: 13px; text-transform: uppercase; color: #94a3b8; font-weight: 600;">Dữ Liệu & Thực Nghiệm</div>
    <div style="color: #0369a1; font-weight: 600;">UCI Online Shoppers (12.330 phiên)</div>
    <div style="color: #64748b; font-size: 14px;">Pipeline Scikit-Learn Python</div>
  </div>
</div>

---

<!-- Slide 2: Bài Toán Thực Tiễn Trong Thương Mại Điện Tử -->
## Bài Toán Tỷ Lệ Chuyển Đổi Trong E-Commerce

<div class="split">
  <div>
    <div class="stat-hero">
      <div class="stat-num">~15,5%</div>
      <div class="stat-desc">Tỷ lệ phiên phát sinh giao dịch thực tế (84,5% người dùng xem rồi rời đi)</div>
    </div>
    <p style="color: #475569; font-size: 15px; margin-top: 14px;">
      Hàng triệu lượt truy cập mỗi ngày nhưng chỉ số ít tạo ra doanh thu. Can thiệp tặng voucher bừa bãi sẽ làm xói mòn lợi nhuận; bỏ qua không hỗ trợ thì vuột mất đơn hàng giá trị cao.
    </p>
    <div style="background: #e0f2fe; border-radius: 8px; padding: 12px 16px; margin-top: 18px;">
      <strong style="color: #0369a1; font-size: 14px;">Mục tiêu cốt lõi:</strong>
      <div style="color: #0c4a6e; font-size: 14px;">Phân loại chính xác ý định thanh toán theo thời gian thực để kích hoạt can thiệp đúng người, đúng thời điểm.</div>
    </div>
  </div>

  <div>
    <div class="step-row">
      <div class="step-badge">1</div>
      <div class="step-content">
        <strong>Bẫy Độ Chính Xác (Accuracy Paradox)</strong>
        <p>Nếu mô hình đoán "không ai mua", Accuracy vẫn đạt 84,5% nhưng vô giá trị thực tiễn. Mục tiêu bắt buộc phải tối ưu F1-Score, Recall và PR-AUC.</p>
      </div>
    </div>
    <div class="step-row">
      <div class="step-badge">2</div>
      <div class="step-content">
        <strong>Không Gian Đặc Trưng Đa Dạng & Thưa</strong>
        <p>Kết hợp giữa thông số lướt web liên tục và biến định danh (trình duyệt, hệ điều hành, tháng) sinh ra không gian 68 chiều sau mã hóa One-Hot.</p>
      </div>
    </div>
    <div class="step-row">
      <div class="step-badge">3</div>
      <div class="step-content">
        <strong>Thực Nghiệm Đối Đầu 5 Thuật Toán Cốt Lõi</strong>
        <p>Hồi quy Logistic, KNN, Cây quyết định, Rừng ngẫu nhiên (Random Forest) và SVM.</p>
      </div>
    </div>
  </div>
</div>

---

<!-- Slide 3: Bản Chất Dữ Liệu & Khám Phá EDA -->
## Khám Phá & Cấu Trúc Bộ Dữ Liệu UCI

<div class="split">
  <div>
    <img src="../outputs/eda_overview.png" style="width: 100%; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);" />
    <div style="font-size: 12px; color: #64748b; text-align: center; margin-top: 6px;">
      Trái: Mất cân bằng nhãn (84,5% vs 15,5%) | Phải: Độ phân hóa cực mạnh của PageValues (thang log)
    </div>
  </div>

  <div>
    <h3 style="color: #0f172a; margin-top: 0;">12.205 Phiên Truy Cập Hợp Lệ</h3>
    <div style="font-size: 14px; color: #475569; line-height: 1.6;">
      <p><strong>10 Đặc Trưng Số (Hành vi truy cập):</strong><br/>
      • Lượt xem & thời lượng: <code>Administrative</code>, <code>Informational</code>, <code>ProductRelated</code>.<br/>
      • Chỉ số đo lường web: <code>BounceRates</code>, <code>ExitRates</code>, <code>PageValues</code>, <code>SpecialDay</code>.</p>
      <p><strong>7 Đặc Trưng Danh Mục (Ngữ cảnh phiên):</strong><br/>
      • Thiết bị & người dùng: <code>VisitorType</code>, <code>OperatingSystems</code>, <code>Browser</code>, <code>Region</code>.<br/>
      • Yếu tố thời gian & nguồn: <code>Month</code>, <code>Weekend</code>, <code>TrafficType</code>.</p>
    </div>
    <div class="stat-hero" style="border-color: #f59e0b;">
      <div style="font-size: 14px; font-weight: 700; color: #b45309;">Quy luật then chốt phát hiện qua EDA:</div>
      <div style="font-size: 13px; color: #78350f;">Giá trị PageValues gần như bằng 0 đối với người không mua và tăng vọt ở nhóm hoàn tất đơn hàng.</div>
    </div>
  </div>
</div>

---

<!-- Slide 4: Thiết Kế Pipeline Tiền Xử Lý Dữ Liệu -->
## Quy Trình Tiền Xử Lý Chống Rò Rỉ Dữ Liệu

<div class="split-even">
  <div>
    <div class="step-row">
      <div class="step-badge">A</div>
      <div class="step-content">
        <strong>Làm Sạch Dữ Liệu</strong>
        <p>Loại bỏ 125 bản ghi trùng lặp tuyệt đối. Dữ liệu sạch hoàn toàn, không chứa giá trị khuyết thiếu (missing values).</p>
      </div>
    </div>
    <div class="step-row">
      <div class="step-badge">B</div>
      <div class="step-content">
        <strong>Phân Chia Tập Dữ Liệu Phân Tầng (80/20)</strong>
        <p>9.764 mẫu huấn luyện và 2.441 mẫu kiểm thử. Bảo toàn nguyên vẹn tỷ lệ 15,5% nhãn dương tính trên cả hai tập.</p>
      </div>
    </div>
    <div class="step-row">
      <div class="step-badge">C</div>
      <div class="step-content">
        <strong>Đóng Gói Bằng ColumnTransformer</strong>
        <p>Chuẩn hóa Z-score (<code>StandardScaler</code>) cho biến số; biến đổi biến giả (<code>OneHotEncoder</code>) an toàn với nhãn mới.</p>
      </div>
    </div>
  </div>

  <div>
    <div class="step-row">
      <div class="step-badge">D</div>
      <div class="step-content">
        <strong>Cân Bằng Trọng Số Phạt Lớp (Cost-Sensitive)</strong>
        <p>Áp dụng hệ số phạt nghịch đảo tỷ lệ mẫu $w_j = \frac{N}{2 \times N_j}$ trực tiếp vào hàm mất mát. Ép thuật toán phải chú trọng lớp thiểu số.</p>
      </div>
    </div>
    <div class="step-row">
      <div class="step-badge">E</div>
      <div class="step-content">
        <strong>Kiểm Định Chéo Phân Tầng 5 Lượt (5-Fold CV)</strong>
        <p>Kiểm tra độ ổn định tham số trước khi đánh giá khách quan trên tập kiểm thử độc lập.</p>
      </div>
    </div>
  </div>
</div>

---

<!-- Slide 5: Bảng Kết Quả Đánh Giá Tổng Hợp -->
## Bảng Hiệu Năng 5 Mô Hình Trên Tập Kiểm Thử

<table>
  <thead>
    <tr>
      <th>Thuật Toán</th>
      <th>Accuracy</th>
      <th>Precision</th>
      <th>Recall</th>
      <th>F1-Score</th>
      <th>ROC-AUC</th>
      <th>PR-AUC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Hồi quy Logistic</strong></td>
      <td>84,60%</td>
      <td>0,5050</td>
      <td>0,7958</td>
      <td>0,6179</td>
      <td>0,9097</td>
      <td>0,6627</td>
    </tr>
    <tr>
      <td><strong>K Láng Giềng (KNN, k=7)</strong></td>
      <td>87,67%</td>
      <td><strong>0,6901</strong></td>
      <td>0,3848</td>
      <td>0,4941</td>
      <td>0,8270</td>
      <td>0,5717</td>
    </tr>
    <tr>
      <td><strong>Cây Quyết Định (CART, d=6)</strong></td>
      <td>83,78%</td>
      <td>0,4892</td>
      <td><strong>0,8272</strong></td>
      <td>0,6148</td>
      <td>0,9119</td>
      <td>0,6673</td>
    </tr>
    <tr class="highlight-row">
      <td><strong>★ Rừng Ngẫu Nhiên (Random Forest)</strong></td>
      <td><strong>87,96%</strong></td>
      <td>0,5894</td>
      <td>0,7592</td>
      <td><strong>0,6636</strong></td>
      <td><strong>0,9258</strong></td>
      <td><strong>0,7096</strong></td>
    </tr>
    <tr>
      <td><strong>Máy Vector Hỗ Trợ (SVM - RBF)</strong></td>
      <td>86,89%</td>
      <td>0,5589</td>
      <td>0,7696</td>
      <td>0,6476</td>
      <td>0,9095</td>
      <td>0,6695</td>
    </tr>
  </tbody>
</table>

<div class="footer-clean">
  <strong>Kết luận thực nghiệm:</strong> Random Forest áp đảo hoàn toàn ở 3 chỉ số then chốt: F1-Score (0,6636), ROC-AUC (0,9258) và PR-AUC (0,7096).
</div>

---

<!-- Slide 6: So Sánh Trực Quan Đa Chỉ Số -->
## Phân Tích Chuyên Sâu Từng Thuật Toán

<div class="split">
  <div>
    <img src="../outputs/model_comparison_bar.png" style="width: 100%; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);" />
  </div>

  <div>
    <div class="step-row">
      <div class="step-badge" style="background: #10b981;">✓</div>
      <div class="step-content">
        <strong>Random Forest: Cân Bằng Xuất Sắc Nhất</strong>
        <p>Dung hòa tối ưu giữa Recall (75,9%) và Precision (58,9%). Phù hợp nhất cho môi trường triển khai thực tế.</p>
      </div>
    </div>
    <div class="step-row">
      <div class="step-badge" style="background: #ef4444;">✗</div>
      <div class="step-content">
        <strong>KNN: Nạn Nhân Của Lời Nguyền Số Chiều</strong>
        <p>Precision cao (69,0%) nhưng Recall sụp đổ còn 38,5%. Bỏ sót hơn 61% khách mua vì khoảng cách Euclidean mất tác dụng trong không gian 68 chiều thưa.</p>
      </div>
    </div>
    <div class="step-row">
      <div class="step-badge" style="background: #3b82f6;">ℹ</div>
      <div class="step-content">
        <strong>Decision Tree: Nhạy Cảm Cao, Sai Số Lớn</strong>
        <p>Bắt trúng 82,7% khách mua nhưng Precision chỉ đạt 48,9%, gây ra lượng cảnh báo giả rất lớn.</p>
      </div>
    </div>
  </div>
</div>

---

<!-- Slide 7: Phân Tích Đường Cong ROC & Precision-Recall -->
## Khả Năng Phân Tách Lớp: ROC & PR Curves

<div class="split-even">
  <div>
    <img src="../outputs/roc_curves.png" style="width: 100%; border-radius: 8px;" />
    <div style="font-size: 13px; color: #64748b; text-align: center; margin-top: 6px;">
      <strong>Đường Cong ROC:</strong> Random Forest dẫn đầu với AUC = 0,93, theo sau sát sao là Cây quyết định và SVM.
    </div>
  </div>

  <div>
    <img src="../outputs/pr_curves.png" style="width: 100%; border-radius: 8px;" />
    <div style="font-size: 13px; color: #64748b; text-align: center; margin-top: 6px;">
      <strong>Đường Cong PR (Phản ánh mất cân bằng):</strong> Random Forest giữ vững độ chính xác vượt trội trên toàn dải phân ngưỡng (AP = 0,71).
    </div>
  </div>
</div>

---

<!-- Slide 8: Đánh Đổi Thực Tế Trên Ma Trận Nhầm Lẫn -->
## Đánh Đổi Vận Hành Qua Ma Trận Nhầm Lẫn

<div style="text-align: center;">
  <img src="../outputs/confusion_matrices.png" style="width: 95%; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);" />
</div>

<div class="split-even" style="margin-top: 18px; font-size: 14px;">
  <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 6px; padding: 10px 14px;">
    <strong style="color: #0f172a;">Decision Tree & Logistic Regression:</strong> Báo động giả cao (~250-310 ca). Thích hợp nếu ưu tiên không bỏ sót khách, nhưng tiêu tốn ngân sách ưu đãi không cần thiết.
  </div>
  <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 6px; padding: 10px 14px;">
    <strong style="color: #166534;">Random Forest:</strong> Tiết giảm cảnh báo giả xuống chỉ 202 trường hợp, đồng thời bắt trúng 290 / 382 khách mua thật. Tổng chi phí sai số kinh doanh thấp nhất.
  </div>
</div>

---

<!-- Slide 9: Giải Thích Tầm Quan Trọng Đặc Trưng -->
## Yếu Tố Nào Thực Sự Quyết Định Giao Dịch?

<div class="split">
  <div>
    <img src="../outputs/rf_feature_importance.png" style="width: 100%; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);" />
  </div>

  <div>
    <h3 style="color: #0f172a; margin-top: 0;">Giải Mã Trọng Số Phân Nhánh (Gini)</h3>
    <div class="step-row">
      <div class="step-badge" style="background: #0d9488;">1</div>
      <div class="step-content">
        <strong>PageValues (Chiếm hơn 38% tỷ trọng)</strong>
        <p>Người dùng ghé qua các trang mang giá trị quy đổi tiền tệ cao là chỉ dấu gần như chắc chắn sẽ thực hiện thanh toán.</p>
      </div>
    </div>
    <div class="step-row">
      <div class="step-badge" style="background: #0d9488;">2</div>
      <div class="step-content">
        <strong>ExitRates & BounceRates</strong>
        <p>Chỉ số tiêu cực mạnh. Tỷ lệ thoát và rời trang cao nhận diện nhóm người lướt web vãng lai, không có nhu cầu mua sắm.</p>
      </div>
    </div>
    <div class="step-row">
      <div class="step-badge" style="background: #0d9488;">3</div>
      <div class="step-content">
        <strong>Tháng 11 (Month_Nov)</strong>
        <p>Biến danh mục có thứ hạng cao nhất. Phản ánh đúng hiệu ứng mùa mua sắm Black Friday và đợt kích cầu cuối năm.</p>
      </div>
    </div>
  </div>
</div>

---

<!-- Slide 10: Kết Luận & Khuyến Nghị Ứng Dụng -->
## Tổng Kết & Định Hướng Triển Khai Thực Tế

<div class="split-even">
  <div>
    <h3 style="color: #0f172a;">Bài Học Rút Ra Từ Dự Án</h3>
    <ul style="font-size: 15px; color: #475569; line-height: 1.7; padding-left: 20px;">
      <li><strong>Mô hình tối ưu nhất:</strong> Random Forest hoàn toàn vượt trội trên dữ liệu dạng bảng clickstream (F1: 0,6636, ROC-AUC: 0,9258).</li>
      <li><strong>Họ cây ưu việt hơn mô hình khoảng cách:</strong> Cơ chế Bagging hấp thụ tốt phi tuyến và đặc trưng thưa, hoàn toàn khắc phục điểm yếu chí mạng của KNN.</li>
      <li><strong>Bắt buộc điều chỉnh trọng số lớp:</strong> Nếu không cân bằng phạt lỗi, mô hình sẽ không có giá trị phát hiện trong kinh doanh.</li>
    </ul>
  </div>

  <div>
    <h3 style="color: #0369a1;">Định Hướng Ứng Dụng Tiếp Theo</h3>
    <div class="stat-hero">
      <div style="font-size: 15px; font-weight: 700; color: #0c4a6e;">Đưa Vào Vận Hành Thực Tế:</div>
      <div style="font-size: 14px; color: #334155; margin-top: 4px;">
        Đóng gói Random Forest thành microservice suy luận luồng (độ trễ &lt; 50ms), tự động kích hoạt can thiệp khi PageValues &gt; 0.
      </div>
    </div>
    <div class="stat-hero" style="border-color: #8b5cf6;">
      <div style="font-size: 15px; font-weight: 700; color: #5b21b6;">Nâng Cấp Thuật Toán:</div>
      <div style="font-size: 14px; color: #334155; margin-top: 4px;">
        Thử nghiệm các họ Gradient Boosting nâng cao (XGBoost, LightGBM, CatBoost) kết hợp tối ưu siêu tham số Bayesian.
      </div>
    </div>
  </div>
</div>

<div style="margin-top: 36px; text-align: center; font-size: 16px; font-weight: 700; color: #0f172a;">
  Xin chân thành cảm ơn! Mời Thầy Cô và các bạn đặt câu hỏi.
</div>
