import React, { useState } from 'react';
import axios from 'axios';

function Chat() {
    const [prompt, setPrompt] = useState('');
    const [idea, setIdea] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const apiUrl = process.env.REACT_APP_API_URL;
            const response = await axios.post(`${apiUrl}/api/v1/generate-idea`, { prompt });
            setIdea(response.data.idea);
        } catch (error) {
            console.error('Error generating idea:', error);
        }
    };

    return (
        <div>
            <h1>Generate a Startup Idea</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={prompt}
                    onChange={(e) => setPrompt(e.target.value)}
                    placeholder="Enter a prompt"
                />
                <button type="submit">Generate Idea</button>
            </form>
            {idea && <p>Idea: {idea}</p>}
        </div>
    );
}

export default Chat;
