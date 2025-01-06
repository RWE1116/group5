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
	    base_path = "downloads" 
            img = Image.open(image_path)
            st.image(img, caption=title, use_column_width=True)  # 使用Streamlit的image顯示圖片
            st.write(f"<h5>{description}</h5>", unsafe_allow_html=True)
            st.markdown("---")  # 分隔線
        except Exception as e:
            st.error(f"無法顯示圖片 {image_path}: {e}")
    else:
        st.error(f"找不到圖片：{image_path}")

# 設置頁面標題和樣式
st.title("期末報告")

# 主選單
page = st.sidebar.selectbox(
    "期末報告",
    ["概論", "原理與設計方法", "實驗量測與數據分析", "結果與討論", "結論", "學期團隊作業/專案設計", "聲明"]
)

# 根據選擇的頁面顯示內容
if page == "概論":
	
    st.markdown(""" 
        ## 主題一、創新夾持裝置機械設計
    """)
    st.markdown(""" 
    1.整理各式(家)真空產生器的特點FT系列真空產生器多種型號選擇：
    
    FT系列包含多個型號，如 FT-050、FT-100、FT-150 和 FT-200，以滿足不同的應用需求。
    
    高真空度：該系列真空產生器的最大真空度可達 -91.8 kPa（-680 mmHg），適用於需要高真空度的作業環境。
    
    廣泛的使用壓力範圍：FT系列的使用壓力範圍為 0.1 至 1.6 MPa，適應多種工作條件。
    
    適用溫度範圍：可在 0 至 60 ℃ 的環境下運行，適合多種工業環境。
    """)
    # 插入圖片
    img_path = "downloads/期末報告1.png"
    display_image(img_path, "產生器外觀與規格", "產生器外觀與規格")
    img_path = "downloads/期末報告2.png"
    display_image(img_path, "產生器尺寸", "產生器尺寸")
    st.markdown(""" 
    2.整理各式(家)真空產生器的產品與功能介紹FT系列真空產生器功能高效真空產生：
    
    利用壓縮空氣通過噴嘴產生真空，提供穩定的吸附能力。
    
    多樣化應用：
    
    適用於自動化設備中的搬運、固定、包裝等需要真空的操作。
    易於安裝：各型號配備不同的接管口徑（如 M5、1/8"、1/4"、3/8"），方便集成到各類系統中。
    """)
    img_path = "downloads/期末報告3.png"
    display_image(img_path, "表格", "表格")
    st.markdown(""" 
    VK真空產生器
    通過將各個單元模塊化並組合各種單元，可以選擇最適合使用目的的單元。
    壓力傳感器選擇
    LED 顯示壓力傳感器( 2 種開關輸出、1 種開關輸出 + 類比輸出)。
    低成本、易於使用的機械壓力傳感器，根據用途選擇適合的型式。
    """)
    img_path = "downloads/期末報告4.png"
    display_image(img_path, "VK真空產生器", "VK真空產生器")
    img_path = "downloads/期末報告5.png"
    display_image(img_path, "VK真空產生器特點", "VK真空產生器特點")
    st.markdown(""" 
    VK真空產生器功能真空產生與破壞：
    
    內建真空產生和破壞電磁閥，實現快速切換，滿足不同工序需求。 
    壓力監控：配備數字顯示壓力傳感器，實時監控真空壓力，確保系統穩定運行。 
    過濾與消音：內置真空過濾器和消音器，保護系統元件，降低運行噪音。
    """)
    img_path = "downloads/期末報告6.png"
    display_image(img_path, "規格表", "規格表")
    st.markdown(""" 
1. 整理各式(家)散熱器元件或模組的特點 台灣協緯金屬:鋁擠型散熱片03特點：

材質：

使用A6063鋁合金，該材料以其良好的導熱性和耐腐蝕性著稱，適合製作高效能散熱片。

應用廣泛：

適用於各類電子設備，如電源供應器、手提電腦、交換器（Switch）、集線器（HUB）、伺服器、數據機（Cable Modem）、不間斷電源系統（UPS）、液晶顯示器（LCD）等，滿足不同設備的散熱需求。

多樣規格：

提供多種規格和尺寸，以適應不同的設計要求和散熱需求。

製造工藝：

公司具備沖壓型、鋁擠型和表面處理等多種製造工藝，確保產品質量和性能達到行業領先水平。
    """)
    img_path = "downloads/期末報告7.png"
    display_image(img_path, "鋁擠型散熱片03", "鋁擠型散熱片03")
 
    st.markdown(""" 
2. 整理各式(家)散熱器元件或模組的產品與功能介紹台灣協緯金屬:鋁擠型散熱片03高效散熱:

鋁擠型設計提供了大表面積，有助於快速散發熱量，保護電子設備在高溫環境下穩定運行。

熱能管理:

能夠有效降低電子元件運作時產生的溫度，延長設備壽命，並提升性能穩定性。
輕量化結構:

使用 A6063 鋁合金製造，具有優良的導熱性，同時重量輕，適合輕量化電子設備需求。

機械穩定性:

經過精密加工和沖壓處理，結構穩定且堅固，能承受多樣化的安裝和使用場景。

多用途設計:

適配多種電子設備，包括伺服器、電源供應器、液晶顯示器（LCD）、數據機、UPS 系統等，廣泛應用於資訊通訊與工業自動化領域。

京業電子:

複合材料散熱器(GDC Series-BCX系列)

高導熱性：

採用先進的複合材料，提供優異的導熱性能，能迅速將熱量從熱源傳導至散熱器表面，提升散熱效率。

輕量化設計：

複合材料的應用使散熱器在保持高強度的同時，減輕了重量，適合對重量敏感的應用場合。

耐腐蝕性：

材料本身具有良好的抗腐蝕能力，適用於各種環境，延長產品使用壽命。
客製化能力：

京業電子提供客製化服務，可根據客戶需求調整散熱器的尺寸、形狀和性能，以滿足特定應用要求。

應用廣泛：

適用於各類電子設備和工業應用，特別是在高功率密度和有限空間的情況下，提供有效的散熱解決方案。
    """)
    img_path = "downloads/期末報告8.png"
    display_image(img_path, "複合材料散熱器(GDC Series-BCX系列)", "複合材料散熱器(GDC Series-BCX系列)") 
    img_path = "downloads/期末報告9.png"
    display_image(img_path, "複合材料散熱器(GDC Series-BCX系列)特性表", "複合材料散熱器(GDC Series-BCX系列)特性表")    
 
    st.markdown(""" 
京業電子:
複合材料散熱器(GDC Series-BCX系列)

高效熱量傳導:

採用導熱性能卓越的複合材料，能快速將熱量從熱源傳遞至散熱器表面，顯著降低熱源溫度。

熱平衡與均溫設計:

複合材料內部結構經過優化，可均勻分布熱量，減少局部過熱現象，提升設備運行穩定性。

空間節省:

輕量化設計使其適合應用於有限空間中，特別適合微型化、高功率密度的電子設備。

環境耐受性:
材料本身具備高抗腐蝕性能，能夠在嚴苛的工作環境下長期穩定運行。

靜音運行:

結合被動散熱技術，降低對風扇等主動散熱部件的需求，實現低噪音運行。

模組化與客製化支持:

支援多樣化的尺寸與形狀定制，並可模組化集成到各類電子設備中，滿足不同應用需求。
    """)
