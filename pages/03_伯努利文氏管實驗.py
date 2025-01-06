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
st.title("實驗三: 伯努利方程")

# 主選單
page = st.sidebar.selectbox(
    "實驗三: 伯努利方程",
    ["實驗目的", "儀器與設備", "實驗原理", "實驗步驟", "實驗數據表格", "圖片與影片", "相關資料"]
)

# 根據選擇的頁面顯示內容
if page == "實驗目的":
    st.markdown("""
    ## 一、實驗目的
    流體力學中，伯努利方程式描述流體沿著一條穩定、非粘滯性及不可壓縮 的流線移動，其壓力、速度及高度的變化形成一關係式，此一關係式對於流體力 學中許多運動的特性做了合理的解釋，
   
   例如：棒球的運動軌跡，飛機機翼的昇力 等。而本裝置的目的為幫助致力於流體力學學習的學員，藉由文氏管的壓力與速 度的量測，來檢驗伯努利方程式能量守恆與質量守恆的概念，
   
   如此對流體運動中 速度與壓力的關係有較深刻的認識與了解。另外，本裝置所使用的標準風量產生 裝置，係根據國際規範AMCA 210-16製造而得，其精確度的可在3 % 以內，
   
   其結構及流量計算原理與目前廣泛應用於工業界風扇及系統阻抗測試之AMCA風洞是一致的，而學員透過實際量測，可對風洞流量量測的原理與方法做深入的了解。 
    
    因此，學習者若能活用部份流體及熱傳遞學裡的知識，並且按部就班學習、測試及體會，同時這個架構是IT產業界在研發及實際生產中正在使用的 工業技術，將使學習者產學的認知關係更加密切，必能裨益不少。

    """)

elif page == "儀器與設備":
    st.markdown(""" 
    ## 二、儀器與設備

    在本實驗中，我們將使用以下儀器與設備來進行實驗：  
    """)

    # 儀器與設備數據
    instrument_data = [
        ["乾溼球溫度計", "用於測量空氣的乾球和濕球溫度，幫助計算空氣的相對濕度及露點溫度。", 1],
        ["控制箱與操作面板", "用來控制實驗設備的啟動與設置，並顯示各項數據。", 1],
        ["測試段與測試件", "用於測試風流動狀況及流量測量，根據不同實驗需求選擇不同的測試件。", 1],
        ["標準流量產生裝置", "用於產生穩定流量的設備，保證流量測量的精確性。", 1],
        ["標準流量產生器用 AMCA 噴嘴", "這是專為標準流量產生裝置設計的噴嘴，能夠確保精確的流量測量。", 1],
        ["水柱壓力計", "用來測量由水柱產生的壓力，用於校準流量和測量差壓。", 1]
    ]

    # 創建 DataFrame 來顯示儀器與設備表格
    df_instruments = pd.DataFrame(instrument_data, columns=["儀器名稱", "描述", "數量"])

    # 顯示儀器與設備表格
    st.dataframe(df_instruments)

    # 插入圖片
    img_path = "downloads/實驗三器材.png"
    display_image(img_path, "實驗所用儀器與設備")


