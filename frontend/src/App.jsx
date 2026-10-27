import { useState } from "react";
import { Routes, Route } from "react-router";

import Sidebar from "./components/Sidebar";
import Workspace from "./pages/Workspace";
import InvestigationTrace from "./pages/InvestigationTrace";
import Findings from "./pages/Findings";
import Reports from "./pages/Reports";

// Main application layout
export default function App() {
  // Control whether the sidebar is collapsed
  const [collapsed, setCollapsed] = useState(false);

  return (
    <div className="app-layout">
      <Sidebar collapsed={collapsed} setCollapsed={setCollapsed} />

      <main className="main-content">
        <Routes>
          <Route path="/" element={<Workspace />} />
          <Route path="/trace" element={<InvestigationTrace />} />
          <Route path="/findings" element={<Findings />} />
          <Route path="/reports" element={<Reports />} />
        </Routes>
      </main>
    </div>
  );
}
