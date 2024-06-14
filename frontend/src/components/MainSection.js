import React, { useState, useEffect } from 'react';
import axios from 'axios';

function MainSection() {

    const [message, setMessage] = useState();

    useEffect(() => {
        axios.get('http://localhost:8000/api/')
          .then(response => {
            setMessage(response.data.message); 
          })
          .catch(error => {
            console.log(error);
          });
    }, []);

    return (
        <div>
            <h1>Message: {message}</h1>
        </div>
    )
}

export default MainSection;