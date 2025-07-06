
import React, { useState } from 'react';

const App = () => {
    const [url, setUrl] = useState('');
    const [result, setResult] = useState(null);

    const checkUrl = async () => {
        const response = await fetch('http://localhost:5000/api/check-url', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url })
        });
        const data = await response.json();
        setResult(data);
    };

    const downloadCSV = () => {
        window.open('http://localhost:5000/api/export-logs', '_blank');
    };

    return (
        <div style={{
            padding: '20px',
            maxWidth: '500px',
            margin: 'auto',
            fontFamily: 'Arial, sans-serif'
        }}>
            <h1 style={{ textAlign: 'center' }}>Phishing URL Detector</h1>
            <input
                type="text"
                placeholder="Enter a URL"
                value={url}
                onChange={e => setUrl(e.target.value)}
                style={{ width: '100%', padding: '10px', marginBottom: '10px' }}
            />
            <button onClick={checkUrl} style={{
                width: '100%',
                padding: '10px',
                backgroundColor: '#007BFF',
                color: 'white',
                border: 'none',
                borderRadius: '5px'
            }}>Check</button>

            {result && (
                <div style={{ marginTop: 20, textAlign: 'center' }}>
                    <p><strong>URL:</strong> {result.url}</p>
                    <p><strong>Result:</strong> {result.is_phishing ? '⚠️ Phishing Detected' : '✅ Safe'}</p>
                </div>
            )}

            <button onClick={downloadCSV} style={{
                width: '100%',
                padding: '10px',
                backgroundColor: '#28a745',
                color: 'white',
                border: 'none',
                borderRadius: '5px',
                marginTop: '20px'
            }}>📁 Export Logs (CSV)</button>

            <div style={{ marginTop: 40 }}>
                <h2>Cyber Security Tips</h2>
                <ul>
                    <li>Check URLs before clicking.</li>
                    <li>Enable 2FA on accounts.</li>
                    <li>Never share OTPs.</li>
                </ul>
            </div>
        </div>
    );
};

export default App;