elif page == "原理與設計方法": 
    st.markdown(""" ## 二、原理與設計方法(機械設計與繪圖)
    主題一、創新夾持裝置機械設計

    1. 把壓縮空氣導入噴嘴
    2. 壓縮空氣在噴嘴受到節流。高速釋放到擴散室，膨脹擴散並散開流向廓壓器
    3. 通過空氣的高速流動，卷吸噴嘴周邊空氣，使擴散室的壓力下降，真空街口空氣會流入擴散器。
    4. 流入的真空接口空氣和噴嘴放出的壓縮空氣一起，從擴散室釋放到大氣中。
    """)
    img_path = "downloads/期末報告11.png"
    display_image(img_path, "設計剖面圖", "設計剖面圖")

    st.markdown(""" 
    1. 整理真空產生器設計方法
    
    可由柏努力定理得流體流速與壓力關係如下:
    Q = V1A1 = V2A2 = V3A3
    """)
    img_path = "downloads/期末報告12.png"
    display_image(img_path, "柏努力定理", "柏努力定理")
    
    st.markdown(""" 
    當流量固定,斷面截面積不同將造成不同的流速,以下分析三種斷面、流速及壓力情形:
    """)
    img_path = "downloads/期末報告13.png"
    display_image(img_path, "流速壓力比較表", "流速壓力比較表")
    
    st.markdown(""" 
    2. 依據原理與工件大小之零組件設計圖
    """)    
    img_path = "downloads/工程圖1.jpg"
    display_image(img_path, "零組件設計圖", "零組件設計圖")
    
    img_path = "downloads/生成器 1.png"  
    display_image(img_path, "生成器3D圖", "生成器3D圖")
    
    cols = st.columns(3)

    image_paths = [
        "downloads/生成器2.jpg", "downloads/生成器3.jpg", "downloads/生成器4.jpg",
    ]
    titles = ["排氣", "真空區", "進氣"]
    descriptions = ["排氣", "真空區", "進氣"]
    for i, (image_path, title, description) in enumerate(zip(image_paths, titles, descriptions)):
        col = cols[i % 3]  
        with col:
            display_image(image_path, title, description)
    
    st.markdown(""" 
    主題二、環境量測與控制裝置機械設計

    1.整理散熱器設計與要求規範散熱片的應用方式散熱片的選用，最簡單的方式是利用熱阻的概念來設計，熱阻是電子熱管理技術中很重要的設計參數，定義為Ｒ＝ΔT / P 
    其中ΔT為溫度差，P為晶片之熱消耗。熱阻代表元件熱傳的難易度，熱阻越大，元件得散熱效果越差，如果熱阻越小，則代表元件越容易散熱。
    
    規範:

    最大熱流密度：確保散熱器可應對設備的熱量輸出，避免局部過熱。
    均溫性能：確保散熱表面的溫度分布均勻，提升整體散熱效果。

    機械結構要求

    尺寸公差：

    滿足設備裝配要求，避免過大或過小影響接觸面積。
    鰭片厚度與間距：需根據散熱需求和空氣流通條件進行設計。

    2.整理散熱器設計方法

    1.散熱器形狀與結構設計
    鰭片設計：選擇合適的鰭片數量、厚度與間距。
    尺寸與體積：散熱器應根據實際空間要求和熱量需求確定大小。

    2.選擇材料
    導熱性：常用材料包括鋁（輕量且具良好導熱性）、銅（導熱性優越但較重）、複合材料（結合高導熱性與輕量設計）。

    3.CFD模擬（計算流體動力學模擬）
    使用CFD軟件（如ANSYS Fluent）進行流體流動與熱傳遞模擬，幫助優化散熱器設計，尤其在強制對流散熱系統中，能更精確地預測氣流與熱量分佈。

    3. 依據原理與工件大小之零組件設計圖
    """)
    
    image_paths = [
        "downloads/散熱器 尺寸1.jpg", "downloads/散熱器 尺寸2.jpg", "downloads/散熱器 尺寸3.jpg","downloads/散熱器 尺寸4.jpg"
    ]
    titles = ["守序圓柱", "守序方柱", "混亂圓柱", "混亂方柱"]
    descriptions = ["守序圓柱", "守序方柱", "混亂圓柱", "混亂方柱"]    
    # 使用二列分配图片
    cols = st.columns(2)
    for i, (image_path, title, description) in enumerate(zip(image_paths, titles, descriptions)):
        col = cols[i % 2]
        with col:
            display_image(image_path, title, description)


