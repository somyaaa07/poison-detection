import streamlit as st
import joblib
import os


# ==========================
# Load model
# ==========================

BASE_DIR = os.path.dirname(__file__)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "model",
    "toxic_detection_model.pkl"
)

model = joblib.load(MODEL_PATH)


# ==========================
# Page
# ==========================

st.set_page_config(
    page_title="Decision Support System - VishAI",
    layout="wide"
)

st.title(" Decision Support System - VishAI")

st.write(
"""
AI assisted forensic toxicology
decision support tool for probable
poison identification.
"""
)

# ====================================
# INPUTS
# ====================================

cns = st.multiselect(

"CNS Symptoms",

[
"confusion",
"coma",
"delirium",
"anxiety",
"seizure",
"headache"
]

)


cvs = st.multiselect(

"CVS Symptoms",

[
"tachycardia",
"bradycardia",
"hypotension",
"cardiac arrest"
]

)


resp = st.multiselect(

"Respiratory Symptoms",

[
"dyspnoea",
"tachypnoea",
"respiratory failure",
"pulmonary edema"
]

)


gi = st.multiselect(

"GI Symptoms",

[
"vomiting",
"nausea",
"abdominal pain",
"diarrhea"
]

)



other = st.multiselect(

"Other/Systemic Symptoms",

[
"fever",
"cyanosis",
"renal failure",
"burning sensation"
]

)



odour = st.selectbox(

"Odour",

[
"Unknown",
"Petroleum",
"Garlic",
"Sweet",
"Bitter Almond",
"None"
]

)



route = st.selectbox(

"Route of Exposure",

[
"Ingestion",
"Inhalation",
"Injection",
"Dermal",
"Unknown"
]

)



timeline = st.selectbox(

"Timeline",

[
"Rapid",
"Acute",
"Subacute",
"Delayed",
"Chronic"
]

)



sample = st.multiselect(

"Available Sample",

[
"Blood",
"Urine",
"Gastric Lavage",
"Hair",
"Nails",
"Viscera"
]

)



# ====================================
# PREDICT
# ====================================

if st.button(" Predict Toxic Substance"):


    symptoms = (

        " ".join(cns)
        + " "
        + " ".join(cvs)
        + " "
        + " ".join(resp)
        + " "
        + " ".join(gi)
        + " "
        + " ".join(other)
        + " "
        + odour

    )


    prediction = model.predict([symptoms])[0]


    # ====================================
    # Toxicology Knowledge Base
    # ====================================

    toxic_db = {

        "Datura":{

            "confidence":"HIGH",

            "severity":"SEVERE",

            "confirmatory":

            "Urine alkaloid analysis\nGC-MS",

            "sample":

            "Blood / Gastric lavage"

        },


        "Snakebite":{

            "confidence":"HIGH",

            "severity":"CRITICAL",

            "confirmatory":

            "ELISA venom assay",

            "sample":

            "Blood"

        },


        "Copper":{

            "confidence":"MODERATE",

            "severity":"MODERATE",

            "confirmatory":

            "Serum copper estimation",

            "sample":

            "Blood"

        },


        "Kerosene":{

            "confidence":"HIGH",

            "severity":"SEVERE",

            "confirmatory":

            "Hydrocarbon toxicology",

            "sample":

            "Blood / Gastric"

        }

    }



    matched = None


    for toxin in toxic_db:

        if toxin.lower() in str(prediction).lower():

            matched = toxic_db[toxin]



    st.success(

        f"""
Predicted Toxic Substance:

{prediction}
"""
    )



    if matched:


        col1,col2,col3 = st.columns(3)


        col1.metric(

            "Confidence",

            matched["confidence"]

        )


        col2.metric(

            "Severity",

            matched["severity"]

        )


        col3.metric(

            "Timeline",

            timeline

        )



        st.write("## Recommended Confirmatory Test")

        st.info(

            matched["confirmatory"]

        )



        st.write("## Best Sample")

        st.success(

            matched["sample"]

        )



    st.write("## Case Summary")


    st.write(

f"""

Route:

{route}



Timeline:

{timeline}



Entered Symptoms:

CNS → {cns}

CVS → {cvs}

Resp → {resp}

GI → {gi}

Other → {other}



Odour:

{odour}



Available Sample:

{sample}

"""
    )



    st.warning(

"""
This is a preliminary forensic
decision-support output.

Laboratory confirmation is required
before medico-legal interpretation.
"""
    )



    st.caption(

"Powered by VishAI Decision Support System"

)
