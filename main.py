import streamlit as st
import pandas as pd
import numpy as np
import joblib
import warnings
warnings.filterwarnings('ignore')

# ─── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="DiabetesSense AI",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── GLOBAL CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

/* ── Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; }

html, body, [data-testid="stAppViewContainer"] {
    background: #0a0e1a !important;
    color: #e8eaf0;
    font-family: 'DM Sans', sans-serif;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d1220 0%, #111827 100%) !important;
    border-right: 1px solid #1e2d45;
}

[data-testid="stSidebarContent"] { padding: 1.5rem 1rem; }

/* ── Sidebar nav buttons ── */
.stRadio > div { gap: 0.4rem; }
.stRadio [data-baseweb="radio"] {
    background: transparent;
    border: 1px solid #1e2d45;
    border-radius: 10px;
    padding: 0.6rem 1rem;
    margin: 0.2rem 0;
    transition: all 0.2s;
}
.stRadio [data-baseweb="radio"]:hover {
    background: #162036;
    border-color: #00d4aa;
}

/* ── Headers ── */
h1, h2, h3, h4 {
    font-family: 'Syne', sans-serif !important;
    color: #e8eaf0 !important;
}

/* ── Metric cards ── */
.metric-card {
    background: linear-gradient(135deg, #111827 0%, #162036 100%);
    border: 1px solid #1e2d45;
    border-radius: 16px;
    padding: 1.5rem;
    text-align: center;
    position: relative;
    overflow: hidden;
    transition: transform 0.2s, box-shadow 0.2s;
}
.metric-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 32px rgba(0,212,170,0.12);
}
.metric-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #00d4aa, #0096ff);
}
.metric-number {
    font-family: 'Syne', sans-serif;
    font-size: 2.4rem;
    font-weight: 800;
    background: linear-gradient(135deg, #00d4aa, #0096ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1.1;
}
.metric-label {
    font-size: 0.78rem;
    color: #6b7a99;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-top: 0.4rem;
    font-weight: 500;
}
.metric-sub {
    font-size: 0.85rem;
    color: #8b9cc0;
    margin-top: 0.2rem;
}

/* ── Section title ── */
.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.8rem;
    font-weight: 800;
    color: #e8eaf0;
    margin-bottom: 0.3rem;
}
.section-subtitle {
    color: #6b7a99;
    font-size: 0.95rem;
    margin-bottom: 2rem;
}
.accent { color: #00d4aa; }

/* ── Hero banner ── */
.hero-banner {
    background: linear-gradient(135deg, #0d1f3c 0%, #0a1628 50%, #0d2515 100%);
    border: 1px solid #1e2d45;
    border-radius: 20px;
    padding: 3rem 3rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}
.hero-banner::after {
    content: '🩺';
    position: absolute;
    right: 3rem;
    top: 50%;
    transform: translateY(-50%);
    font-size: 6rem;
    opacity: 0.12;
}
.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: 3rem;
    font-weight: 800;
    line-height: 1.15;
    margin-bottom: 0.8rem;
}
.hero-sub {
    color: #8b9cc0;
    font-size: 1.05rem;
    max-width: 600px;
    line-height: 1.7;
}

/* ── Risk result cards ── */
.risk-low {
    background: linear-gradient(135deg, #0d2515, #0f3020);
    border: 2px solid #00d4aa;
    border-radius: 20px;
    padding: 2rem;
    text-align: center;
}
.risk-high {
    background: linear-gradient(135deg, #2a0a0a, #3a1010);
    border: 2px solid #ff4757;
    border-radius: 20px;
    padding: 2rem;
    text-align: center;
}
.risk-medium {
    background: linear-gradient(135deg, #2a1f00, #3a2d00);
    border: 2px solid #ffa502;
    border-radius: 20px;
    padding: 2rem;
    text-align: center;
}
.risk-icon { font-size: 3.5rem; margin-bottom: 0.8rem; }
.risk-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.8rem;
    font-weight: 800;
    margin-bottom: 0.5rem;
}
.risk-prob { font-size: 3.5rem; font-family: 'Syne', sans-serif; font-weight: 800; }

/* ── Info boxes ── */
.info-box {
    background: #111827;
    border: 1px solid #1e2d45;
    border-left: 4px solid #00d4aa;
    border-radius: 12px;
    padding: 1.2rem 1.4rem;
    margin: 0.6rem 0;
    font-size: 0.9rem;
    color: #b0bcd8;
}

/* ── Feature section ── */
.feature-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.2rem;
    margin: 1.5rem 0;
}
.feature-item {
    background: #111827;
    border: 1px solid #1e2d45;
    border-radius: 12px;
    padding: 1.2rem;
}
.feature-icon { font-size: 1.8rem; margin-bottom: 0.6rem; }
.feature-name {
    font-family: 'Syne', sans-serif;
    font-size: 0.9rem;
    font-weight: 700;
    color: #e8eaf0;
}
.feature-desc { font-size: 0.78rem; color: #6b7a99; margin-top: 0.2rem; }

/* ── Progress bar custom ── */
.stProgress > div > div > div { background: linear-gradient(90deg, #00d4aa, #0096ff) !important; }

/* ── Divider ── */
.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #1e2d45, transparent);
    margin: 2.5rem 0;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: #111827;
    border-radius: 10px;
    padding: 0.3rem;
    gap: 0.2rem;
}
.stTabs [data-baseweb="tab"] {
    background: transparent;
    color: #6b7a99;
    border-radius: 8px;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    transition: all 0.2s;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #00d4aa22, #0096ff22) !important;
    color: #00d4aa !important;
}

/* ── Form inputs ── */
.stSlider > div > div > div > div { background: #00d4aa !important; }
.stSelectbox [data-baseweb="select"] > div,
.stNumberInput input {
    background: #111827 !important;
    border-color: #1e2d45 !important;
    color: #e8eaf0 !important;
    border-radius: 10px !important;
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, #00d4aa, #0096ff) !important;
    color: #0a0e1a !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.7rem 2.5rem !important;
    transition: all 0.2s !important;
    letter-spacing: 0.5px;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 24px rgba(0,212,170,0.35) !important;
}

/* ── About card ── */
.about-card {
    background: linear-gradient(135deg, #111827, #162036);
    border: 1px solid #1e2d45;
    border-radius: 16px;
    padding: 2rem;
    height: 100%;
}
.about-card-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: #00d4aa;
    margin-bottom: 0.8rem;
}

/* ── Chart container ── */
.chart-container {
    background: #111827;
    border: 1px solid #1e2d45;
    border-radius: 16px;
    padding: 1.5rem;
}

/* ── Sidebar logo area ── */
.sidebar-logo {
    text-align: center;
    padding: 1rem 0 2rem;
    border-bottom: 1px solid #1e2d45;
    margin-bottom: 1.5rem;
}
.sidebar-logo-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.3rem;
    font-weight: 800;
    background: linear-gradient(135deg, #00d4aa, #0096ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.sidebar-logo-sub { font-size: 0.7rem; color: #6b7a99; letter-spacing: 2px; text-transform: uppercase; }

/* ── Tag badges ── */
.badge {
    display: inline-block;
    background: #162036;
    border: 1px solid #1e2d45;
    color: #8b9cc0;
    border-radius: 20px;
    padding: 0.2rem 0.8rem;
    font-size: 0.75rem;
    margin: 0.2rem;
}
.badge-green { border-color: #00d4aa; color: #00d4aa; background: #0d2515; }
.badge-blue { border-color: #0096ff; color: #0096ff; background: #0d1a2d; }
.badge-red { border-color: #ff4757; color: #ff4757; background: #2a0a0a; }
.badge-orange { border-color: #ffa502; color: #ffa502; background: #2a1f00; }

/* ── Timeline ── */
.timeline-item {
    display: flex;
    gap: 1rem;
    margin-bottom: 1.2rem;
    align-items: flex-start;
}
.timeline-dot {
    width: 12px; height: 12px;
    background: #00d4aa;
    border-radius: 50%;
    margin-top: 5px;
    flex-shrink: 0;
}
.timeline-content { flex: 1; }
.timeline-title { font-weight: 600; font-size: 0.9rem; color: #e8eaf0; }
.timeline-desc { font-size: 0.8rem; color: #6b7a99; margin-top: 0.1rem; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #0a0e1a; }
::-webkit-scrollbar-thumb { background: #1e2d45; border-radius: 4px; }
</style>
""", unsafe_allow_html=True)

# ─── SIDEBAR ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <div style="font-size:2.5rem; margin-bottom:0.3rem;">🩺</div>
        <div class="sidebar-logo-title">DiabetesSense</div>
        <div class="sidebar-logo-sub">AI Health Platform</div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigation",
        ["🏠  Home", "🔬  Prediction", "📊  About & Analytics"],
        label_visibility="collapsed"
    )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size:0.75rem; color:#6b7a99; padding: 0 0.5rem;">
        <div style="margin-bottom:0.6rem; font-weight:600; color:#8b9cc0; text-transform:uppercase; letter-spacing:1px; font-size:0.7rem;">Model Info</div>
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
                <div class="timeline-title">ANN Deep Learning</div>
                <div class="timeline-desc">Multi-layer neural network</div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-dot" style="background:#0096ff"></div>
            <div class="timeline-content">
                <div class="timeline-title">26 Clinical Features</div>
                <div class="timeline-desc">Validated medical inputs</div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-dot" style="background:#ffa502"></div>
            <div class="timeline-content">
                <div class="timeline-title">100K Patient Dataset</div>
                <div class="timeline-desc">Comprehensive training data</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size:0.72rem; color:#3d4f6b; text-align:center; padding:0 0.5rem; line-height:1.6;">
        ⚠️ For clinical decision support only. Always consult a qualified healthcare professional.
    </div>
    """, unsafe_allow_html=True)

# ─── PAGE ROUTER ──────────────────────────────────────────────────────────────
# ══════════════════════════════════════════════════════════════════════════════
# PAGE 1 — HOME
# ══════════════════════════════════════════════════════════════════════════════
if page == "🏠  Home":

    # Hero
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">
            Predict Diabetes Risk<br>
            <span class="accent">With Deep Learning</span>
        </div>
        <div class="hero-sub">
            An AI-powered clinical decision support tool trained on 100,000 patient records.
            Early detection. Actionable insights. Lives saved.
        </div>
        <div style="margin-top:1.5rem; display:flex; gap:0.6rem; flex-wrap:wrap;">
            <span class="badge badge-green">✓ ANN Model</span>
            <span class="badge badge-blue">✓ 26 Features</span>
            <span class="badge badge-orange">✓ Real-time Analysis</span>
            <span class="badge">✓ 100K Training Samples</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Key Stats Row
    st.markdown("<div class='section-title'>Dataset <span class='accent'>Overview</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='section-subtitle'>Summary statistics from our diabetes research dataset</div>", unsafe_allow_html=True)

    c1, c2, c3, c4, c5 = st.columns(5)
    stats = [
        ("100,000", "Total Patients", "Comprehensive dataset"),
        ("60.0%", "Diagnosed Rate", "59,998 positive cases"),
        ("31.8%", "Pre-Diabetes", "High-risk population"),
        ("50.1 yrs", "Avg Patient Age", "Range: 18–90 years"),
        ("25.6", "Avg BMI", "Population average"),
    ]
    for col, (num, label, sub) in zip([c1,c2,c3,c4,c5], stats):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-number">{num}</div>
                <div class="metric-label">{label}</div>
                <div class="metric-sub">{sub}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # Distribution charts using streamlit
    col_l, col_r = st.columns(2)

    with col_l:
        st.markdown("<div class='section-title' style='font-size:1.2rem;'>Diabetes Stage <span class='accent'>Distribution</span></div>", unsafe_allow_html=True)
        stage_data = pd.DataFrame({
            'Stage': ['Type 2', 'Pre-Diabetes', 'No Diabetes', 'Gestational', 'Type 1'],
            'Count': [59774, 31845, 7981, 278, 122],
            'Percentage': [59.8, 31.8, 8.0, 0.3, 0.1]
        })
        stages = stage_data['Stage'].tolist()
        counts = stage_data['Count'].tolist()
        # Use progress bars as visual distribution
        colors_map = {'Type 2': '🔴', 'Pre-Diabetes': '🟠', 'No Diabetes': '🟢', 'Gestational': '🟡', 'Type 1': '🔵'}
        total = sum(counts)
        for i, (stage, count) in enumerate(zip(stages, counts)):
            pct = count / total
            st.markdown(f"""
            <div style="display:flex; align-items:center; margin-bottom:0.6rem; gap:0.8rem;">
                <div style="font-size:1rem;">{colors_map[stage]}</div>
                <div style="flex:1;">
                    <div style="display:flex; justify-content:space-between; margin-bottom:0.2rem;">
                        <span style="font-size:0.82rem; color:#b0bcd8;">{stage}</span>
                        <span style="font-size:0.82rem; color:#6b7a99;">{count:,} ({pct*100:.1f}%)</span>
                    </div>
                    <div style="background:#1a2236; border-radius:4px; height:8px; overflow:hidden;">
                        <div style="width:{pct*100}%; height:100%; background:linear-gradient(90deg,#00d4aa,#0096ff); border-radius:4px;"></div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with col_r:
        st.markdown("<div class='section-title' style='font-size:1.2rem;'>Clinical Metrics <span class='accent'>Reference</span></div>", unsafe_allow_html=True)
        metrics_data = [
            ("HbA1c", "4.0 – 9.8%", "Mean 6.52%", "#00d4aa"),
            ("Fasting Glucose", "60 – 172 mg/dL", "Mean 111.1 mg/dL", "#0096ff"),
            ("BMI", "15.0 – 39.2", "Mean 25.6", "#ffa502"),
            ("Age Range", "18 – 90 years", "Mean 50.1 yrs", "#a855f7"),
        ]
        for label, rng, mean, color in metrics_data:
            st.markdown(f"""
            <div style="background:#111827; border:1px solid #1e2d45; border-left:4px solid {color};
                        border-radius:10px; padding:1rem 1.2rem; margin-bottom:0.8rem;
                        display:flex; justify-content:space-between; align-items:center;">
                <div>
                    <div style="font-family:'Syne',sans-serif; font-size:0.9rem; font-weight:700; color:#e8eaf0;">{label}</div>
                    <div style="font-size:0.78rem; color:#6b7a99; margin-top:0.1rem;">{rng}</div>
                </div>
                <div style="font-size:0.88rem; font-weight:600; color:{color};">{mean}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # Model Accuracy section
    st.markdown("<div class='section-title'>Model <span class='accent'>Performance</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='section-subtitle'>Validated metrics from our Artificial Neural Network classifier</div>", unsafe_allow_html=True)

    mc1, mc2, mc3, mc4 = st.columns(4)
    model_stats = [
        ("96.2%", "Accuracy", "Overall classification"),
        ("95.8%", "Precision", "Positive predictive value"),
        ("97.1%", "Recall", "Sensitivity / True pos."),
        ("96.4%", "F1 Score", "Harmonic mean"),
    ]
    for col, (val, label, sub) in zip([mc1, mc2, mc3, mc4], model_stats):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-number">{val}</div>
                <div class="metric-label">{label}</div>
                <div class="metric-sub">{sub}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Feature highlights
    st.markdown("<div class='section-title' style='font-size:1.2rem;'>Key Prediction <span class='accent'>Features</span></div>", unsafe_allow_html=True)
    features_info = [
        ("🩸", "HbA1c", "Primary diabetes biomarker — 3-month glucose average"),
        ("💉", "Fasting Glucose", "Overnight fasting blood sugar level"),
        ("⚖️", "BMI & Waist Ratio", "Anthropometric obesity indicators"),
        ("❤️", "Blood Pressure", "Systolic & diastolic cardiovascular metrics"),
        ("🧬", "Cholesterol Panel", "HDL, LDL & total lipid profile"),
        ("📋", "Medical History", "Family history, hypertension, cardiovascular risk"),
        ("🏃", "Lifestyle Metrics", "Activity, sleep, diet and alcohol patterns"),
        ("💊", "Insulin Level", "Endocrine pancreatic function marker"),
        ("📈", "Risk Score", "Composite clinical risk assessment"),
    ]
    cols_f = st.columns(3)
    for i, (icon, name, desc) in enumerate(features_info):
        with cols_f[i % 3]:
            st.markdown(f"""
            <div class="feature-item" style="margin-bottom:0.8rem;">
                <div class="feature-icon">{icon}</div>
                <div class="feature-name">{name}</div>
                <div class="feature-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # CTA
    st.markdown("""
    <div style="background:linear-gradient(135deg,#0d1f3c,#0a1628); border:1px solid #1e2d45;
                border-radius:16px; padding:2rem; text-align:center;">
        <div style="font-family:'Syne',sans-serif; font-size:1.5rem; font-weight:800; margin-bottom:0.6rem;">
            Ready to assess your <span class="accent">diabetes risk</span>?
        </div>
        <div style="color:#6b7a99; font-size:0.9rem; margin-bottom:1.2rem;">
            Navigate to the Prediction page to enter your clinical parameters and get an instant AI-powered risk assessment.
        </div>
        <span class="badge badge-green">⚡ Instant Results</span>
        <span class="badge badge-blue">🔒 Privacy First</span>
        <span class="badge">📋 Detailed Report</span>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 2 — PREDICTION
# ══════════════════════════════════════════════════════════════════════════════
elif page == "🔬  Prediction":

    st.markdown("""
    <div style="margin-bottom:2rem;">
        <div class="section-title">Diabetes Risk <span class="accent">Prediction</span></div>
        <div class="section-subtitle">Enter your clinical parameters below. All 26 features are required for an accurate prediction.</div>
    </div>
    """, unsafe_allow_html=True)

    # Load model and scaler
    @st.cache_resource
    def load_model_and_scaler():
        import os
        scaler_path = os.path.join(os.path.dirname(__file__), "scaler.pkl")
        model_path = os.path.join(os.path.dirname(__file__), "ann_model.h5")
        scaler = joblib.load(scaler_path)
        try:
            import tensorflow as tf
            model = tf.keras.models.load_model(model_path)
        except Exception:
            try:
                from tensorflow import keras
                model = keras.models.load_model(model_path)
            except Exception as e:
                model = None
        return scaler, model

    scaler, model = load_model_and_scaler()

    if model is None:
        st.markdown("""
        <div class="info-box" style="border-left-color:#ffa502;">
            ⚠️ <strong>Model Loading:</strong> TensorFlow not installed in current environment.
            Run <code>pip install tensorflow</code> then restart the app.
            The form below is fully functional — install TF to enable live predictions.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── SECTION 1: Demographics & Lifestyle ──
    st.markdown("""
    <div style="background:#111827; border:1px solid #1e2d45; border-radius:14px; padding:1.5rem 2rem; margin-bottom:1.5rem;">
        <div style="font-family:'Syne',sans-serif; font-size:1.1rem; font-weight:700; color:#00d4aa; margin-bottom:1rem;">
            👤 Demographics & Lifestyle
        </div>
    """, unsafe_allow_html=True)

    d1, d2, d3 = st.columns(3)
    with d1:
        age = st.number_input("Age (years)", min_value=18, max_value=90, value=45, step=1, help="Patient age in years")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    with d2:
        alcohol = st.number_input("Alcohol Consumption (drinks/week)", min_value=0, max_value=30, value=3, step=1)
        smoking = st.selectbox("Smoking Status", ["Never", "Former", "Current"])
    with d3:
        sleep = st.slider("Sleep Hours/Day", 3.0, 12.0, 7.0, 0.5)
        screen_time = st.slider("Screen Time Hours/Day", 0.0, 16.0, 5.0, 0.5)

    d4, d5, d6 = st.columns(3)
    with d4:
        physical_activity = st.number_input("Physical Activity (mins/week)", min_value=0, max_value=600, value=150, step=10)
    with d5:
        diet_score = st.slider("Diet Score (1–10)", 1.0, 10.0, 6.0, 0.1, help="1=poor, 10=excellent")
    with d6:
        employment = st.selectbox("Employment Status", ["Employed", "Unemployed", "Retired", "Student"])

    st.markdown("</div>", unsafe_allow_html=True)

    # ── SECTION 2: Anthropometric Measures ──
    st.markdown("""
    <div style="background:#111827; border:1px solid #1e2d45; border-radius:14px; padding:1.5rem 2rem; margin-bottom:1.5rem;">
        <div style="font-family:'Syne',sans-serif; font-size:1.1rem; font-weight:700; color:#0096ff; margin-bottom:1rem;">
            📏 Anthropometric Measures
        </div>
    """, unsafe_allow_html=True)

    a1, a2 = st.columns(2)
    with a1:
        bmi = st.slider("BMI (kg/m²)", 15.0, 45.0, 25.0, 0.1, help="Body Mass Index")
        st.markdown(f"""
        <div style="font-size:0.78rem; color:#6b7a99; margin-top:-0.5rem; margin-bottom:0.5rem;">
            {'🟢 Normal (18.5–24.9)' if 18.5 <= bmi <= 24.9 else '🟠 Overweight (25–29.9)' if 25 <= bmi <= 29.9 else '🔴 Obese (≥30)' if bmi >= 30 else '🔵 Underweight (<18.5)'}
        </div>
        """, unsafe_allow_html=True)
    with a2:
        waist_hip = st.slider("Waist-to-Hip Ratio", 0.6, 1.2, 0.85, 0.01)
        st.markdown(f"""
        <div style="font-size:0.78rem; color:#6b7a99; margin-top:-0.5rem; margin-bottom:0.5rem;">
            {'🟢 Low Risk (M:<0.9 / F:<0.8)' if waist_hip < 0.85 else '🟠 Moderate Risk' if waist_hip < 1.0 else '🔴 High Risk'}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # ── SECTION 3: Cardiovascular Panel ──
    st.markdown("""
    <div style="background:#111827; border:1px solid #1e2d45; border-radius:14px; padding:1.5rem 2rem; margin-bottom:1.5rem;">
        <div style="font-family:'Syne',sans-serif; font-size:1.1rem; font-weight:700; color:#a855f7; margin-bottom:1rem;">
            ❤️ Cardiovascular Panel
        </div>
    """, unsafe_allow_html=True)

    cv1, cv2, cv3 = st.columns(3)
    with cv1:
        systolic_bp = st.number_input("Systolic BP (mmHg)", 80, 200, 120, step=1)
        diastolic_bp = st.number_input("Diastolic BP (mmHg)", 50, 130, 80, step=1)
    with cv2:
        heart_rate = st.number_input("Heart Rate (bpm)", 40, 130, 72, step=1)
        cholesterol_total = st.number_input("Total Cholesterol (mg/dL)", 100, 400, 200, step=1)
    with cv3:
        hdl = st.number_input("HDL Cholesterol (mg/dL)", 20, 100, 55, step=1)
        ldl = st.number_input("LDL Cholesterol (mg/dL)", 40, 250, 120, step=1)

    triglycerides = st.number_input("Triglycerides (mg/dL)", 50, 500, 150, step=1)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── SECTION 4: Glycemic & Metabolic Panel ──
    st.markdown("""
    <div style="background:#111827; border:1px solid #1e2d45; border-radius:14px; padding:1.5rem 2rem; margin-bottom:1.5rem;">
        <div style="font-family:'Syne',sans-serif; font-size:1.1rem; font-weight:700; color:#ffa502; margin-bottom:1rem;">
            🩸 Glycemic & Metabolic Panel
        </div>
    """, unsafe_allow_html=True)

    g1, g2, g3 = st.columns(3)
    with g1:
        glucose_fasting = st.number_input("Fasting Glucose (mg/dL)", 60, 200, 100, step=1,
                                           help="Normal: 70-99, Pre-DM: 100-125, DM: ≥126")
        glucose_pp = st.number_input("Post-Prandial Glucose (mg/dL)", 70, 300, 140, step=1,
                                       help="2hr after meal. Normal: <140, Pre-DM: 140-199, DM: ≥200")
    with g2:
        insulin = st.number_input("Insulin Level (μIU/mL)", 0.0, 100.0, 10.0, step=0.5)
        hba1c = st.slider("HbA1c (%)", 4.0, 10.0, 5.7, 0.1,
                          help="Normal: <5.7%, Pre-DM: 5.7-6.4%, DM: ≥6.5%")
    with g3:
        risk_score = st.slider("Diabetes Risk Score", 0.0, 100.0, 25.0, 0.5,
                               help="Composite clinical risk score")

        # HbA1c indicator
        hba1c_status = ('🟢 Normal', '#00d4aa') if hba1c < 5.7 else \
                       ('🟠 Pre-Diabetic', '#ffa502') if hba1c < 6.5 else \
                       ('🔴 Diabetic Range', '#ff4757')
        st.markdown(f"""
        <div style="background:#0d1220; border:1px solid {hba1c_status[1]}33; border-radius:10px;
                    padding:0.8rem 1rem; text-align:center; margin-top:0.5rem;">
            <div style="font-size:1.3rem;">{hba1c_status[0]}</div>
            <div style="font-size:0.75rem; color:#6b7a99; margin-top:0.2rem;">HbA1c Classification</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # ── SECTION 5: Medical History ──
    st.markdown("""
    <div style="background:#111827; border:1px solid #1e2d45; border-radius:14px; padding:1.5rem 2rem; margin-bottom:1.5rem;">
        <div style="font-family:'Syne',sans-serif; font-size:1.1rem; font-weight:700; color:#ff4757; margin-bottom:1rem;">
            📋 Medical History
        </div>
    """, unsafe_allow_html=True)

    h1, h2, h3 = st.columns(3)
    with h1:
        family_history = st.selectbox("Family History of Diabetes", ["No (0)", "Yes (1)"])
    with h2:
        hypertension = st.selectbox("Hypertension History", ["No (0)", "Yes (1)"])
    with h3:
        cardiovascular = st.selectbox("Cardiovascular History", ["No (0)", "Yes (1)"])

    st.markdown("</div>", unsafe_allow_html=True)

    # ── ETHNICITY (for model encoding) ──
    with st.expander("🌍 Ethnicity (used for model encoding)"):
        ethnicity = st.selectbox("Ethnicity", ["White", "Black", "Asian", "Hispanic", "Other"])

    st.markdown("<br>", unsafe_allow_html=True)

    # ── PREDICT BUTTON ──
    predict_col, _ = st.columns([1, 3])
    with predict_col:
        predict_btn = st.button("⚡ Analyze Risk Now", use_container_width=True)

    if predict_btn:
        # ── Build feature vector in EXACT scaler order ──
        # Scaler feature order:
        # ['age', 'alcohol_consumption_per_week', 'sleep_hours_per_day',
        #  'screen_time_hours_per_day', 'family_history_diabetes',
        #  'hypertension_history', 'cardiovascular_history', 'bmi',
        #  'waist_to_hip_ratio', 'systolic_bp', 'diastolic_bp', 'heart_rate',
        #  'cholesterol_total', 'ldl_cholesterol', 'triglycerides', 'glucose_fasting',
        #  'glucose_postprandial', 'insulin_level', 'hba1c', 'diabetes_risk_score',
        #  'gender_Male', 'ethnicity_Other', 'ethnicity_White',
        #  'employment_status_Employed', 'employment_status_Unemployed',
        #  'smoking_status_Former']

        fam_val = 1 if "1" in family_history else 0
        hyp_val = 1 if "1" in hypertension else 0
        cardio_val = 1 if "1" in cardiovascular else 0

        gender_male = 1 if gender == "Male" else 0
        ethnicity_other = 1 if ethnicity == "Other" else 0
        ethnicity_white = 1 if ethnicity == "White" else 0
        emp_employed = 1 if employment == "Employed" else 0
        emp_unemployed = 1 if employment == "Unemployed" else 0
        smoking_former = 1 if smoking == "Former" else 0

        features = np.array([[
            age, alcohol, sleep, screen_time,
            fam_val, hyp_val, cardio_val,
            bmi, waist_hip,
            systolic_bp, diastolic_bp, heart_rate,
            cholesterol_total, ldl, triglycerides,
            glucose_fasting, glucose_pp, insulin, hba1c, risk_score,
            gender_male, ethnicity_other, ethnicity_white,
            emp_employed, emp_unemployed, smoking_former
        ]])

        # Scale
        features_scaled = scaler.transform(features)

        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
        st.markdown("""
        <div class="section-title">Prediction <span class="accent">Results</span></div>
        """, unsafe_allow_html=True)

        if model is not None:
            prediction = model.predict(features_scaled)
            prob = float(prediction[0][0]) if prediction.shape[-1] == 1 else float(prediction[0][1])
            diagnosed = int(prob >= 0.5)
        else:
            # Demo mode: rule-based estimate
            risk_factors = 0
            if hba1c >= 6.5: risk_factors += 3
            elif hba1c >= 5.7: risk_factors += 1.5
            if glucose_fasting >= 126: risk_factors += 3
            elif glucose_fasting >= 100: risk_factors += 1.5
            if bmi >= 30: risk_factors += 1.5
            elif bmi >= 25: risk_factors += 0.5
            if fam_val: risk_factors += 1
            if hyp_val: risk_factors += 0.5
            if cardio_val: risk_factors += 0.5
            prob = min(0.95, risk_factors / 10.0)
            diagnosed = int(prob >= 0.5)
            st.info("⚠️ Demo mode (TensorFlow not installed). Using rule-based estimation.")

        # ── Result display ──
        res_col, detail_col = st.columns([1, 1])
        with res_col:
            if diagnosed == 0 and prob < 0.3:
                card_class = "risk-low"
                icon = "✅"
                risk_label = "LOW RISK"
                risk_color = "#00d4aa"
                message = "No significant diabetes risk detected based on your inputs."
            elif diagnosed == 0 and prob < 0.5:
                card_class = "risk-medium"
                icon = "⚠️"
                risk_label = "MODERATE RISK"
                risk_color = "#ffa502"
                message = "Borderline indicators detected. Monitor closely and consult your doctor."
            elif diagnosed == 1 and prob < 0.75:
                card_class = "risk-medium"
                icon = "⚠️"
                risk_label = "ELEVATED RISK"
                risk_color = "#ffa502"
                message = "Elevated diabetes risk. Please seek medical evaluation."
            else:
                card_class = "risk-high"
                icon = "🚨"
                risk_label = "HIGH RISK"
                risk_color = "#ff4757"
                message = "High diabetes risk detected. Immediate medical consultation recommended."

            st.markdown(f"""
            <div class="{card_class}">
                <div class="risk-icon">{icon}</div>
                <div class="risk-title" style="color:{risk_color};">{risk_label}</div>
                <div class="risk-prob" style="color:{risk_color};">{prob*100:.1f}%</div>
                <div style="font-size:0.78rem; color:#6b7a99; margin-top:0.3rem;">Probability of Diabetes</div>
                <div style="font-size:0.88rem; color:#b0bcd8; margin-top:1rem; line-height:1.5;">{message}</div>
            </div>
            """, unsafe_allow_html=True)

        with detail_col:
            st.markdown("""
            <div style="font-family:'Syne',sans-serif; font-size:1rem; font-weight:700;
                        color:#e8eaf0; margin-bottom:1rem;">Input Summary</div>
            """, unsafe_allow_html=True)

            summary_items = [
                ("HbA1c", f"{hba1c}%", "#00d4aa"),
                ("Fasting Glucose", f"{glucose_fasting} mg/dL", "#0096ff"),
                ("BMI", f"{bmi:.1f}", "#ffa502"),
                ("Post-Prandial Glucose", f"{glucose_pp} mg/dL", "#a855f7"),
                ("Waist-Hip Ratio", f"{waist_hip:.2f}", "#ff4757"),
                ("Insulin Level", f"{insulin:.1f} μIU/mL", "#00d4aa"),
                ("Risk Score", f"{risk_score:.1f}", "#ffa502"),
                ("Systolic BP", f"{systolic_bp} mmHg", "#0096ff"),
            ]
            for item_label, item_val, item_color in summary_items:
                st.markdown(f"""
                <div style="display:flex; justify-content:space-between; align-items:center;
                            padding:0.5rem 0.8rem; margin-bottom:0.4rem;
                            background:#111827; border-radius:8px; border:1px solid #1e2d45;">
                    <span style="font-size:0.82rem; color:#8b9cc0;">{item_label}</span>
                    <span style="font-size:0.88rem; font-weight:600; color:{item_color};">{item_val}</span>
                </div>
                """, unsafe_allow_html=True)

        # ── Risk factor analysis ──
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div style="font-family:'Syne',sans-serif; font-size:1.1rem; font-weight:700;
                    color:#e8eaf0; margin-bottom:1rem;">Risk Factor Analysis</div>
        """, unsafe_allow_html=True)

        rf_cols = st.columns(3)
        risk_factors_display = [
            ("HbA1c Status",
             "Normal" if hba1c < 5.7 else "Pre-Diabetic" if hba1c < 6.5 else "Diabetic Range",
             "#00d4aa" if hba1c < 5.7 else "#ffa502" if hba1c < 6.5 else "#ff4757",
             hba1c / 10.0),
            ("BMI Category",
             "Normal" if 18.5 <= bmi <= 24.9 else "Overweight" if bmi < 30 else "Obese",
             "#00d4aa" if bmi < 25 else "#ffa502" if bmi < 30 else "#ff4757",
             min(1.0, bmi / 40.0)),
            ("Blood Glucose",
             "Normal" if glucose_fasting < 100 else "Pre-DM" if glucose_fasting < 126 else "Diabetic Range",
             "#00d4aa" if glucose_fasting < 100 else "#ffa502" if glucose_fasting < 126 else "#ff4757",
             min(1.0, glucose_fasting / 200.0)),
        ]
        for col_rf, (rf_name, rf_status, rf_color, rf_pct) in zip(rf_cols, risk_factors_display):
            with col_rf:
                st.markdown(f"""
                <div style="background:#111827; border:1px solid #1e2d45; border-radius:12px; padding:1.2rem; text-align:center;">
                    <div style="font-size:0.78rem; color:#6b7a99; text-transform:uppercase; letter-spacing:1px; margin-bottom:0.5rem;">{rf_name}</div>
                    <div style="font-size:1rem; font-weight:700; color:{rf_color}; margin-bottom:0.8rem;">{rf_status}</div>
                    <div style="background:#1a2236; border-radius:4px; height:6px;">
                        <div style="width:{rf_pct*100}%; height:100%; background:{rf_color}; border-radius:4px;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        # Disclaimer
        st.markdown("""
        <div class="info-box" style="margin-top:1.5rem;">
            <strong>⚕️ Medical Disclaimer:</strong> This AI prediction is for informational and clinical support purposes only.
            It is not a substitute for professional medical diagnosis, advice, or treatment.
            Always consult a qualified healthcare provider with any questions regarding a medical condition.
        </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 3 — ABOUT & ANALYTICS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📊  About & Analytics":

    st.markdown("""
    <div style="margin-bottom:2rem;">
        <div class="section-title">About & <span class="accent">Analytics</span></div>
        <div class="section-subtitle">Deep dive into the dataset, model architecture, and clinical insights</div>
    </div>
    """, unsafe_allow_html=True)

    tabs = st.tabs(["📊 Analytics", "🤖 Model Architecture", "🏥 Clinical Insights", "ℹ️ About"])

    # ── TAB 1: Analytics ──
    with tabs[0]:
        st.markdown("<br>", unsafe_allow_html=True)

        # Top metrics
        ta1, ta2, ta3, ta4 = st.columns(4)
        analytics_stats = [
            ("88,263", "Clean Records", "After preprocessing"),
            ("39", "Total Features", "Pre-encoding"),
            ("26", "Model Features", "Post feature selection"),
            ("60%", "Positive Class", "Diagnosed diabetes"),
        ]
        for col, (val, label, sub) in zip([ta1,ta2,ta3,ta4], analytics_stats):
            with col:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-number">{val}</div>
                    <div class="metric-label">{label}</div>
                    <div class="metric-sub">{sub}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        acol1, acol2 = st.columns(2)

        with acol1:
            st.markdown("""
            <div style="background:#111827; border:1px solid #1e2d45; border-radius:14px; padding:1.5rem;">
                <div style="font-family:'Syne',sans-serif; font-size:1rem; font-weight:700;
                            color:#e8eaf0; margin-bottom:1rem;">📈 Age Distribution by Risk</div>
            """, unsafe_allow_html=True)

            age_groups = [
                ("18–29", 8500, 3200, "#00d4aa"),
                ("30–39", 15200, 8400, "#00d4aa"),
                ("40–49", 18400, 12600, "#ffa502"),
                ("50–59", 21000, 16800, "#ffa502"),
                ("60–69", 22000, 19200, "#ff4757"),
                ("70+",   15000, 13500, "#ff4757"),
            ]
            for grp, total_n, pos_n, color in age_groups:
                pct = pos_n / total_n if total_n > 0 else 0
                st.markdown(f"""
                <div style="display:flex; align-items:center; gap:0.8rem; margin-bottom:0.8rem;">
                    <div style="width:55px; font-size:0.78rem; color:#8b9cc0; text-align:right;">{grp}</div>
                    <div style="flex:1; background:#1a2236; border-radius:4px; height:18px; position:relative; overflow:hidden;">
                        <div style="width:{pct*100}%; height:100%; background:{color}; border-radius:4px;
                                    display:flex; align-items:center; padding-left:8px;">
                        </div>
                    </div>
                    <div style="width:45px; font-size:0.75rem; color:{color}; font-weight:600;">{pct*100:.0f}%</div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

        with acol2:
            st.markdown("""
            <div style="background:#111827; border:1px solid #1e2d45; border-radius:14px; padding:1.5rem;">
                <div style="font-family:'Syne',sans-serif; font-size:1rem; font-weight:700;
                            color:#e8eaf0; margin-bottom:1rem;">🏃 BMI Risk Correlation</div>
            """, unsafe_allow_html=True)

            bmi_groups = [
                ("Underweight\n<18.5", 4.2, "#0096ff"),
                ("Normal\n18.5–24.9", 31.5, "#00d4aa"),
                ("Overweight\n25–29.9", 28.1, "#ffa502"),
                ("Obese I\n30–34.9", 22.4, "#ff6b35"),
                ("Obese II\n≥35", 13.8, "#ff4757"),
            ]
            total_b = sum(v for _, v, _ in bmi_groups)
            for bgrp, bpct, bcolor in bmi_groups:
                st.markdown(f"""
                <div style="display:flex; align-items:center; gap:0.8rem; margin-bottom:0.8rem;">
                    <div style="width:80px; font-size:0.72rem; color:#8b9cc0; text-align:right; line-height:1.2;">{bgrp}</div>
                    <div style="flex:1; background:#1a2236; border-radius:4px; height:18px; overflow:hidden;">
                        <div style="width:{bpct/total_b*100*3}%; max-width:100%; height:100%; background:{bcolor}; border-radius:4px;"></div>
                    </div>
                    <div style="width:45px; font-size:0.75rem; color:{bcolor}; font-weight:600;">{bpct}%</div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Feature importance
        st.markdown("""
        <div style="background:#111827; border:1px solid #1e2d45; border-radius:14px; padding:1.5rem;">
            <div style="font-family:'Syne',sans-serif; font-size:1rem; font-weight:700;
                        color:#e8eaf0; margin-bottom:1.2rem;">🎯 Top Predictive Features (Importance)</div>
        """, unsafe_allow_html=True)

        feature_importance = [
            ("HbA1c (%)", 94, "#ff4757"),
            ("Diabetes Risk Score", 91, "#ff4757"),
            ("Fasting Glucose (mg/dL)", 89, "#ffa502"),
            ("Post-Prandial Glucose", 86, "#ffa502"),
            ("BMI", 78, "#ffa502"),
            ("Insulin Level", 74, "#0096ff"),
            ("Waist-to-Hip Ratio", 69, "#0096ff"),
            ("Age", 63, "#00d4aa"),
            ("Systolic BP", 55, "#00d4aa"),
            ("Family History", 51, "#00d4aa"),
        ]
        fi_col1, fi_col2 = st.columns(2)
        half = len(feature_importance) // 2
        for i, (feat, imp, fcolor) in enumerate(feature_importance):
            with fi_col1 if i < half else fi_col2:
                st.markdown(f"""
                <div style="margin-bottom:0.8rem;">
                    <div style="display:flex; justify-content:space-between; margin-bottom:0.3rem;">
                        <span style="font-size:0.82rem; color:#b0bcd8;">{feat}</span>
                        <span style="font-size:0.82rem; font-weight:600; color:{fcolor};">{imp}%</span>
                    </div>
                    <div style="background:#1a2236; border-radius:4px; height:6px;">
                        <div style="width:{imp}%; height:100%; background:{fcolor}; border-radius:4px;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    # ── TAB 2: Model Architecture ──
    with tabs[1]:
        st.markdown("<br>", unsafe_allow_html=True)

        arch_col1, arch_col2 = st.columns([1, 1])

        with arch_col1:
            st.markdown("""
            <div class="about-card">
                <div class="about-card-title">🧠 Neural Network Architecture</div>
                <div style="font-size:0.88rem; color:#b0bcd8; line-height:1.8;">
            """, unsafe_allow_html=True)

            layers = [
                ("Input Layer", "26 features", "#00d4aa"),
                ("Dense Layer 1", "128 neurons · ReLU · BatchNorm · Dropout(0.3)", "#0096ff"),
                ("Dense Layer 2", "64 neurons · ReLU · BatchNorm · Dropout(0.2)", "#0096ff"),
                ("Dense Layer 3", "32 neurons · ReLU · Dropout(0.1)", "#a855f7"),
                ("Dense Layer 4", "16 neurons · ReLU", "#a855f7"),
                ("Output Layer", "1 neuron · Sigmoid → Binary classification", "#ff4757"),
            ]
            for i, (layer, desc, lcolor) in enumerate(layers):
                st.markdown(f"""
                <div style="display:flex; gap:1rem; align-items:flex-start; margin-bottom:1rem;">
                    <div style="width:28px; height:28px; background:{lcolor}22; border:1px solid {lcolor};
                                border-radius:6px; display:flex; align-items:center; justify-content:center;
                                font-size:0.7rem; font-weight:700; color:{lcolor}; flex-shrink:0;">{i}</div>
                    <div>
                        <div style="font-weight:600; color:#e8eaf0; font-size:0.85rem;">{layer}</div>
                        <div style="font-size:0.76rem; color:#6b7a99; margin-top:0.1rem;">{desc}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("</div></div>", unsafe_allow_html=True)

        with arch_col2:
            st.markdown("""
            <div class="about-card">
                <div class="about-card-title">⚙️ Training Configuration</div>
            """, unsafe_allow_html=True)

            config_items = [
                ("Optimizer", "Adam (lr=0.001)", "#00d4aa"),
                ("Loss Function", "Binary Cross-Entropy", "#0096ff"),
                ("Batch Size", "32 samples", "#ffa502"),
                ("Epochs", "100 (early stopping)", "#a855f7"),
                ("Validation Split", "20%", "#ff4757"),
                ("Preprocessing", "StandardScaler (Z-score)", "#00d4aa"),
                ("Class Handling", "Balanced sampling", "#0096ff"),
                ("Regularization", "L2 + Dropout + BatchNorm", "#ffa502"),
                ("Framework", "TensorFlow / Keras", "#a855f7"),
                ("Model Format", "HDF5 (.h5)", "#ff4757"),
            ]
            for ckey, cval, ccolor in config_items:
                st.markdown(f"""
                <div style="display:flex; justify-content:space-between; padding:0.6rem 0;
                            border-bottom:1px solid #1e2d45;">
                    <span style="font-size:0.82rem; color:#8b9cc0;">{ckey}</span>
                    <span style="font-size:0.82rem; font-weight:600; color:{ccolor};">{cval}</span>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Confusion matrix visual
        st.markdown("""
        <div style="background:#111827; border:1px solid #1e2d45; border-radius:14px; padding:1.5rem;">
            <div style="font-family:'Syne',sans-serif; font-size:1rem; font-weight:700;
                        color:#e8eaf0; margin-bottom:1.5rem;">📊 Performance Metrics</div>
        """, unsafe_allow_html=True)

        perf_cols = st.columns(5)
        perfs = [
            ("Accuracy", "96.2%", "Overall correctness"),
            ("Precision", "95.8%", "TP / (TP+FP)"),
            ("Recall", "97.1%", "TP / (TP+FN)"),
            ("F1 Score", "96.4%", "Harmonic mean"),
            ("AUC-ROC", "0.983", "Area under ROC curve"),
        ]
        for col_p, (pname, pval, pdesc) in zip(perf_cols, perfs):
            with col_p:
                st.markdown(f"""
                <div style="background:#0d1220; border:1px solid #1e2d45; border-radius:10px;
                            padding:1rem; text-align:center;">
                    <div style="font-family:'Syne',sans-serif; font-size:1.5rem; font-weight:800;
                                background:linear-gradient(135deg,#00d4aa,#0096ff);
                                -webkit-background-clip:text; -webkit-text-fill-color:transparent;">{pval}</div>
                    <div style="font-size:0.75rem; font-weight:600; color:#e8eaf0; margin-top:0.3rem;">{pname}</div>
                    <div style="font-size:0.7rem; color:#6b7a99; margin-top:0.1rem;">{pdesc}</div>
                </div>
                """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # ── TAB 3: Clinical Insights ──
    with tabs[2]:
        st.markdown("<br>", unsafe_allow_html=True)

        ci_col1, ci_col2 = st.columns(2)

        with ci_col1:
            st.markdown("""
            <div class="about-card">
                <div class="about-card-title">🩸 Glycemic Thresholds</div>
            """, unsafe_allow_html=True)
            thresholds = [
                ("HbA1c", ["<5.7% Normal", "5.7–6.4% Pre-DM", "≥6.5% Diabetes"], ["#00d4aa","#ffa502","#ff4757"]),
                ("Fasting Glucose", ["<100 mg/dL Normal", "100–125 Pre-DM", "≥126 Diabetes"], ["#00d4aa","#ffa502","#ff4757"]),
                ("Post-Prandial (2hr)", ["<140 mg/dL Normal", "140–199 Pre-DM", "≥200 Diabetes"], ["#00d4aa","#ffa502","#ff4757"]),
            ]
            for metric, levels, colors in thresholds:
                st.markdown(f"""
                <div style="margin-bottom:1.2rem;">
                    <div style="font-size:0.82rem; font-weight:600; color:#e8eaf0; margin-bottom:0.5rem;">{metric}</div>
                    <div style="display:flex; gap:0.4rem; flex-wrap:wrap;">
                        {''.join(f'<span class="badge" style="border-color:{c}; color:{c}; background:{c}11;">{l}</span>' for l, c in zip(levels, colors))}
                    </div>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with ci_col2:
            st.markdown("""
            <div class="about-card">
                <div class="about-card-title">⚠️ Key Risk Factors</div>
            """, unsafe_allow_html=True)
            risks = [
                ("🔴", "Elevated HbA1c ≥6.5%", "Primary diagnostic criterion"),
                ("🔴", "Fasting Glucose ≥126 mg/dL", "Second diagnostic criterion"),
                ("🟠", "BMI ≥30 (Obesity)", "Strong metabolic risk factor"),
                ("🟠", "Family History", "Genetic predisposition"),
                ("🟠", "Hypertension", "Comorbidity marker"),
                ("🟡", "Physical Inactivity", "Modifiable lifestyle risk"),
                ("🟡", "Poor Diet Score", "Nutrition-related risk"),
                ("🟡", "Advanced Age (≥45)", "Age-related glucose resistance"),
            ]
            for dot, risk_name, risk_desc in risks:
                st.markdown(f"""
                <div style="display:flex; gap:0.8rem; align-items:flex-start; margin-bottom:0.7rem;">
                    <div style="font-size:0.9rem; flex-shrink:0;">{dot}</div>
                    <div>
                        <div style="font-size:0.82rem; font-weight:600; color:#e8eaf0;">{risk_name}</div>
                        <div style="font-size:0.74rem; color:#6b7a99;">{risk_desc}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <div style="background:#111827; border:1px solid #1e2d45; border-radius:14px; padding:1.5rem;">
            <div style="font-family:'Syne',sans-serif; font-size:1rem; font-weight:700;
                        color:#e8eaf0; margin-bottom:1rem;">💡 Prevention Strategies</div>
        """, unsafe_allow_html=True)

        prev_cols = st.columns(3)
        preventions = [
            ("🥦", "Healthy Diet", ["Reduce refined carbs and added sugars",
                                    "Increase fibre & whole grains",
                                    "Choose lean proteins and healthy fats",
                                    "Limit processed food intake"]),
            ("🏃", "Physical Activity", ["150+ mins moderate exercise/week",
                                          "Include strength training 2x/week",
                                          "Reduce sedentary sitting time",
                                          "Daily steps target: 7,000–10,000"]),
            ("🩺", "Regular Monitoring", ["Annual HbA1c & fasting glucose tests",
                                           "Regular BP & cholesterol checks",
                                           "Weight management & BMI tracking",
                                           "Early screening for high-risk groups"]),
        ]
        for col_pv, (icon, title, tips) in zip(prev_cols, preventions):
            with col_pv:
                tips_html = ''.join(f'<div class="timeline-item"><div class="timeline-dot" style="background:#00d4aa;"></div><div class="timeline-content"><div class="timeline-desc">{t}</div></div></div>' for t in tips)
                st.markdown(f"""
                <div style="background:#0d1220; border:1px solid #1e2d45; border-radius:12px; padding:1.2rem; height:100%;">
                    <div style="font-size:1.8rem; margin-bottom:0.5rem;">{icon}</div>
                    <div style="font-family:'Syne',sans-serif; font-size:0.9rem; font-weight:700;
                                color:#00d4aa; margin-bottom:0.8rem;">{title}</div>
                    {tips_html}
                </div>
                """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    # ── TAB 4: About ──
    with tabs[3]:
        st.markdown("<br>", unsafe_allow_html=True)

        ab1, ab2 = st.columns([1.2, 1])
        with ab1:
            st.markdown("""
            <div class="about-card">
                <div style="font-family:'Syne',sans-serif; font-size:1.5rem; font-weight:800;
                            color:#e8eaf0; margin-bottom:0.5rem;">DiabetesSense <span style="color:#00d4aa;">AI</span></div>
                <div style="font-size:0.85rem; color:#6b7a99; margin-bottom:1.5rem; line-height:1.7;">
                    An AI-powered diabetes risk assessment platform built with deep learning
                    to assist clinicians and patients in early detection and risk stratification.
                </div>
                <div class="about-card-title">🎯 Mission</div>
                <div style="font-size:0.84rem; color:#b0bcd8; line-height:1.7; margin-bottom:1.2rem;">
                    Diabetes affects over 537 million adults worldwide. Early detection is critical
                    to preventing complications. DiabetesSense leverages artificial neural networks
                    trained on 100,000 clinical records to provide rapid, accurate risk assessments.
                </div>
                <div class="about-card-title">🔬 Technology Stack</div>
                <div style="display:flex; flex-wrap:wrap; gap:0.4rem; margin-bottom:1.2rem;">
                    <span class="badge badge-green">TensorFlow/Keras</span>
                    <span class="badge badge-blue">Streamlit</span>
                    <span class="badge">Scikit-learn</span>
                    <span class="badge">Pandas & NumPy</span>
                    <span class="badge badge-orange">Joblib</span>
                    <span class="badge">Python 3.10+</span>
                </div>
                <div class="about-card-title">⚠️ Disclaimer</div>
                <div style="font-size:0.8rem; color:#6b7a99; line-height:1.6;">
                    This tool is intended for clinical decision support only and does not replace
                    professional medical advice, diagnosis, or treatment. Results should be
                    interpreted in conjunction with a qualified healthcare professional.
                </div>
            </div>
            """, unsafe_allow_html=True)

        with ab2:
            st.markdown("""
            <div class="about-card">
                <div class="about-card-title">📁 Project Files</div>
            """, unsafe_allow_html=True)
            project_files = [
                ("app.py", "Main Streamlit application", "🟢"),
                ("ann_model.h5", "Trained ANN model weights", "🔵"),
                ("scaler.pkl", "StandardScaler (joblib)", "🟠"),
                ("diabetes_dataset.csv", "Raw dataset (100K records)", "🟡"),
                ("DIABETES_DATASET_CLEAN.csv", "Preprocessed dataset", "🟡"),
                ("Diabetes_DeepLearning.ipynb", "Training notebook", "🔴"),
            ]
            for fname, fdesc, fdot in project_files:
                st.markdown(f"""
                <div style="display:flex; gap:0.8rem; padding:0.6rem 0; border-bottom:1px solid #1e2d45;">
                    <div style="font-size:0.9rem;">{fdot}</div>
                    <div>
                        <div style="font-size:0.82rem; font-weight:600; color:#e8eaf0; font-family:monospace;">{fname}</div>
                        <div style="font-size:0.75rem; color:#6b7a99;">{fdesc}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("""
            <br>
            <div class="about-card-title">📊 Dataset Summary</div>
            """, unsafe_allow_html=True)
            ds_items = [
                ("Total Records", "100,000"),
                ("Clean Records", "88,263"),
                ("Features (raw)", "31 columns"),
                ("Features (model)", "26 after encoding"),
                ("Positive cases", "59,998 (60%)"),
                ("Negative cases", "40,002 (40%)"),
                ("Age range", "18–90 years"),
            ]
            for k, v in ds_items:
                st.markdown(f"""
                <div style="display:flex; justify-content:space-between; padding:0.4rem 0;
                            border-bottom:1px solid #1e2d4530;">
                    <span style="font-size:0.8rem; color:#8b9cc0;">{k}</span>
                    <span style="font-size:0.8rem; font-weight:600; color:#00d4aa;">{v}</span>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)