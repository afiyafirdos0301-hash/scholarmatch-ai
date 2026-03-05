import streamlit as st

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(page_title="ScholarGate AI", page_icon="🎓", layout="wide")

# ==========================================================
# SESSION STATE
# ==========================================================

if "step" not in st.session_state:
    st.session_state.step = 1

if "data" not in st.session_state:
    st.session_state.data = {}

# ==========================================================
# LANGUAGE SYSTEM
# ==========================================================

LANG = {

"English":{
"title":"ScholarGate AI",
"tag":"AI powered scholarship discovery for Indian students",
"personal":"Personal Information",
"academic":"Academic Information",
"financial":"Financial & Extra Details",
"name":"Full Name",
"age":"Age",
"gender":"Gender",
"state":"State",
"category":"Category",
"marks":"12th Percentage",
"course":"Degree Program",
"income":"Annual Family Income",
"sports":"Extracurricular Achievements",
"documents":"Upload Documents",
"next":"Next →",
"back":"← Back",
"search":"Find Scholarships",
"results":"Scholarship Results",
"none":"None",
"about":"About",
"ad":"Advertisement",
"found":"scholarships matched",
"no":"No scholarships matched"
},

"Hindi":{
"title":"स्कॉलरगेट AI",
"tag":"भारतीय छात्रों के लिए छात्रवृत्ति खोजें",
"personal":"व्यक्तिगत जानकारी",
"academic":"शैक्षणिक जानकारी",
"financial":"वित्तीय विवरण",
"name":"पूरा नाम",
"age":"आयु",
"gender":"लिंग",
"state":"राज्य",
"category":"वर्ग",
"marks":"12वीं प्रतिशत",
"course":"डिग्री",
"income":"वार्षिक आय",
"sports":"अतिरिक्त उपलब्धियां",
"documents":"दस्तावेज़ अपलोड करें",
"next":"आगे",
"back":"पीछे",
"search":"छात्रवृत्ति खोजें",
"results":"परिणाम",
"none":"कोई नहीं",
"about":"के बारे में",
"ad":"विज्ञापन",
"found":"छात्रवृत्तियाँ मिलीं",
"no":"कोई छात्रवृत्ति नहीं मिली"
},

"Telugu":{
"title":"స్కాలర్ గేట్ AI",
"tag":"భారత విద్యార్థుల కోసం స్కాలర్షిప్ శోధన",
"personal":"వ్యక్తిగత సమాచారం",
"academic":"విద్యా వివరాలు",
"financial":"ఆర్థిక వివరాలు",
"name":"పూర్తి పేరు",
"age":"వయసు",
"gender":"లింగం",
"state":"రాష్ట్రం",
"category":"వర్గం",
"marks":"12వ శాతం",
"course":"డిగ్రీ",
"income":"కుటుంబ ఆదాయం",
"sports":"అదనపు ప్రతిభ",
"documents":"పత్రాలు అప్లోడ్ చేయండి",
"next":"తదుపరి",
"back":"వెనక్కి",
"search":"స్కాలర్షిప్‌లు కనుగొను",
"results":"ఫలితాలు",
"none":"ఏదీ లేదు",
"about":"గురించి",
"ad":"ప్రకటన",
"found":"స్కాలర్షిప్‌లు కనుగొనబడ్డాయి",
"no":"స్కాలర్షిప్‌లు లభించలేదు"
}
}

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("⚙ Settings")

language = st.sidebar.selectbox("Language / भाषा / భాష",["English","Hindi","Telugu"])
T = LANG[language]

st.sidebar.markdown("---")

st.sidebar.subheader("📘 " + T["about"])
st.sidebar.write(
"ScholarGate AI helps Indian students discover scholarships based on marks, income, degree, category and state eligibility rules."
)

st.sidebar.markdown("---")

st.sidebar.subheader("💡 " + T["ad"])
st.sidebar.info("Explore online courses in AI, Cloud Computing, Cybersecurity and Data Science.")

# ==========================================================
# STYLING
# ==========================================================

st.markdown("""
<style>
body{background:#f8fafc}

.title{font-size:46px;font-weight:700;color:#2563eb}
.subtitle{color:#64748b;margin-bottom:30px}

.card{
background:white;
padding:30px;
border-radius:14px;
box-shadow:0 8px 20px rgba(0,0,0,0.06);
margin-bottom:20px
}

.scholar{
background:white;
padding:25px;
border-left:8px solid #10b981;
border-radius:12px;
margin-bottom:15px;
box-shadow:0 6px 14px rgba(0,0,0,0.05)
}
</style>
""", unsafe_allow_html=True)

# ==========================================================
# HEADER
# ==========================================================

st.markdown(f"<div class='title'>🎓 {T['title']}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='subtitle'>{T['tag']}</div>", unsafe_allow_html=True)

# ==========================================================
# STEP 1
# ==========================================================

