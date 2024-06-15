import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/pages/Home';
import Login from './components/pages/Login';
import Navbar from './components/Navbar';

function App() {
  return (
    <Router>
      <div>
        <Navbar />  

        <Routes>

          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />

        </Routes>
        
      </div>
    </Router>
  );
}

export default App;
