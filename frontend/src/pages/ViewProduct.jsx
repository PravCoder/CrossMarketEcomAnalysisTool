import ProductInfo from "../components/ProductInfo";
import { useParams } from 'react-router-dom';


// view product page loads in componenxts
function ViewProduct() {
    const { id } = useParams();  // get id from url-path, apss it in component as prop
    return (
      <>
        <ProductInfo prod_id={id}/>  
      </>
    );
  }
  
  export default ViewProduct;