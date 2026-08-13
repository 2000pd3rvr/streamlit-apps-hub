#!/usr/bin/env python3
"""Apps hub — Streamlit Community Cloud."""

from __future__ import annotations

import streamlit as st

st.set_page_config(
    page_title="Apps · Deborah Akuoko Minka",
    page_icon="🔬",
    layout="wide",
)

st.title("Apps by Deborah Akuoko Minka")
st.write(
    "Each app below runs live on Streamlit Community Cloud, connected to its GitHub repository. "
    "Hugging Face Spaces remain available as an alternate host."
)

apps = [
    ("careTalk", "Structured care notes for health assistants and admins.", "https://caretalk.streamlit.app/", "https://github.com/2000pd3rvr/careTalk", "https://huggingface.co/spaces/0001AMA/careTalk"),
    ("Corner Cafe", "Hospitality site with enquiry and gallery support.", "https://corner-cafe.streamlit.app/", "https://github.com/2000pd3rvr/corner_cafe", "https://huggingface.co/spaces/0001AMA/corner_cafe"),
    ("Golden Green Sporting Club", "Public club website — Dream Big, Do More.", "https://golden-green-sc.streamlit.app/", "https://github.com/2000pd3rvr/GoldenGreenFC", "https://huggingface.co/spaces/0001AMA/GoldenGreenFC"),
    ("SMOS", "Multilingual ordering with a live kitchen workflow.", "https://smos.streamlit.app/", "https://github.com/2000pd3rvr/SMOS", "https://huggingface.co/spaces/0001AMA/SMOS"),
]

for name, blurb, live, gh, hf in apps:
    st.markdown(f"### {name}")
    st.write(blurb)
    c1, c2, c3 = st.columns(3)
    c1.link_button("Open live app", live, use_container_width=True)
    c2.link_button("GitHub", gh, use_container_width=True)
    c3.link_button("Hugging Face", hf, use_container_width=True)

st.markdown("---")
st.markdown(
    "[WordPress](https://deborahakuokominka.wordpress.com/) · "
    "[ORCID](https://orcid.org/0009-0008-6219-154X) · "
    "[GitHub](https://github.com/2000pd3rvr) · "
    "[Google Scholar](https://scholar.google.co.uk/citations?hl=en&user=ab0EyjYAAAAJ)"
)
st.caption("Deborah Akuoko Minka · also written Deborah Akuoko-Minka")
