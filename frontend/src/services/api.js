
const API_URL = "http://127.0.0.1:8000";


// Check whether FastAPI is running
export async function checkBackend() {

    const response = await fetch(`${API_URL}/health`);

    if (!response.ok) {
        throw new Error("Backend connection failed");
    }

    return await response.json();
}


// Check whether PostgreSQL is connected
export async function checkDatabase() {

    const response = await fetch(`${API_URL}/health/database`);

    if (!response.ok) {
        throw new Error("Database connection failed");
    }

    return await response.json();
}
