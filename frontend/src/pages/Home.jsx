import React, { useState } from 'react';
import "../styles/Home.css";
import api from "../api";

function Home() {
    const [url, setUrl] = useState('');
    const [products, setProducts] = useState([
        { id: 1, name: 'Product 1', price: '$100', site: 'Amazon', url: 'https://www.amazon.com/product1' },
        { id: 2, name: 'Product 2', price: '$200', site: 'eBay', url: 'https://www.ebay.com/product2' },
        { id: 3, name: 'Product 3', price: '$150', site: 'Walmart', url: 'https://www.walmart.com/product3' }
    ]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const res = await api.post("/api/", { url });
            // Handle API response if needed
        } catch (error) {
            alert(error);
        } finally {
            // Clear input after submission
            setUrl('');
        }
    };

    return (
        <div className="home-container">
            <h1>Product Search</h1>
            <form onSubmit={handleSubmit} className="search-form">
                <div className="form-group">
                    <label htmlFor="product-url">Product URL</label>
                    <input type="text" id="product-url" value={url} onChange={(e) => setUrl(e.target.value)} placeholder="Enter product URL" required />
                </div>
                <button type="submit" className="search-button">Search</button>
            </form>

            <h2>Currently Tracked Products</h2>
            <ul className="product-list">
                {products.map(product => (
                    <li key={product.id} className="product-item">
                        <a href={product.url} target="_blank" rel="noopener noreferrer" className="product-link">
                            <h3>{product.name}</h3>
                            <p>Price: {product.price}</p>
                            <p>Site: {product.site}</p>
                        </a>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default Home;
