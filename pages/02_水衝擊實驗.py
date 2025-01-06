import streamlit as st
import pandas as pd
from PIL import Image
import os

# 定義顯示圖片的函數
def display_image(image_path, title, description="無描述"):
    """顯示圖片及其描述，並檢查圖片是否存在"""
    # 確保圖片路徑存在
    if os.path.exists(image_path):
        try:
            img = Image.open(image_path)
            st.image(img, caption=title, use_column_width=True)  # 使用Streamlit的image顯示圖片
            st.write(f"<h5>{description}</h5>", unsafe_allow_html=True)
            st.markdown("---")  # 分隔線
        except Exception as e:
            st.error(f"無法顯示圖片 {image_path}: {e}")
    else:
        st.error(f"找不到圖片：{image_path}")

# 設置頁面標題和樣式
st.title("實驗二: 水衝擊實驗")

# 主選單
page = st.sidebar.selectbox(
    "實驗二: 水衝擊實驗",
    ["實驗目的", "儀器與設備", "實驗原理", "實驗步驟", "實驗數據表格", "圖片與影片", "相關資料"]
)

# 根據選擇的頁面顯示內容
if page == "實驗目的":
    st.markdown("""
    ## 一、實驗目的
    本實驗的主要目的是探討水流衝擊不同形狀與角度的板面時，所產生的衝擊力變化與其影響因素，並驗證理論計算值與實際量測值之間的差異。透過改變噴嘴直徑（如 8 mm 和 5 mm）、板面形狀（平面、45錐形、半圓形），測量在不同條件下水流對板面的實際衝擊力，並計算出相應的理論衝擊力。此實驗將分析水流量、速度及板面特性對衝擊力的影響，以理解水流動力學中的基本原理。最終，本實驗期望能提供在工業領域中進行水流控制和衝擊力預測的參考依據，協助優化設計並提升系統效率。瞭解流體流動時，其動量變化與其承受力量間之關係，以驗證動量方程式。
 """)
elif page == "儀器與設備":
    st.markdown(""" 
    ## 二、儀器與設備

    在本實驗中，我們將使用以下儀器與設備來進行實驗： 
    """)
    
    # 儀器與描述列表，並加入編號列
    instrument_data = [
        ["出口水壓計", "用於測量水流出口處的水壓，幫助分析水流速和衝擊力的關聯。", 1],
        ["測量流速用水箱", "用於測量水流速，確保水流符合預設的實驗條件。", 1],
        ["水量刻度表", "用來測量水流量，以便於計算衝擊力和進行實驗數據的分析。", 1],
        ["測量流速用水箱之洩放閥", "控制水箱的水流速，調節流量以便進行不同條件下的實驗。", 1],
        ["儲水槽", "存儲實驗用水，並保持水源穩定供應實驗所需水量。", 1],
        ["輪子", "用來調節實驗設備的位置，確保設備在不同實驗過程中能夠穩定運行。", 4],
        ["離心泵及馬達", "提供水流的動力，通過馬達驅動離心泵來實現穩定水流。", 1],
        ["進口閥", "控制進水流量的裝置，調節水流量以符合實驗需求。", 1],
        ["進口水壓計", "測量進水端的水壓，為後續分析提供關鍵數據。", 1],
        ["浮沉式流量計", "通過測量流體的浮沉來精確計算水流量，是一種重要的流量計量工具。", 1],
        ["機架底座", "支撐所有儀器設備，確保實驗設備在運行過程中的穩定性。", 1],
        ["馬達開關", "用於啟動或停止實驗中的馬達，控制水流的啟動與停止。", 1],
        ["馬達速度控制表錶", "用來調節馬達的速度，進而控制水流的流速。", 1],
        ["流量控制閥", "用來精確調節水流的流量，對應不同的實驗條件。", 1],
        ["水衝擊器", "直接將水流衝擊到不同形狀的板面上，用於測量衝擊力。", 1],
        ["重量平衡器(秤重)", "用來測量衝擊力造成的重力變化，進行力學分析。", 1],
        ["平衡指標", "用來監測設備運行狀態是否平衡，保證實驗準確性。", 1],
        ["重量塊", "用於校準儀器，或者模擬不同重量條件下的衝擊力測量。", 3]
    ]
    
    # 正確的 DataFrame
    df_instruments = pd.DataFrame(instrument_data, columns=["儀器名稱", "描述", "數量"])
    st.dataframe(df_instruments)
    
    # 插入圖片
    img_path = "Y:/a/downloads/實驗二器材1.png"
    display_image(img_path, "實驗所用儀器與設備")
    
    img_path = "Y:/a/downloads/實驗二器材2.jpg"
    display_image(img_path, "砝碼")

