import streamlit as st
import requests

# ===== CONFIG =====
BACKEND_URL = "https://patient-discharge-decision-agent.onrender.com/api/v1/decide-discharge"

st.set_page_config(
    page_title="Patient Discharge Decision Agent",
    page_icon="🏥",
    layout="centered"
)

# ===== HEADER =====
st.markdown(
    """
    <h1 style='text-align: center;'>🏥 Patient Discharge Decision Agent</h1>
    <p style='text-align: center; color: gray;'>
    Decision Intelligence for safer, explainable hospital discharge decisions
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# ===== INPUT FORM =====
st.subheader("🧾 Enter Patient Details")

with st.form("patient_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 18, 100, 45)
        heart_rate = st.number_input("Heart Rate (bpm)", 40, 150, 85)
        systolic_bp = st.number_input("Systolic BP (mmHg)", 70, 200, 120)

    with col2:
        oxygen = st.number_input("Oxygen Saturation (%)", 70, 100, 95)
        days = st.number_input("Days Admitted", 1, 60, 3)
        prev = st.number_input("Previous Readmissions", 0, 10, 0)

    submitted = st.form_submit_button("🚀 Run Decision Intelligence")

# ===== API CALL =====
if submitted:
    payload = {
        "patient_id": "ui-demo",
        "age": int(age),
        "heart_rate": int(heart_rate),
        "systolic_bp": int(systolic_bp),
        "oxygen_level": int(oxygen),
        "days_admitted": int(days),
        "previous_readmissions": int(prev)
    }

    with st.spinner("Analyzing patient data and running decision intelligence..."):
        try:
            response = requests.post(BACKEND_URL, json=payload, timeout=120)

            if response.status_code == 200:
                data = response.json()

                st.divider()
                st.subheader("📊 Decision Result")

                # Decision Badge
                decision = data.get("decision", "UNKNOWN")

                if decision == "DISCHARGE":
                    st.success(f"✅ Decision: {decision}")
                elif decision == "DELAY_DISCHARGE":
                    st.warning(f"⏳ Decision: {decision}")
                else:
                    st.error(f"🚨 Decision: {decision}")

                # Metrics
                col1, col2 = st.columns(2)
                col1.metric("Risk Score", data.get("risk_score", "N/A"))
                col2.metric("Model Used", data.get("model_used", "N/A"))

                # Explanations
                st.subheader("🧠 Explanation & Reasoning")
                for exp in data.get("explanations", []):
                    st.write(f"• {exp}")

            else:
                st.error(f"Backend error: {response.status_code}")
                st.text(response.text)

        except Exception as e:
            st.error("Could not connect to backend service.")
            st.text(str(e))

# ===== FOOTER =====
st.divider()
st.markdown(
    """
    <p style='text-align: center; color: gray; font-size: 12px;'>
    Built as a Decision Intelligence platform with ML + Rules + Explainability.<br>
    Live backend powered by FastAPI on Render.
    </p>
    """,
    unsafe_allow_html=True
)
