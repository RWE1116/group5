import streamlit as st
from PIL import Image  # 確保這行有被引入
import os
import pandas as pd  # 添加這一行來引入 pandas 套件

# 定義顯示圖片的函數
def display_image(image_path, title, description="無描述"):
    """顯示圖片及其描述，並檢查圖片是否存在"""
    if os.path.exists(image_path):
        try:
            img = Image.open(image_path)  # 使用PIL庫的Image來打開圖片
            st.image(img, caption=title, use_column_width=True)  # 使用Streamlit的image顯示圖片
            st.write(f"<h5>{description}</h5>", unsafe_allow_html=True)
            st.markdown("---")  # 分隔線
        except Exception as e:
            st.error(f"無法顯示圖片 {image_path}: {e}")
    else:
        st.error(f"找不到圖片：{image_path}")

# 設置頁面標題和樣式
st.title("實驗六: 真空抽氣性能實驗")

# 主選單
page = st.sidebar.selectbox(
    "實驗六: 真空抽氣性能實驗",
    ["實驗目的", "儀器與設備", "實驗原理", "實驗步驟", "實驗數據表格", "圖片與影片", "相關資料"]
)

# 根據選擇的頁面顯示內容
if page == "實驗目的":
    st.markdown("""
    ## 一、實驗目的
    本實驗的主要目的是
    1. 學習真空技術的基本原理、設備與操作方法。
    2. 評估真空幫浦在不同條件下的性能，包括抽真空速率和壓力變化。
    3. 探討真空系統的漏氣檢測方法。
    4. 記錄和分析實驗數據，了解不同參數對真空系統性能的影響。
    5. 為真空技術在工程應用中的實現提供基礎。
    """)
elif page == "儀器與設備":
    st.markdown("""
    ## 二、儀器與設備
    在本實驗中，我們將使用以下儀器與設備來進行實驗：
    """)
    # 儀器與描述列表，並加入編號列
    instrument_data = [
        ["自製真空系統", 1],
        ["水氣Trap", 1],
        ["計時器", 1],
        ["水盤", 1],
        ["吸水紙", "數張"],  
        ["精密天平", 1],
    ]
    df_instruments = pd.DataFrame(instrument_data, columns=["儀器名稱", "數量"])
    st.dataframe(df_instruments)

    # 插入圖片
    img_path = "Y:/a/downloads/實驗六器材1.png"
    display_image(img_path, "實驗所用儀器與設備位置圖", "實驗所用儀器與設備")

    img_path = "Y:/a/downloads/實驗六器材2.png"
    display_image(img_path, "實驗所用儀器與設備", "實驗所用儀器與設備")

elif page == "實驗原理":
    st.markdown(""" ## 三、實驗原理 
    1. 真空的概念
    真空是指系統內的壓力低於大氣壓力的狀態，分為低真空、高真空和超高真空。
    透過真空幫浦移除系統中的氣體，達到所需的真空度。
    2. 抽真空過程的基本原理
    真空幫浦利用機械或物理的方式抽除氣體，使系統壓力逐漸下降。
    在抽真空過程中，壓力隨時間呈指數下降，依賴於系統的體積、幫浦的抽氣速率以及氣體導流特性。
    3. 壓力變化模型
    抽真空過程中的壓力變化可以表示為： 
    """)
    # 添加圖片展示
    img_path = os.path.join("Y:/a/downloads", "實驗六原理.png")
    display_image(img_path, "壓力變化模型", "壓力變化模型")
    img_path = os.path.join("Y:/a/downloads", "實驗六原理1.png")
    display_image(img_path, "壓力變化模型項目解釋", "壓力變化模型項目解釋")
    st.markdown(""" 
    4. 漏氣檢測
    真空系統中可能存在微小漏氣，影響真空性能。
    使用壓力觀察法和酒精測試法檢測系統的密封性。
    5. 壓力測量
    壓力分為穩態壓力和暫態壓力： 
    穩態壓力：系統達到穩定時的最低壓力。
    暫態壓力：抽真空過程中壓力隨時間的變化。
    使用真空計測量不同開度下的壓力變化，分析壓力曲線。
    6. 等效氣導 (Conductance)
    系統中管路的氣體導通性影響抽氣效率，等效氣導可用公式計算，表示管路對氣體流動的限制程度。
    """)
    img_path = os.path.join("Y:/a/downloads", "實驗六原理2.png")
    display_image(img_path, "等效氣導 (Conductance)", "等效氣導 (Conductance)")

