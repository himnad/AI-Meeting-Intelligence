# 🎙️ MeetingMind — AI Meeting Intelligence Platform

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.136-009688?style=for-the-badge&logo=fastapi)
![Next.js](https://img.shields.io/badge/Next.js-16-black?style=for-the-badge&logo=next.js)
![TypeScript](https://img.shields.io/badge/TypeScript-5.0-3178C6?style=for-the-badge&logo=typescript)
![Gemini](https://img.shields.io/badge/Gemini_2.5_Flash-API-4285F4?style=for-the-badge&logo=google)
![Vercel](https://img.shields.io/badge/Deployed-Vercel-black?style=for-the-badge&logo=vercel)
![Render](https://img.shields.io/badge/Backend-Render-46E3B7?style=for-the-badge&logo=render)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A production-grade, full-stack Generative AI platform that transforms raw meeting audio into structured intelligence — transcripts, speaker-separated dialogues, meeting summaries, action items, and professional PDF reports.**

[🚀 Live Demo](https://ai-meeting-intelligence-nine.vercel.app/) · [📦 GitHub](https://github.com/himnad/AI-Meeting-Intelligence) · [📖 API Docs](https://ai-meeting-intelligence-iw1r.onrender.com/docs)

</div>

---

## 📌 Project Overview

MeetingMind is a full-stack AI-powered SaaS-style application designed to eliminate the manual effort of taking meeting notes. It accepts raw audio recordings and automatically generates:

- 🗣️ **Speaker-separated transcripts** using neural diarization
- 📝 **Structured meeting minutes** via large language model extraction
- 🎯 **Action items and decisions** extracted intelligently
- 📊 **Discussion summaries** with key points
- 📄 **Professional two-page PDF reports** with multilingual support
- 🗂️ **Persistent meeting history** with searchable records

This project demonstrates end-to-end integration of modern AI/ML models, REST API design, full-stack web development, and production deployment — making it a strong showcase for AI engineering roles.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🎙️ Audio Upload | Drag-and-drop or file picker for MP3, WAV, M4A, MPEG |
| 🔊 Speech-to-Text | Faster-Whisper with VAD filtering and beam search |
| 👥 Speaker Diarization | Pyannote.audio 3.1 for multi-speaker identification |
| 🤖 AI Summarization | Gemini 2.5 Flash for structured meeting intelligence |
| 📄 PDF Reports | Two-page professional reports with Unicode/Hindi support |
| 🗂️ Meeting History | SQLite + SQLAlchemy persistent storage with CRUD APIs |
| 🌐 Full Deployment | Vercel (frontend) + Render (backend) + GitHub CI/CD |
| 📚 API Documentation | Auto-generated Swagger UI via FastAPI |
| 🌏 Multilingual | Hindi/Devanagari script support in transcripts and PDFs |

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     USER BROWSER                            │
│              Next.js + TypeScript + Tailwind                │
│         (Deployed on Vercel)                                │
└──────────────────────┬──────────────────────────────────────┘
                       │ HTTPS REST API
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                   FASTAPI BACKEND                           │
│              (Deployed on Render)                           │
│                                                             │
│  ┌──────────────┐  ┌─────────────┐  ┌──────────────────┐  │
│  │   Whisper    │  │  Pyannote   │  │   Gemini 2.5     │  │
│  │ Transcriber  │  │  Diarizer   │  │   Flash API      │  │
│  └──────────────┘  └─────────────┘  └──────────────────┘  │
│                                                             │
│  ┌──────────────┐  ┌─────────────┐                        │
│  │  ReportLab   │  │   SQLite    │                        │
│  │ PDF Generator│  │  Database   │                        │
│  └──────────────┘  └─────────────┘                        │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔄 End-to-End Pipeline Workflow

```
🎵 Audio Upload (.mp3/.wav/.m4a)
        │
        ▼
🔧 Audio Preprocessing
   └── Format validation
   └── Resampling to 16kHz mono
   └── Noise filtering via VAD
        │
        ▼
👥 Speaker Diarization (Pyannote 3.1)
   └── Neural speaker embedding
   └── Clustering speakers
   └── Generating timestamps [SPEAKER_00: 0.0s → 3.2s]
        │
        ▼
📝 Whisper Transcription (Faster-Whisper)
   └── Small model, int8 quantization
   └── Beam search (beam_size=5)
   └── VAD filtering (silence removal)
   └── Word-level timestamps
        │
        ▼
🔗 Speaker Mapping
   └── Aligning transcript segments with diarization
   └── Merging consecutive same-speaker segments
   └── Building structured dialogue
        │
        ▼
🤖 Gemini AI Processing
   └── Meeting Summary
   └── Key Discussion Points
   └── Action Items
   └── Final Decisions
        │
        ▼
📄 PDF Report Generation (ReportLab)
   └── Page 1: AI Meeting Summary
   └── Page 2: Speaker Dialogue Transcript
   └── Unicode/Devanagari font support
        │
        ▼
🗂️ Database Storage (SQLite + SQLAlchemy)
   └── Transcript saved
   └── Summary saved
   └── Meeting history updated
        │
        ▼
🌐 Frontend Visualization (Next.js)
   └── Tabbed summary/transcript view
   └── PDF download button
   └── Meeting history dashboard
```

---

## 🛠️ Technologies Used

### Frontend
| Technology | Version | Purpose |
|---|---|---|
| Next.js | 16.x | React framework with SSR |
| TypeScript | 5.x | Type-safe JavaScript |
| Tailwind CSS | 3.x | Utility-first styling |
| React | 18.x | UI component library |

### Backend
| Technology | Version | Purpose |
|---|---|---|
| Python | 3.11.x | Core backend language |
| FastAPI | 0.136.x | REST API framework |
| Uvicorn | 0.46.x | ASGI server |
| SQLAlchemy | 2.0.x | ORM for database |
| SQLite | 3.x | Persistent storage |
| ReportLab | 4.5.x | PDF generation |
| python-dotenv | 1.2.x | Environment management |

### AI / ML Stack
| Model | Version | Purpose |
|---|---|---|
| Faster-Whisper | 1.2.x | Speech-to-text transcription |
| Pyannote.audio | 4.0.x | Speaker diarization |
| Gemini 2.5 Flash | API | Meeting intelligence extraction |
| Torch | 2.12.x | Deep learning framework |
| TorchAudio | 2.11.x | Audio processing |
| ONNX Runtime | 1.26.x | Optimized model inference |
| SoundFile | 0.13.x | Audio file I/O |

### DevOps & Deployment
| Tool | Purpose |
|---|---|
| GitHub | Version control + CI/CD |
| Vercel | Frontend deployment |
| Render | Backend deployment |
| Git | Source control |

---

## 🤖 AI/ML Models Used

### 1. Faster-Whisper (Speech-to-Text)
- **Model:** `small` (244M parameters)
- **Compute Type:** `int8` quantization for CPU efficiency
- **Beam Size:** 5 for improved accuracy
- **VAD Filter:** Active — removes silence automatically
- **Language:** Hindi (`hi`) with multilingual fallback
- **Word Timestamps:** Enabled for speaker alignment

### 2. Pyannote.audio (Speaker Diarization)
- **Model:** `pyannote/speaker-diarization-3.1`
- **Segmentation:** `pyannote/segmentation-3.0`
- **Input:** 16kHz mono waveform tensor
- **Output:** Speaker segments with timestamps
- **Authentication:** HuggingFace token required

### 3. Gemini 2.5 Flash (LLM Summarization)
- **Model:** `gemini-2.5-flash`
- **SDK:** `google-genai` (new SDK)
- **Retry Logic:** 3 attempts with 30s delay on 503
- **Output:** Structured meeting intelligence in 4 sections

---

## 🔧 Backend Architecture

```
backend/
├── app/
│   ├── main.py              # Full backend (local with diarization)
│   ├── main_deploy.py       # Production backend (without diarization)
│   ├── transcriber.py       # Whisper transcription (local)
│   ├── transcriber_deploy.py# Whisper transcription (production)
│   ├── diarizer.py          # Pyannote speaker diarization
│   ├── gemini_utils.py      # Gemini AI integration
│   ├── pdf_generator.py     # ReportLab PDF creation
│   ├── database.py          # SQLAlchemy models + CRUD
│   └── NotoSans-Regular.ttf # Unicode font for Hindi support
├── uploads/                 # Audio file storage
├── requirements.txt         # Full local dependencies
├── requirements_deploy.txt  # Lightweight production dependencies
├── runtime.txt              # Python 3.11.9 specification
├── .env                     # Environment variables (not committed)
└── meetings.db              # SQLite database (not committed)
```

### API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check |
| `POST` | `/upload-audio` | Upload and process audio |
| `GET` | `/meetings` | List all meetings |
| `GET` | `/meetings/{id}` | Get specific meeting |
| `GET` | `/download-report` | Download latest PDF |
| `GET` | `/download-report/{id}` | Download PDF by meeting ID |

---

## 🎨 Frontend Architecture

```
frontend/
├── app/
│   ├── page.tsx             # Main single-page application
│   ├── layout.tsx           # Root layout
│   └── globals.css          # Global styles
├── public/                  # Static assets
├── package.json             # Node dependencies
├── tailwind.config.js       # Tailwind configuration
├── tsconfig.json            # TypeScript configuration
└── next.config.ts           # Next.js configuration
```

### Frontend Features
- **Single Page Application** — Upload and History views in one file
- **Drag & Drop Upload** — Audio file upload with visual feedback
- **Real-time Loading States** — Animated processing indicators
- **Tabbed Results** — AI Summary and Transcript tabs
- **Meeting History** — Browse and download past meetings
- **PDF Download** — One-click report download
- **Responsive Design** — Works on desktop and mobile

---

## 📁 Folder Structure

```
AI-Meeting-Intelligence/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── main_deploy.py
│   │   ├── transcriber.py
│   │   ├── transcriber_deploy.py
│   │   ├── diarizer.py
│   │   ├── gemini_utils.py
│   │   ├── pdf_generator.py
│   │   ├── database.py
│   │   └── NotoSans-Regular.ttf
│   ├── uploads/
│   ├── requirements.txt
│   ├── requirements_deploy.txt
│   ├── runtime.txt
│   └── .env
├── frontend/
│   ├── app/
│   │   ├── page.tsx
│   │   ├── layout.tsx
│   │   └── globals.css
│   ├── public/
│   ├── package.json
│   └── next.config.ts
└── README.md
```

---

## 🔌 API Flow

### Upload Audio
```http
POST /upload-audio
Content-Type: multipart/form-data

file: <audio_file.mp3>
```

**Response:**
```json
{
  "message": "File uploaded successfully",
  "meeting_id": 1,
  "filename": "meeting.mp3",
  "transcript": "SPEAKER_01: Hello everyone...\nSPEAKER_02: Good morning...",
  "language": "hi",
  "meeting_summary": "1. Meeting Summary\n...",
  "diarized_segments": [
    {"speaker": "SPEAKER_01", "start": 0.0, "end": 3.2},
    {"speaker": "SPEAKER_02", "start": 3.5, "end": 7.1}
  ]
}
```

### List Meetings
```http
GET /meetings
```

**Response:**
```json
[
  {
    "id": 1,
    "filename": "meeting.mp3",
    "language": "hi",
    "created_at": "2026-05-17T09:30:00",
    "summary_preview": "The meeting discussed Q3 budget..."
  }
]
```

---

## ⚙️ Detailed Pipeline Explanation

### 1. Audio Preprocessing
The uploaded audio is saved locally, then converted to 16kHz mono WAV format using FFmpeg (or SoundFile) for compatibility with both Pyannote and Whisper models. VAD (Voice Activity Detection) removes silent portions before transcription.

### 2. Speaker Diarization
Pyannote.audio 3.1 loads the audio as a PyTorch tensor and runs neural speaker embedding to cluster speakers. The output is a list of `{speaker, start, end}` segments identifying who spoke when.

### 3. Whisper Transcription
Faster-Whisper processes the audio in segments, generating text with word-level timestamps. The small model with int8 quantization balances accuracy and CPU performance.

### 4. Speaker Mapping
Each Whisper segment's midpoint timestamp is matched against diarization segments to assign speaker labels. Consecutive segments from the same speaker are merged for readability.

### 5. Gemini AI Summarization
The structured speaker transcript is sent to Gemini 2.5 Flash with a carefully engineered prompt requesting four structured outputs: Meeting Summary, Key Discussion Points, Action Items, and Final Decisions.

### 6. PDF Report Generation
ReportLab generates a two-page PDF — Page 1 contains the AI summary, Page 2 contains the speaker dialogue. NotoSans font enables Hindi/Devanagari rendering. Each page includes branding and a footer.

### 7. Database Storage
SQLAlchemy ORM saves the meeting record (filename, language, transcript, summary, timestamp) to SQLite. Full CRUD endpoints enable history retrieval and report re-downloading.

---

##  Installation

### Prerequisites
- Python 3.11.x
- Node.js 20+
- Git
- FFmpeg (for audio conversion)
- HuggingFace account + token
- Google Gemini API key

### 1. Clone the Repository
```bash
git clone https://github.com/himnad/AI-Meeting-Intelligence.git
cd AI-Meeting-Intelligence
```

### 2. Backend Setup
```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Frontend Setup
```bash
cd frontend
npm install
```

---

##  Environment Variable Setup

Create `backend/.env`:
```env
GEMINI_API_KEY=your_gemini_api_key_here
HF_TOKEN=your_huggingface_token_here
```

**Getting API Keys:**
- **Gemini API Key:** [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)
- **HuggingFace Token:** [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

**HuggingFace Model Access (required):**
- Accept terms at [pyannote/speaker-diarization-3.1](https://huggingface.co/pyannote/speaker-diarization-3.1)
- Accept terms at [pyannote/segmentation-3.0](https://huggingface.co/pyannote/segmentation-3.0)

---

##  Running the Backend

```bash
cd backend
venv\Scripts\activate  # Windows
uvicorn app.main:app --reload
```

Backend runs at: `http://127.0.0.1:8000`
Swagger UI at: `http://127.0.0.1:8000/docs`

---

##  Running the Frontend

```bash
cd frontend
npm run dev
```

Frontend runs at: `http://localhost:3000`

---

## 📬 Example API Requests

### Upload Audio (cURL)
```bash
curl -X POST "http://127.0.0.1:8000/upload-audio" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@meeting.mp3;type=audio/mpeg"
```

### Get All Meetings
```bash
curl -X GET "http://127.0.0.1:8000/meetings"
```

### Download PDF Report
```bash
curl -X GET "http://127.0.0.1:8000/download-report/1" \
  --output meeting_report.pdf
```

---

##  Example Outputs

### Transcript Output
```
Speaker 1: Hello everyone, let's begin the meeting.
Speaker 2: Sure, I'll start with the Q3 budget update.
Speaker 1: Great, please go ahead.
Speaker 2: We have exceeded our targets by 12% this quarter.
```

### AI Summary Output
```
1. Meeting Summary
The Q3 budget review meeting focused on financial performance...

2. Key Discussion Points
• Q3 revenue exceeded targets by 12%
• Marketing spend optimization discussed
• New product launch timeline reviewed

3. Action Items
• Finance team to prepare Q4 projections by Friday
• Marketing to submit revised budget proposal

4. Final Decisions
• Q4 budget approved with 15% increase in AI investments
```

---

## 📸 Screenshots

> _Add screenshots of your application here_

| Upload Screen | Results View | PDF Report |
|---|---|---|
| ![Upload](screenshots/upload.png) | ![Results](screenshots/results.png) | ![PDF](screenshots/pdf.png) |

---

##  Challenges Faced

| Challenge | Solution |
|---|---|
| Pyannote `DiarizeOutput` format change in v4.0 | Discovered `speaker_diarization` attribute via runtime debugging |
| Hindi/Devanagari rendering in PDF | Integrated NotoSans Unicode font via ReportLab `pdfmetrics` |
| Torch + Pyannote RAM exceeded Render free tier (512MB) | Created lightweight deployment version without diarization |
| gRPC/protobuf version conflicts on Render | Created minimal `requirements_deploy.txt` without pinned versions |
| TorchCodec missing FFmpeg DLLs on Windows | Used SoundFile for audio loading instead |
| Gemini `google-generativeai` deprecated | Migrated to new `google-genai` SDK with updated client syntax |
| Render using Python 3.14 instead of 3.11 | Added `runtime.txt` with explicit Python version |

---

##  Novelty of the Project

1. **Diarization + LLM Integration** — Combines neural speaker diarization with large language model extraction in a single automated pipeline, a pattern used in enterprise-grade products.

2. **Automatic Meeting Intelligence** — Goes beyond simple transcription to generate structured, actionable intelligence from unstructured audio.

3. **Multilingual Support** — Handles Hindi/English code-switching common in Indian corporate environments, with proper Unicode rendering in PDF reports.

4. **Speaker-Level Analytics** — Attributes every statement to individual speakers, enabling participation analysis.

5. **Enterprise-Style Reporting** — Two-page professional PDF reports with branding, headers, footers, and multilingual content — ready for corporate use.

6. **Production Deployment** — Fully deployed with CI/CD pipeline, environment variable management, and separate development/production configurations.

---

##  Future Scope

- 🎙️ **Real-time Live Transcription** — Stream audio from Zoom/Google Meet directly
- 🌍 **Full Multilingual Support** — 100+ languages via Whisper large-v3
- 😊 **Sentiment Analysis** — Detect conflict, positivity, and urgency per speaker
- ✅ **Action Item Assignment** — Auto-assign tasks to speakers via NLP
- 📅 **Calendar Integration** — Push action items to Google Calendar
- 🔗 **Zoom/Teams Integration** — Direct meeting platform connectors
- 🧠 **RAG-based Meeting Memory** — "What did we decide last week?" via vector search
- 👤 **Multi-user Authentication** — JWT auth with user-specific meeting libraries
- 🐳 **Docker Deployment** — Containerized deployment for enterprise on-premise
- ⚡ **Streaming Transcription** — Real-time word-by-word display
- 🔍 **Semantic Search** — Search across all past meetings by topic
- 📊 **Participation Analytics** — Speaking time, interruptions, topic distribution

---

##  Scalability Discussion

The current architecture uses SQLite for simplicity. For production scale:

- **Database:** Migrate to PostgreSQL for concurrent access
- **Storage:** Move audio files to AWS S3 or Google Cloud Storage
- **Processing:** Use Celery + Redis for async task queues
- **Caching:** Redis for frequent meeting history queries
- **Load Balancing:** Multiple Uvicorn workers behind Nginx
- **GPU Inference:** Switch Whisper to CUDA for 10x speed improvement

---

## Security Considerations

- API keys stored in environment variables, never committed to Git
- `.env` and `meetings.db` in `.gitignore`
- CORS configured to allow only trusted frontend origins
- File upload validation (audio MIME types only)
- No user PII stored beyond meeting content

---

##  Performance Optimization

| Optimization | Impact |
|---|---|
| Whisper `tiny` model on deployment | Fits in 512MB RAM on free tier |
| int8 quantization | 4x memory reduction vs float32 |
| VAD filtering | Removes silence, reduces processing time |
| beam_size=1 on deployment | Faster inference at slight accuracy cost |
| SQLite WAL mode | Better concurrent read performance |

---

##  Deployment

| Component | Platform | URL |
|---|---|---|
| Frontend | Vercel | [ai-meeting-intelligence-nine.vercel.app](https://ai-meeting-intelligence-nine.vercel.app/) |
| Backend | Render | [ai-meeting-intelligence-iw1r.onrender.com](https://ai-meeting-intelligence-iw1r.onrender.com) |
| API Docs | Render | [/docs](https://ai-meeting-intelligence-iw1r.onrender.com/docs) |
| Source Code | GitHub | [himnad/AI-Meeting-Intelligence](https://github.com/himnad/AI-Meeting-Intelligence) |

---

##  Resume Value

This project demonstrates proficiency in:

- ✅ **Generative AI Integration** — Real-world LLM API usage with prompt engineering
- ✅ **Speech AI** — ASR pipeline with state-of-the-art Whisper model
- ✅ **Speaker Diarization** — Neural audio ML model integration
- ✅ **Full-Stack Development** — End-to-end Next.js + FastAPI application
- ✅ **REST API Design** — RESTful endpoints with proper HTTP semantics
- ✅ **Database Design** — ORM-based persistent storage with CRUD
- ✅ **PDF Generation** — Programmatic document creation with Unicode support
- ✅ **Production Deployment** — CI/CD with Vercel + Render + GitHub
- ✅ **System Design** — Multi-model AI pipeline orchestration
- ✅ **DevOps Basics** — Environment management, dependency isolation, deployment configs

---

## Learning Outcomes

- Building multi-model AI pipelines combining ASR, diarization, and LLMs
- Integrating Google's Gemini API with the new `google-genai` SDK
- Deploying Python AI applications to cloud with RAM constraints
- Handling multilingual text and Unicode rendering in PDFs
- Debugging dependency conflicts in production environments
- Designing RESTful APIs with FastAPI and automatic documentation
- Building modern React applications with Next.js and TypeScript

---

## 👨‍💻 Contributors

| Name | Role |
|---|---|
| Akhil Himnad | Full-Stack Developer & AI Engineer |

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgements

- [OpenAI Whisper](https://github.com/openai/whisper) — Speech recognition model
- [Faster-Whisper](https://github.com/SYSTRAN/faster-whisper) — Optimized Whisper implementation
- [Pyannote.audio](https://github.com/pyannote/pyannote-audio) — Speaker diarization toolkit
- [Google Gemini](https://ai.google.dev/) — Large language model API
- [FastAPI](https://fastapi.tiangolo.com/) — Modern Python web framework
- [ReportLab](https://www.reportlab.com/) — PDF generation library
- [Vercel](https://vercel.com/) — Frontend deployment platform
- [Render](https://render.com/) — Backend deployment platform

---

<div align="center">

**Built with ❤️ by Akhil Himnad**

⭐ Star this repo if you found it useful!

</div>
