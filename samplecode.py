import streamlit as st

# Title and description
st.title("Field Biologist Notebook App")
st.write("Add notes with geolocation data, photos, videos, and audio.")

# Note input
note_text = st.text_area("Enter your note here")

# Geolocation
if st.checkbox("Include Geolocation"):
    latitude = st.number_input("Latitude")
    longitude = st.number_input("Longitude")

# Media Upload
media_option = st.selectbox("Select Media Type", ["None", "Photo", "Video", "Audio"])
if media_option != "None":
    uploaded_file = st.file_uploader(f"Upload {media_option}", type=["jpg", "png", "mp4", "wav"])

# Save Button
if st.button("Save Note"):
    # Save the note data to your database or storage
    st.success("Note saved successfully!")

# Display uploaded media
if uploaded_file:
    st.write("Uploaded Media:")
    if media_option == "Photo":
        st.image(uploaded_file)
    elif media_option == "Video":
        st.video(uploaded_file)
    elif media_option == "Audio":
        st.audio(uploaded_file)