elif page == "實驗步驟":
    st.markdown("""
    ## 四、實驗步驟
    1. 真空系統組裝：
    (1)以擦拭紙沾酒精將所有O-ring及封合面清潔乾淨，並檢察有無損傷。
    (2)依照示意圖與實體圖將所有KF25接頭包括O-ring鎖緊(要對準不可太用力，避免將O-ring壓傷)，完成真空系統組裝。
    2. 簡易測漏方法：
    (1)開啟真空幫浦，並注意真空計之讀值，若壓力一直無法下降，則立刻關閉真空幫浦電源。
    3. 真空壓力量測：
    (1)將真空幫浦進氣口位置之NW25 Angle valve開度調整為1/4。
    (2)啟動真空幫浦，每5秒紀錄真空計之壓力讀數與時間，總計錄時間為10分鐘。
    """)

elif page == "實驗數據表格":
    st.subheader("真空度與時間數據展示")
    data_1_2_open = {
        "時間 (t) Valve 1/2 open [sec]": [5, 10, 15, 20, 25, 30, 35, 40],
        "真空度 (P) Valve 1/2 open [Torr]": [9.8, 8.4, 7.9, 7.4, 7.1, 6.9, 6.8, 6.7]
    }

    data_full_open = {
        "時間 (t) Valve full open [sec]": [5, 10, 15, 20, 25],
        "真空度 (P) Valve full open [Torr]": [9.9, 8.1, 7.1, 6.9, 6.8]
    }

    df_1_2_open = pd.DataFrame(data_1_2_open)
    df_full_open = pd.DataFrame(data_full_open)

    st.subheader("真空度與時間變化 (Valve 1/2 open)")
    st.dataframe(df_1_2_open)
    st.subheader("真空度與時間變化 (Valve full open)")
    st.dataframe(df_full_open)

elif page == "圖片與影片":
    st.subheader("圖片與影片展示")
    
    # 創建 3 列的版面來顯示圖片
    cols = st.columns(3)

    image_paths = [
        "Y:/a/downloads/實驗6-1.jpg", "Y:/a/downloads/實驗6-2.jpg", "Y:/a/downloads/實驗6-3.jpg",
        "Y:/a/downloads/實驗6-4.jpg", "Y:/a/downloads/實驗6-5.jpg", "Y:/a/downloads/實驗6-6.jpg"
    ]
    titles = ["實驗儀器", "壓力表 (最高數值)", "壓力表 (10秒數值)", "壓力表 (15秒數值)", "壓力表 (35秒數值)", "壓力表 (40秒數值)"]
    descriptions = ["機械幫浦啟動", "最高數值", "10秒數值", "15秒數值", "35秒數值", "40秒數值"]

    for i, (image_path, title, description) in enumerate(zip(image_paths, titles, descriptions)):
        col = cols[i % 3]  # 用取餘數的方式將圖片分配到三列
        with col:
            display_image(image_path, title, description)

    st.subheader("半開實驗影片")
    video_path = 'Y:/a/downloads/半開.mp4'
    if os.path.exists(video_path):
        st.video(video_path)
    else:
        st.error(f"找不到影片：{video_path}")

    st.subheader("全開實驗影片")
    video_path = 'Y:/a/downloads/全開.mp4'
    if os.path.exists(video_path):
        st.video(video_path)
    else:
        st.error(f"找不到影片：{video_path}")

