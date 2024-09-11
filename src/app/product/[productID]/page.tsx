export default function ProductDetail({params} : {params: {productID : string}}) {
  return   <>
    <h1>Product №{params.productID}'s Information</h1>
  </>;
}
