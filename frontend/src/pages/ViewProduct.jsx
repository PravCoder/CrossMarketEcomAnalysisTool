import ProductInfo from "../components/ProductInfo";
import { useParams } from 'react-router-dom';
import React, { useState, useEffect } from 'react';
import api from "../api";


// view product page loads in components
function ViewProduct() {
    const { id } = useParams();  // get id from url-path, apss it in component as prop
    const [crossProducts, setCrossProducts] = useState([]);


    useEffect(() => {
      api.get(`/api/get-product-cross-products/${id}/`)
          .then(response => {
            setCrossProducts(response.data.cross_products);  
          })
          .catch(error => {
              console.log(error);
          });
      }, [])
    console.log(crossProducts);

    return (
      <>
        <ProductInfo prod_id={id} is_cross={"false"}/>  
        <ul>
            {crossProducts.map((product) => (
               <ProductInfo prod_id={product.id} is_cross={"true"}/>  
            ))}
        </ul>
      </>
    );
  }
  
  export default ViewProduct;