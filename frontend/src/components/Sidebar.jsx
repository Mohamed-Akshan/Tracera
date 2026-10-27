import { NavLink } from "react-router";
import {
  Activity,
  MessageSquare,
  Workflow,
  ChartNoAxesColumn,
  FileText,
  PanelLeftClose
} from "lucide-react";

// Main navigation links
const links = [
  { name: "AI Workspace", path: "/", icon: MessageSquare },
  { name: "Investigation Trace", path: "/trace", icon: Workflow },
  { name: "Findings", path: "/findings", icon: ChartNoAxesColumn },
  { name: "Reports", path: "/reports", icon: FileText }
];

export default function Sidebar({ collapsed, setCollapsed }) {
  return (
    <aside className={`sidebar ${collapsed ? "collapsed" : ""}`}>
      <div className="sidebar-top">
        <div className="brand">
          <div className="brand-icon"><Activity size={23} /></div>
          {!collapsed && (
            <div>
              <h2>Tracera</h2>
              <small>Incident Intelligence</small>
            </div>
          )}
        </div>
        <button
          className="icon-button"
          onClick={() => setCollapsed(!collapsed)}
          title="Toggle sidebar"
          aria-label="Toggle sidebar"
        >
          <PanelLeftClose size={19} />
        </button>
      </div>

      <p className="nav-label">{!collapsed && "WORKSPACE"}</p>

      <nav className="nav-links">
        {links.map((link) => {
          const Icon = link.icon;
          return (
            <NavLink
              key={link.path}
              to={link.path}
              end={link.path === "/"}
              title={link.name}
              className={({ isActive }) => `nav-link ${isActive ? "active" : ""}`}
            >
              <Icon size={19} />
              {!collapsed && <span>{link.name}</span>}
            </NavLink>
          );
        })}
      </nav>

      <div className="sidebar-bottom">
        {!collapsed && (
          <div className="system-status">
            <span className="status-dot"></span>
            UI preview mode
          </div>
        )}
      </div>
    </aside>
  );
}