elif page == "實驗量測與數據分析":
    st.markdown(""" ## 三、實驗量測與數據分析 

    主題一、創新夾持裝置機械設計

    1.依照Excel檔進行設計參數計算""")
    
    st.markdown(""" 
    三、實驗量測與數據分析

    主題一、創新夾持裝置機械設計

    1.依照Excel檔進行設計參數計算

    """)  
    
    img_path = "downloads/期末報告14.png"
    display_image(img_path, "設計參數計算", "設計參數計算")
    
    st.markdown(""" 
    1.	導入模型

    2.	在設置里設置入口面、出口、壁面後生成網格

    3.	進入分析介面，選擇空氣，設置入口邊界條件速度分別有1.5.10，設置完後先初始化後，開始計算

    4.	查看跡線確認負壓區是否正確，及記錄數值
    """)
    img_path = "downloads/期末報告15.png"
    display_image(img_path, "三組設計", "三組設計參數計算結果")
    
    st.markdown(""" 
    主題二、環境量測與控制裝置機械設計
    1.依照Excel檔進行設計參數計算
    """)    
    
    img_path = "downloads/期末報告16.png"
    display_image(img_path, "三組設計", "三組設計參數計算結果")
    
    st.markdown(""" 
    1.導入幾何模型

    2.網格生成

    3.邊界條件設置:
    入口邊界:設置進入流體的速度、溫度等條件。

    設置出口邊界：定義流體的出口壓力或質量流量。

    設置壁面邊界：設定散熱器表面的熱傳遞條件，如 熱通量、溫度，以及熱對流邊界條件。

    5.	設置完後先初始化後，開始計算
    6.	結果可視化
    使用等溫線、流場可視化、熱流線圖等工具，分析散熱器的熱分布情況。
    確認熱點區域，並觀察流場是否與預期一致，是否有流動死區或回流區域。

    主題三、bladeless wind turbine結構設計(僅Fluent模擬)
    1.	詳細列出軟體分析之過程(CAD模型、條件、材料常數、計算方法、其他)
    1.	導入模型
    2.	網格設置
    3.	設置邊界條件:
    入口條件速度有0.1，0.5，1，由於0.1過小，故需要選擇層流。
    4.	設定分析項目:阻尼及升力
    5.	初始化完後開始計算
    6.	找到time	drag	lift文件位置後，在EXCEL生成圖表
    7.	紀錄跡線及數據
    """)   
    img_path = "downloads/期末報告17.png"
    display_image(img_path, "excel計算", "excel計算")
    img_path = "downloads/期末報告18.png"
    display_image(img_path, "記錄跡線及數據", "記錄跡線及數據")    


