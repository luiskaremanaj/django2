function formFunction(event) {
    event.preventDefault()
    let name = document.getElementById("name").value.trim();
    let phone = document.getElementById("phone").value.trim();
    let email = document.getElementById("email").value.trim();
    let messg = document.getElementById("messg").value.trim();
    
    let sms = document.getElementById("sms")

 

    if (name != "" && phone != "" && email != "" && messg != "") {
        sms.textContent = "Thank You " + name + " for contacting us."

        document.querySelector('.loginform').submit();
    } else {
        sms.textContent = "You should fill all the of the fields!"
    }
}



$(document).ready(function() {
    let navbarColor = $("nav")
    console.log(navbarColor.css("backgroundColor"))
 
    $(window).on("scroll", function(){
     let windowHeight = $(window).scrollTop()
     console.log(windowHeight)
 
     if (windowHeight >= 105){
         navbarColor.css("backgroundColor", "rgb(1, 51, 1)")
     }else {
         navbarColor.css("backgroundColor", "transparent")
     }
    })
 
 });


$(document).ready(function(){
    $('.navbar-toggler').click(function()
        {
            $('.navbar').toggleClass('toggled');

        });
    

});

$(document).ready(function(){
    if($('body').hasClass('shopnavbar')){
        $('.navbar').css('color','rgb(1, 51, 1)');
    }   
});
