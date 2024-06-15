import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/pages/Home';
import Login from './components/pages/Login';
import Register from './components/pages/Register';
import Navbar from './components/Navbar';

function App() {
  return (
    <Router>
      <div>
        <Navbar />  

        <Routes>

          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />

        </Routes>
        
      </div>
    </Router>
  );
}

export default App;
