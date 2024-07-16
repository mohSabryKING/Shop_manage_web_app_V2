console.log("js file zone 3");


function get_user_img(input_id, output_id) {
    console.log("getting the user-item-bkg image");
    const view_output = document.getElementById(output_id);
    let get_input = document.getElementById(input_id);
    console.log("we got\nin->" + input_id + ":out->" + output_id);
    get_input.onchange = function() {
        view_output.src = URL.createObjectURL(get_input.files[0]);
        console.log("the image path:" + view_output.src)
    }




}

function get_user_bkg(input_id, output_id) {
    console.log("getting the user bkg");
    const view_output = document.getElementById(output_id);
    let get_input = document.getElementById(input_id);
    console.log("we got\nin->" + input_id + ":out->" + output_id);
    get_input.onchange = function() {
        view_output.style.backgroundImage = URL.createObjectURL("../../");
        console.log("the image path:" + view_output.src)
    }

}