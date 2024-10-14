![](https://user-images.githubusercontent.com/970858/63474771-d6734700-c469-11e9-83bb-9429da563909.png)

# LAB-Foundations-of-GenerativeAI-Audio-to-Text-for-Content-Creation

## Introduction

In this lab, students will work with pre-trained **audio-to-text** models, such as **Wav2Vec2** and **Whisper**, available through Hugging Face, to explore their applications in content creation. The goal is for students to understand how these models work and learn to apply them in real-world projects without needing to build models from scratch.

Students will:
1. Use pre-trained audio-to-text models.
2. Implement audio-to-text transcription tasks using these models.
3. Evaluate the models’ performance and their real-world applications.
4. Analyze how audio-to-text models are impacting creative industries.

---

## Initial Setup

### Requirements

Start by forking the provided GitHub repository to your account and then clone it locally. This will be your workspace for completing the lab exercises.

- [Learn how to fork this repo](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project)
- Clone this repo into your code/labs folder.

```bash
git clone https://github.com/codeskills-ai/LAB-Foundations-of-GenerativeAI-Audio-to-Text-for-Content-Creation.git
cd LAB-Foundations-of-GenerativeAI-Audio-to-Text-for-Content-Creation
```
Setup Instructions
Create a virtual environment and install the required packages:

```bash
pip install -r requirements.txt
Start Jupyter Notebook:
```

Start Jupyter Notebook:

```bash
jupyter notebook
```

Once your environment is ready, you're all set to dive into the exercises.

## Iteration 1: Audio Transcription with Speech2Text and Word Error Rate Calculation

**Model**: **Speech2Text** from Hugging Face.

**Task**: Load a pre-trained model and transcribe the audio file `mozilla_tts_output.wav` to text using **Speech2Text**. Then, calculate the **Word Error Rate (WER)** by comparing the generated transcription with the reference text.

### Steps:
1. Load the pre-trained `facebook/s2t-small-librispeech-asr` model and the processor.
2. Load the audio file `mozilla_tts_output.wav`, resample it to 16,000 Hz if necessary, and prepare it for inference.
3. Generate the transcription using the model.
4. Compare the generated transcription with the ground truth (reference transcription).
5. Calculate the **WER** to assess the accuracy of the transcription.

---

## Iteration 2: Key Technologies in Audio-to-Text Generation with Speech2Text

**Task**: Explore the underlying technology used by **Speech2Text**, particularly focusing on automatic speech recognition (**ASR**) systems.

**Objective**: Understand how ASR systems, specifically those utilized in models like **Speech2Text**, are applied in real-world scenarios such as voice assistants, customer service automation, and accessibility tools.

**Steps**:
1. Investigate the architecture behind **Speech2Text** and its application of ASR technology.
2. Explore how ASR models process audio signals and convert them into meaningful text.
3. Analyze different real-world applications that benefit from the integration of **Speech2Text** models.

---

## Iteration 3: Applications of Audio-to-Text Models

**Task**: Use the **Whisper** model for audio-to-text conversion. Transcribe an audio clip from a podcast or news article.

**Practical Discussion**: Discuss how **audio-to-text** models are transforming content creation in industries such as journalism, media production, and e-learning. How can these models improve efficiency and accuracy in content creation?

---

## Iteration 4: Implementing a Basic Audio-to-Text Model

**Task**: Load a second pre-trained model (such as **Whisper** or **Conformer**) and transcribe a custom audio file that you have recorded yourself.

**Objective**: Understand how to work with pre-trained models in real-world use cases, saving time and resources in content creation workflows.

**Analysis**: Compare the results between different models and discuss which one is better suited for your specific project or task.

---

## Iteration 5: Performance and Limitations of Audio-to-Text Models

**Task**: Compare the performance of the two models used so far (**Wav2Vec2** and **Whisper**). Try transcribing an audio clip with background noise, unclear speech, or different accents, and assess how each model performs under these conditions.

**Analysis**: Discuss the limitations of these models, including how they handle noisy environments or accents, and consider areas where improvements are still needed.

---

## Iteration 6: Impact of Audio-to-Text Models on Creative Industries

**Task**: Analyze the broader impact of audio-to-text models on industries such as content creation, media, and accessibility. Research how companies are using these technologies to enhance their workflows and deliver better services.

**Practical Application**: Explore how media companies, podcast creators, or e-learning platforms use audio-to-text models to improve content accessibility and engagement.

**Presentation**: Each student will present a professional use case where audio-to-text models are used and discuss the benefits and challenges these models bring to the industry.

---

## Bonus: Combining Text-to-Audio and Audio-to-Text Models

**Task**: Combine the power of both text-to-audio and audio-to-text models. Create a small application that takes audio input, transcribes it into text, allows editing of the text, and then converts it back into audio using a text-to-speech model like **gTTS**.

**Objective**: Understand how different AI models can be integrated to create a seamless content creation pipeline.


## Additional Resources
Hugging Face Wav2Vec2 Documentation
Whisper Documentation

# Submission
Once you have completed the lab, push your Jupyter notebook to your forked GitHub repository and create a pull request.

```bash
$ git add .
$ git commit -m "completed lab"
$ git push origin main
```

![happy_coding](https://user-images.githubusercontent.com/970858/63899010-c23fc480-c9ea-11e9-84a2-542907e42362.png)
