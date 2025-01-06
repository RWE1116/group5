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
            st.image(img, caption=title,use_container_width=True)  # 使用Streamlit的image顯示圖片
            st.write(f"<h5>{description}</h5>", unsafe_allow_html=True)
            st.markdown("---")  # 分隔線
        except Exception as e:
            st.error(f"無法顯示圖片 {image_path}: {e}")
    else:
        st.error(f"找不到圖片：{image_path}")

# 設置頁面標題和樣式
st.title("實驗一: 雷諾數測定")

# 主選單
page = st.sidebar.selectbox(
    "實驗一: 雷諾數測定",
    ["實驗目的", "儀器與設備", "實驗原理", "實驗步驟", "實驗數據表格", "圖片與影片", "相關資料"]
)

# 根據選擇的頁面顯示內容
if page == "實驗目的":
    st.markdown("""
    ## 一、實驗目的
本實驗的主要目的為以墨汁流入透明之壓克力管流中，觀察流體在管路中流動的情形，並配合計算出雷諾數(Re)，以膫解層流和紊流與雷諾數(Re)之間的關係。""")
elif page == "儀器與設備":
    st.markdown(""" 
    ## 二、儀器與設備
本套儀器是由一透明之壓克力製內外雙套管、機架台座、點滴液瓶、進出口閥、洩水閥及溢水 管等和管路連接而成 
    """)
    
    # 儀器與描述列表，並加入編號列
    instrument_data = [
        ["套管式測試管", "用於觀察水流", 1],
        ["點滴液瓶", "用於儲存墨水", 1],
        ["機架", "用來固定套管式測試管", 1],
        ["節流閥", "控制墨水流量", 1],
        ["內管", "實驗主要發生地", 1],
        ["墨水", "顯現水流形式", 1],

    ]
    
    # 正確的 DataFrame
    df_instruments = pd.DataFrame(instrument_data, columns=["儀器名稱", "描述", "數量"])
    st.dataframe(df_instruments)
    
    # 插入圖片
    img_path = "downloads/實驗一器材1.png"
    display_image(img_path, "器材位置尺寸圖", "器材組合位置尺寸圖")
    


elif page == "實驗原理":
    st.markdown(""" ## 三、實驗原理 
當Re<2300時，流場為層流，Re>4000時為擾流，2300<Re<4000時則為轉換區。

在研究流體力學的過程中，我們會遇到為數不少的無因次參數，如Re、Fr、Ma等， 但其中最為大家所熟知的則為Re，及雷諾數。 

如大家在研讀流力時所知，其物理意義維慣性力與黏性力之比值，式中 為密度，V為平均速度，為絕對黏度(或動力黏度) ，L為特徵長度，對一管流而言，特徵長度為直徑D，則若採國際單位(SI)系統，取 [kg/m3] ，V取 [m/s]，D為[m]，為[Ns/m2] ,則Re之單位為 
""")

    # 添加圖片展示
    img_path = os.path.join("downloads", "實驗一原理1.png")
    display_image(img_path, "雷諾數單位換算", "雷諾數單位換算")
    st.markdown(""" 
由上可知，Re為一無因次參數，亦即其值不因使用之單位系統不同而發生變化。此 參數之重要性乃在Re之大小與流體之流動情況是層流或擾流有關。當雷諾數小時，流動形態成層狀或板狀運動，在巨觀下，其相鄰各層並無混合現象。此時若將一細絲狀之染料注入其中， 可看出此染料成一條線而不致散開，此即大家所熟知的層流。現若稍微加快流速，使Re稍微家大，吾人可發現此層狀流體在管路下游 處成不穩定之擾動現象，此種上游層流，下游擾流之現象，稱為轉換區。""")
    

