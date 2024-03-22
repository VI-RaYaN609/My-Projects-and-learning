function preview (){
    const list = document.querySelectorAll("select")
    const Quantity = document.querySelectororAll("input")
    var condition = true
    if(Quantity[0].value<0 ||Quantity[0].value>1000){condition = false}
    if(Quantity[1].value<0 ||Quantity[1].value>1000){condition = false}
    if(Quantity[2].value<0 ||Quantity[2].value>1000){condition = false}
    if (!Quantity[3].checked){
        exoneration = prixtotal*0.19
    }
    var exoneration = 0
    const prixproduit1= 100*list[0].value
    const prixproduit2= 100*list[1].value
    const prixproduit3= 100*list[2].value
    const prixtotal  = prixproduit1*Quantity[0].value + prixproduit2*Quantity[1].value + prixproduit3*Quantity[2].value
    let reduction = 0
    if(Quantity[5].checked){reduction = 0.05}
    if(Quantity[6].checked){reduction = 0.1}
    if(condition==true){
    document.write(`
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>orders</title>
        <style>      
         table{
            margin-top: 20px;
         }
            th{
                font-size: 25px;
            }
            @media (max-width: 1120px) {
                th{
                    font-size: 20px;
                    transition: 0.5s ease-out;
                }
            }
            @media (max-width : 850px){
                th{
                    font-size: 17.5px;
                    transition: 0.5s ease-out;
                }
            }
            @media (max-width: 550px) {
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
                <th>Product ${list[0].value}</th>
                <th>${prixproduit1} DA</th>
                <th>${Quantity[0].value}</th>
                <th>${prixproduit1*Quantity[0].value} DA</th>
            </tr>
            <tr>
                <th>Product ${list[1].value}</th>
                <th>${prixproduit2} DA</th>
                <th>${Quantity[1].value}</th>
                <th>${prixproduit2*Quantity[1].value} DA</th>
            </tr>
            <tr>
                <th>Product ${list[2].value}</th>
                <th>${prixproduit3} DA</th>
                <th>${Quantity[2].value}</th>
                <th>${prixproduit3*Quantity[2].value} DA</th>
            </tr>
            <tr>
                <th colspan="3">Exoneration Amount(19%)</th>
                <th>${exoneration} DA</th>
            </tr>
            <tr>
                <th colspan="3">Reduction Amount</th>
                <th>${reduction*100}% (${prixtotal*reduction}DA)</th>
            </tr>
            <tr>
                <th colspan="2"></th>
                <th>Net Amount</th>
                <th>${prixtotal} DA</th>
            </tr>
            <tr>
                <th colspan="2"></th>
                <th>Brut Amount</th>
                <th>${prixtotal+exoneration-reduction*prixtotal} DA</th>
            </tr>
        </table>
        <a class="hyperlinks" id="back" href="order.html">Other Order Entry</a>
        <script src="../index.js"></script>
    </body>
    </html>
    `)
}
}
