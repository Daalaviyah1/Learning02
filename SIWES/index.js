let counter = 0;
function count(){
    counter++;
    document.querySelector('h1').innerHTML = counter
    if (counter % 10 === 0)

    // elif (counter >= 10 )

    alert('The count is now the multiple of 10' ,{counter})

}
