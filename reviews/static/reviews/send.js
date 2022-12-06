function sendMail(params) {
    var tempParams = {
        from_name: "Ilya",
        to_name: "Pavel",
        message: "You shit",
    };
    
    emailjs.send("service_srl4rwe","template_8eytnpn", tempParams)
    .then(function(res){
        console.log("succes", res.status);
    });
}

//from_name: document.getElementById("fromName").value,
//to_name: document.getElementById("toName").value,
//message: document.getElementById("msg").value,