elif page == "結果與討論":
    st.markdown("""
    ## 四、結果與討論
主題一、創新夾持裝置機械設計

1.依照Excel檔建立真空產生器與周邊3D設計圖(零件、組合、爆炸)

    """)
    img_path = "downloads/生成器 1.png"
    display_image(img_path, "記錄跡線及數據", "記錄跡線及數據")
    st.markdown("""
    2.	依照Excel檔建立真空產生器計算書(公式法)

    """)
    img_path = "downloads/期末報告19.png"
    display_image(img_path, "記錄跡線及數據", "記錄跡線及數據")
    st.markdown("""
    3.	繪圖並討論數值模擬結果及計算書結果與數值模擬(CAE法)之誤差?
    """)    
    image_paths = [
        "downloads/期末報告21.png", "downloads/期末報告22.png"
    ]
    titles = ["期末考評分表", "計算過程"]
    descriptions = ["計算過程", "期末考評分表"]
    # 使用二列分配图片
    cols = st.columns(2)
    for i, (image_path, title, description) in enumerate(zip(image_paths, titles, descriptions)):
        col = cols[i % 2]
        with col:
            display_image(image_path, title, description)
   
    st.markdown("""
   4.	繪圖並討論實驗測試結果及可能誤差大小與原因?

經過內插法求解後，發現本次實驗與分析數據誤差在23%，存在誤差可能性為加工時的誤差，由於直徑3的鑽頭不能一次貫穿，加上鑽床定位較差，加工時可能產生偏移，或者是鑽深未達標等因素，而解決辦法可以透過更好的加工設備，如銑床，透過光學尺的輔助可以使加工效果達到設計參數，從而減少誤差。
 

 
主題二、環境量測與控制裝置機械設計

1.依照Excel檔建立散熱器與周邊3D設計圖(零件、組合、爆炸)

2.依照Excel檔建立散熱器計算書(公式法)

    """)
    img_path = "downloads/期末報告23.png"
    display_image(img_path, "記錄跡線及數據", "記錄跡線及數據")
    st.markdown("""
    3.	繪圖並討論數值模擬結果及計算書結果與數值模擬(CAE法)之誤差?
    """)
    img_path = "downloads/期末報告21.png"
    display_image(img_path, "期末考評分表", "計算過程")
    st.markdown("""
    4.	繪圖並討論實驗測試結果及可能誤差大小與原因?
本次實驗誤差頂部在12%，底部在15%，存在誤差原因可能在於當天的溫度及濕度，底部貼在桌面可能導致熱量被分散。

    """)    