elif page == "實驗原理":
    st.markdown("## 三、實驗原理")
    
    # 添加图片展示
    img_path = os.path.join("downloads", "實驗三原理1.png")
    display_image(img_path, "噴嘴設計示意圖", "其中，對於關鍵元件─噴嘴(Nozzle)的設計，也有其依據的準則，其尺寸、表 面粗糙度都受到規範的限制。噴嘴為一特殊設計的漸縮管，具有較高且穩定的Cd 值，在不同的雷諾數狀態下，可達0.95 ~ 0.99，表示流體通過時會有較小的摩擦損失，可有效用做流量計算。")
    
    # 多张图片及其描述
    image_paths = [
        "downloads/實驗三原理2.png", "downloads/實驗三原理3.png",
    ]
    titles = ["規格示意", "與雷諾數關係圖"]
    descriptions = ["噴頭尺寸", "尺寸比值"]

    # 使用二列分配图片
    cols = st.columns(2)
    for i, (image_path, title, description) in enumerate(zip(image_paths, titles, descriptions)):
        col = cols[i % 2]
        with col:
            display_image(image_path, title, description)
    
    st.markdown("""
 噴嘴流量計屬於差壓式流量計，進行流量量測時，首先需要得到噴嘴喉部的速 度。在流體水平流動而不考慮位能變化的情況下，符合伯努利方程式(Bernoulli’s equation)的公式可寫為
    $$ P_1 + \frac{1}{2} \rho v_1^2 + \rho g h_1 = P_2 + \frac{1}{2} \rho v_2^2 + \rho g h_2 $$
    其中，$P_1$、$P_2$ 分別為兩個位置的壓力，$v_1$、$v_2$ 分別為兩個位置的流速，$h_1$、$h_2$ 是兩位置的高度。
    """)
    
    img_path = os.path.join("downloads", "實驗三原理4.png")
    display_image(img_path, "伯努利方程式(Bernoulli’s equation)", "由於噴嘴上游腔室可視為均壓型壓力腔室，其流體速度遠小於喉部速度，故 U1小於U2，則伯努利方程式可簡化為")
    img_path = os.path.join("downloads", "實驗三原理5.png")
    display_image(img_path, "伯努利方程式(Bernoulli’s equation)", "根據符合質量守恆的連續方程式(Continuous equation)，通過噴嘴喉部的理論 流量為：")
    img_path = os.path.join("downloads", "實驗三原理6.png")
    display_image(img_path, "伯努利方程式(Bernoulli’s equation)", "實際流量則需要考慮流量係數Cd：")
    img_path = os.path.join("downloads", "實驗三原理7.png")
    display_image(img_path, "伯努利方程式(Bernoulli’s equation)", "由於風洞設計係依AMCA 210-16之規範條件設計，則Cd值計算可參考規範 中之經驗公式，其為雷諾數的函數，如下：")
    img_path = os.path.join("downloads", "實驗三原理8.png")
    display_image(img_path, "伯努利方程式(Bernoulli’s equation)", "藉由以上公式推導，可以了解此流量產生裝置的計算方法。")

elif page == "實驗步驟":
    st.markdown("""
    ## 四、實驗步驟

   
    **Step 1**: 啟動控制面板上的 1.1 System Power：系統源開關。  
    
    **Step 2**: 確認乾溼球溫度計的濕球水箱有水。  
   
    **Step 3**: 啟動設備後需暖機 10 分鐘，並紀錄乾溼球溫度及大氣壓力。  
    
    **Step 4**: 調整輔助風機頻率旋鈕，逆時針旋轉至底，並確認輔助風機頻率顯示器顯示為 0.0 Hz。  
   
    **Step 5**: 根據所需實驗的風量選擇合適的噴嘴後，於標準流量產生器安裝噴嘴，噴嘴 安裝方式可參考3.2 標準風量產生裝置 操作。
    
    **Step 6** :5.4PL6噴嘴腔室往前輕推，關閉噴嘴 前後腔室。並且將噴嘴腔室兩側5.8固 定扣拑扣上，以固定噴嘴腔室。
   
    
    **Step 7** :擇欲測試之測試件，以及相對應之手 輪，如左圖中選擇孔口板測試件。
   
    **Step 8** :測試件安裝於標準流量產生器上之測 試段。
    
    **Step 9** :下面板RUN按鍵，使變頻器與風機產 生連動關係。 調整變頻器旋鈕，使P56顯示為一定值， 如：35 mmAq。
  
    **Step 10** :察噴嘴前後差壓（P56）並記錄，將此 數值與Step2中紀錄的環境狀態，輸入 AMCA210軟體中，計算出當前流量。
   
    **Step 11**:記錄其他溫度、壓力的參數數值，以利 帶入AMCA 210 風量計算軟體。 Pb:大氣壓力，mmHg。 P56:噴嘴差壓，mmAq。 Ps(P8):PL8腔室壓力，mmAq。 Tc(T8):PL8腔室溫度，ºC。 Td:乾球溫度，ºC。 Tw:濕球溫度，ºC。
   
    **Step 12** :錄水柱壓力計之壓力分佈數值。 或使用dP表紀錄其顯示值。
  
    **Step 13** :標準流量產生裝置參數值輸入AMCA 210軟體，得到標準流量值。 Pb:大氣壓力，mmHg。 P56:噴嘴差壓，mmAq。 P5腔室壓力=Ps(P8+P56)，mmAq。 T8:PL8腔室溫度=T5溫度，ºC。 Td:乾球溫度，ºC。 Tw:濕球溫度，ºC。
  
    """)

elif page == "實驗數據表格":
    st.subheader("實驗數據表格展示")
    data = {
        "電壓 (V)": [20, 30, 40],
        "流速 (m/s)": [1.2, 1.5, 1.8],
        "壓力差 (Pa)": [100, 150, 200],
        "溫度 (°C)": [22.5, 23.0, 23.5],
        "測量時間 (min)": [10, 12, 15]
    }
    df = pd.DataFrame(data)
    st.dataframe(df)