elif page == "實驗步驟":
    st.markdown("""
    ## 四、實驗步驟

1.墨水加水稀釋（約1：5）後裝入點滴液瓶內並裝置在儀器上端。  

2.打開進水口閥及內管出水口閥，並將進出口流量控制在穩定流動狀 態(即外管水位維持在某一固定位置不變)。 

3.將墨水之控制閥打開讓墨水穩定的滴入套筒中。 

4.觀察墨水於管路中流動的情形(層流、紊流或於臨界區域)同時用 量杯(或水筒)量取流量並 用碼錶確實測量時間(秒)將此等資料數據(流動情形、流量、測量時間)詳細計錄。 

5.改變流量(由小到大)至少取五種不同的流量，以確實觀察由層流變化到完全紊流的情形。     

6.實驗結束，將墨水關閉，洗淨針頭後置淸水桶內，以免墨汁乾化，堵塞針孔，同時開大進水閥(出口閥維持略開)讓淸水充滿套筒內部(此時有多餘的水從溢水口流出)讓其自然循環數分鐘將墨汁淸洗掉。 

7.最後再將進水閥關閉，並打開出口閥和洩水閥將水排乾。 

8.擦淨儀器本身及四周地板。

    """)

elif page == "實驗數據表格":
    st.subheader("實驗數據表格展示")

    # 顯示圖片
    img_path = os.path.join("downloads", "實驗一表格.png")
    display_image(img_path, "雷諾數計算", "雷諾數計算")

    # 實驗數據字典
    data = {
        "次別": [1, 2, 3],
        "測量時間 (sec)": [10, 10, 10],
        "測量水量 (c.c.)": [1000, 650, 200],
        "測量 Q (m³/sec)": [1.00E-04, 6.50E-05, 2.00E-05],
        "流速 V (m/sec)": [0.2041, 0.1327, 0.0408],
        "雷諾數 Re": [5102.04, 3316.33, 1020.41],
        "流動情形": ["紊流", "過渡流", "層流"],
        "與理論是否相符": ["是", "是", "是"]
    }

    # 創建 DataFrame
    df = pd.DataFrame(data)

    # 顯示報告標題與其他說明
    st.subheader("水流實驗報告")
    st.write(f"水溫：20℃，密度：1000 kg/m³，黏度係數：1×10⁻³ N-s/m³")
    st.write(f"內管直徑：25 mm = 0.025 m，截面積：{(3.14159 * 0.025**2) / 4:.5f} m²")

    # 顯示流動狀態描述
    st.write("""
    雷諾數分類:
    - Re < 2300: 層流
    - 2300 < Re < 4000: 過渡區
    - Re > 4000: 擾流
    """)

    # 顯示表格
    st.dataframe(df)

elif page == "圖片與影片":
    st.subheader("實驗圖片與影片展示")
    
    images = [
    ("downloads/實驗1-1.jpg", "墨水控制閥", "打開墨水控制閥"),
    ("downloads/實驗1-2.jpg", "量杯", "測量水量以及紀錄時間"),
    ("downloads/實驗1-3.jpg", "水閥", "控制水量"),
    ("downloads/實驗1-4.jpg", "點滴液瓶", "墨水管及控制閥"),
]

    
    for image_path, title, description in images:
        display_image(image_path, title, description)


elif page == "相關資料":
    st.subheader("相關資料下載")
    
    # 下載 PDF 文件
    try:
        with open(r"downloads/實驗1. 雷諾數實驗.pdf", "rb") as file:
            st.download_button(
                label="下載 實驗1. 雷諾數實驗.pdf",
                data=file.read(),
                file_name="實驗1. 雷諾數實驗.pdf",
                mime="application/pdf"  # 設置 MIME 類型為 PDF
            )
    except FileNotFoundError:
        st.error("找不到文件：downloads/實驗1. 雷諾數實驗.pdf")

    # 下載 DOC 檔案
    try:
        with open(r"downloads/實驗1. 雷諾數實驗.doc", "rb") as file:
            st.download_button(
                label="下載 實驗1. 雷諾數實驗.doc",
                data=file.read(),
                file_name="實驗1. 雷諾數實驗.doc",
                mime="application/msword"  # DOC 文件的 MIME 類型
            )
    except FileNotFoundError:
        st.error("找不到文件：downloads/實驗1. 雷諾數實驗.doc")
    # 下載 Excel 文件
    try:
        with open(r"downloads/實驗1. 雷諾數實驗.xlsx", "rb") as file:
            st.download_button(
                label="下載 實驗1. 雷諾數實驗.xlsx",  # 按鈕標籤
                data=file.read(),            # 文件內容
                file_name="實驗1. 雷諾數實驗.xlsx",  # 文件名稱
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"  # MIME 類型，Excel 文件
            )
    except FileNotFoundError:
        st.error("找不到文件：downloads/實驗1. 雷諾數實驗.xlsx")
