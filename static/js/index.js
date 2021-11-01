$(window).scroll(function(){
    var scroll = $(window).scrollTop();
    
    document.getElementById("myBoddy").style.marginTop = (-100 - scroll) + "px";
    
    if(scroll >= 200){
        $("#myNavbar").addClass("bg-dark");
    } else{
        $("#myNavbar").removeClass("bg-dark");
    }
});