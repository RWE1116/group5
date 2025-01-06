import streamlit as st
import pandas as pd
from PIL import Image

# 設置頁面標題和樣式
st.title("實驗五: 溫度與散熱實驗")

# 使用側邊欄選擇不同的頁面
page = st.sidebar.selectbox(
    "選擇頁面", 
    ["實驗目的", "儀器與設備", "實驗原理", "實驗步驟", "實驗數據", "圖片與影片", "相關資料"]
)

# 定義顯示圖片的函數
def display_image(image_path, title, description):
    try:
        img = Image.open(image_path)
        st.image(img, caption=title, use_column_width=True)  # 使用Streamlit的image顯示圖片
        st.write(f"<h3 style='font-size: 20px;'>{description}</h3>", unsafe_allow_html=True)
        st.markdown("---")  # 分隔線
    except FileNotFoundError:
        st.error(f"找不到圖片：{image_path}")

# 根據選擇的頁面顯示內容
if page == "實驗目的":
    st.markdown("""
    ## 一、實驗目的
    在許多科學和工程應用中，理解熱的傳遞過程至關重要。無論是在電子設備的設計、建築節能、機械散熱，還是熱管理系統的優化中，都需要透過散熱來控制物體的溫度。因此，溫度與散熱實驗是一種基礎的熱學實驗，目的是研究不同材料或物體的散熱行為及其影響因素。

    不同電壓或電流下，加熱片所產生不同功率及光照度，觀察溫度的變化，所得到照度的數據會填入表格中，並以此得出結果。
    """)

elif page == "儀器與設備":
    st.markdown("""
    ## 二、儀器與設備
    1. T-type熱電偶線數條
    2. 水銀溫度計乙支
    3. 加熱片乙片
    4. 鋁合金散熱片乙個
    5. 導熱膏乙罐(共用)
    6. 多功能電表(FLUKE 87-5)乙台
    7. 多功能電表(FLUKE 287)乙台
    8. 直流電源供應器(Agilent U8002A)兩台
    9. 三孔延長線乙條
    10. 銲槍乙支(含銲錫及耗材、電線等)
    11. 照度計乙台
    """)

elif page == "實驗原理":
    st.markdown("""
    ## 三、實驗原理
    (這部分可以加入具體的實驗理論)
    """)

    # 顯示實驗原理圖片
    image_path = r"Y:/a/downloads/實驗五實驗原理.png"
    try:
        img = Image.open(image_path)
        st.image(img, caption="實驗五實驗原理", use_column_width=True)  # 顯示圖片
    except FileNotFoundError:
        st.error(f"找不到圖片：{image_path}")

elif page == "實驗步驟":
    st.markdown("""
    ## 四、實驗步驟
    1. 將加熱片至於盒子內，引線遷出，接至電供，調整電壓及電流(3.0V，0.01A)。
    2. 輸入後加熱片會發光，將光照測量器遮住杯口測量光照。
    3. 同時在縫隙內插入探針測量杯中溫度。
    4. 重複相同步驟，測量不同電壓急電流下的數據，總共需要三組。
    """)

elif page == "實驗數據":
    # 實驗數據表格展示
    st.subheader("LED 實驗數據表格")
    data = {
        "電壓 (V)": [3, 3.3, 3.9],
        "電流 (I) (mA)": [10, 10, 10],
        "輸入功率 (W)": [0.03, 0.033, 0.039],
        "接面溫度 (Ts) (℃)": [28.5, 28.8, 32.4],
        "基板溫度 (Tb) (℃)": [None, None, None],  # 基板溫度此處暫無數據
        "溫差 (ΔT) (℃)": [None, None, None],  # 溫差此處暫無數據
        "熱阻 (Rth) (℃/W)": [116.67, 115.15, 189.74],
        "照度 (I) (Lm)": [200, 198, 175],
        "效率 (I/W) (%)": [6.004, 6.534, 6.892]
    }

    # 創建 DataFrame
    df = pd.DataFrame(data)

    # 將缺失數據顯示為 'N/A'
    df['基板溫度 (Tb) (℃)'] = df['基板溫度 (Tb) (℃)'].fillna('N/A')
    df['溫差 (ΔT) (℃)'] = df['溫差 (ΔT) (℃)'].fillna('N/A')

    # 顯示表格
    st.dataframe(df)  # 顯示互動表格

elif page == "圖片與影片":
    st.subheader("實驗圖片與影片展示")
    
    # 圖片區域
    st.markdown("### 圖片展示")
    
    images = [
        (r"Y:/a/downloads/實驗5-1.jpg", "當電壓為3V時的結果", "第一組實驗，直流電源供應器"),
        (r"Y:/a/downloads/實驗5-2.jpg", "當電壓為3V時的結果", "第一組實驗，照度計"),
        (r"Y:/a/downloads/實驗5-3.jpg", "當電壓為3V時的結果", "第一組實驗，多功能電表(FLUKE 287)"),
        (r"Y:/a/downloads/實驗5-4.jpg", "當電壓為3.3V時的結果", "第二組實驗，直流電源供應器"),
        (r"Y:/a/downloads/實驗5-5.jpg", "當電壓為3.3V時的結果", "第二組實驗，照度計"),
        (r"Y:/a/downloads/實驗5-6.jpg", "當電壓為3.3V時的結果", "第二組實驗，多功能電表(FLUKE 287)"),
        (r"Y:/a/downloads/實驗5-7.jpg", "當電壓為3.9V時的結果", "第三組實驗，直流電源供應器"),
        (r"Y:/a/downloads/實驗5-8.jpg", "當電壓為3.9V時的結果", "第三組實驗，照度計"),
        (r"Y:/a/downloads/實驗5-9.jpg", "當電壓為3.9V時的結果", "第三組實驗，多功能電表(FLUKE 287)"),
    ]
    
    # 每行顯示3張圖片
    num_images_per_row = 3
    for i in range(0, len(images), num_images_per_row):
        # 創建三列
        cols = st.columns(num_images_per_row)
        
        # 顯示每列的圖片
        for j in range(num_images_per_row):
            if i + j < len(images):  # 防止索引超出範圍
                image_path, title, description = images[i + j]
                with cols[j]:
                    display_image(image_path, title, description)

    

        

elif page == "相關資料":
    st.subheader("相關資料下載")

    # 下載 第5組 實驗5.溫度與散熱實驗 PDF 檔案
    try:
        with open(r"Y:/a/downloads/實驗5. 溫度與散熱實驗.pdf", "rb") as file:
            st.download_button(
                label="下載 實驗5. 溫度與散熱實驗 PDF 檔案",
                data=file.read(),
                file_name="實驗5. 溫度與散熱實驗.pdf",
                mime="application/pdf"  # 設置 MIME 類型為 PDF
            )
    except FileNotFoundError:
        st.error("找不到文件：Y:/a/downloads/實驗5. 溫度與散熱實驗.pdf")

    # 下載 實驗5.溫度與散熱實驗 DOC 檔案
    try:
        with open(r"Y:/a/downloads/實驗5. 溫度與散熱實驗.doc", "rb") as file:
            st.download_button(
                label="下載 實驗5. 溫度與散熱實驗 DOC 檔案",
                data=file.read(),
                file_name="實驗5. 溫度與散熱實驗.doc",
                mime="application/msword"  # DOC 文件的 MIME 類型
            )
    except FileNotFoundError:
        st.error("找不到文件：Y:/a/downloads/實驗5. 溫度與散熱實驗.doc")


