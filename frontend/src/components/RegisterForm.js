import React, { useState } from 'react';
import axios from 'axios';
import './styles/Register.css';

function RegisterForm () {
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8000/api/register/', {
            first_name: firstName,
            last_name: lastName,
            email: email,
            password: password
        })
        .then(response => {
            setMessage('Registration successful');  // on response set the message
        })
        .catch(error => {
            console.error('Error registering user:', error);
            setMessage('Registration failed');
        });
    };

    return (
        <div className="register-container">
            <h1>Register</h1>
            <form onSubmit={handleSubmit} className="register-form">

                <div className="form-group">
                    <label>First Name</label>
                    <input type="text" value={firstName} onChange={(e) => setFirstName(e.target.value)} required />
                </div>

                <div className="form-group">
                    <label>Last Name</label>
                    <input type="text" value={lastName} onChange={(e) => setLastName(e.target.value)} required />
                </div>

                <div className="form-group">
                    <label>Email</label>
                    <input type="text" value={email} onChange={(e) => setEmail(e.target.value)} required/>
                </div>

                <div className="form-group">
                    <label>Password</label>
                    <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required/>
                </div>

                <button type="submit" className="register-button">Register</button>
            </form>
            {message && <p className="message">{message}</p>}
        </div>
    );
};

export default RegisterForm;
