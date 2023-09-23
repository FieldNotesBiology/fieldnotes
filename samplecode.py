import streamlit as st
import pymongo
from pymongo import MongoClient

#rachels mongodb uri
mongo_uri = "mongodb+srv://rnd22:<RaeRae13!>@cluster0.nmrig91.mongodb.net/?retryWrites=true&w=majority"


# Create a MongoDB client
client = MongoClient(mongo_uri)

# Access your database (replace 'mydatabase' with your actual database name)
db = client["mydatabase"]
# Title and description

st.title("Field Biologist Notebook")
st.write("Add notes with geolocation data, photos, videos, and audio.")


# Note input
note_title = st.text_area("Note Title")
note_text = st.text_area("Enter your note here")

# JavaScript code to access the Geolocation API
geolocation_code = """
<script>
    function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition);
        } else {
            document.getElementById("location").innerHTML = "Geolocation is not supported by this browser.";
        }
    }

    function showPosition(position) {
        var latitude = position.coords.latitude;
        var longitude = position.coords.longitude;
        document.getElementById("location").innerHTML = "Latitude: " + latitude + "<br>Longitude: " + longitude;
    }

    // Call the getLocation function when the page loads
    getLocation();
</script>
"""

# Display the HTML content with JavaScript code
st.write(geolocation_code, unsafe_allow_html=True)

# Display the location information
st.markdown("<p id='location'>Location: Loading...</p>", unsafe_allow_html=True)

# Geolocation
if st.checkbox("Include Geolocation"):
    latitude = st.number_input("Latitude")
    longitude = st.number_input("Longitude")

uploaded_file = None  # Initialize to None by default

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
