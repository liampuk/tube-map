var i = 0;

function init(){

    anim();
}

function anim(){
    setTimeout(function(){
        document.getElementById('jubilee').setAttribute('stroke-dashoffset', i);
        i++;
        anim();
    }, 10);
    
}