elif page == "結論":
    st.markdown("""
    ## 結論

主題一、創新夾持裝置機械設計

本組這次在設計真空產生器之初，遇到負壓區無法在正確位置，所以在設計時花費大量時間，在第一次分析成功後，進行加工時卻失敗了，負壓區無法進行吸附，後來我們進行大量設計與模擬，發現空氣進入後在直徑3的管道被壓縮後我們的設計管道過長，導致在擴散時真空區的空氣不會被吸，反而成為出氣口，後來針對這點，我們在出氣口原來直徑3的地方擴成6直至與真空區的管道接觸，再進行實驗時已可以進行吸附，同時吸力也很好。

 主題二、環境量測與控制裝置機械設計

在環境量測與控制裝置的機械設計中，結合了精確度、可靠性和耐用性的需求，以確保在各種環境條件下進行精確測量和控制。設計過程中，必須考量到測量儀器的穩定性和反應時間，並確保控制系統的反應速度與精確性，這樣才能在不斷變化的環境中保持高效運行。

    """)
elif page == "學期團隊作業/專案設計":
    st.markdown("""
    ## 學期團隊作業/專案設計

    課號：0835(四設計四乙)

    學年：113學年度第1學期

    題目：期末專案

    組別：第5組

    成員：
    """)
    
    data = {
        '組員': ['莊雨薰', '陳靚芸', '陳瑨維', '葉桓亞', '詹耀賢'],
        '學號': ['41023203', '41023205', '41023228', '41023240', '41023241'],
        '分工': ['實驗紀錄，報告撰寫', '實驗紀錄，報告撰寫', '實驗紀錄，報告撰寫，實驗數據計算，網站維護，分析，繪圖', '實驗紀錄，報告撰寫，分析，繪圖', '實驗紀錄，報告撰寫，分析，加工'],
        '分工比率': ['15%', '15%', '30%', '20%', '20%']  # 根據項目重要性和數量設定的比率
    }

    df = pd.DataFrame(data)

    # 顯示表格
    st.write(df)  # Add this line to display the dataframe

    st.markdown("""
    貢獻度總計為100%，請自行核算。

    完成日期：  113年  01月  03日
    """)
elif page == "聲明":
    st.markdown("""
    ## 聲明
本人在此聲明，本設計作業皆由本人與同組成員共同獨立完成，並無其他第三者參與作業之進行，若有抄襲或其他違反正常教學之行為，自願接受該次成績以零分計。同時本人亦同意在上述表格中所記載之作業貢獻度，並以此計算本次個人作業成績。

成員簽名：
    """)
    image_paths = [
        "downloads/聲明1.jpg", "downloads/聲明2.jpg", "downloads/聲明3.jpg", "downloads/聲明4.jpg", "downloads/聲明5.jpg"
    ]
    titles = [" 詹耀賢", "葉桓亞", "陳瑨維", "陳靚芸", "莊雨薰"]
    descriptions = ["詹耀賢親簽", "葉桓亞親簽", "陳瑨維親簽", "陳靚芸親簽", "莊雨薰親簽"]
    # 使用二列分配图片
    cols = st.columns(2)
    for i, (image_path, title, description) in enumerate(zip(image_paths, titles, descriptions)):
        col = cols[i % 2]
        with col:
            display_image(image_path, title, description)


	

