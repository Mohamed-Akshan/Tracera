
import { useEffect, useState } from "react";

import { checkBackend, checkDatabase } from "../services/api";


// Show backend and database connection status
export default function BackendStatus() {

    const [backend, setBackend] = useState("Checking...");
    const [database, setDatabase] = useState("Checking...");


    // Check connections when the component loads
    useEffect(() => {

        async function checkConnections() {

            try {
                await checkBackend();
                setBackend("Connected");
            } catch (error) {
                setBackend("Disconnected");
                setDatabase("Unavailable");
                return;
            }

            try {
                await checkDatabase();
                setDatabase("Connected");
            } catch (error) {
                setDatabase("Disconnected");
            }
        }

        checkConnections();

    }, []);


    return (
        <div className="backend-status">

            <span>
                FastAPI: {backend}
            </span>

            <span>
                PostgreSQL: {database}
            </span>

        </div>
    );
}
