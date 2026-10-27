import BackendStatus from "../components/BackendStatus";
import { useState } from "react";
import { ArrowUp, Paperclip, Sparkles, Search, ShieldCheck, Activity } from "lucide-react";

export default function Workspace() {
  // Store the user's current message
  const [message, setMessage] = useState("");

  return (
    <div className="workspace-page">
      <header className="topbar">
        <div>
          <span className="eyebrow">TRACERA / WORKSPACE</span>
          <h3>AI Workspace</h3>
        </div>
        <BackendStatus />
      </header>

      <div className="workspace-center">
        <div className="hero-icon"><Activity size={27} /></div>
        <div className="hero-heading">
          <span className="eyebrow">YOUR INCIDENT INTELLIGENCE PARTNER</span>
          <h1>What can we investigate today?</h1>
          <p>Understand production failures, uncover recurring patterns, and turn technical evidence into clarity.</p>
        </div>

        <div className="chat-composer">
          <textarea
            placeholder="Ask Tracera about a production incident..."
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            rows={3}
          />
          <div className="composer-actions">
            <span className="composer-hint"><Paperclip size={17} />Evidence upload coming soon</span>
            <button className="send-button" disabled title="AI chat will be enabled in a later sprint">
              <ArrowUp size={20} />
            </button>
          </div>
        </div>

        <div className="suggestions">
          <div className="suggestion"><Search size={19} /><span>Analyze error logs</span></div>
          <div className="suggestion"><Sparkles size={19} /><span>Discover recurring failures</span></div>
          <div className="suggestion"><ShieldCheck size={19} /><span>Investigate root causes</span></div>
        </div>
        <p className="workspace-note">AI messaging and evidence uploads will be activated in upcoming sprints.</p>
      </div>
    </div>
  );
}