elif page == "實驗原理":
    st.markdown(""" ## 三、實驗原理 
水衝擊實驗的原理基於流體動力學中的動量守恆定律，當水流撞擊到障礙物時會產生衝擊力。此實驗透過調整噴嘴直徑、噴射角度和板面形狀，分析水流在不同條件下的衝擊力變化。根據動量定理，水流撞擊板面時會發生速度變化，這種變化會產生一個作用力，稱為衝擊力。理論上，衝擊力F 可透過公式F= 計算，其中 為水的密度Q 為流量、  為噴嘴速度。
實驗中將測量實際衝擊力並與理論值比較，以了解流速、流量和板面特性對水衝擊力的影響，驗證理論計算的準確性。
""")

    # 添加圖片展示
    img_path = os.path.join("Y:/a/downloads", "實驗二原理1.png")
    display_image(img_path, "水平噴流及圓錐噴流示意圖", "噴流的設計對受力的影響。")
    
    img_path = os.path.join("Y:/a/downloads", "實驗二原理2.png")
    display_image(img_path, "半圓噴流示意圖", "噴流的設計對受力的影響。")

    img_path = os.path.join("Y:/a/downloads", "實驗二原理3.png")
    display_image(img_path, "柏努利公式", "流體在水平射流與柏努利公式的關係。")
    img_path = os.path.join("Y:/a/downloads", "實驗二原理4.png")
    display_image(img_path, "器械工作圖", "流體在器械中運作方式。")
elif page == "實驗步驟":
    st.markdown("""
    ## 四、實驗步驟

    1. **連接電源**：將 110V 的電源接入實驗設備，確保電源正常運行。

    2. **加水至儲水槽**：將水量加入儲水槽，水量約為儲水槽的九分滿。

    3. **安裝噴嘴與硯板**：將噴嘴和硯板安裝到水衝擊器內，準備開始實驗。

    4. **調整動量平衡器**：
        - 預加上荷重約 350~450 克，使壓縮彈簧達到約 80% 的壓縮量。
        - 不要將彈簧完全壓縮，否則會產生較大的誤差。
        - 調整平衡指標，將其切口對準與平板同高。
        - 記錄試重實際重（包括容器、杯子等），這是預負荷。

    5. **啟動馬達並調節流量**：
        - 按下啟動馬達開關，開啟水流。
        - 逐漸打開流量控制閥至設定的流量。

    6. **測量水流衝擊力**：
        - 水流衝擊硯板，並將硯板推至最高點。
        - 開始加入荷重，直至平板回到原來的平衡位置。
        - 取下容杯並重新稱重，計算衝擊力，即為水對硯板的衝擊力。

    7. **重複測量**：
        - 逐步增加流量控制閥（出口閥）開啟度，改變水流量。
        - 重複第 6 步，並記錄至少五個不同流量下的數據。

    8. **關閉設備**：
        - 實驗結束後，關閉馬達並關閉流量控制閥。

    9. **更換噴嘴或硯板**：
        - 根據需要，依序更換噴嘴或硯板，並重複步驟 3~8。

    10. **清理實驗設備**：
        - 實驗結束後，關閉所有電源，將儲水槽中的水排放，並清理實驗設備。
    """)

elif page == "實驗數據表格":
    st.subheader("實驗數據表格展示")
    data = {
        "次別": [1, 1, 1, 1, 1, 1],
        "噴嘴直徑(mm)": [8, 8, 8, 5, 5, 5],
        "硯板型式": ["水平硯板", "45°圓錐形硯板", "半圓形硯板", "水平硯板", "45°圓錐形硯板", "半圓形硯板"],
        "預負荷(kgw)": [230, 230, 230, 230, 250, 230],
        "W1 (kgw)": [870, 520, 990, 820, 735, 1005],
        "W2 (kgw)": [0.64, 0.29, 0.76, 0.59, 0.485, 0.775],
        "實際測得之衝擊力 (N)": [6.27, 2.84, 7.45, 5.78, 4.75, 7.59],
        "測量水量 (L/min)": [33, 32, 26, 20, 25.5, 18],
        "實際量測流量 Q (m³/s)": [0.00055, 0.00053, 0.00043, 0.00033, 0.00043, 0.00028],
        "噴嘴速度V (m/s)": [10.9, 10.6, 8.6, 17.0, 21.6, 14.4],
        "理論衝擊力 F (N)": [6.02, 2.69, 7.47, 5.66, 4.37, 8.18],
        "誤差 (%)": [4.2, 5.8, 0.3, 2.2, 8.9, 7.1]
    }

    # 創建 DataFrame
    df = pd.DataFrame(data)

    # 顯示表格
    st.subheader("水衝擊實驗報告")
    st.write(f"水溫：26℃ 密度(ρ)：1000kg/m3")
    st.dataframe(df)

