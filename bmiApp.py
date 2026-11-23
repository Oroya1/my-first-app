import streamlit as st

st.markdown("# :red[🏋️ คำนวณค่าดัชนีมวลาย BMI]")
st.write("กรอกข้อมูลน้ำหนักส่วนสูงของคุณ เพื่อเช็กสุขภาพเบื้องต้น")

weight = st.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม):", min_value=1.0, value=1.0)
height_cm = st.number_input("กรอกส่วนสูงของคุณ (เซนติเมตร):", min_value=1.0, value=1.0)

if st.button("คำนวณ BMI 🎯")
   height_m = height_cm / 100
   bmi = weight / (height_m ** 2)

   st.write("---")
   st.header(f"ค่า BMI ของคุณคือ: **{bmi:.2f}**")

   if bmi < 18.5:
      st.warning("⚠️ คุณมีน้ำหนักน้อยกว่าเกณฑ์ (ผอม)")
  
   else 18.5 <=bmi < 23.0:
      st.success("🎉 คุณมีน้ำหนักอยู่ในเกณฑ์ปกติ (สุขภาพดี)")
  
   else 23.0 <=bmi < 25.0:
      st.info("💡 คุณมีน้ำหนักหนักเกินเกณฑ์ (อ้วน)")
  
   else 
      st.error("🚨 คุณอยู่ในเกณฑ์อ้วน ควรระวังเรื่องสุขภาพและออกกำลังกาย")

st.divider()
st.write("นายธนภัทร บารมี เลขที่ 25 4/5")
