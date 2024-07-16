console.log("js file zone 1")

console.log("\ndisplay the image\n")
const get_prod = document.getElementById('show_prod_img').src
let set_prod = document.getElementById('id_img_prod')
get_prod = URL.createObjectURL(set_prod.files[0])