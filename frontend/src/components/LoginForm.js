import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './styles/Login.css';

function LoginForm() {

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [message, setMessage] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8000/api/login/', { email, password })
            .then(response => {
                setMessage(response.data.message);
            })
            .catch(error => {
                console.log(error);
                setMessage('Login failed');
            });
    };

    return (
        <div className="login-container">
            <h1>Login</h1>
            <form onSubmit={handleSubmit} className="login-form">

                <div className="form-group">
                    <label>Email</label>
                    <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
                </div>

                <div className="form-group">
                    <label>Password</label>
                    <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
                </div>

                <button type="submit" className="login-button">Login</button>
                {message && <p className="message">{message}</p>}
            </form>
        </div>
    );
}

export default LoginForm;