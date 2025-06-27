import streamlit as st
import os
from tempfile import NamedTemporaryFile
import whisper
from gtts import gTTS
import openai
import io

# Initialize session state
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Configuration (you should replace these with your actual API keys or models)
OPENAI_API_KEY = "your-openai-api-key"  # Replace with your actual key
MODEL_NAME = "gpt-3.5-turbo"  # Or any other model you prefer
WHISPER_MODEL = "base"  # Options: tiny, base, small, medium, large

# Initialize models
@st.cache_resource
def load_whisper_model():
    return whisper.load_model(WHISPER_MODEL)

whisper_model = load_whisper_model()

# Set OpenAI API key
openai.api_key = OPENAI_API_KEY

def detect_input_type(user_input):
    """Detect whether the input is text or an audio file."""
    if isinstance(user_input, str):
        return "text"
    elif hasattr(user_input, 'read'):  # File-like object
        return "audio"
    return None

def transcribe_audio(audio_file):
    """Transcribe audio to text using Whisper."""
    try:
        # Save the uploaded file to a temporary file
        with NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            tmp_file.write(audio_file.read())
            tmp_file_path = tmp_file.name
        
        # Load audio and pad/trim it to fit 30 seconds
        audio = whisper.load_audio(tmp_file_path)
        audio = whisper.pad_or_trim(audio)
        
        # Make log-Mel spectrogram and move to the same device as the model
        mel = whisper.log_mel_spectrogram(audio).to(whisper_model.device)
        
        # Detect the spoken language
        _, probs = whisper_model.detect_language(mel)
        detected_lang = max(probs.items(), key=lambda x: x[1])[0]
        
        # Decode the audio
        options = whisper.DecodingOptions(fp16=False)
        result = whisper.decode(whisper_model, mel, options)
        
        # Clean up the temporary file
        os.unlink(tmp_file_path)
        
        return result.text, detected_lang
    except Exception as e:
        st.error(f"Error in transcription: {str(e)}")
        return None, None

def generate_response(prompt):
    """Generate a response using the OpenAI API."""
    try:
        response = openai.ChatCompletion.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"Error generating response: {str(e)}"

def text_to_speech(text, lang='en'):
    """Convert text to speech using gTTS."""
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        audio_bytes = io.BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        return audio_bytes
    except Exception as e:
        st.error(f"Error in text-to-speech conversion: {str(e)}")
        return None

# Streamlit UI
st.title("🎤 Multimodal Chatbot 🗨️")
st.write("This chatbot can process both text and audio inputs. Try typing or uploading an audio file!")

# Input options
input_option = st.radio("Choose input method:", ("Text", "Audio"))

user_input = None
detected_lang = 'en'  # Default to English

if input_option == "Text":
    user_input = st.text_area("Enter your message:")
else:
    uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "ogg"])
    if uploaded_file is not None:
        st.audio(uploaded_file, format='audio/wav')
        user_input = uploaded_file

if st.button("Send"):
    if user_input:
        input_type = detect_input_type(user_input)
        
        if input_type == "audio":
            with st.spinner("Transcribing audio..."):
                transcribed_text, detected_lang = transcribe_audio(user_input)
            if transcribed_text:
                st.session_state.conversation.append(("You (Audio)", transcribed_text))
                user_input = transcribed_text
        
        if input_type == "text" or (input_type == "audio" and transcribed_text):
            with st.spinner("Generating response..."):
                response = generate_response(user_input)
            
            if response:
                st.session_state.conversation.append(("Bot", response))
                
                # Offer audio response option
                if st.checkbox("Convert response to audio"):
                    with st.spinner("Generating audio..."):
                        audio_response = text_to_speech(response, lang=detected_lang)
                    if audio_response:
                        st.audio(audio_response, format='audio/mp3')
    else:
        st.warning("Please enter a message or upload an audio file.")

# Display conversation
st.subheader("Conversation History")
for speaker, message in st.session_state.conversation:
    if speaker.startswith("You"):
        st.markdown(f"**{speaker}:** {message}")
    else:
        st.markdown(f"**{speaker}:** {message}")
    st.write("---")