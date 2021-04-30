var width = $(window).width(); // Retrieve current window width
window.onscroll = function(){   // Execute function() when window is being scrolled:
if ((width >= 1000)){

    // If pixels of content (vertically) is greater than 80, change the navbar. 
    if(document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {

        $("#header").css("background","#fff");
        $("#header").css("color","#000");
        $("#header").css("box-shadow","0px 0px 20px rgba(0,0,0,0.09)");
        $("#header").css("padding","4vh 4vw");
        $("#navigation a").hover(function(){ // When mouse pointer hovers over any element in navbar under <a> elements
            $(this).css("border-bottom","2px solid rgb(98, 116, 255)"); // create a blue line under the element
        },function(){
            $(this).css("border-bottom","2px solid transparent");
        });
        // Else if content (vertically scrolled is less than 80 [top of page])
    }else{
        $("#header").css("background","transparent"); // Set background as transparent for navbar background
        $("#header").css("color","#fff"); //  Set color of text to white
        $("#header").css("box-shadow","0px 0px 0px rgba(0,0,0,0)");
        $("#header").css("padding","6vh 4vw");
        $("#navigation a").hover(function(){ // When mouse pointer hovers over any element in navbar under <a> elements
            $(this).css("border-bottom","2px solid #fff"); // create a white line under the element that has a moust pointer hovering over it
        },function(){
            $(this).css("border-bottom","2px solid transparent");
        });
    }
}
}
