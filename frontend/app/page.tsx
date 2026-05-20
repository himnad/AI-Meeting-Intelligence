"use client";

import { useState, useRef, useCallback, useEffect } from "react";

type MeetingResult = {
  filename: string;
  transcript: string;
  language: string;
  meeting_summary: string;
};

type Meeting = {
  id: number;
  filename: string;
  language: string;
  created_at: string;
  summary_preview: string;
};

export default function Home() {
  // Navigation
  const [view, setView] = useState<"upload" | "history">("upload");

  // Upload state
  const [isDragging, setIsDragging] = useState(false);
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<MeetingResult | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [activeTab, setActiveTab] = useState<"summary" | "transcript">(
    "summary"
  );
  const fileInputRef = useRef<HTMLInputElement>(null);

  // History state
  const [meetings, setMeetings] = useState<Meeting[]>([]);
  const [historyLoading, setHistoryLoading] = useState(false);

  // Backend URL
  const BACKEND_URL =
    "https://ai-meeting-intelligence-iw1r.onrender.com";

  // Load history when switching to history view
  useEffect(() => {
    if (view === "history") {
      setHistoryLoading(true);

      fetch(`${BACKEND_URL}/meetings`)
        .then((res) => res.json())
        .then((data) => {
          setMeetings(data);
          setHistoryLoading(false);
        })
        .catch(() => setHistoryLoading(false));
    }
  }, [view]);

  const handleDrop = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);

    const dropped = e.dataTransfer.files[0];

    if (dropped) setFile(dropped);
  }, []);

  const handleUpload = async () => {
    if (!file) return;

    setLoading(true);
    setError(null);
    setResult(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch(`${BACKEND_URL}/upload-audio`, {
        method: "POST",
        body: formData,
      });

      if (!res.ok) {
        throw new Error("Server error. Please try again.");
      }

      const data = await res.json();

      setResult(data);
    } catch (err: unknown) {
      setError(
        err instanceof Error ? err.message : "Something went wrong."
      );
    } finally {
      setLoading(false);
    }
  };

  const reset = () => {
    setFile(null);
    setResult(null);
    setError(null);
  };

  const formatDate = (iso: string) => {
    const d = new Date(iso);

    return d.toLocaleDateString("en-IN", {
      day: "numeric",
      month: "short",
      year: "numeric",
      hour: "2-digit",
      minute: "2-digit",
    });
  };

  return (
    <div
      className="min-h-screen bg-[#0c0c0f] text-white font-sans"
      style={{ fontFamily: "'DM Sans', sans-serif" }}
    >
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=DM+Serif+Display:ital@0;1&display=swap');

        .gradient-border {
          background:
            linear-gradient(#0c0c0f, #0c0c0f) padding-box,
            linear-gradient(135deg, #4ade80, #06b6d4, #8b5cf6) border-box;

          border: 1px solid transparent;
        }

        .glow-green {
          box-shadow: 0 0 40px rgba(74, 222, 128, 0.15);
        }

        @keyframes pulse-dot {
          0%, 100% {
            opacity: 1;
          }

          50% {
            opacity: 0.3;
          }
        }

        @keyframes spin-slow {
          from {
            transform: rotate(0deg);
          }

          to {
            transform: rotate(360deg);
          }
        }

        @keyframes fadeUp {
          from {
            opacity: 0;
            transform: translateY(16px);
          }

          to {
            opacity: 1;
            transform: translateY(0);
          }
        }

        .fade-up {
          animation: fadeUp 0.5s ease forwards;
        }

        .dot-1 {
          animation: pulse-dot 1.4s ease infinite 0s;
        }

        .dot-2 {
          animation: pulse-dot 1.4s ease infinite 0.2s;
        }

        .dot-3 {
          animation: pulse-dot 1.4s ease infinite 0.4s;
        }

        .spinner {
          animation: spin-slow 1.2s linear infinite;
        }

        .tab-active {
          background: rgba(74, 222, 128, 0.1);
          color: #4ade80;
          border-color: rgba(74, 222, 128, 0.3);
        }

        .card-hover:hover {
          background: rgba(255,255,255,0.03);
        }

        .nav-active {
          color: rgba(255,255,255,0.8);
          border-bottom: 2px solid #4ade80;
        }
      `}</style>

      {/* Header */}
      <header className="border-b border-white/5 px-8 py-5 flex items-center justify-between">
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-green-400 to-cyan-400 flex items-center justify-center">
            <svg
              width="16"
              height="16"
              viewBox="0 0 24 24"
              fill="none"
              stroke="white"
              strokeWidth="2.5"
            >
              <path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z" />
              <path d="M19 10v2a7 7 0 0 1-14 0v-2" />
              <line x1="12" y1="19" x2="12" y2="22" />
            </svg>
          </div>

          <span
            style={{ fontFamily: "'DM Serif Display', serif" }}
            className="text-lg text-white/90 tracking-wide"
          >
            MeetingMind
          </span>
        </div>

        {/* Nav Tabs */}
        <div className="flex items-center gap-6">
          <button
            onClick={() => {
              setView("upload");
              reset();
            }}
            className={`text-sm pb-1 transition-colors ${
              view === "upload"
                ? "nav-active"
                : "text-white/30 hover:text-white/50"
            }`}
          >
            Upload
          </button>

          <button
            onClick={() => setView("history")}
            className={`text-sm pb-1 transition-colors ${
              view === "history"
                ? "nav-active"
                : "text-white/30 hover:text-white/50"
            }`}
          >
            History
          </button>

          <div className="flex items-center gap-2 text-xs text-white/30 ml-4">
            <div className="w-1.5 h-1.5 rounded-full bg-green-400 dot-1"></div>
            <span>AI Ready</span>
          </div>
        </div>
      </header>

      <main className="max-w-3xl mx-auto px-6 py-16">
        {/* ===== UPLOAD VIEW ===== */}
        {view === "upload" && (
          <>
            {!result ? (
              <>
                {/* Hero */}
                <div className="mb-14 text-center">
                  <p className="text-xs uppercase tracking-[0.3em] text-green-400/70 mb-4 font-medium">
                    AI Meeting Intelligence
                  </p>

                  <h1
                    style={{ fontFamily: "'DM Serif Display', serif" }}
                    className="text-5xl text-white/95 leading-tight mb-4"
                  >
                    Turn meetings into
                    <br />
                    <span className="italic text-white/50">
                      actionable insights
                    </span>
                  </h1>

                  <p className="text-white/35 text-base leading-relaxed max-w-md mx-auto">
                    Upload any meeting audio and get instant transcription,
                    summary, action items and decisions — powered by Gemini AI.
                  </p>
                </div>

                {/* Upload Card */}
                <div
                  className={`gradient-border rounded-2xl p-8 cursor-pointer transition-all duration-300 ${
                    isDragging
                      ? "glow-green bg-green-400/5"
                      : "hover:bg-white/[0.02]"
                  }`}
                  onDragOver={(e) => {
                    e.preventDefault();
                    setIsDragging(true);
                  }}
                  onDragLeave={() => setIsDragging(false)}
                  onDrop={handleDrop}
                  onClick={() =>
                    !file && fileInputRef.current?.click()
                  }
                >
                  <input
                    ref={fileInputRef}
                    type="file"
                    accept="audio/*,.mp3,.wav,.mpeg,.m4a"
                    className="hidden"
                    onChange={(e) =>
                      e.target.files?.[0] &&
                      setFile(e.target.files[0])
                    }
                  />

                  {!file ? (
                    <div className="flex flex-col items-center gap-4 py-8">
                      <div
                        className={`w-16 h-16 rounded-2xl border border-white/10 flex items-center justify-center transition-colors ${
                          isDragging
                            ? "border-green-400/40 bg-green-400/10"
                            : "bg-white/[0.03]"
                        }`}
                      >
                        <svg
                          width="28"
                          height="28"
                          viewBox="0 0 24 24"
                          fill="none"
                          stroke={
                            isDragging
                              ? "#4ade80"
                              : "rgba(255,255,255,0.3)"
                          }
                          strokeWidth="1.5"
                        >
                          <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
                          <polyline points="17 8 12 3 7 8" />
                          <line x1="12" y1="3" x2="12" y2="15" />
                        </svg>
                      </div>

                      <div className="text-center">
                        <p className="text-white/60 text-sm mb-1">
                          {isDragging
                            ? "Drop your audio file here"
                            : "Drag & drop your audio file"}
                        </p>

                        <p className="text-white/20 text-xs">
                          MP3, WAV, M4A, MPEG supported
                        </p>
                      </div>

                      <button className="px-5 py-2.5 rounded-xl bg-white/5 hover:bg-white/10 border border-white/10 text-white/50 text-sm transition-colors">
                        Browse files
                      </button>
                    </div>
                  ) : (
                    <div className="flex items-center justify-between py-4">
                      <div className="flex items-center gap-4">
                        <div className="w-12 h-12 rounded-xl bg-green-400/10 border border-green-400/20 flex items-center justify-center">
                          <svg
                            width="20"
                            height="20"
                            viewBox="0 0 24 24"
                            fill="none"
                            stroke="#4ade80"
                            strokeWidth="1.5"
                          >
                            <path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z" />
                            <path d="M19 10v2a7 7 0 0 1-14 0v-2" />
                          </svg>
                        </div>

                        <div>
                          <p className="text-white/80 text-sm font-medium truncate max-w-[280px]">
                            {file.name}
                          </p>

                          <p className="text-white/25 text-xs mt-0.5">
                            {(file.size / 1024 / 1024).toFixed(2)} MB
                          </p>
                        </div>
                      </div>

                      <button
                        onClick={(e) => {
                          e.stopPropagation();
                          reset();
                        }}
                        className="text-white/20 hover:text-white/50 transition-colors p-2"
                      >
                        ✕
                      </button>
                    </div>
                  )}
                </div>

                {/* Error */}
                {error && (
                  <div className="mt-4 px-4 py-3 rounded-xl bg-red-500/10 border border-red-500/20 text-red-400 text-sm">
                    {error}
                  </div>
                )}

                {/* Upload Button */}
                {file && (
                  <button
                    onClick={handleUpload}
                    disabled={loading}
                    className="mt-4 w-full py-4 rounded-xl bg-gradient-to-r from-green-400 to-cyan-400 text-black font-semibold text-sm tracking-wide hover:opacity-90 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-3"
                  >
                    {loading
                      ? "Processing with AI..."
                      : "Analyse Meeting"}
                  </button>
                )}
              </>
            ) : (
              <div className="fade-up">
                <div className="flex items-center justify-between mb-8">
                  <div>
                    <div className="flex items-center gap-2 mb-1">
                      <div className="w-2 h-2 rounded-full bg-green-400"></div>

                      <span className="text-green-400 text-xs font-medium uppercase tracking-widest">
                        Analysis Complete
                      </span>
                    </div>

                    <h2
                      style={{
                        fontFamily: "'DM Serif Display', serif",
                      }}
                      className="text-2xl text-white/90"
                    >
                      {result.filename}
                    </h2>

                    <p className="text-white/25 text-xs mt-1">
                      Language detected:{" "}
                      {result.language?.toUpperCase()}
                    </p>
                  </div>

                  <div className="flex items-center gap-2">
                    <button
                      onClick={() =>
                        window.open(
                          `${BACKEND_URL}/download-report`,
                          "_blank"
                        )
                      }
                      className="flex items-center gap-2 px-4 py-2 rounded-xl bg-green-400/10 border border-green-400/20 text-green-400 text-sm hover:bg-green-400/20 transition-colors"
                    >
                      Download PDF
                    </button>

                    <button
                      onClick={reset}
                      className="px-4 py-2 rounded-xl border border-white/10 text-white/30 text-sm hover:text-white/60 hover:border-white/20 transition-colors"
                    >
                      New Upload
                    </button>
                  </div>
                </div>

                {/* Tabs */}
                <div className="flex gap-2 mb-6">
                  {(["summary", "transcript"] as const).map((tab) => (
                    <button
                      key={tab}
                      onClick={() => setActiveTab(tab)}
                      className={`px-4 py-2 rounded-lg border text-sm font-medium transition-all capitalize ${
                        activeTab === tab
                          ? "tab-active border-green-400/30"
                          : "border-white/5 text-white/25 hover:text-white/50 hover:border-white/10"
                      }`}
                    >
                      {tab === "summary"
                        ? "AI Summary"
                        : "Transcript"}
                    </button>
                  ))}
                </div>

                {activeTab === "summary" ? (
                  <div className="gradient-border rounded-2xl p-6">
                    <p className="text-white/55 text-sm leading-relaxed whitespace-pre-wrap">
                      {result.meeting_summary}
                    </p>
                  </div>
                ) : (
                  <div className="gradient-border rounded-2xl p-6">
                    <p className="text-white/40 text-sm leading-8 whitespace-pre-wrap font-mono">
                      {result.transcript}
                    </p>
                  </div>
                )}
              </div>
            )}
          </>
        )}

        {/* ===== HISTORY VIEW ===== */}
        {view === "history" && (
          <div className="fade-up">
            <div className="mb-10">
              <p className="text-xs uppercase tracking-[0.3em] text-green-400/70 mb-3 font-medium">
                Meeting History
              </p>

              <h1
                style={{
                  fontFamily: "'DM Serif Display', serif",
                }}
                className="text-4xl text-white/95"
              >
                Past Meetings
              </h1>

              <p className="text-white/30 text-sm mt-2">
                {meetings.length} meeting
                {meetings.length !== 1 ? "s" : ""} recorded
              </p>
            </div>

            {historyLoading ? (
              <div className="text-white/30">
                Loading meetings...
              </div>
            ) : meetings.length === 0 ? (
              <div className="gradient-border rounded-2xl p-12 text-center">
                <p className="text-white/30 text-sm">
                  No meetings yet
                </p>
              </div>
            ) : (
              <div className="flex flex-col gap-3">
                {meetings.map((meeting) => (
                  <div
                    key={meeting.id}
                    className="card-hover gradient-border rounded-2xl p-5 transition-all duration-200"
                  >
                    <div className="flex items-start justify-between gap-4">
                      <div className="flex-1 min-w-0">
                        <p className="text-white/80 text-sm font-medium truncate">
                          {meeting.filename}
                        </p>

                        <p className="text-white/25 text-xs mt-0.5">
                          {formatDate(meeting.created_at)}
                        </p>

                        <p className="text-white/35 text-xs mt-2 leading-5 line-clamp-2">
                          {meeting.summary_preview}
                        </p>
                      </div>

                      <button
                        onClick={() =>
                          window.open(
                            `${BACKEND_URL}/download-report/${meeting.id}`,
                            "_blank"
                          )
                        }
                        className="p-2 rounded-lg text-white/20 hover:text-green-400 hover:bg-green-400/10 transition-colors"
                      >
                        Download
                      </button>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        )}
      </main>
    </div>
  );
}