elif page == "圖片與影片":
    st.subheader("實驗圖片與影片展示")

    # 添加图片展示
    img_path = os.path.join("Y:/a/downloads", "實驗2-1.jpg")
    display_image(img_path, "重量", "8mm噴頭搭配水平硯板測量結果為870gw，測得之水量為33L/min")
    
    # 多张图片及其描述
    image_paths = [
        "Y:/a/downloads/實驗2-2.jpg", "Y:/a/downloads/實驗2-3.jpg", "Y:/a/downloads/實驗2-4.jpg", "Y:/a/downloads/實驗2-5.jpg","Y:/a/downloads/實驗2-6.jpg", "Y:/a/downloads/實驗2-7.jpg","Y:/a/downloads/實驗2-8.jpg", "Y:/a/downloads/實驗2-9.jpg"
    ]
    titles = ["重量", "水量","重量", "水量","重量","重量","重量", "水量"]
    descriptions = ["8mm噴頭搭配45度硯板測量結果為735gw，測得之水量為32L/min", "8mm噴頭搭配45度硯板測量結果為735gw，測得之水量為32L/min","8mm噴頭搭配半圓形硯板測量結果為1005gw，測得之水量為26L/min", "8mm噴頭搭配半圓形硯板測量結果為1005gw，測得之水量為26L/min","5mm噴頭搭配水平硯板測量結果為820gw，測得之水量為20L/min", "5mm噴頭搭配45度硯板測量結果為735gw，測得之水量為25.5L/min","5mm噴頭搭配半圓形硯板測量結果為1005gw，測得之水量為18L/min", "5mm噴頭搭配半圓形硯板測量結果為1005gw，測得之水量為18L/min"]

    # 使用二列分配图片
    cols = st.columns(2)
    for i, (image_path, title, description) in enumerate(zip(image_paths, titles, descriptions)):
        col = cols[i % 2]
        with col:
            display_image(image_path, title, description)

elif page == "相關資料":
    st.subheader("相關資料下載")
    
    # 下載 PDF 文件
    try:
        with open(r"Y:/a/downloads/實驗2. 水衝擊實驗.pdf", "rb") as file:
            st.download_button(
                label="下載 實驗2. 水衝擊實驗.pdf",
                data=file.read(),
                file_name="實驗2. 水衝擊實驗.pdf",
                mime="application/pdf"  # 設置 MIME 類型為 PDF
            )
    except FileNotFoundError:
        st.error("找不到文件：Y:/a/downloads/實驗2. 水衝擊實驗.pdf")

    # 下載 DOC 檔案
    try:
        with open(r"Y:/a/downloads/實驗2. 水衝擊實驗.doc", "rb") as file:
            st.download_button(
                label="下載 實驗2. 水衝擊實驗.doc",
                data=file.read(),
                file_name="實驗2. 水衝擊實驗.doc",
                mime="application/msword"  # DOC 文件的 MIME 類型
            )
    except FileNotFoundError:
        st.error("找不到文件：Y:/a/downloads/實驗2. 水衝擊實驗.doc")
    
    # 下載 Excel 檔案
    try:
        with open(r"Y:/a/downloads/實驗2. 水衝擊實驗.xls", "rb") as file:
            st.download_button(
                label="下載 實驗2. 水衝擊實驗.xls",  # 按鈕標籤
                data=file.read(),            # 文件內容
                file_name="實驗2. 水衝擊實驗.xls",  # 文件名稱
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"  # MIME 類型，Excel 文件
            )
    except FileNotFoundError:
        st.error("找不到文件：Y:/a/downloads/實驗2. 水衝擊實驗.xls")


