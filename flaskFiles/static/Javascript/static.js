var width = $(window).width(); 
window.onscroll = function(){
if ((width >= 1000)){
        $("#header").css("background","#000");
        $("#header").css("color","#000");
        // $("#header").css("box-shadow","0px 0px 20px rgba(0,0,0,0.09)");
        // $("#header").css("padding","4vh 4vw");
        // $("#navigation a").hover(function(){
        //     $(this).css("border-bottom","2px solid rgb(255, 44, 90)");
        // },function(){
        //     $(this).css("border-bottom","2px solid transparent");
        // });
    }
}