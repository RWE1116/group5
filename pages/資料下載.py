import streamlit as st

def download_file(file_path, file_label, mime_type, file_name, unique_key):
    """通用文件下載功能"""
    try:
        with open(file_path, "rb") as file:
            st.download_button(
                label=file_label,
                data=file.read(),
                file_name=file_name,
                mime=mime_type,
                key=unique_key  # 使用動態的唯一 key
            )
    except FileNotFoundError:
        st.error(f"找不到文件：{file_path}")

# 顯示相關資料下載部分
st.subheader("相關資料下載")

# 下載文件1 (水衝擊實驗)
download_file(r"Y:/a/downloads/實驗1. 雷諾數實驗.pdf", "下載 實驗1. 雷諾數實驗.pdf", "application/pdf", "實驗1. 雷諾數實驗.pdf", "key1")
download_file(r"Y:/a/downloads/實驗1. 雷諾數實驗.doc", "下載 實驗1. 雷諾數實驗.doc", "application/msword", "實驗1. 雷諾數實驗.doc", "key2")
download_file(r"Y:/a/downloads/實驗1. 雷諾數實驗.xlsx", "下載 實驗1. 雷諾數實驗.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "實驗1. 雷諾數實驗.xlsx", "key3")
st.markdown("---")  # 分隔線

# 下載文件2 (水衝擊實驗)
download_file(r"Y:/a/downloads/實驗2. 水衝擊實驗.pdf", "下載 實驗2. 水衝擊實驗.pdf", "application/pdf", "實驗2. 水衝擊實驗.pdf", "key4")
download_file(r"Y:/a/downloads/實驗2. 水衝擊實驗.doc", "下載 實驗2. 水衝擊實驗.doc", "application/msword", "實驗2. 水衝擊實驗.doc", "key5")
download_file(r"Y:/a/downloads/實驗2. 水衝擊實驗.xls", "下載 實驗2. 水衝擊實驗.xls", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "實驗2. 水衝擊實驗.xls", "key6")
st.markdown("---")  # 分隔線

# 下載文件3 (伯努利文氏管實驗)
download_file(r"Y:/a/downloads/實驗3. 伯努利文氏管實驗.pdf", "下載 實驗3. 伯努利文氏管實驗.pdf", "application/pdf", "實驗3. 伯努利文氏管實驗.pdf", "key7")
download_file(r"Y:/a/downloads/實驗3. 伯努利文氏管實驗.doc", "下載 實驗3. 伯努利文氏管實驗.doc", "application/msword", "實驗3. 伯努利文氏管實驗.doc", "key8")
download_file("Y:/a/downloads/文氏管.STEP", "下載 文氏管.STEP 檔案", "application/step", "文氏管.STEP", "key9")
download_file(r"Y:/a/downloads/Venturi_Geom_3d.zip", "下載 Venturi_Geom_3d.zip", "application/zip", "Venturi_Geom_3d.zip", "key10")
download_file(r"Y:/a/downloads/Venturi_Geom_2d.zip", "下載 Venturi_Geom_2d.zip", "application/zip", "Venturi_Geom_2d.zip", "key11")
st.markdown("---")  # 分隔線

# 下載文件4(管路摩擦損失)
download_file(r"Y:/a/downloads/實驗4. 黏滯係數量測.pdf", "實驗4. 黏滯係數量測 PDF 檔案", "application/pdf", "實驗4. 黏滯係數量測.pdf", "key12")
download_file(r"Y:/a/downloads/實驗4. 黏滯係數量測.doc", "實驗4. 黏滯係數量測 DOC 檔案", "application/msword", "實驗4. 黏滯係數量測.doc", "key13")
download_file(r"Y:/a/downloads/實驗4. 黏滯係數量測.xlsx", "實驗4. 黏滯係數量測.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "實驗4. 黏滯係數量測.xlsx", "key14")
st.markdown("---")  # 分隔線

# 下載文件5(溫度與散熱實驗)
download_file(r"Y:/a/downloads/實驗5. 溫度與散熱實驗.pdf", "下載 實驗5. 溫度與散熱實驗 PDF 檔案", "application/pdf", "實驗5. 溫度與散熱實驗.pdf", "key15")
download_file(r"Y:/a/downloads/實驗5. 溫度與散熱實驗.doc", "下載 實驗5. 溫度與散熱實驗 DOC 檔案", "application/msword", "實驗5. 溫度與散熱實驗.doc", "key16")
st.markdown("---")  # 分隔線

# 下載文件6 (真空抽氣性能實驗)
download_file(r"Y:/a/downloads/實驗6. 真空抽氣性能實驗.pdf", "下載 實驗6. 真空抽氣性能實驗.pdf", "application/pdf", "實驗6. 真空抽氣性能實驗.pdf", "key17")
download_file(r"Y:/a/downloads/實驗6. 真空抽氣性能實驗.doc", "下載 實驗6. 真空抽氣性能實驗.doc", "application/msword", "實驗6. 真空抽氣性能實驗.doc", "key18")
download_file("Y:/a/downloads/final.stp", "下載 真空管.stp", "application/stp", "final.stp", "key19")
download_file(r"Y:/a/downloads/實驗6. 真空抽氣性能實驗.xls", "下載 實驗6. 真空抽氣性能實驗.xls", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "實驗6. 真空抽氣性能實驗.xls", "key20")
download_file(r"Y:/a/downloads/Vacuum Generator Design(1131225)template.xlsx", "下載 Vacuum Generator Design(1131225)template.xlsx", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "Vacuum Generator Design(1131225)template.xlsx", "key21")
st.markdown("---")  # 分隔線

# 下載 ZIP 文件 (Venturi Geom)
download_file(r"Y:/a/downloads/Venturi_Geom_3d.zip", "下載 Venturi_Geom_3d.zip", "application/zip", "Venturi_Geom_3d.zip", "key22")
download_file(r"Y:/a/downloads/Venturi_Geom_2d.zip", "下載 Venturi_Geom_2d.zip", "application/zip", "Venturi_Geom_2d.zip", "key23")
download_file(r"Y:/a/downloads/3D(Generator).zip", "下載 3D(Generator).zip", "application/zip", "3D(Generator).zip", "key24")
st.markdown("---")  # 分隔線

# 下載文件(期末報告)
download_file(r"Y:/a/downloads/(113上)期末報告(template).pdf", "(113上)期末報告(template).pdf", "application/pdf", "(113上)期末報告(template).pdf", "key25")
download_file(r"Y:/a/downloads/(113上)期末報告(template).doc", "(113上)期末報告(template).doc", "application/msword", "(113上)期末報告(template).doc", "key26")