elif page == "相關資料":
    st.subheader("相關資料下載")
    
    # 下載 PDF 文件
    try:
        with open(r"Y:/a/downloads/實驗6. 真空抽氣性能實驗.pdf", "rb") as file:
            st.download_button(
                label="下載 實驗6. 真空抽氣性能實驗.pdf",
                data=file.read(),
                file_name="實驗6. 真空抽氣性能實驗.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.error("找不到文件：Y:/a/downloads/實驗6. 真空抽氣性能實驗.pdf")

    # 下載 DOC 檔案
    try:
        with open(r"Y:/a/downloads/實驗6. 真空抽氣性能實驗.doc", "rb") as file:
            st.download_button(
                label="下載 實驗6. 真空抽氣性能實驗.doc",
                data=file.read(),
                file_name="實驗6. 真空抽氣性能實驗.doc",
                mime="application/msword"  # DOC 文件的 MIME 類型
            )
    except FileNotFoundError:
        st.error("找不到文件：Y:/a/downloads/實驗6. 真空抽氣性能實驗.doc")
    
    # 下載 STEP 檔案
    try:
        with open("Y:/a/downloads/final.stp", "rb") as file:
            st.download_button(
                label="下載 真空管.stp",  # 按鈕標籤
                data=file.read(),        # 文件內容
                file_name="final.stp",  # 文件名稱
                mime="application/stp"   # MIME 類型，STEP 文件通常使用 "application/step"
            )
    except FileNotFoundError:
        st.error("找不到文件：Y:/a/downloads/final.stp")
    
    # 下載 ZIP 文件
    try:
        with open(r"Y:/a/downloads/3D(Generator).zip", "rb") as file:
            st.download_button(
                label="下載 3D(Generator).zip",
                data=file.read(),
                file_name="3D(Generator).zip",
                mime="application/zip"  # 設置 MIME 類型為 ZIP
            )
    except FileNotFoundError:
        st.error("找不到文件：Y:/a/downloads/3D(Generator).zip")
    
    # 顯示圖片
    images = [
        (r"Y:/a/downloads/工程圖1.jpg", "真空管設計", "經過測試後考量加工預值"),
        ("Y:/a/downloads/模擬1.png", "真空管壓力", "這是V=1m/s下的實驗結果"),
        ("Y:/a/downloads/模擬2.png", "真空管流速", "這是V=1m/s下的實驗結果"),
        (r"Y:/a/downloads/模擬3.png", "真空管流量", "這是V=1m/s下的實驗結果"),
    ]
    for image_path, title, description in images:
        display_image(image_path, title, description)
    
    # 下載 Excel 文件
    try:
        with open(r"Y:/a/downloads/Vacuum Generator Design(1131225)template.xlsx", "rb") as file:
            st.download_button(
                label="下載 Vacuum Generator Design(1131225)template.xlsx",  # 按鈕標籤
                data=file.read(),            # 文件內容
                file_name="Vacuum Generator Design(1131225)template.xlsx",  # 文件名稱
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"  # MIME 類型，Excel 文件
            )
    except FileNotFoundError:
        st.error("找不到文件：Y:/a/downloads/Vacuum Generator Design(1131225)template.xlsx")
    
    # 下載 Excel 文件
    try:
        with open(r"Y:/a/downloads/實驗6.真空抽氣性能實驗.xls", "rb") as file:
            st.download_button(
                label="下載 實驗6.真空抽氣性能實驗.xls",  # 按鈕標籤
                data=file.read(),            # 文件內容
                file_name="實驗6.真空抽氣性能實驗.xls",  # 文件名稱
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"  # MIME 類型，Excel 文件
            )
    except FileNotFoundError:
        st.error("找不到文件：Y:/a/downloads/實驗6.真空抽氣性能實驗.xls")