elif page == "圖片與影片":
    st.subheader("實驗圖片與影片展示")

    # 定義圖片和描述
    images = [
        ("downloads/實驗30V.jpg", "當電壓為0V時的結果", "這是0V下的實驗結果，液面平穩。"),
        ("downloads/實驗320V.jpg", "當電壓為20V時的結果", "這是20V下的實驗結果，平穩微升高。"),
        (r"downloads/實驗330V.jpg", "當電壓為230V時的結果", "這是30V下的實驗結果，明顯升高。"),
        (r"downloads/實驗340V.jpg", "當電壓為240V時的結果", "這是40V下的實驗結果，與前次相比無明顯升高。"),
	("downloads/文氏管.png", "文氏管示意圖", "展示文氏管的結構與運作方式。")
    ]
    # 使用二列分配圖片
    cols = st.columns(2)  # 創建二列
    # 提取圖片、標題和描述
    image_paths = [image[0] for image in images]
    titles = [image[1] for image in images]
    descriptions = [image[2] for image in images]

    # 分配圖片到二列
    for i, (image_path, title, description) in enumerate(zip(image_paths, titles, descriptions)):
        col = cols[i % 2]  # 使用餘數分配到二列
        with col:
            display_image(image_path, title, description)

    st.subheader("實驗影片")
    video_path = 'downloads/實作影片1.mp4'
    if os.path.exists(video_path):
        st.video(video_path)
    else:
        st.error(f"找不到影片：{video_path}")

elif page == "相關資料":
    st.subheader("相關資料下載")
    
    # 下載 PDF 文件
    try:
        with open(r"downloads/實驗3. 伯努利文氏管實驗.pdf", "rb") as file:
            st.download_button(
                label="下載 實驗3. 伯努利文氏管實驗.pdf",
                data=file.read(),
                file_name="實驗3. 伯努利文氏管實驗.pdf",
                mime="application/pdf"  # 設置 MIME 類型為 PDF
            )
    except FileNotFoundError:
        st.error("找不到文件：downloads/實驗3. 伯努利文氏管實驗.pdf")

    # 下載 DOC 檔案
    try:
        with open(r"downloads/實驗3. 伯努利文氏管實驗.doc", "rb") as file:
            st.download_button(
                label="下載 實驗3. 伯努利文氏管實驗.doc",
                data=file.read(),
                file_name="實驗3. 伯努利文氏管實驗.doc",
                mime="application/msword"  # DOC 文件的 MIME 類型
            )
    except FileNotFoundError:
        st.error("找不到文件：downloads/實驗3. 伯努利文氏管實驗.doc")

    # 下載 STEP 檔案
    try:
        with open("downloads/文氏管.STEP", "rb") as file:
            st.download_button(
                label="下載 文氏管.STEP 檔案",  # 按鈕標籤
                data=file.read(),        # 文件內容
                file_name="文氏管.STEP",  # 文件名稱
                mime="application/step"   # MIME 類型，STEP 文件通常使用 "application/step"
            )
    except FileNotFoundError:
        st.error("找不到文件：downloads/文氏管.STEP")

    # 下載 ZIP 文件
    try:
        with open(r"downloads/Venturi_Geom_3d.zip", "rb") as file:
            st.download_button(
                label="下載 Venturi_Geom_3d.zip",
                data=file.read(),
                file_name="Venturi_Geom_3d.zip",
                mime="application/zip"  # 設置 MIME 類型為 ZIP
            )
        with open(r"downloads/Venturi_Geom_2d.zip", "rb") as file:
            st.download_button(
                label="下載 Venturi_Geom_2d.zip",
                data=file.read(),
                file_name="Venturi_Geom_2d.zip",
                mime="application/zip"  # 設置 MIME 類型為 ZIP
            )
    except FileNotFoundError:
        st.error("找不到文件：downloads/Venturi_Geom_2d.zip")

    # 下載 Excel 文件
    try:
        with open(r"downloads/Vacuum Generator Design(1131225)template.xlsx", "rb") as file:
            st.download_button(
                label="下載 Vacuum Generator Design(1131225)template.xlsx",  # 按鈕標籤
                data=file.read(),            # 文件內容
                file_name="Vacuum Generator Design(1131225)template.xlsx",  # 文件名稱
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"  # MIME 類型，Excel 文件
            )
    except FileNotFoundError:
        st.error("找不到文件：downloads/Vacuum Generator Design(1131225)template.xlsx")

