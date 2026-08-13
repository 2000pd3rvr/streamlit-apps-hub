#!/usr/bin/env python3
"""Hub of Streamlit description pages for running HF Spaces (Deborah Akuoko Minka)."""
import streamlit as st
st.set_page_config(page_title="Apps · Deborah Akuoko Minka", page_icon="🔬", layout="wide")
st.title("Research & product apps")
st.subheader("Deborah Akuoko Minka / Deborah Akuoko-Minka — machine intelligence demos")
st.write(
    "This Streamlit hub indexes public apps that also run on Hugging Face Spaces. "
    "Each page is crawlable and links to GitHub source + live Space."
)
apps = [
    ("Golden Green SC", "https://huggingface.co/spaces/0001AMA/GoldenGreenFC", "https://github.com/2000pd3rvr/GoldenGreenFC"),
    ("careTalk", "https://huggingface.co/spaces/0001AMA/careTalk", "https://github.com/2000pd3rvr/careTalk"),
    ("careTalk demo", "https://huggingface.co/spaces/0001AMA/careTalk-demo", "https://github.com/2000pd3rvr/careTalk"),
    ("Auto Object Annotator", "https://huggingface.co/spaces/0001AMA/auto_object_annotator_0.0.4", "https://github.com/2000pd3rvr/auto_object_annotator_0.0.4"),
    ("Corner Cafe", "https://huggingface.co/spaces/0001AMA/corner_cafe", "https://github.com/2000pd3rvr/corner_cafe"),
    ("SMOS", "https://huggingface.co/spaces/0001AMA/SMOS", "https://github.com/2000pd3rvr/SMOS"),
]
for name, hf, gh in apps:
    st.markdown(f"- **{name}** — [HF Space]({hf}) · [GitHub]({gh})")
st.markdown("---")
st.markdown(
    "Author profiles: [WordPress](https://deborahakuokominka.wordpress.com/) · "
    "[ORCID](https://orcid.org/0009-0008-6219-154X) · "
    "[GitHub](https://github.com/2000pd3rvr) · "
    "[Scholar](https://scholar.google.co.uk/citations?hl=en&user=ab0EyjYAAAAJ)"
)
