export default function ReviewInformation({params} : {params: {productID : string; reviewID:string}}) {
  return   <>
    <h1>Product №{params.productID}'s {params.reviewID} review</h1>
  </>;
}
