import streamlit as st

st.set_page_config(page_title="My Private App Store", page_icon="📱", layout="centered")

st.title("📱 My Private App Store")
st.write("Welcome! Download the latest version of my app below:")
st.balloons()
st.snow()

# APK file download
with open("app-release.apk", "rb") as file:
    apk_data = file.read()

st.download_button(
    label="⬇️ Download APK",
    data=apk_data,
    file_name="app-release.apk",
    mime="application/vnd.android.package-archive"
)

st.info("Make sure you allow installations from unknown sources on your Android device.")
