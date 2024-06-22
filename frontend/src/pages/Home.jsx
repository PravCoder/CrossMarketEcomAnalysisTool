import React, { useState, useEffect } from 'react';
import "../styles/Home.css";
import api from "../api";
import { Link } from 'react-router-dom';

function Home() {
    const [url, setUrl] = useState("");
    const [products, setProducts] = useState();

    useEffect(() => {
        api.get("/api/get-tracked-products/")
          .then(response => {
              setProducts(response.data.tracked_products);  // response-obj.data.key = value
          })
          .catch(error => {
            console.log(error);
          });
    }, [])

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const res = await api.post("/api/", { url });
            setProducts(res.data.tracked_products)
        } catch (error) {
            alert(error);
        } finally {
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
                {products && products.map(product =>  (
                    <li key={product.id} className="product-item">
                        <Link to={`view-product/${product.id}/`} className="product-link">
                            <h3>{product.title}</h3>
                            <p>Price: ${product.price}</p>
                            <p>Site: {product.website}</p>
                        </Link>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default Home;
