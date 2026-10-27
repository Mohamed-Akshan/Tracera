import { ChartNoAxesColumn, AlertTriangle, ShieldCheck, FileSearch } from "lucide-react";

export default function Findings() {
  const cards = [
    { title: "Total Findings", value: "—", icon: FileSearch },
    { title: "High Severity", value: "—", icon: AlertTriangle },
    { title: "Verified Findings", value: "—", icon: ShieldCheck }
  ];

  return (
    <div className="page">
      <header className="topbar">
        <div><span className="eyebrow">TRACERA / INSIGHTS</span><h3>Findings Dashboard</h3></div>
        <span className="topbar-tag">No investigation selected</span>
      </header>
      <div className="page-content">
        <div className="page-heading">
          <div className="page-icon"><ChartNoAxesColumn size={24} /></div>
          <h1>Investigation Findings</h1>
          <p>Explore detected issues, evidence quality, severity, and AI-generated explanations.</p>
        </div>
        <div className="stats-grid">
          {cards.map((card) => {
            const Icon = card.icon;
            return (
              <div className="stat-card" key={card.title}>
                <Icon size={22} /><h2>{card.value}</h2><p>{card.title}</p>
              </div>
            );
          })}
        </div>
        <div className="section-card empty-state">
          <FileSearch size={35} /><h3>No findings yet</h3>
          <p>Findings will appear here after Tracera completes an investigation.</p>
        </div>
      </div>
    </div>
  );
}
