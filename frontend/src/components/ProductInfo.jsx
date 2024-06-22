import "../styles/ProductInfo.css";
import React, { useState, useEffect } from 'react';
import api from "../api";


function ProductInfo({prod_id}) {  // take in product-id as prop
    const [product, setProduct] = useState({});
    // get the product-obj
    useEffect(() => {
    api.get(`/api/view-product/${prod_id}/`)
        .then(response => {
            setProduct(response.data.product);  
        })
        .catch(error => {
            console.log(error);
        });
    }, [])

    return (
      <>
        <div className="product-info-container">
            <h2 className="product-title">{product.title}</h2>
            <p className="product-price">Price: ${product.price}</p>
            <p className="product-website">Website: {product.website}</p>
            <p className="product-upc">UPC: {product.UPC}</p>
            {/* Add more details as needed */}
        </div>
      </>
    );
  }
  
  export default ProductInfo;