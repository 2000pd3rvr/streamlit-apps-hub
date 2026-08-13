#!/usr/bin/env python3
"""Apps hub — Streamlit Community Cloud (GitHub-connected)."""

from __future__ import annotations

import streamlit as st

st.set_page_config(
    page_title="Apps · Deborah Akuoko Minka",
    page_icon="🔬",
    layout="wide",
)

WP_URL = "https://deborahakuokominka.wordpress.com/"
ORCID = "https://orcid.org/0009-0008-6219-154X"
SCHOLAR = "https://scholar.google.co.uk/citations?hl=en&user=ab0EyjYAAAAJ"
GH_PROFILE = "https://github.com/2000pd3rvr"

st.title("Apps by Deborah Akuoko Minka")
st.subheader("Product demos and research interfaces")
st.write(
    "These projects run as public Hugging Face Spaces and are also published from "
    "GitHub to Streamlit Community Cloud. Start with the three primary apps, then "
    "open the others if you want more of the portfolio."
)

apps = [
    {
        "name": "careTalk",
        "blurb": "Structured care notes for health assistants and admins.",
        "hf": "https://huggingface.co/spaces/0001AMA/careTalk",
        "gh": "https://github.com/2000pd3rvr/careTalk",
        "streamlit": "https://caretalk.streamlit.app",
        "priority": True,
    },
    {
        "name": "Corner Cafe",
        "blurb": "Hospitality site with enquiry and gallery support.",
        "hf": "https://huggingface.co/spaces/0001AMA/corner_cafe",
        "gh": "https://github.com/2000pd3rvr/corner_cafe",
        "streamlit": "https://corner-cafe.streamlit.app",
        "priority": True,
    },
    {
        "name": "Golden Green Sporting Club",
        "blurb": "Public club website — Dream Big, Do More.",
        "hf": "https://huggingface.co/spaces/0001AMA/GoldenGreenFC",
        "gh": "https://github.com/2000pd3rvr/GoldenGreenFC",
        "streamlit": "https://golden-green-sc.streamlit.app",
        "priority": True,
    },
    {
        "name": "SMOS",
        "blurb": "Multilingual ordering with a live kitchen workflow.",
        "hf": "https://huggingface.co/spaces/0001AMA/SMOS",
        "gh": "https://github.com/2000pd3rvr/SMOS",
        "streamlit": "https://smos.streamlit.app",
        "priority": False,
    },
    {
        "name": "Auto Object Annotator",
        "blurb": "Lightweight annotation loop for vision datasets.",
        "hf": "https://huggingface.co/spaces/0001AMA/auto_object_annotator_0.0.4",
        "gh": "https://github.com/2000pd3rvr/auto_object_annotator_0.0.4",
        "streamlit": "https://auto-object-annotator.streamlit.app",
        "priority": False,
    },
]

st.header("Primary apps")
for app in [a for a in apps if a["priority"]]:
    st.markdown(f"### {app['name']}")
    st.write(app["blurb"])
    c1, c2, c3 = st.columns(3)
    c1.link_button("Streamlit app", app["streamlit"], use_container_width=True)
    c2.link_button("Hugging Face", app["hf"], use_container_width=True)
    c3.link_button("GitHub", app["gh"], use_container_width=True)

st.header("More apps")
for app in [a for a in apps if not a["priority"]]:
    st.markdown(f"**{app['name']}** — {app['blurb']}")
    st.markdown(
        f"[Streamlit]({app['streamlit']}) · [Hugging Face]({app['hf']}) · [GitHub]({app['gh']})"
    )

st.markdown("---")
st.markdown(
    f"Profiles: [WordPress]({WP_URL}) · [ORCID]({ORCID}) · "
    f"[GitHub]({GH_PROFILE}) · [Google Scholar]({SCHOLAR})"
)
st.caption("Deborah Akuoko Minka · also written Deborah Akuoko-Minka")
