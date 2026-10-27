import { FileText, Download } from "lucide-react";

export default function Reports() {
  return (
    <div className="page">
      <header className="topbar">
        <div><span className="eyebrow">TRACERA / REPORTING</span><h3>Reports</h3></div>
        <span className="topbar-tag">Report workspace</span>
      </header>
      <div className="page-content">
        <div className="page-heading">
          <div className="page-icon"><FileText size={24} /></div>
          <h1>Investigation Reports</h1>
          <p>Review evidence-backed investigation summaries, root-cause analysis, and recommended actions.</p>
        </div>
        <div className="section-card empty-state">
          <div className="empty-icon"><FileText size={32} /></div>
          <h3>Your reports will appear here</h3>
          <p>Complete an investigation to generate a structured technical report.</p>
          <span className="upcoming-feature"><Download size={16} />PDF export planned</span>
        </div>
      </div>
    </div>
  );
}
