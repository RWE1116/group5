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
st.title("實驗四: 管路摩擦損失")

# 主選單
page = st.sidebar.selectbox(
    "實驗四: 管路摩擦損失",
    ["實驗目的", "儀器與設備", "實驗原理", "實驗步驟", "實驗數據表格", "圖片與影片", "相關資料"]
)

# 根據選擇的頁面顯示內容
if page == "實驗目的":
    st.markdown("""
    ## 一、實驗目的
    
量測液體黏滯係數，實驗中改變液體溫度，紀錄黏滯系數與溫度變化的關係。

 """)
elif page == "儀器與設備":
    st.markdown(""" 
    ## 二、儀器與設備
本實驗使用儀器為黏度計、恆溫箱、轉針、燒杯 
    """)
    
    # 儀器與描述列表，並加入編號列
    instrument_data = [
        ["黏度計", "用於測量液體黏度值，幫助分析水流速和衝擊力的關聯。", 1],
        ["恆溫箱", "用於確保實驗準確度，確保水流符合預設的實驗條件。", 1],
        ["轉針", "用來攪動液體測量黏度值，以便於計算衝擊力和進行實驗數據的分析。", 1],
        ["燒杯", "控制水箱的水流速，調節流量以便進行不同條件下的實驗。", 1],

    ]
    image_paths = [
        "downloads/實驗四器材1.png", "downloads/實驗四器材2.png", "downloads/實驗四器材3.png"
    ]
    titles = ["黏度計面板", "黏度計背面", "黏度計本體"]
    descriptions = ["黏度計面板", "黏度計背面", "黏度計本體"]    
    # 使用二列分配图片
    cols = st.columns(2)
    for i, (image_path, title, description) in enumerate(zip(image_paths, titles, descriptions)):
        col = cols[i % 2]
        with col:
            display_image(image_path, title, description)
    # 正確的 DataFrame
    df_instruments = pd.DataFrame(instrument_data, columns=["儀器名稱", "描述", "數量"])
    st.dataframe(df_instruments)


elif page == "實驗原理":
    st.markdown(""" 
    ## 三、實驗原理
    黏滯係數分為兩種：
    
    一為絕對黏度(Absolute Viscosity)，單位為 P(poise)，1 P = 1(g/cm)s = 100 cP；
    一為動力黏度(Kinematic Viscosity)，單位為 St(stoke)，1 St = 1cm²/s = 100 cSt。
    
    又絕對黏度與動力黏度之關係為下式： 
    centiPoises (cP) = centiStokes (cSt) x Density(g/cm³)
    
    固體：當一剪應力（shear stress）施於固體時，固體之變形角度正比於施力，而變形不隨時間而變化。
    """)

    # 顯示第一張圖片
    img_path = os.path.join("downloads", "實驗四原理1.png")
    display_image(img_path, "剪應力", "剪應力。")

    st.markdown("""
    流體（液體或氣體）：任一大小之剪應力施於流體時，流體之變形角度將隨時間而增加。
    """)

    # 顯示第二張圖片
    img_path = os.path.join("downloads", "實驗四原理2.png")
    display_image(img_path, "流體角度", "流體角度")

    st.markdown(""" 
    黏滯力之物理意義：
    氣體: 氣體之黏滯力是由氣體分子之間碰撞，造成「動量交換」而產生。
    """)

    # 顯示第三張圖片
    img_path = os.path.join("downloads", "實驗四原理3.png")
    display_image(img_path, "氣體之黏滯力", "氣體之黏滯力")

    st.markdown(""" 
    液體: 液體的分子以「長鍊」形式組成，液體之黏滯力乃由於長鍊間的凝聚力所造成。
    """)

    # 顯示第四張圖片
    img_path = os.path.join("downloads", "實驗四原理4.png")
    display_image(img_path, "液體分子的長鍊", "液體分子的長鍊。")
    st.markdown(""" 
黏滯力與溫度之關係： 

當溫度增加，氣體分子之能量與動量均增加，分子間之碰撞及動量交換亦增加，故黏滯力增加。對於液體，分子鍊間之凝聚力隨溫度增加而破壞，黏滯力亦減小。

當馬達旋轉帶動轉子(Rotor)同步旋轉，轉子表面與液體間產生相對摩擦力，藉由簡單的換算公式，轉換成讀取之數據(黏度值)。馬達與轉子之間最重要的介質，是一條經過校正的精密游絲。當液體黏度大於游絲彈性時，會帶動指針於刻度盤上產生一個偏角，即可得知樣本的絕對黏度。

    """)

