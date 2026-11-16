import streamlit as st

st.title("🛒แอปพลิเคชั่นส่วนลดและ VAT 7%")

price = st.number_input("กรอกราคาสินค้า (บาท):", min_value=0.0 , value=0.0)
price = st.number_input("กรอกส่วนลด (เปอร์เซ็นต์):", min_value=0.0 , value=0.0)

discount = price * (percent/100)
vat = price * 0.07
net_price = discount + vat

st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")
st.header(f"• ราคาสุทธิ: {discount:.2f} บาท")
st.header(f"• ราคาสุทธิ: {percent:.2f} เปอร์เซ็นต์")
st.header(f"• ราคาสุทธิ: {price:.2f} บาท")
st.divider()
st.write("นายธนภัทร บารมี เลขที่ 25  ม.4/5")
