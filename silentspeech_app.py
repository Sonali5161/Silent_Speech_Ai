import streamlit as st
import os
from video_processing.frame_extractor import extract_frames
from video_processing.lip_reader import predict_text
from audio_generation.tts import text_to_speech

# Set page title and layout
st.set_page_config(page_title="SilentSpeech AI", layout="centered")

# Title and subtitle
st.title("🎤 SilentSpeech AI")
st.subheader("🔇 Giving Voice to the Voiceless")

# Upload video
video_file = st.file_uploader("📤 Upload a silent video", type=["mp4", "mov"])

if video_file:
    # Save uploaded video to 'uploaded' directory
    video_path = os.path.join("uploaded", "uploaded_video.mp4")
    with open(video_path, "wb") as f:
        f.write(video_file.read())

    # Show uploaded video preview
    st.video(video_path)

    if st.button("🔍 Analyze & Generate Voice"):
        with st.spinner("Extracting frames from video..."):
            frames = extract_frames(video_path)

        with st.spinner("Predicting speech from lip movement..."):
            text = predict_text(frames)

        st.success(f"🧠 AI Prediction: \"{text}\"")

        with st.spinner("Generating voice from text..."):
            audio_path = text_to_speech(text)
            with open(audio_path, "rb") as audio_file:
                st.audio(audio_file.read(), format="audio/mp3")

        st.success("✅ Audio generated successfully!")
        st.download_button("⬇️ Download Audio", data=open(audio_path, "rb"), file_name="output_audio.mp3")