elif page == "實驗步驟":
    st.markdown("""
    ## 四、實驗步驟
1.	先將黏度計安裝完成並調整水平調整使水瓶氣泡至於黑圈中且打開黏度計電源
    """)
    img_path = os.path.join("downloads", "實驗四器材4.png")
    display_image(img_path, "調整水平", "打開黏度計電源")
    st.markdown("""
2.	取一個 600ml 標準燒杯，將樣品加至轉針測量高度，黏度計準備好參數設定完成。
    """)
    img_path = os.path.join("downloads", "實驗四器材5.png")
    display_image(img_path, "燒杯與黏度計", "燒杯與黏度計")
    
    st.markdown("""
3.	設定轉針號碼與轉速並打開馬達開關鈕測量樣品黏度。帶黏度穩定後，讀取顯示幕數據並記錄，將冷凍開關關閉，再依序設定進行量測。
    """)    
elif page == "實驗數據表格":
    st.subheader("實驗數據表格展示")
    
    # 新的實驗數據字典，將轉速作為列，並將溫度數據排成橫列
    data = {
        "溫度(˚C)": ["18.1˚C", "36˚C", "56.7˚C"],
        "水黏滯係數(CP) 轉速30rpm": [2.9, 1.4, 2.4],
        "水黏滯係數(CP) 轉速50rpm": [11.5, 9.1, 4.7],
        "水黏滯係數(CP) 轉速60rpm": [15.8, 11.7, 2.2]
    }

    # 創建 DataFrame
    df = pd.DataFrame(data)

    # 顯示標題和實驗參數
    st.subheader("實驗數據")
    st.write("""
    由實驗得知：
    固體在虎克定理（Hooke’s law）下，變形角度正比於施予之剪應力。
    """)

    # 顯示表格
    st.dataframe(df)

elif page == "圖片與影片":
    st.subheader("實驗圖片與影片展示")
    

elif page == "相關資料":
    st.subheader("相關資料下載")
    
    # 下載 PDF 文件
    try:
        with open(r"downloads/實驗4. 黏滯係數量測.pdf", "rb") as file:
            st.download_button(
                label="下載 實驗4. 黏滯係數量測.pdf",
                data=file.read(),
                file_name="實驗4. 黏滯係數量測.pdf",
                mime="application/pdf"  # 設置 MIME 類型為 PDF
            )
    except FileNotFoundError:
        st.error("找不到文件：downloads/實驗4. 黏滯係數量測.pdf")

    # 下載 DOC 檔案
    try:
        with open(r"downloads/實驗4. 黏滯係數量測.doc", "rb") as file:
            st.download_button(
                label="下載 實驗4. 黏滯係數量測.doc",
                data=file.read(),
                file_name="實驗4. 黏滯係數量測.doc",
                mime="application/msword"  # DOC 文件的 MIME 類型
            )
    except FileNotFoundError:
        st.error("找不到文件：downloads/實驗4. 黏滯係數量測.doc")
    # 下載 Excel 文件
    try:
        with open(r"downloads/實驗4. 黏滯係數量測.xlsx", "rb") as file:
            st.download_button(
                label="下載 實驗4. 黏滯係數量測.xlsx",  # 按鈕標籤
                data=file.read(),            # 文件內容
                file_name="實驗4. 黏滯係數量測.xlsx",  # 文件名稱
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"  # MIME 類型，Excel 文件
            )
    except FileNotFoundError:
        st.error("找不到文件：downloads/實驗4. 黏滯係數量測.xlsx")
