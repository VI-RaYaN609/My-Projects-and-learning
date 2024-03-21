function result (){
    const select = document.querySelectorAll("select")
    const inputs = document.querySelectorAll("input")
    const price1= 100*select[0].value
    const price2= 100*select[1].value
    const price3= 100*select[2].value
    const sum  = price1*inputs[0].value + price2*inputs[1].value + price3*inputs[2].value
    let exoneration = 0
    let state = true
    if(inputs[0].value<0 ||inputs[0].value>9999){state = false}
    if(inputs[1].value<0 ||inputs[1].value>9999){state = false}
    if(inputs[2].value<0 ||inputs[2].value>9999){state = false}
    if (!inputs[3].checked){
        exoneration = sum*0.19
    }
    let reduction = 0
    if(inputs[5].checked){reduction = 0.05}
    if(inputs[6].checked){reduction = 0.1}
    if(state){
    document.write(`<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <style>      
         table{
            margin-top: 20px;
         }
            th{
                font-size: 25px;
            }
            @media (max-width: 1200px) {
                th{
                    font-size: 20px;
                    transition: 0.5s ease-out;
                }
            }
            @media (max-width : 900px){
                th{
                    font-size: 17.5px;
                    transition: 0.5s ease-out;
                }
            }
            @media (max-width: 450px) {
                th{
                    font-size: 15px;
                    transition: 0.5s ease-out;
                }
            }
        </style>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <table>
            <tr>
                <th class="strong">Product</th>
                <th class="strong">Unit Price</th>
                <th class="strong">Quantity</th>
                <th class="strong">Amount</th>
            </tr>
            <tr>
                <th>Product ${select[0].value}</th>
                <th>${price1} DA</th>
                <th>${inputs[0].value}</th>
                <th>${price1*inputs[0].value} DA</th>
            </tr>
            <tr>
                <th>Product ${select[1].value}</th>
                <th>${price2} DA</th>
                <th>${inputs[1].value}</th>
                <th>${price2*inputs[1].value} DA</th>
            </tr>
            <tr>
                <th>Product ${select[2].value}</th>
                <th>${price3} DA</th>
                <th>${inputs[2].value}</th>
                <th>${price3*inputs[2].value} DA</th>
            </tr>
            <tr>
                <th colspan="3">Exoneration Amount(19%)</th>
                <th>${exoneration} DA</th>
            </tr>
            <tr>
                <th colspan="3">Reduction Amount</th>
                <th>${reduction*100}% (${sum*reduction}DA)</th>
            </tr>
            <tr>
                <th colspan="2"></th>
                <th>Net Amount</th>
                <th>${sum} DA</th>
            </tr>
            <tr>
                <th colspan="2"></th>
                <th>Brut Amount</th>
                <th>${sum+exoneration-reduction*sum} DA</th>
            </tr>
        </table>
        <a class="hyperlinks" id="back" href="order.html">Other Order Entry</a>
        <script src="../index.js"></script>
    </body>
    </html>`)
}
}