if st.session_state.step == 1:

    st.subheader(T["personal"])

    name = st.text_input(T["name"])
    age = st.number_input(T["age"],min_value=16,max_value=40)
    gender = st.selectbox(T["gender"],["Male","Female","Other"])
    state = st.selectbox(T["state"],["Andhra Pradesh","Telangana","Tamil Nadu","Karnataka","Kerala","Maharashtra","Delhi","Uttar Pradesh","Gujarat","West Bengal"])
    category = st.selectbox(T["category"],["General","EWS","OBC","SC","ST","Minority"])

    if st.button(T["next"]):

        st.session_state.data.update({
        "name":name,
        "age":age,
        "gender":gender,
        "state":state,
        "category":category
        })

        st.session_state.step = 2
        st.rerun()

# ==========================================================
# STEP 2
# ==========================================================

elif st.session_state.step == 2:

    st.subheader(T["academic"])

    marks = st.number_input(T["marks"],min_value=0,max_value=100)

    course = st.selectbox(
    T["course"],
    ["B.Tech","MBBS","B.Sc","B.Com","BA","BBA","BCA","LLB","B.Pharm","B.Arch","BDS","B.Ed"]
    )

    col1,col2 = st.columns(2)

    with col1:
        if st.button(T["back"]):
            st.session_state.step = 1
            st.rerun()

    with col2:
        if st.button(T["next"]):

            st.session_state.data.update({
            "marks":marks,
            "course":course
            })

            st.session_state.step = 3
            st.rerun()

# ==========================================================
# STEP 3
# ==========================================================

elif st.session_state.step == 3:

    st.subheader(T["financial"])

    income = st.number_input(T["income"],min_value=0,max_value=2000000)

    sports = st.selectbox(
    T["sports"],
    [T["none"],"Sports Quota","NCC","NSS","State Level Athlete","National Level Athlete"]
    )

    st.file_uploader(T["documents"], type=["pdf","jpg","png"])

    col1,col2 = st.columns(2)

    with col1:
        if st.button(T["back"]):
            st.session_state.step = 2
            st.rerun()

    with col2:
        if st.button(T["search"]):

            st.session_state.data.update({
            "income":income,
            "sports":sports
            })

            st.session_state.step = 4
            st.rerun()

# ==========================================================
# SCHOLARSHIPS DATABASE
# ==========================================================

scholarships = [

{"name":"Central Sector Scheme Scholarship","marks":80,"income":800000,"course":["B.Tech","BA","B.Com","B.Sc"],"state":"All","link":"https://scholarships.gov.in"},

{"name":"INSPIRE Scholarship","marks":85,"income":1000000,"course":["B.Sc"],"state":"All","link":"https://online-inspire.gov.in"},

{"name":"AICTE Pragati Scholarship","marks":70,"income":800000,"course":["B.Tech"],"state":"All","link":"https://www.aicte-india.org/schemes/students-development-schemes/Pragati"},

{"name":"Reliance Foundation Undergraduate Scholarship","marks":60,"income":1500000,"course":["B.Tech","BA","B.Com","B.Sc"],"state":"All","link":"https://scholarships.reliancefoundation.org"},

{"name":"Jagananna Vidya Deevena","marks":60,"income":500000,"course":["B.Tech","MBBS","BBA","BCA"],"state":"Andhra Pradesh","link":"https://navasakam.ap.gov.in"},

{"name":"Telangana ePASS Scholarship","marks":60,"income":200000,"course":["B.Tech","BA","B.Com","B.Sc"],"state":"Telangana","link":"https://telanganaepass.cgg.gov.in"},

{"name":"Khelo India Scholarship","marks":50,"income":1000000,"course":["B.Tech","BA","B.Com","B.Sc"],"state":"All","link":"https://kheloindia.gov.in"}
]

# ==========================================================
# STEP 4 RESULTS
# ==========================================================

if st.session_state.step == 4:

    data = st.session_state.data

    matches = []

    for s in scholarships:

        if data["marks"] >= s["marks"] and data["income"] <= s["income"]:

            if data["course"] in s["course"]:

                if s["state"] == "All" or data["state"] == s["state"]:

                    matches.append(s)

    st.subheader(T["results"])

    if matches:

        st.success(f"{len(matches)} {T['found']}")

        for s in matches:

            st.markdown(f"""
            <div class='scholar'>
            <h4>{s['name']}</h4>
            Minimum Marks: {s['marks']}%<br>
            Income Limit: ₹{s['income']:,}<br><br>
            <a href='{s['link']}' target='_blank'>Visit Official Scholarship Page</a>
            </div>
            """, unsafe_allow_html=True)

    else:

        st.error(T["no"])

    if st.button("Start Over"):
        st.session_state.step = 1
        st.session_state.data = {}
        st.rerun()

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")
st.caption("ScholarGate AI • Helping Indian students discover scholarships faster")