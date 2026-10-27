import { Workflow, GitBranch, Search, ShieldCheck } from "lucide-react";

export default function InvestigationTrace() {
  const steps = [
    { name: "Supervisor Agent", detail: "Plans and coordinates the investigation", icon: GitBranch },
    { name: "Retrieval Agent", detail: "Searches relevant logs and technical evidence", icon: Search },
    { name: "Verification Agent", detail: "Checks findings against available evidence", icon: ShieldCheck }
  ];

  return (
    <div className="page">
      <header className="topbar">
        <div><span className="eyebrow">TRACERA / INVESTIGATION</span><h3>Investigation Trace</h3></div>
        <span className="topbar-tag">Workflow preview</span>
      </header>
      <div className="page-content">
        <div className="page-heading">
          <div className="page-icon"><Workflow size={24} /></div>
          <h1>Investigation Journey</h1>
          <p>Follow how Tracera's agents reason, retrieve evidence, and verify conclusions.</p>
        </div>
        <div className="section-card">
          <h3>Agent workflow</h3>
          <p className="muted">Example stages of a future investigation.</p>
          <div className="trace-list">
            {steps.map((step, index) => {
              const Icon = step.icon;
              return (
                <div className="trace-step" key={step.name}>
                  <div className="step-icon"><Icon size={20} /></div>
                  <div><h4>{step.name}</h4><p>{step.detail}</p></div>
                  <span className="step-number">{String(index + 1).padStart(2, "0")}</span>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </div>
  );
}
